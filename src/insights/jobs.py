from typing import List, Dict
import csv

jobs = [
    {"id": 1, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 2, "industry": "Healthcare", "job_type": "PART_TIME"},
]


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            dict_csv = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in dict_csv:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        list_type_jobs = []
        for row in self.jobs_list:
            if not row["job_type"] in list_type_jobs:
                list_type_jobs.append(row["job_type"])

        return list_type_jobs

    def filter_by_multiple_criteria(
        self, list_dict_jobs, filter_criteria
    ) -> List[dict]:
        filters_jobs = []
        if type(filter_criteria) is not dict:
            raise TypeError
        for job in list_dict_jobs:
            if (
                job["industry"] == filter_criteria["industry"]
                and job["job_type"] == filter_criteria["job_type"]
            ):
                filters_jobs.append(job)
        return filters_jobs
