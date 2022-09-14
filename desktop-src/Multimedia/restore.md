---
title: restore command
description: The restore command copies a still image from a file to the frame buffer. This is the reverse of the capture command. Digital-video devices recognize this command.
ms.assetid: 'e84a478a-3e0f-4767-94d7-eb3c79c31b8b'
keywords:
- restore command Windows Multimedia
topic_type:
- apiref
api_name:
- restore
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# restore command

The restore command copies a still image from a file to the frame buffer. This is the reverse of the [capture](capture.md) command. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("restore %s %s %s"), 
  lpszDeviceID, 
  lpszRestore, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszRestore"></span><span id="lpszrestore"></span><span id="LPSZRESTORE"></span>*lpszRestore*
</dt> <dd>

One or more of the following flags.



| Value           | Meaning                                                                                                                                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle*  | Specifies a rectangle relative to the frame buffer origin. The *rectangle* is specified as *X1 Y1 X2 Y2*. The coordinates *X1 Y1* specify the upper left corner and the coordinates *X2 Y2* specify the width and height.If this flag is not used, the image is copied to the upper left corner of the frame buffer.<br/> |
| from *filename* | Specifies the image filename to recall. This flag is required.                                                                                                                                                                                                                                                                  |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Devices can recognize a variety of image formats; a Windows device-independent bitmap is always recognized.

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

[capture](capture.md)
</dt> </dl>

 

