from airflow.hooks.base_hook import BaseHook
from sodapy import Socrata


class SocrateHook(BaseHook):
    """Custom hook that returns a Socrata connection instance.
    Requires connection in Airflow with name of SOCRATA_CONN value.
    """
    SOCRATA_CONN = "http_socrata"

    def get_conn(self):
        """Returns Socrata connection.

        :return: Socrata instance
        :rtype: Socrata
        """
        conn = self.get_connection(self.SOCRATA_CONN)
        return Socrata(
            conn.host,
            conn.extra_dejson["app_token"],
            conn.login,
            conn.password
        )
