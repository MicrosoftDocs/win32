---
title: Handling Errors with Audio Functions
description: Handling Errors with Audio Functions
ms.assetid: '76f132f1-61dc-4bfc-9e4a-7c841a487794'
keywords: ["multimedia audio,waveform audio errors", "audio,waveform audio errors", "multimedia audio,auxiliary audio errors", "audio,auxiliary audio errors", "waveform audio,errors", "auxiliary audio,errors"]
---

# Handling Errors with Audio Functions

The waveform-audio and auxiliary-audio functions return a nonzero value when an error occurs. Windows provides functions that convert these error values into textual descriptions of the errors. The application must still examine the error values to determine how to proceed, but textual descriptions of errors can be used in dialog boxes that describe errors to users.

You can use the following functions to retrieve textual descriptions of audio error values:



| Function                                           | Description                                                                 |
|----------------------------------------------------|-----------------------------------------------------------------------------|
| [**waveInGetErrorText**](waveingeterrortext.md)   | Retrieves a textual description of a specified waveform-audio input error.  |
| [**waveOutGetErrorText**](waveoutgeterrortext.md) | Retrieves a textual description of a specified waveform-audio output error. |



 

The only audio functions that do not return error values are [**auxGetNumDevs**](auxgetnumdevs.md), [**waveInGetNumDevs**](waveingetnumdevs.md), and [**waveOutGetNumDevs**](waveoutgetnumdevs.md). These functions return zero if no devices are present in a system or if they encounter any errors.

 

 




