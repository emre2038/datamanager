from django.http import HttpResponse
from models import FinancialYear, Dataset, Department
import yaml

from .utils import get_budget_resources


def department_list(request, financial_year_id):
    context = {
        'financial_years': [],
        'selected_financial_year': financial_year_id,
    }

    selected_year = None
    for year in FinancialYear.objects.order_by('slug'):
        is_selected = year.slug == financial_year_id
        if is_selected:
            selected_year = year
        context['financial_years'].append({
            'id': year.slug,
            'is_selected': is_selected,
            'closest_match': {
                'is_exact_match': True,
                'name': 'Departments',
                'slug': 'departments',
                'organisational_unit': 'financial_year',
                'url_path': "%s/departments" % year.slug,
            },
        })

    for sphere_name in ('national', 'provincial'):
        context[sphere_name] = []
        for government in selected_year.spheres.filter(slug=sphere_name).first().governments.all():
            departments = []
            for department in government.departments.all():
                departments.append({
                    'name': department.name,
                    'slug': str(department.slug),
                    'vote_number': department.vote_number,
                    'url_path': department.get_url_path(),
                })
            departments = sorted(departments, key=lambda d: d['vote_number'])
            context[sphere_name].append({
                'name': government.name,
                'slug': str(government.slug),
                'departments': departments,
            })

    response_yaml = yaml.safe_dump(context, default_flow_style=False, encoding='utf-8')
    return HttpResponse(response_yaml, content_type='text/x-yaml')


def department(request, financial_year_id, sphere_slug, government_slug, department_slug):
    department = None

    years = list(FinancialYear.objects.order_by('slug'))
    for year in years:
        if year.slug == financial_year_id:
            selected_year = year
            sphere = selected_year \
                     .spheres \
                     .filter(slug=sphere_slug) \
                     .first()
            government = sphere \
                         .governments \
                         .filter(slug=government_slug) \
                         .first()
            department = government \
                         .departments \
                         .filter(slug=department_slug) \
                         .first()

    financial_years_context = []
    for year in years:
        closest_match, closest_is_exact = year.get_closest_match(department)
        financial_years_context.append({
            'id': year.slug,
            'is_selected': year.slug == financial_year_id,
            'closest_match': {
                'name': closest_match.name,
                'slug': str(closest_match.slug),
                'url_path': closest_match.get_url_path(),
                'organisational_unit': closest_match.organisational_unit,
                'is_exact_match': closest_is_exact,
            },
        })
    contributed_datasets = []
    for dataset in department.get_contributed_datasets():
        contributed_datasets.append({
            'name': dataset.name,
            'contributor': dataset.get_organization()['name'],
            'url_path': dataset.get_url_path(),
        })
    budget = []
    budget_data = department.get_budget_totals(selected_year)
    if budget_data:
        for cells in budget_data['cells']:
            budget.append(
                {
                    'name': cells['activity_programme_number.programme'],
                    'total_budget': cells['value.sum']
                }
            )
    else:
        budget.append(
            {'name': p.name,
             'total_budget': None}
            for p in department.programmes.order_by('programme_number')
        )

    context = {
        'name': department.name,
        'slug': str(department.slug),
        'vote_number': department.vote_number,
        'total_budget': budget_data['summary']['value.sum'] if budget_data else None,
        'government': {
            'name': department.government.name,
            'slug': str(department.government.slug),
        },
        'sphere': {
            'name': department.government.sphere.name,
            'slug': department.government.sphere.slug,
        },
        'selected_financial_year': financial_year_id,
        'financial_years': financial_years_context,
        'intro': department.intro,
        'treasury_datasets': department.get_treasury_datasets(),
        'contributed_datasets': contributed_datasets if contributed_datasets else None,
        'programmes': budget,
        'government_functions': [f.name for f in department.get_govt_functions()],
    }

    response_yaml = yaml.safe_dump(context, default_flow_style=False, encoding='utf-8')
    return HttpResponse(response_yaml, content_type='text/x-yaml')


def dataset_list(request, financial_year_id):
    context = {
        'financial_years': [],
        'selected_financial_year': financial_year_id,
        'datasets': [],
    }

    selected_year = None
    for year in FinancialYear.objects.order_by('slug'):
        is_selected = year.slug == financial_year_id
        if is_selected:
            selected_year = year
        context['financial_years'].append({
            'id': year.slug,
            'is_selected': is_selected,
            'closest_match': {
                'is_exact_match': True,
                'name': 'Datasets',
                'slug': 'datasets',
                'organisational_unit': 'financial_year',
                'url_path': "%s/datasets" % year.slug,
            },
        })

    for dataset in selected_year.get_contributed_datasets():
        context['datasets'].append({
            'url_path': dataset.get_url_path(),
            'slug': dataset.slug,
        })

    response_yaml = yaml.safe_dump(context, default_flow_style=False, encoding='utf-8')
    return HttpResponse(response_yaml, content_type='text/x-yaml')


def dataset(request, financial_year_id, dataset_slug):
    context = {
        'financial_years': [],
        'selected_financial_year': financial_year_id,
    }

    for year in FinancialYear.objects.order_by('slug'):
        is_selected = year.slug == financial_year_id
        if is_selected:
            dataset = Dataset.fetch(year, dataset_slug)

            context['financial_years'].append({
                'id': year.slug,
                'is_selected': is_selected,
                'closest_match': {
                    'is_exact_match': True,
                    'name': dataset.name,
                    'slug': dataset.slug,
                    'organisational_unit': 'dataset',
                    'url_path': dataset.get_url_path(),
                },
            })
        else:
            context['financial_years'].append({
                'id': year.slug,
                'is_selected': is_selected,
                'closest_match': {
                    'is_exact_match': False,
                    'name': year.slug,
                    'slug': year.slug,
                    'organisational_unit': 'financial_year',
                    'url_path': year.get_url_path(),
                },
            })

    context.update({
        'slug': dataset.slug,
        'name': dataset.name,
        'resources': dataset.resources,
        'organization': dataset.get_organization(),
        'author': dataset.author,
        'created': dataset.created_date,
        'last_updated': dataset.last_updated_date,
        'license': dataset.license,
        'intro': dataset.intro,
        'methodology': dataset.methodology,
    })

    response_yaml = yaml.safe_dump(context, default_flow_style=False, encoding='utf-8')
    return HttpResponse(response_yaml, content_type='text/x-yaml')
