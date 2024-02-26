from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        list_new = []
        for row in self.jobs_list:
            if len(row["max_salary"]) != 0 and row["max_salary"].isdigit():
                salary = int(row["max_salary"])
                list_new.append(salary)
        max_salary = max(list_new)
        return max_salary

    def get_min_salary(self) -> int:
        list_new = []
        for row in self.jobs_list:
            if len(row["min_salary"]) != 0 and row["min_salary"].isdigit():
                salary = int(row["min_salary"])
                list_new.append(salary)
        min_salary = min(list_new)
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            if int(job["min_salary"]) > int(job["max_salary"]):
                raise ValueError

            return job["min_salary"] <= int(salary) <= job["max_salary"]
        except (TypeError, KeyError, ValueError):
            raise ValueError

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        new_list = []
        for job in jobs:
            result = self.matches_salary_range(job, salary)
            if result:
                new_list.append(job)
        return new_list.sort()
