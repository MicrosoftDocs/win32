---
title: Devices and Data Types
description: Devices and Data Types
ms.assetid: 46247983-19c3-4c7a-a615-ba6cd8bd3289
keywords:
- waveform audio,opening output devices
- waveform-audio interface,opening output devices
- opening waveform-audio output devices
- waveform audio,querying output devices
- waveform-audio interface,querying output devices
- querying waveform-audio output devices
- waveform audio,device handles
- waveform-audio interface,device handles
- waveform audio,device identifiers
- waveform-audio interface,device identifiers
- waveform audio,output data types
- waveform-audio interface,output data types
- waveform audio,data formats
- waveform-audio interface,data formats
- writing waveform-audio data
- waveform audio,writing data
- waveform-audio interface,writing data
- PCM waveform-audio data
- waveform audio,PCM data
- waveform-audio interface,PCM data
- waveform audio,closing output devices
- waveform-audio interface,closing output devices
- closing waveform-audio output devices
ms.topic: article
ms.date: 05/31/2018
---

# Devices and Data Types

This section describes working with waveform-audio devices, and includes information on how to open, close and query them for their capabilities. It also describes how to keep track of the devices in a system by using device handles and device identifiers.

## Opening Waveform-Audio Output Devices

Use the [**waveOutOpen**](https://msdn.microsoft.com/library/Dd743866(v=VS.85).aspx) function to open a waveform-audio output device for playback. This function opens the device associated with the specified device identifier and returns a handle of the open device by writing the handle of a specified memory location.

Some multimedia computers have multiple waveform-audio output devices. Unless you want to open a specific waveform-audio output device in a system, you should use the WAVE\_MAPPER flag for the device identifier when you open a device. The **waveOutOpen** function chooses the device in the system that is best able to play the specified data format.

## Querying Audio Devices

Windows provides the following functions to determine how many devices of a certain type are available in a system.



| Function                                       | Description                                                                  |
|------------------------------------------------|------------------------------------------------------------------------------|
| [**auxGetNumDevs**](https://msdn.microsoft.com/library/Dd756713(v=VS.85).aspx)         | Retrieves the number of auxiliary output devices present in the system.      |
| [**waveInGetNumDevs**](https://msdn.microsoft.com/library/Dd743844(v=VS.85).aspx)   | Retrieves the number of waveform-audio input devices present in the system.  |
| [**waveOutGetNumDevs**](https://msdn.microsoft.com/library/Dd743860(v=VS.85).aspx) | Retrieves the number of waveform-audio output devices present in the system. |



 

Audio devices are identified by a device identifier. The device identifier is determined implicitly from the number of devices present in a system. Device identifiers range from zero to one less than the number of devices present. For example, if there are two waveform-audio output devices in a system, valid device identifiers are 0 and 1.

After you determine how many devices of a certain type are present in a system, you can use one of the following functions to query the capabilities of each device.



| Function                                       | Description                                                             |
|------------------------------------------------|-------------------------------------------------------------------------|
| [**auxGetDevCaps**](https://msdn.microsoft.com/library/Dd756712(v=VS.85).aspx)         | Retrieves the capabilities of a specified auxiliary output device.      |
| [**waveInGetDevCaps**](https://msdn.microsoft.com/library/Dd743841(v=VS.85).aspx)   | Retrieves the capabilities of a specified waveform-audio input device.  |
| [**waveOutGetDevCaps**](https://msdn.microsoft.com/library/Dd743857(v=VS.85).aspx) | Retrieves the capabilities of a specified waveform-audio output device. |



 

Each of these functions fills a structure with information about the capabilities of a specified device. The following table lists the structures that correspond to each of these functions.



|                                                |                                    |
|------------------------------------------------|------------------------------------|
| Function                                       | Structure                          |
| [**auxGetDevCaps**](https://msdn.microsoft.com/library/Dd756712(v=VS.85).aspx)         | [**AUXCAPS**](https://msdn.microsoft.com/library/Dd756711(v=VS.85).aspx)         |
| [**waveInGetDevCaps**](https://msdn.microsoft.com/library/Dd743841(v=VS.85).aspx)   | [**WAVEINCAPS**](https://msdn.microsoft.com/library/Dd743839(v=VS.85).aspx)   |
| [**waveOutGetDevCaps**](https://msdn.microsoft.com/library/Dd743857(v=VS.85).aspx) | [**WAVEOUTCAPS**](https://msdn.microsoft.com/library/Dd743855(v=VS.85).aspx) |



 

Standard formats are listed in the **dwFormats** member of the **WAVEOUTCAPS** structure. Waveform-audio devices can support nonstandard formats. To determine whether a particular format (standard or nonstandard) is supported by a device, you can call the [**waveOutOpen**](https://msdn.microsoft.com/library/Dd743866(v=VS.85).aspx) function with the WAVE\_FORMAT\_QUERY flag. This flag does not open the device. You specify the format in question in the [**WAVEFORMATEX**](https://msdn.microsoft.com/library/Dd757713(v=VS.85).aspx) structure pointed to by the *pwfx* parameter passed to **waveOutOpen**.

Waveform-audio output devices vary in the capabilities they support. The **dwSupport** member of the [**WAVEOUTCAPS**](https://msdn.microsoft.com/library/Dd743855(v=VS.85).aspx) structure indicates whether a device supports such capabilities as volume and pitch changes.

## Device Handles and Device Identifiers

Each function that opens an audio device specifies a device identifier, a pointer to a memory location, and some parameters that are unique to each type of device. The memory location is filled with a device handle. Use this device handle to identify the open audio device when calling other audio functions.

The difference between identifiers and handles for audio devices is subtle but important:

-   Device identifiers are determined implicitly from the number of devices present in a system. This number is obtained by using the [**auxGetNumDevs**](https://msdn.microsoft.com/library/Dd756713(v=VS.85).aspx), [**waveInGetNumDevs**](https://msdn.microsoft.com/library/Dd743844(v=VS.85).aspx), or [**waveOutGetNumDevs**](https://msdn.microsoft.com/library/Dd743860(v=VS.85).aspx) function.
-   Device handles are returned when device drivers are opened by using the [**waveInOpen**](https://msdn.microsoft.com/library/Dd743847(v=VS.85).aspx) or [**waveOutOpen**](https://msdn.microsoft.com/library/Dd743866(v=VS.85).aspx) function.

There are no functions that open or close auxiliary audio devices. Auxiliary audio devices need not be opened and closed like waveform-audio devices because there is no continuous data transfer associated with them. All auxiliary audio functions use device identifiers to identify devices.

## Waveform-Audio Output Data Types

The following data types are defined for waveform-audio output functions.



| Type                                 | Description                                                                                                                                                   |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HWAVEOUT**                         | Handle to an open waveform-audio output device.                                                                                                               |
| [**WAVEFORMATEX**](https://msdn.microsoft.com/library/Dd757713(v=VS.85).aspx) | Structure that specifies the data formats supported by a particular waveform-audio input device. This structure is also usedfor waveform-audio input devices. |
| [**WAVEHDR**](https://msdn.microsoft.com/library/Dd743837(v=VS.85).aspx)           | Structure used as a header for a block of waveform-audio input data. This structure is also used for waveform-audio input devices.                            |
| [**WAVEOUTCAPS**](https://msdn.microsoft.com/library/Dd743855(v=VS.85).aspx)   | Structure used to query the capabilities of a particular waveform-audio output device.                                                                        |



 

## Specifying Waveform-Audio Data Formats

When you call the [**waveOutOpen**](https://msdn.microsoft.com/library/Dd743866(v=VS.85).aspx) function to open a device driver for playback or to query whether the driver supports a particular data format, use the *pwfx* parameter to specify a pointer to a [**WAVEFORMATEX**](https://msdn.microsoft.com/library/Dd757713(v=VS.85).aspx) structure containing the requested waveform-audio data format. **WAVEFORMATEX** supersedes the [**WAVEFORMAT**](/windows/desktop/api/mmeapi/ns-mmeapi-twaveformatex) and [**PCMWAVEFORMAT**](https://msdn.microsoft.com/library/Dd743663(v=VS.85).aspx) structures.

For audio data that is separated into more than two channels or has a sample size that is not a multiple of 8, you should use [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/Dd757714(v=VS.85).aspx). This structure simply configures the extra bytes pointed to by the **cbSize** member of **WAVEFORMATEX** to give extra information about the format. **WAVEFORMATEXTENSIBLE** can be cast as **WAVEFORMATEX**.

There are also two clipboard formats you can use to represent audio data: CF\_WAVE and CF\_RIFF. Use the CF\_WAVE format to represent data in one of the standard formats, such as 11 kHz or 22 kHz PCM. Use the CF\_RIFF format to represent more complex data formats that cannot be represented as standard waveform-audio files.

## Writing Waveform-Audio Data

After successfully opening a waveform-audio output device driver, you can begin playing a sound. Windows provides the [**waveOutWrite**](https://msdn.microsoft.com/library/Dd743876(v=VS.85).aspx) function for sending data blocks to waveform-audio output devices.

Use the [**WAVEHDR**](https://msdn.microsoft.com/library/Dd743837(v=VS.85).aspx) structure to specify the waveform-audio data block you are sending using **waveOutWrite**. This structure contains a pointer to a locked data block, the length of the data block, and some flags. This data block must be prepared before you use it; for information about preparing a data block, see [Audio Data Blocks](audio-data-blocks.md).

After you send a data block to an output device by using **waveOutWrite**, you must wait until the device driver is finished with the data block before freeing it. If you are sending multiple data blocks, you must monitor the completion of data blocks to know when to send additional blocks. For more information about data blocks, see [Audio Data Blocks](audio-data-blocks.md).

## PCM Waveform-Audio Data Format

The **lpData** member of the [**WAVEHDR**](https://msdn.microsoft.com/library/Dd743837(v=VS.85).aspx) structure pointsetts to the waveform-audio data samples. For 8-bit PCM data, each sample is represented by a single unsigned data byte. For 16-bit PCM data, each sample is represented by a 16-bit signed value. The following table summarizes the maximum, minimum, and midpoint values for PCM waveform-audio data.



|             |                 |                  |                |
|-------------|-----------------|------------------|----------------|
| Data format | Maximum value   | Minimum value    | Midpoint value |
| 8-bit PCM   | 255 (0xFF)      | 0                | 128 (0x80)     |
| 16-bit PCM  | 32,767 (0x7FFF) | –32,768 (0x8000) | 0              |



 

## PCM Data Packing

The order of the data bytes varies between 8-bit and 16-bit formats and between mono and stereo formats. The following list describes data packing for the different PCM waveform-audio data formats.



| PCM waveform-audio format | Description                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 8-bit mono                | Each sample is 1 byte that corresponds to a single audio channel. Sample 1 is followed by samples 2, 3, 4, and so on.                                                                                                                                                                                                                           |
| 8-bit stereo              | Each sample is 2 bytes. Sample 1 is followed by samples 2, 3, 4, and so on. For each sample, the first byte is channel 0 (the left channel) and the second byte is channel 1 (the right channel).                                                                                                                                               |
| 16-bit mono               | Each sample is 2 bytes. Sample 1 is followed by samples 2, 3, 4, and so on. For each sample, the first byte is the low-order byte of channel 0 and the second byte is the high-order byte of channel 0.                                                                                                                                         |
| 16-bit stereo             | Each sample is 4 bytes. Sample 1 is followed by samples 2, 3, 4, and so on. For each sample, the first byte is the low-order byte of channel 0 (left channel); the second byte is the high-order byte of channel 0; the third byte is the low-order byte of channel 1 (right channel); and the fourth byte is the high-order byte of channel 1. |
| Others                    | Each sample is contained in a block that is a multiple of 4 bytes, but the samples may be non-byte-aligned. The arrangement of channels is specified by a mask. For more information, see [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/Dd757714(v=VS.85).aspx).                                                                                                 |



 

## Closing Waveform-Audio Output Devices

After waveform-audio playback is complete, call [**waveOutClose**](https://msdn.microsoft.com/library/Dd743856(v=VS.85).aspx) to close the output device. If **waveOutClose** is called while a waveform-audio file is playing, the close operation fails and the function returns an error code indicating that the device was not closed. If you do not want to wait for playback to end before closing the device, call the [**waveOutReset**](https://msdn.microsoft.com/library/Dd743870(v=VS.85).aspx) function before closing. This ends playback and allows the device to be closed. Be sure to use the [**waveOutUnprepareHeader**](https://msdn.microsoft.com/library/Dd743875(v=VS.85).aspx) function to clean up the preparation on all data blocks before closing the device.

 

 




