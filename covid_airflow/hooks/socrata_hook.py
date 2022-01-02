from airflow.hooks.base_hook import BaseHook
from sodapy import Socrata


class SocrataHook(BaseHook):
    """Custom hook that returns a Socrata connection instance.
    Requires connection in Airflow with name of SOCRATA_CONN value.
    """

    SOCRATA_CONN = "http_socrata"

    def __init__(self, *, socrata_conn_id: str = SOCRATA_CONN, **kwargs):
        """Initializes Socrata hook

        :param socrata_conn_id: Name of Airflow connection to use,
        defaults to SOCRATA_CONN
        :type socrata_conn_id: str, optional
        """
        self.conn_id = socrata_conn_id
        super().__init__(**kwargs)

    def get_conn(self):
        """Returns Socrata connection

        :return: Socrata instance
        :rtype: Socrata
        """
        conn = self.get_connection(self.conn_id)
        return Socrata(
            conn.host,
            conn.extra_dejson["app_token"],
            conn.login,
            conn.password
        )
