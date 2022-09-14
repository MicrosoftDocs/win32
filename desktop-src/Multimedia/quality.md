---
title: quality command
description: The quality command defines a custom quality level for either audio, video or still image data compression. Digital-video devices recognize this command.
ms.assetid: 'cc920ec9-362c-43db-808e-b9fb59d1df6d'
keywords:
- quality command Windows Multimedia
topic_type:
- apiref
api_name:
- quality
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# quality command

The quality command defines a custom quality level for either audio, video or still image data compression. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("quality %s %s %s"), 
  lpszDeviceID, 
  lpszQuality, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszQuality"></span><span id="lpszquality"></span><span id="LPSZQUALITY"></span>*lpszQuality*
</dt> <dd>

One or more of the following flags. (One of the three flags "audio", "still", and "video" must be present.)



| Value                 | Meaning                                                                                                                                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| algorithm *algorithm* | Associates the quality level with the specified *algorithm*. This *algorithm* must be supported by the device and be compatible with the "audio", "still", or "video" flag that is used. If omitted, the current algorithm is used. |
| audio *name*          | Indicates this command specifies an "audio" quality level identified with *name*.                                                                                                                                                   |
| dialog                | Requests that the device display a dialog box. This dialog box has algorithm-specific fields that are used internally by the device to create the structure describing a specific quality level.                                    |
| handle *handle*       | Specifies a *handle* to a structure that contains algorithmic-specific data describing a specific quality level. The structures for the data referenced by this handle are device specific.                                         |
| still *name*          | Indicates the command specifies a "still" quality level identified with *name.*                                                                                                                                                     |
| video *name*          | Indicates the command specifies a "video" quality level identified with *name*.                                                                                                                                                     |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

This command defines a string name for the quality level, which can then be used in a [setvideo](setvideo.md) "quality", setvideo "still quality", or [setaudio](setaudio.md) "quality" command to establish it as the current video, still, or audio-compression quality level.

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

[setaudio](setaudio.md)
</dt> <dt>

[setvideo](setvideo.md)
</dt> </dl>

 

