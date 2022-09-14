---
description: The following topic describes how to perform simple playback.
ms.assetid: 37869822-aed7-4102-8110-5a896400885c
title: Simple Playback
ms.topic: article
ms.date: 05/31/2018
---

# Simple Playback

The following topic describes how to perform simple playback.

**To perform simple playback**

1.  Select the File Playback Terminal at the call level.
2.  Create the Playback Terminal on the TAPI call.
3.  Set properties—file name and type of storage.
4.  Call the [**Start**](/windows/desktop/api/tapi3if/nf-tapi3if-itmediacontrol-start) method on the File Playback Terminal to start playback of streams.

The following example code demonstrates simple playback.

First, use the [**ITBasicCallControl2**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol2) interface to create the terminal for recording. This instructs the TSP/MSP to perform file playback on this call. The TSP/MSP creates a terminal for the application to use, and returns it on success.


```C++

```



Get the [**ITMediaPlayback**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediaplayback) interface pointer from the terminal interface and use it to set the file name to play back.


```C++
pMediaPlayback->Release();
```



Assuming that the file contains one audio stream, and the call has a capture audio stream, the audio content in the file will play back on that stream.

 

 



