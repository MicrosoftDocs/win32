---
title: resume command
description: The resume command continues playing or recording on a device that has been paused using the pause command.
ms.assetid: '0a2cdd23-8c1d-4d9e-9b63-3fdcbb13e3a2'
keywords:
- resume command Windows Multimedia
topic_type:
- apiref
api_name:
- resume
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# resume command

The resume command continues playing or recording on a device that has been paused using the [pause](pause.md) command. Digital-video, VCR, and waveform-audio devices recognize this command. Although CD audio, MIDI sequencer, and videodisc devices also recognize this command, the MCICDA, MCISEQ, and MCIPIONR device drivers do not support it.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("resume %s %s"), 
  lpszDeviceID, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Examples

The following command continues playing or recording the "newsound" device.

``` syntax
resume newsound
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

[pause](pause.md)
</dt> </dl>

 

