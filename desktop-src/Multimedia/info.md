---
title: info command
description: The info command retrieves a hardware description from a device. All MCI devices recognize this command.
ms.assetid: 'cdd6628b-bff8-4a0d-9dad-a63321f584ea'
keywords:
- info command Windows Multimedia
topic_type:
- apiref
api_name:
- info
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# info command

The info command retrieves a hardware description from a device. All MCI devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("info %s %s %s"), 
  lpszDeviceID, 
  lpszInfoType, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszInfoType"></span><span id="lpszinfotype"></span><span id="LPSZINFOTYPE"></span>*lpszInfoType*
</dt> <dd>

Flag that identifies the type of information required. The following table lists device types that recognize the **info** command and the flags used by each type.



| Value        | Meaning                                                             | Meaning                                             |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------|
| cdaudio      | info identityinfo upc                                               | product                                             |
| digitalvideo | audio algorithmaudio qualityfileproductstill algorithmstill quality | usageversionvideo algorithmvideo qualitywindow text |
| overlay      | fileproduct                                                         | window text                                         |
| sequencer    | copyrightfile                                                       | nameproduct                                         |
| vcr          | product                                                             | version                                             |
| videodisk    | product                                                             |                                                     |
| waveaudio    | fileinput                                                           | outputproduct                                       |



 

The following table lists the flags that can be specified in the **lpszInfoType** parameter and their meanings.



| Value           | Meaning                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| audio algorithm | Returns the name of the current audio compression algorithm.                                                                                                                                       |
| audio quality   | Returns the name for the current audio quality descriptor. This might return "unknown" if the application has set parameters to specific values that do not correspond to defined qualities.       |
| copyright       | Retrieves the MIDI file copyright notice from the copyright meta event.                                                                                                                            |
| file            | Retrieves the name of the file used by the compound device. If the device is opened without a file and the [load](load.md) command has not been used, a null string is returned.                  |
| info identity   | Produces a unique identifier for the audio CD currently loaded in the player being queried.                                                                                                        |
| info upc        | Produces the Universal Product Code (UPC) that is encoded on an audio CD. The UPC is a string of digits. It might not be available for all CDs.                                                    |
| input           | Retrieves the description of the current input device. Returns "none" if an input device is not set.                                                                                               |
| name            | Retrieves the sequence name from the sequence/track name meta event.                                                                                                                               |
| output          | Retrieves the description of the current output device. Returns "none" if an output device is not set.                                                                                             |
| product         | Retrieves a description of the device. This information often includes the product name and model. The string length will be 31 characters or fewer.                                               |
| still algorithm | Returns the name of the current still image compression algorithm.                                                                                                                                 |
| still quality   | Returns the name for the current still image quality descriptor. This might return "unknown" if the application has set parameters to specific values that do not correspond to defined qualities. |
| usage           | Returns a string describing usage restrictions that might be imposed by the owner of the visual or audio data in the workspace.                                                                    |
| version         | Returns the release level of the device driver and hardware.                                                                                                                                       |
| video algorithm | Returns the name of the current video compression algorithm.                                                                                                                                       |
| video quality   | Returns the name for the current video quality descriptor. This might return "unknown" if the application has set parameters to specific values that do not correspond to defined qualities.       |
| window text     | Retrieves the caption of the window used by the device.                                                                                                                                            |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Examples

The following command retrieves a description of the hardware associated with the "mysound" device.

``` syntax
info mysound product
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Command Strings](mci-command-strings.md)
</dt> <dt>

[load](load.md)
</dt> </dl>

 

