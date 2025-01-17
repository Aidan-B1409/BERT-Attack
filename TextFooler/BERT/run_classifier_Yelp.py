import os

command = 'python run_classifier.py --data_dir /nfs/guille/eecs_research/soundbendor/beerya/CS-579/BERT-Attack/datasets/adversary_training_corpora/yelp ' \
          '--bert_model bert-base-uncased --max_seq_length 128 --train_batch_size 32 ' \
          '--task_name yelp --output_dir results/yelp --cache_dir pytorch_cache --do_train  --do_eval --do_lower_case ' \
          '--num_train_epochs 2.'

os.system(command)
