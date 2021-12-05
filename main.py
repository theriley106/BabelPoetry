import gpt_2_simple as gpt2
import os
import requests

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/



sess = gpt2.start_tf_sess()
# sess = gpt2.start_tf_sess()
# gpt2.load_gpt2(sess)
gpt2.finetune(sess,
              "all.txt",
              run_name="poetry.txt",
              model_name=model_name,
              steps=1000)   # steps is max number of training steps

gpt2.generate(sess)

#single_text = gpt2.generate(sess, return_as_list=True)[0]
#print(single_text)