import os

command = 'python run_classifier.py --data_dir ../../datasets/adversarial_training_corpora/ag ' \
          '--bert_model bert-base-uncased ' \
          '--task_name ag --output_dir results/ag --cache_dir pytorch_cache --do_train  --do_eval --do_lower_case '

os.system(command)
