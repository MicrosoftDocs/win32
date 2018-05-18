---
title: Audio Data Blocks
description: Audio Data Blocks
ms.assetid: '9646e18c-294b-4532-bd5e-709d66ad31f4'
keywords: ["multimedia audio,data blocks", "audio,data blocks", "waveform audio,data blocks", "audio data blocks,about", "WAVEHDR structure"]
---

# Audio Data Blocks

The [**waveInAddBuffer**](waveinaddbuffer.md) and [**waveOutWrite**](waveoutwrite.md) functions require applications to allocate data blocks to pass to the device drivers for recording or playback purposes. Both of these functions use the [**WAVEHDR**](wavehdr.md) structure to describe its data block.

Before using one of these functions to pass a data block to a device driver, you must allocate memory for the data block and the header structure that describes the data block. The headers can be prepared and unprepared by using the following functions.



| Function                                                 | Description                                                      |
|----------------------------------------------------------|------------------------------------------------------------------|
| [**waveInPrepareHeader**](waveinprepareheader.md)       | Prepares a waveform-audio input data block.                      |
| [**waveInUnprepareHeader**](waveinunprepareheader.md)   | Cleans up the preparation on a waveform-audio input data block.  |
| [**waveOutPrepareHeader**](waveoutprepareheader.md)     | Prepares a waveform-audio output data block.                     |
| [**waveOutUnprepareHeader**](waveoutunprepareheader.md) | Cleans up the preparation on a waveform-audio output data block. |



 

Before you pass an audio data block to a device driver, you must prepare the data block by passing it to either [**waveInPrepareHeader**](waveinprepareheader.md) or [**waveOutPrepareHeader**](waveoutprepareheader.md). When the device driver is finished with the data block and returns it, you must clean up this preparation by passing the data block to either [**waveInUnprepareHeader**](waveinunprepareheader.md) or [**waveOutUnprepareHeader**](waveoutunprepareheader.md) before any allocated memory can be freed.

Unless the waveform-audio input and output data is small enough to be contained in a single data block, applications must continually supply the device driver with data blocks until playback or recording is complete.

Even if a single data block is used, an application must be able to determine when a device driver is finished with the data block so the application can free the memory associated with the data block and header structure. There are several ways to determine when a device driver is finished with a data block:

-   By specifying a callback function to receive a message sent by the driver when it is finished with a data block
-   By using an event callback
-   By specifying a window or thread to receive a message sent by the driver when it is finished with a data block
-   By polling the WHDR\_DONE bit in the **dwFlags** member of the [**WAVEHDR**](wavehdr.md) structure sent with each data block

If an application does not get a data block to the device driver when needed, there can be an audible gap in playback or a loss of incoming recorded information. This requires at least a double-buffering scheme — staying at least one data block ahead of the device driver.

The following topics describe ways to determine when a device driver is finished with a data block:

Using a Callback Function to Process Driver Messages

-   [Using a Callback Function to Process Driver Messages](using-a-callback-function-to-process-driver-messages.md)
-   [Using an Event Callback to Process Driver Messages](using-an-callback-to-process-driver-messages.md)
-   [Using a Window or Thread to Process Driver Messages](using-a-window-or-thread-to-process-driver-messages.md)
-   [Managing Data Blocks by Polling](managing-data-blocks-by-polling.md)

 

 




