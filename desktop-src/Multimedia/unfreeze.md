---
title: unfreeze command
description: The unfreeze command reenables video acquisition to the frame buffer after it has been disabled by the freeze command. Digital-video, VCR, and video-overlay devices recognize this command.
ms.assetid: 'ca90c299-2003-44cb-a879-4bc767480965'
keywords:
- unfreeze command Windows Multimedia
topic_type:
- apiref
api_name:
- unfreeze
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# unfreeze command

The unfreeze command reenables video acquisition to the frame buffer after it has been disabled by the [freeze](freeze.md) command. Digital-video, VCR, and video-overlay devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("unfreeze %s %s %s"), 
  lpszDeviceID, 
  lpszUnfreeze, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszUnfreeze"></span><span id="lpszunfreeze"></span><span id="LPSZUNFREEZE"></span>*lpszUnfreeze*
</dt> <dd>

Flag for reenabling video acquisition to the frame buffer. The following table lists device types that recognize the **unfreeze** command and the flags used by each type.



| Value        | Meaning        |
|--------------|----------------|
| digitalvideo | at *rectangle* |
| overlay      | at *rectangle* |
| vcr          | input output   |



 

The following table lists the flags that can be specified in the **lpszUnfreeze** parameter and their meanings.



| Value          | Meaning                                                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle* | Specifies the region that will have video acquisition reenabled. The rectangle is relative to the video buffer origin and is specified as *X1 Y1 X2 Y2*. The coordinates *X1 Y1* specify the upper left corner of the rectangle, and the coordinates *X2 Y2* specify the width and height. |
| input          | Unfreeze the input image.                                                                                                                                                                                                                                                                  |
| output         | Unfreeze the output image. If neither "input" nor "output" is given, "output" is assumed.                                                                                                                                                                                                  |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Examples

The following command unfreezes a region of the video buffer.

``` syntax
unfreeze vboard at 10 20 90 165
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

[freeze](freeze.md)
</dt> </dl>

 

