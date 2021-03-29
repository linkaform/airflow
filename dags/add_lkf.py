from airflow.models import DagBag
import os

lkf_dir = os.getcwd() + '/dags_lkf'
dag_bag = DagBag(lkf_dir)

if dag_bag:
   for dag_id, dag in dag_bag.dags.items():
      globals()[dag_id] = dag

