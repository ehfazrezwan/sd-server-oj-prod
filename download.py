# In this file, we define download_model
# It runs during container build time to get model weights built into the container
import os
import time
import torch
from diffusers import StableDiffusionPipeline


def download_model():
    # do a dry run of loading the huggingface model, which will download weights at build time
    # this is done to avoid downloading weights at runtime, which would cause a cold start
    # and slow down the first request

    # model_id is the HuggingFace model ID that you set in the Banana Console
    # i.e. in "Build Arguments" on your model settings page. Defaults to OpenJourney v4
    model_id = "prompthero/openjourney-v4"
    t1 = time.time()
    model = StableDiffusionPipeline.from_pretrained(model_id)
    t2 = time.time()
    print("Download took - ", t2 - t1, "seconds")


if __name__ == "__main__":
    download_model()
