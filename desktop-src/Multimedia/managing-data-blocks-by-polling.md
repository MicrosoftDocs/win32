---
title: Managing Data Blocks by Polling
description: Managing Data Blocks by Polling
ms.assetid: 0a517f1d-4993-49b8-be86-bc63e5687cba
keywords:
- waveform audio,polling data blocks
- audio data blocks,polling
- polling audio data blocks
- WAVEHDR structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing Data Blocks by Polling

In addition to using a callback function, you can poll the **dwFlags** member of a [**WAVEHDR**](https://msdn.microsoft.com/en-us/library/Dd743837(v=VS.85).aspx) structure to determine when an audio device is finished with a data block. Sometimes it is better to poll **dwFlags** than to wait for another mechanism to receive messages from the drivers. For example, after you call the [**waveOutReset**](https://msdn.microsoft.com/en-us/library/Dd743870(v=VS.85).aspx) function to release pending data blocks, you can immediately poll to be sure that the data blocks have been released before calling [**waveOutUnprepareHeader**](https://msdn.microsoft.com/en-us/library/Dd743875(v=VS.85).aspx) and freeing the memory for the data block.

You can use the WHDR\_DONE flag to test the **dwFlags** member. As soon as the WHDR\_DONE flag is set in the **dwFlags** member of the **WAVEHDR** structure, the driver is finished with the data block.

 

 




