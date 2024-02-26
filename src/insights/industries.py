from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        list_unique_industries = []
        for row in self.jobs_list:
            if (
                not row["industry"] in list_unique_industries
                and len(row["industry"]) != 0
            ):
                list_unique_industries.append(row["industry"])
        return list_unique_industries
