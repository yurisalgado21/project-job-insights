from typing import List, Dict
import csv


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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
