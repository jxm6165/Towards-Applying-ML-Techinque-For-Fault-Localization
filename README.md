# Towards Applying ML Techinque For Fault Localization
Github Repository for Paper "Towards Applying Machine Learning Technique For Fault Localization" as the Undergraduate Honor Thesis

## Step 1: Source Code Database
* Download the source code collection from Defects4J project.

  [Defects4J](https://github.com/rjust/defects4j)

* Use `checkout` command to retrieve all buggy and fixed versions.

  e.g. `defects4j checkout -p Lang -v 1b -w /tmp/lang_1_buggy`

* Extract function level and block level source code snippets.

  The LLVM Pass for function level is called [Function_Extract_Pass.cpp](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Code_Snippet_Extarction/Function_Extract_Pass.cpp), and that for block level is called [Block_Extract_Pass.cpp](https://github.com/jxm6165/Towards-Applying-ML-Techinque-For-Fault-Localization/blob/master/Code_Snippet_Extarction/Block_Extract_Pass.cpp) The result will be printed to stdout. In this case, we can easily write a script to split the functions into single files with extension called `.infunc` and similar for blocks called `.block`. The extensions are just to ensure the consistency between our scripts.

* Remove Duplicates
  
  Since there are duplicated files containing the same code snippet. We need to remove the duplicated ones. Run `clean_dup.py` several times until there is no more duplicate.
 

