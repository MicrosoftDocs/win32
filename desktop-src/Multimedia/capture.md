---
title: capture command
description: The capture command copies the contents of the frame buffer and stores it in the specified file. Digital-video devices recognize this command.
ms.assetid: 'cdf177b9-874e-40d8-af3e-59070c55903d'
keywords:
- capture command Windows Multimedia
topic_type:
- apiref
api_name:
- capture
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# capture command

The capture command copies the contents of the frame buffer and stores it in the specified file. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("capture %s %s %s"), 
  lpszDeviceID, 
  lpszCapture, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszCapture"></span><span id="lpszcapture"></span><span id="LPSZCAPTURE"></span>*lpszCapture*
</dt> <dd>

One or more of the following flags:



| Value          | Meaning                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| as *pathname*  | Specifies the destination path and filename for the captured image. This flag is required.                                                                                                                                                                |
| at *rectangle* | Specifies the rectangular region within the frame buffer that the device crops and saves to disk. If omitted, the cropped region defaults to the rectangle specified or defaulted on a previous [put](put.md) "source" command for this device instance. |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

This command might fail if the device is currently playing motion video or executing some other resource-intensive operation. If the frame buffer is being updated in real time, the updating momentarily pauses so that a complete image is captured. If the device pauses the updating, there might be a visual or audible effect. If the file format, compression algorithm, and quality levels have not been set, their defaults are used.

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

[put](put.md)
</dt> </dl>

 

