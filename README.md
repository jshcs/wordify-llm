# Wordify

This project serves two use cases:
1. Idiom Explainer
2. Reverse Dictionary. This is an extension of a [project](https://github.com/jshcs/wordify) that I had worked on in 2017 using LSTM.<br>The world has changed a bit since then! :) 

## Idiom Explainer
Came across a tricky, mind-bending idiom at work, at school, or at home? This tool will give a quick, helpful one-line explanation!

## Reverse Dictionary
Struggling to remember that word that's usually at the tip of your tongue? This tool will provide 5 word suggestions that best describe the phrase or thought that's lingering in your mind. 

## How to use this tool?

Currently, this tool can be run in a Python IDE or a terminal. A Gradio-based UI integration is in the works. 
```
$ python3 run.py -u=<user input> -t=<type of execution> -m=<GPT model>
```

-t = "idiom" for Idiom Explainer or "reverse" for Reverse Dictionary

-m = Name of the GPT model to use. "gpt-3.5-turbo-0125" is the default model if no argument is provided

-u = If using as an Idiom Explainer, enter the idiom. If using as a reverse dictionary, enter the phrase/sentence that you want to get summarized to a single word.

### Examples
1. Idiom Explainer
```
$ python3 run.py -u="time and tide wait for no one" -t="idiom"
```
```
This idiom means that opportunities and events will not wait for anyone to be ready or prepared.
```
2. Reverse Dictionary
```
$ python3 run.py -u="someone who codes for a living" -t="reverse"
```
```
Best Match: Programmer  
Alternatives: Developer, Engineer, Coder, Software Architect
```

## Prerequisites
1. Python 3.7+
3. OpenAI SDK. Please follow the instructions in this [tutorial](https://platform.openai.com/docs/quickstart) to set up the development enviroment.

## Next steps
1. Integrate with Gradio for local UI
2. Play around and compare the performance against other open-source LLMs 
