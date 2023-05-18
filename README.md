<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ehfazrezwan/sd-serverless-template">
    <img src="./images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Stable Diffusion Serverless Template</h3>

  <p align="center">
    Stable Diffusion model template for Banana's serverless GPU platform.
    <br />
    <a href="https://github.com/ehfazrezwan/sd-serverless-template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ehfazrezwan/sd-serverless-template">View Demo</a>
    ·
    <a href="https://github.com/ehfazrezwan/sd-serverless-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/ehfazrezwan/sd-serverless-template/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
        <ul>
            <li><a href="#optimizations">Optimizations</a></li>
            <li><a href="#testing-your-model">Testing your model</a></li>
        </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This is a template file for deploying Stable Diffusion models on banana.dev - a platform that allows you to run inference on GPUs without having to worry about the infrastructure. Banana is a serverless platform that allows you to deploy your models in a few clicks. You can learn more about Banana [here](https://docs.banana.dev/banana-docs/quickstart).

For those new to serverless, allow me to explain its role in my use case. I wanted to allow users of my site to generate images using Stable Diffusion models, however, keeping a GPU server running 24/7 is expensive. So I decided to use a serverless platform. This way, I only pay for the time my model is running, and I don't have to worry about the infrastructure. I can just focus on the model. For reference, my total bill for 800 image generations over a period of a month was only $5.00. Compare that with platforms like rundiffusion, which charges $0.5/hr at their lowest tier, and you can see why I chose to go with a serverless platform.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [Stable Diffusion](https://stablediffusionweb.com/)
- [Banana](https://banana.dev/)
- [Python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

As mentioned above, this is a model template that you will deploy on Banana. While you can go through their docs for a more detailed explanation, I will provide a brief overview of the steps here.

### Prerequisites

- Create an account on banana.dev
- Link your payment method to your account (although they do offer free credits for new users)
- Once ready, move on to the usage section below

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

1. Fork or clone this repository
2. Go back to the banana dashboard, link your GitHub account, and provide permission to banana to access the repository you just forked/cloned
   1. On your Banana dashboard, click on the "Team" tab on the left sidebar
   2. You should now see an option to Manage your GitHub account. Click on that and follow the instructions to link your GitHub account and/or provide permission to banana to access your repository
3. Click on the "Deploy" tab on the left sidebar. Choose "Deploy from GitHub" and select the repository you just forked/cloned
4. That's it! If everything goes according to plan, you should be redirected to the model page, where you can keep track of its build progress. I've noticed that the first deploy always takes a while, around 45 minutes.
5. Once the model is deployed, you can go to the "Settings" tab and add build arguments. Do this if you want to change the MODEL_ID - a unique identifier for your model, which you will find on the HuggingFace model page - since this template downloads the models from HuggingFace.

### Optimizations

Here are some optimizations that I've found to be useful:

1. Turn on Turboboot
   1. Once your model is deployed, go to the "Settings" tab and turn on Turboboot
   2. This will allow your model to start up much faster, reducing cold start times
2. Change other settings as you see fit, but I've found the default parameters to be balanced enough for my use case

### Testing your model

After deploying the model, you can now use Banana's API to start the inference engine i.e. the generation and download of images. It's a simple REST API, so feel free to use either the code on `test.py` which includes some default code (modify the input arguments as you see fit). You may also use the provided Postman collection to test your model.

You will notice that you'll need your banana.dev API Key and Model Key, both of which you will find on the Banana dashboard. Another thing to note is that there are essentially two ways to call the API:

1. Get image result back in the same call you use to start the inference engine

   1. This is the default behavior, where you will get the image result back in the same call you use to start the inference engine. This means that you will have to wait a while to get a response back (around 45 seconds on average for a 512x512 image with no other generation in queue).
   2. I find this method difficult to handle exceptions for, especially at scale where you have multiple users in the queue waiting for their generation. The call times out after 60 secnds, so you may get the image back, or you might get back a Call ID, if the inference engine hasn't finished processing the image yet.
   3. **Example payload**:
      <br/>
      <br/>

   ```
   POST https://api.banana.dev/start/v4/
   ```

   ```json
   {
       "apiKey": "{{apiKey}}",
       "modelKey": "{{modelKey}}",
       "startOnly": false,
       "modelInputs": {
           "prompt": "nightclub",
           ...other model inputs
           }
   }
   ```

   4. **Example Output**:
      <br/>
      <br/>

   **Inference engine still running**:

   ```json
   {
     "id": "de874913-cf15-43ba-84be-f8b1121b62b0",
     "message": "",
     "created": 1684444779,
     "apiVersion": "January 11, 2023",
     "callID": "call_0d82c386-cb9f-4da6-89b4-236c4b69bb47",
     "finished": false,
     "modelOutputs": null
   }
   ```

   **Inference complete**:

   ```json
   {
     "id": "3b0fc375-6b0c-4552-bacc-5340a61e66d5",
     "message": "success",
     "created": 1684445192,
     "apiVersion": "January 11, 2023",
     "modelOutputs": [
       {
         "image_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAA"
       }
     ]
   }
   ```

2. Get image result back in a separate call

   1. This is the method I prefer, where you get back a Call ID in the same call you use to start the inference engine. You can then use this Call ID to get the image result back in a separate call.
   2. This way, you can handle exceptions much better, since you can just keep polling the API until you get back the image result.
   3. **Example request/response**:
      <br/>
      <br/>

   **Start inference engine**

   ```
   POST https://api.banana.dev/start/v4/
   ```

   ```json
   {
       "apiKey": "{{apiKey}}",
       "modelKey": "{{modelKey}}",
       "startOnly": true,
       "modelInputs": {
           "prompt": "nightclub",
           ...other model inputs
           }
   }
   ```

   **Example Output**:

   ```json
   {
     "id": "a2394a1a-003c-4d99-a7f6-e8bb9fcb3fe3",
     "message": "",
     "created": 1684444926,
     "apiVersion": "January 11, 2023",
     "callID": "call_3612a41d-f033-4a3a-866e-f5eb4fed60e3",
     "finished": false,
     "modelOutputs": null
   }
   ```

   **Get image result**

   ```
   POST https://api.banana.dev/check/v4
   ```

   ```json
   {
     "apiKey": "{{apiKey}}",
     "callID": "{{callID}}",
     "longPoll": false
   }
   ```

   **Example Output (Inference still running)**:

   ```json
   {
     "id": "63fd9e3c-9903-47af-921a-edd93d10897b",
     "message": "running",
     "created": 1684445127,
     "apiVersion": "January 11, 2023",
     "modelOutputs": null
   }
   ```

   **Example Output (Inference complete)**:

   ```json
   {
     "id": "3b0fc375-6b0c-4552-bacc-5340a61e66d5",
     "message": "success",
     "created": 1684445192,
     "apiVersion": "January 11, 2023",
     "modelOutputs": [
       {
         "image_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAA"
       }
     ]
   }
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Comprehensive logging
- [ ] Img2Img models
- [ ] ControlNet

See the [open issues](https://github.com/ehfazrezwan/sd-serverless-template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Ehfaz Rezwan - [@siliconinjax](https://twitter.com/siliconinjax) - ehfaz.rezwan@gmail.com

Project Link: [https://github.com/ehfazrezwan/sd-serverless-template](https://github.com/ehfazrezwan/sd-serverless-template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/ehfazrezwan/sd-serverless-template.svg?style=for-the-badge
[contributors-url]: https://github.com/ehfazrezwan/sd-serverless-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ehfazrezwan/sd-serverless-template.svg?style=for-the-badge
[forks-url]: https://github.com/ehfazrezwan/sd-serverless-template/network/members
[stars-shield]: https://img.shields.io/github/stars/ehfazrezwan/sd-serverless-template.svg?style=for-the-badge
[stars-url]: https://github.com/ehfazrezwan/sd-serverless-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/ehfazrezwan/sd-serverless-template.svg?style=for-the-badge
[issues-url]: https://github.com/ehfazrezwan/sd-serverless-template/issues
[license-shield]: https://img.shields.io/github/license/ehfazrezwan/sd-serverless-template.svg?style=for-the-badge
[license-url]: https://github.com/ehfazrezwan/sd-serverless-template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ehfaz-rezwan
[product-screenshot]: images/screenshot.png
