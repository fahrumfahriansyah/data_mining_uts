# data
company_name_list = [{'name': 'Company 1'},
          {'name': 'Company 2'},
          {'name': 'Company 3'}]

employee_name_list = [{'name': 'John Doe'},
          {'name': 'Tom Smith'},
          {'name': 'Andrew Sebastian'}]

company_detail_list = {
      'Company 1': {
          'name': 'Company 1',
          'domain': 'Retail',
          'clients': [
              {
                  'name': 'acme.inc',
                  'country': 'united states'
              },
              {
                  'name': 'Wayne.co',
                  'country': 'united states'
              }
          ]
      },
      'Company 2': {
          'name': 'Company 2',
          'domain': 'Construction',
          'clients': [
              {
                  'name': 'Tesla',
                  'country': 'united states'
              },
              {
                  'name': 'Japan Airlines',
                  'country': 'japan'
              },
              {
                  'name': 'Indofood',
                  'country': 'indonesia'
              }
          ]
      },
      'Company 3': {
          'name': 'Company 3',
          'domain': 'Healthcare',
          'clients': [
              {
                  'name': 'Petronas',
                  'country': 'malaysia'
              },
              {
                  'name': 'VW Group',
                  'country': 'germany'
              },
              {
                  'name': 'IBM',
                  'country': 'united states'
              },
              {
                  'name': 'Mitsubishi',
                  'country': 'japan'
              }
          ]
      }
  }

employee_detail_list = {
      'John Doe': {
          'name': 'EMP-0001',
          'first_name': 'John',
          'last_name': 'Doe',
          'full_name': 'John Doe',
          'company': 'Company 1'
      },
      'Tom Smith': {
          'name': 'EMP-0002',
          'first_name': 'Tom',
          'last_name': 'Smith',
          'full_name': 'Tom Smith',
          'company': 'Company 2'
      },
      'Andrew Sebastian': {
          'name': 'EMP-0003',
          'first_name': 'Andrew',
          'last_name': 'Sebastian',
          'full_name': 'Andrew Sebastian',
          'company': 'Company 2'
      },
  }

# 1
# Please get the list of all Companies and sort by Company Domain in reverse order.
def sort_company():
    sorted_companies = sorted(company_detail_list.values(), key=lambda x: x['domain'], reverse=True)
    return [{"name": company['name'], "domain": company['domain']} for company in sorted_companies]

# 2
# Please print all Domain value in every company.
def get_company_domain():
    for company in company_detail_list.values():
        num_clients = len(company['clients'])
        print(f"{company['name']}: {company['domain']}, relation: {num_clients} clients")

# 3
# Create a function that return employees with it's company domain.
def get_employees():
    employees = []
    for employee_detail in employee_detail_list.values():
        company_name = employee_detail['company']
        domain = company_detail_list[company_name]['domain']
        employees.append({
            "full_name": employee_detail['full_name'],
            "company": company_name,
            "domain": domain
        })
    return employees

# 4
# Create a function that return companies with list of employees that are working in the company.
def get_employees_by_company():
    employees_by_company = []
    for company_name in company_detail_list:
        employees = [employee_detail['full_name'] for employee_detail in employee_detail_list.values() if employee_detail['company'] == company_name]
        employees_by_company.append({
            "company": company_name,
            "employees": employees
        })
    return employees_by_company


print("Sorted Companies:")
print(sort_company())
print("\nCompany Domain:")
get_company_domain()
print("\nEmployees with Company Domain:")
print(get_employees())
print("\nEmployees by Company:")
print(get_employees_by_company())
