

class parameters():

    prog_name = "generator"

    # set up your own path here
    root_path = "/home/leo_lin_colab/FinQA-main/"
    output_path = "path_to_store_outputs/finqa_normal"  # finqa_normal
    cache_dir = "path_for_other_cache/finqa_normal"  # finqa_normal

    model_save_name = "bert-base"

    train_file = root_path + "dataset/train.json"  # train_toy.json
    valid_file = root_path + "dataset/dev.json"  # dev_toy.json
    test_file = root_path + "dataset/test.json"  # test_toy.json

    ### files from the retriever results
    # train_file = root_path + "dataset/train_toy_retrieve.json"
    # valid_file = root_path + "dataset/dev_toy_retrieve.json"
    # test_file = root_path + "dataset/test_toy_retrieve.json"

    # infer table-only text-only
    # test_file = root_path + "dataset/test_retrieve_7k_text_only.json"

    op_list_file = "operation_list.txt"
    const_list_file = "constant_list.txt"

    # # model choice: bert, roberta, albert
    # pretrained_model = "bert"
    # model_size = "bert-base-uncased"

    # model choice: bert, roberta, albert
    pretrained_model = "roberta"
    model_size = "roberta-large"

    # # finbert
    # pretrained_model = "finbert"
    # model_size = root_path + "pre-trained-models/finbert/"

    # pretrained_model = "longformer"
    # model_size = "allenai/longformer-base-4096"

    # single sent or sliding window
    # single, slide, gold, none
    retrieve_mode = "gold"

    # use seq program or nested program
    program_mode = "seq"

    # train or test
    device = "cuda"
    mode = "train"  # train
    saved_model_path = output_path + "/bert-base_20211209130805/saved_model/loads/51/model.pt"
    # saved_model_path = output_path + "/bert-base_20211209024546/saved_model/loads/42/model.pt"  # change this part
    build_summary = False

    sep_attention = True
    layer_norm = True
    num_char = False  # if false, run original finqa baseline
    
    num_decoder_layers = 1
    num_encoder_layers = 1
    
    max_seq_length = 512 # 2k for longformer, 512 for others
    max_program_length = 30
    max_num_length = 10
    num_emb_dim = 300
    n_best_size = 20
    dropout_rate = 0.1

    batch_size = 12  # 16
    batch_size_test = 12  # 16
    epoch = 300
    learning_rate = 2e-5

    report = 300
    report_loss = 100

    max_step_ind = 11
