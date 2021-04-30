---
title: freeze command
description: The freeze command freezes video input or video output on a VCR or disables video acquisition to the frame buffer. Digital-video, video-overlay, and VCR devices recognize this command.
ms.assetid: 49f3ab98-e893-402a-be78-6140af3b81df
keywords:
- freeze command Windows Multimedia
topic_type:
- apiref
api_name:
- freeze
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# freeze command

The freeze command freezes video input or video output on a VCR or disables video acquisition to the frame buffer. Digital-video, video-overlay, and VCR devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("freeze %s %s %s"), 
  lpszDeviceID, 
  lpszFreezeFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszFreezeFlags"></span><span id="lpszfreezeflags"></span><span id="LPSZFREEZEFLAGS"></span>*lpszFreezeFlags*
</dt> <dd>

Flag that identifies what to freeze. The following table lists device types that recognize the **freeze** command and the flags used by each type.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>digitalvideo</td>
<td>at <em>rectangle</em></td>
<td>outside</td>
</tr>
<tr class="even">
<td>overlay</td>
<td>at <em>rectangle</em></td>

</tr>
<tr class="odd">
<td>vcr</td>
<td><ul>
<li>field</li>
<li>frame</li>
</ul></td>
<td><ul>
<li>input</li>
<li>output</li>
</ul></td>
</tr>
</tbody>
</table>



 

The following table lists the flags that can be specified in the *lpszFreezeFlags* parameter and their meanings.



| Value          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle* | Specifies the region that will be frozen. For video-overlay devices, this region will have video acquisition disabled. For digital-video devices, the pixels within the rectangle will have their lock mask bit turned on (unless the "outside" flag is specified). The rectangle is relative to the video buffer origin and is specified as *X1 Y1 X2 Y2*. The coordinates *X1 Y1* specify the upper left corner of the rectangle, and the coordinates *X2 Y2* specify the width and height. |
| field          | Freezes the first field. Field is assumed by default (if neither frame nor field is specified).                                                                                                                                                                                                                                                                                                                                                                                               |
| frame          | Freezes the entire frame, displaying both fields.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| input          | Freezes the current frame of the input image, whether it is paused or running.                                                                                                                                                                                                                                                                                                                                                                                                                |
| output         | Freezes the current frame of the output from the VCR. If the VCR is playing when freeze is issued, the current frame is frozen and the VCR is paused. If the VCR is paused when this command is issued, the current frame is frozen. The frozen image remains on the output device until an [unfreeze](unfreeze.md) command is issued. If neither "input" nor "output" is specified, "output" is assumed.                                                                                    |
| outside        | Indicates that the area outside the region specified using the "at" flag is frozen.                                                                                                                                                                                                                                                                                                                                                                                                           |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

When used with VCR devices, this command is intended for frame-grabbing cards.

To specify irregular acquisition regions with the "at" flag, use a series of freeze and [unfreeze](unfreeze.md) commands. Some video-overlay devices limit the complexity of the acquisition region.

This command is supported only if a call to the [capability](capability.md) command with the "can freeze" flag returns **TRUE**.

## Examples

The following command disables video acquisition in a 100-pixel square at the upper left corner of the video buffer.

``` syntax
freeze vboard at 0 0 100 100
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

[capability](capability.md)
</dt> <dt>

[unfreeze](unfreeze.md)
</dt> </dl>

 

