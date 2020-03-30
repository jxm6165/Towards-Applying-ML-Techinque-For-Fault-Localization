# Towards Applying ML Techinque For Fault Localization

Github Repository for Paper "Towards Applying Machine Learning Technique For Fault Localization" as the Undergraduate Honor Thesis

*Note: Step 1 to Step 4 are preprocessing parts. To start training and testing immediately, we can start from Step 5 with `.csv` files in either [Function_Level_Dataset](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/tree/master/Function_Level_Dataset) or [Block_Level_Dataset](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/tree/master/Block_Level_Dataset).*

## Step 1: Source Code Database
* Download the source code collection from Defects4J project.

  [Defects4J](https://github.com/rjust/defects4j)

* Use `checkout` command to retrieve all buggy and fixed versions.

  e.g. `defects4j checkout -p Lang -v 1b -w /tmp/lang_1_buggy`

* Extract function level and block level source code snippets.

  The LLVM Pass for function level is called [`Function_Extract_Pass.cpp`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Code_Snippet_Extarction/Function_Extract_Pass.cpp), and that for block level is called [`Block_Extract_Pass.cpp`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Code_Snippet_Extarction/Block_Extract_Pass.cpp). Make and compile each project using LLVM. The result will be printed to stdout. According to [`clean_buggy_lines`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/clean_buggy_lines) and [`clean_fixed_lines`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/clean_fixed_lines), we can allocate the source files in projects. We can then easily write a script to split the functions into single files with extension called `.infunc` and similar for blocks called `.block`. The extensions are just to ensure the consistency between our scripts.

* Remove Duplicates.
  
  Since there are duplicated files containing the same code snippet. We need to remove the duplicated ones. Run [`clean_dup.py`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/clean_dup.py) several times until there is no more duplicate.
 
* Store the source file seperately in directories.

  To keep track with the classes for code snippets. We can store the functions with buggy lines in a directory call `BuggyFunctions` and unsuspicious ones in `GoodFunctions`. Blocks are similar.
  
## Step 2: Code Vector Transformance

* Download and Install the dependencies for [code2vec](https://github.com/tech-srl/code2vec) project. 

  It is easier for us to download the trained model, e.g. [java14m_model](https://s3.amazonaws.com/code2vec/model/java14m_model_trainable.tar.gz) to generate the code vectors for our code snippets.

* Replace `interactive_predict.py` in code2vec project with [`interactive_predict.py`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/interactive_predict.py) provided in this repository.

  This step is to enable recursive prediction of files in one directory. 
 
* Start Prediction and Get Vectors.

 To start predict the code snippet files. Modify [`interactive_predict.py`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/interactive_predict.py) to change the directory into that storing code snippet files.
 
 Then, run 
 ```bash
 python3 code2vec.py --load models/java14_model/saved_model_iter8.release --export_code_vectors --predict > vectors.log
 ```
 We will get code vectors corresponding to each code snippet in that directory saved in `vectors.log`.
 
* Split to Seperate Files.

  Then, modify and run [`splitfiles.py`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/splitfiles.py). We will get seperate `.vectors` files which each contains a single vector with respect to one code snippet.

## Step 3: Train and Test Split

* Migrate `.vectors` Files.

  Put the `.vectors` files into `Data/` Directory. If the vectors are corresponding to buggy code snippets, put them into `Data/0/`. Otherwise, put them into `Data/1/`.
 
* Split Train and Test Sets

  Run [`train_test_split.py`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/train_test_split.py). Now, we can see that either `Data/0/` or `Data/1/` directory will contain two generated directories called `/train/` and `test/`.
  
## Step 4: Generate Dataset

  Open and run [`Dataset_Generation.ipynb`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Dataset_Generation.ipynb). Now we can see four new `.csv` files are produced.

  Or we can use the provided `.csv` files in either [Function_Level_Dataset](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/tree/master/Function_Level_Dataset) or [Block_Level_Dataset](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/tree/master/Block_Level_Dataset).

## Step 5: Training and Testing

* Function Level

  Open and run [`Function_Models_1.ipynb`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Function_Models_1.ipynb) and [`Function_Models_2.ipynb`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Function_Models_2.ipynb). Function_Models_1.ipynb contains LR, NB, SGD, RF, DT and kNN models. Function_Models_2.ipynb contains SVM and MLP models. We can use `.csv` files in [Function_Level_Dataset](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/tree/master/Function_Level_Dataset) or generated from Step 4.

* Block Level

  Open and run [`Block_Models_1.ipynb`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Block_Models_1.ipynb) and [`Block_Models_2.ipynb`](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Block_Models_2.ipynb). Block_Models_1.ipynb contains LR, NB, SGD, RF, DT and kNN models. Block_Models_2.ipynb contains SVM and MLP models. We can use `.csv` files in [Block_Level_Dataset](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/tree/master/Block_Level_Dataset) or generated from Step 4.

## More Resources about LLVM

- Ammar Ben Khadra LLVM Pass Tutorial ([link](https://github.com/abenkhadra/llvm-pass-tutorial/blob/master/README.md))
- Adrian Sampson's blog entry "LLVM for Grad Students" ([link](http://adriansampson.net/blog/llvm.html))
- LLVM documentation: Writing an LLVM pass ([link](http://llvm.org/docs/WritingAnLLVMPass.html))
- LLVM documentation: Building LLVM with CMake ([link](http://llvm.org/docs/CMake.html#cmake-out-of-source-pass))
