"""Tests for utils."""

from google_cloud_pipeline_components.experimental.automl.tabular import utils
import unittest


class UtilsTest(unittest.TestCase):

  def test_input_dictionary_to_parameter_none(self):
    self.assertEqual(utils.input_dictionary_to_parameter(None), '')

  def test_input_dictionary_to_parameter_dict(self):
    self.assertEqual(
        utils.input_dictionary_to_parameter({'foo': 'bar'}),
        r'{\"foo\": \"bar\"}')

  def test_get_skip_evaluation_pipeline_and_parameters(self):
    _, parameter_values = utils.get_skip_evaluation_pipeline_and_parameters(
        'project', 'us-central1', 'gs://foo', 'target', 'classification',
        'maximize-au-prc', {'auto': {
            'column_name': 'feature_1'
        }}, {
            'fraction_split': {
                'training_fraction': 0.8,
                'validation_fraction': 0.2,
                'test_fraction': 0.0
            }
        }, {'csv_data_source': {
            'csv_filenames': ['gs://foo/bar.csv']
        }}, 1000)
    self.assertEqual(
        parameter_values, {
            'project':
                'project',
            'location':
                'us-central1',
            'image_uri':
                'us-docker.pkg.dev/vertex-ai-restricted/automl-tabular/training:prod',
            'prediction_image_uri':
                'us-docker.pkg.dev/vertex-ai/automl-tabular/prediction-server:prod',
            'dataflow_worker_image_uri':
                'us-docker.pkg.dev/vertex-ai/automl-tabular/dataflow-worker:prod',
            'root_dir':
                'gs://foo',
            'target_column_name':
                'target',
            'prediction_type':
                'classification',
            'optimization_objective':
                'maximize-au-prc',
            'transformations':
                '{\\"auto\\": {\\"column_name\\": \\"feature_1\\"}}',
            'split_spec':
                '{\\"fraction_split\\": {\\"training_fraction\\": 0.8, \\"validation_fraction\\": 0.2, \\"test_fraction\\": 0.0}}',
            'data_source':
                '{\\"csv_data_source\\": {\\"csv_filenames\\": [\\"gs://foo/bar.csv\\"]}}',
            'stage_1_deadline_hours':
                0.7708333333333334,
            'stage_1_num_parallel_trials':
                35,
            'stage_1_num_selected_trials':
                7,
            'stage_1_single_run_max_secs':
                634,
            'reduce_search_space_mode':
                'minimal',
            'stage_2_deadline_hours':
                0.22916666666666663,
            'stage_2_num_parallel_trials':
                35,
            'stage_2_num_selected_trials':
                5,
            'stage_2_single_run_max_secs':
                634,
            'weight_column_name':
                '',
            'optimization_objective_recall_value':
                -1,
            'optimization_objective_precision_value':
                -1,
            'study_spec_override':
                '',
            'stage_1_tuner_worker_pool_specs_override':
                '',
            'cv_trainer_worker_pool_specs_override':
                '',
            'export_additional_model_without_custom_ops':
                False,
            'stats_and_example_gen_dataflow_machine_type':
                'n1-standard-16',
            'stats_and_example_gen_dataflow_max_num_workers':
                25,
            'stats_and_example_gen_dataflow_disk_size_gb':
                40,
            'transform_dataflow_machine_type':
                'n1-standard-16',
            'transform_dataflow_max_num_workers':
                25,
            'transform_dataflow_disk_size_gb':
                40,
            'encryption_spec_key_name':
                ''
        })

  def test_get_skip_architecture_search_pipeline_and_parameters(self):
    _, parameter_values = utils.get_skip_architecture_search_pipeline_and_parameters(
        'project', 'us-central1', 'gs://foo', 'target', 'classification',
        'maximize-au-prc', {'auto': {
            'column_name': 'feature_1'
        }}, {
            'fraction_split': {
                'training_fraction': 0.8,
                'validation_fraction': 0.2,
                'test_fraction': 0.0
            }
        }, {'csv_data_source': {
            'csv_filenames': ['gs://foo/bar.csv']
        }}, 1000, 'gs://bar')
    self.assertEqual(
        parameter_values, {
            'cv_trainer_worker_pool_specs_override':
                '',
            'data_source':
                '{\\"csv_data_source\\": {\\"csv_filenames\\": [\\"gs://foo/bar.csv\\"]}}',
            'dataflow_worker_image_uri':
                'us-docker.pkg.dev/vertex-ai/automl-tabular/dataflow-worker:prod',
            'encryption_spec_key_name':
                '',
            'export_additional_model_without_custom_ops':
                False,
            'image_uri':
                'us-docker.pkg.dev/vertex-ai-restricted/automl-tabular/training:prod',
            'location':
                'us-central1',
            'optimization_objective':
                'maximize-au-prc',
            'optimization_objective_precision_value':
                -1,
            'optimization_objective_recall_value':
                -1,
            'prediction_image_uri':
                'us-docker.pkg.dev/vertex-ai/automl-tabular/prediction-server:prod',
            'prediction_type':
                'classification',
            'project':
                'project',
            'root_dir':
                'gs://foo',
            'split_spec':
                '{\\"fraction_split\\": {\\"training_fraction\\": 0.8, \\"validation_fraction\\": 0.2, \\"test_fraction\\": 0.0}}',
            'stage_1_tuning_result_artifact_uri':
                'gs://bar',
            'stage_2_deadline_hours':
                1.0,
            'stage_2_num_parallel_trials':
                35,
            'stage_2_num_selected_trials':
                5,
            'stage_2_single_run_max_secs':
                2769,
            'stats_and_example_gen_dataflow_machine_type':
                'n1-standard-16',
            'stats_and_example_gen_dataflow_max_num_workers':
                25,
            'target_column_name':
                'target',
            'transform_dataflow_machine_type':
                'n1-standard-16',
            'transform_dataflow_max_num_workers':
                25,
            'transformations':
                '{\\"auto\\": {\\"column_name\\": \\"feature_1\\"}}',
            'weight_column_name':
                ''
        })


if __name__ == '__main__':
  unittest.main()
