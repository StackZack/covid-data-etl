from airflow.models.baseoperator import BaseOperator
from hooks.socrata_hook import SocrataHook
import pandas as pd


class SocrataOperator(BaseOperator):
    """Interacts with Socrata to load data and save to CSV file
    """

    def __init__(self, data_id: str, file_dir: str, **kwargs) -> None:
        """Initializes Socrata operator

        :param data_id: unique identifier for Socrata data set
        :type data_id: str
        :param file_dir: path to save file locally
        :type file_dir: str
        """
        self.data_id = data_id
        self.file_dir = file_dir
        super().__init__(**kwargs)

    def execute(self):
        """Execute main method for Socrata operator
        """
        socrata_instance = SocrataHook.get_conn()
        response_data = socrata_instance.get(self.data_id)
        df_data = pd.DataFrame.from_records(response_data)
        df_data.to_csv(self.file_dir)
