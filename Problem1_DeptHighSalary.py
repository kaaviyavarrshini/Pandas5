import pandas as pd

#Soln 1 : Using MAX
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    maxsalary=employee.groupby('departmentId')['salary'].transform(max)
    employee=employee[employee['salary']==maxsalary] # type: ignore
    df=employee.merge(department,left_on='departmentId',right_on='id',how='left')
    return df[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})     # type: ignore

#SOLN2: Using Rank
    df=employee.merge(department,left_on='departmentId',right_on='id',how='left')
    df['rank']=df.groupby('departmentId')['salary'].rank(method='dense',ascending=False)
    df=df[df['rank']==1]   
    return df[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})