import os

command = 'python run_classifier.py --data_dir /nfs/guille/eecs_research/soundbendor/beerya/CS-579/BERT-Attack/datasets/adversary_training_corpora/fake ' \
          '--bert_model bert-base-uncased --max_seq_length 256 --train_batch_size 16 ' \
          '--task_name fake --output_dir results/fake --cache_dir pytorch_cache --do_train  --do_eval --do_lower_case '

os.system(command)
