from airflow.models.baseoperator import BaseOperator
from hooks.socrata_hook import SocrataHook
from datetime import datetime
import pandas as pd
import os


class SocrataOperator(BaseOperator):
    """Interacts with Socrata to load data and save to CSV file"""

    def __init__(self, data_id: str, file_dir: str, **kwargs) -> None:
        """Initializes Socrata operator

        :param data_id: unique identifier for Socrata data set
        :type data_id: str
        :param file_dir: path to directory to save file
        :type file_dir: str
        """
        self.data_id = data_id
        self.file_dir = file_dir
        super().__init__(**kwargs)

    def execute(self, context):
        """Execute main method for Socrata operator.
        Performs xcom_push to key 'soc_file_path' with path to local CSV
        """
        socrata_instance = SocrataHook.get_conn()
        response_data = socrata_instance.get(self.data_id)
        df_data = pd.DataFrame.from_records(response_data)
        time_stamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "_".join(self.data_id, time_stamp) + '.csv'
        file_path = os.path.join(self.file_dir, file_name)
        df_data.to_csv(file_path)
        self.xcom_push(context=context, key='soc_file_path', value=file_path)
