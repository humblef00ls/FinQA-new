# cs 590 Final Project 2021 Fall
Our project is to improve the baseline of FinQA task which proposed by the paper the FinQA dataset and code from EMNLP 2021 paper: FinQA: A Dataset of Numerical Reasoning over Financial Data
<https://arxiv.org/abs/2109.00122>

![alt text](https://github.com/czyssrs/FinQA/blob/main/eg-intro.png?raw=true)

This repo is based on <https://github.com/czyssrs/FinQA>.

## Requirements:

- pytorch 1.7.1
- huggingface transformers 4.4.2

## Dataset
The dataset is stored as json files in folder "dataset", each entry has the following format:

```
"pre_text": the texts before the table;
"post_text": the text after the table;
"table": the table;
"id": unique example id. composed by the original report name plus example index for this report. 

"qa": {
  "question": the question;
  "program": the reasoning program;
  "gold_inds": the gold supporting facts;
  "exe_ans": the gold execution result;
  "program_re": the reasoning program in nested format;
}
```

## Code

### The generator
Go to folder "generator".

#### Train
First we need to convert the results from the retriever to the files used for training. Edit the main entry in Convert.py to set the file paths to the retriever results path you specified in the previous step - for all 3 train, dev, and test files. Then run:

```
python Convert.py
```

to generate the train, dev, test files for the generator. 

Edit other parameters in config.py, like your project path, data path, the saved model name, etc. To train the generator, run:

```
sh run.sh
```

You can observe the dev performance to select the checkpoint. 

#### Inference
To run inference, edit config.py to change "mode" to "test", "saved_model_path" to the path of your selected checkpoint in the training, and "model_save_name" to the name of the folder to save the result files. Then run:

```
python Test.py
```

It will generate the result files in the created folder. 


## Citation
If you find this project useful, please cite it using the following format

```
@article{chen2021finqa,
  title={FinQA: A Dataset of Numerical Reasoning over Financial Data},
  author={Chen, Zhiyu and Chen, Wenhu and Smiley, Charese and Shah, Sameena and Borova, Iana and Langdon, Dylan and Moussa, Reema and Beane, Matt and Huang, Ting-Hao and Routledge, Bryan and Wang, William Yang},
  journal={Proceedings of EMNLP 2021},
  year={2021}
}
```
