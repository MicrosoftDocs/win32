---
title: monitor command
description: The monitor command specifies the presentation source. (The default presentation source is the workspace.) Switching the presentation source switches all audio and video streams in the source. Digital-video devices recognize this command.
ms.assetid: '5cacbe88-b94e-4101-badf-2bb4796b19cf'
keywords:
- monitor command Windows Multimedia
topic_type:
- apiref
api_name:
- monitor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# monitor command

The monitor command specifies the presentation source. (The default presentation source is the workspace.) Switching the presentation source switches all audio and video streams in the source. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("monitor %s %s %s"), 
  lpszDeviceID, 
  lpszMonitor, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszMonitor"></span><span id="lpszmonitor"></span><span id="LPSZMONITOR"></span>*lpszMonitor*
</dt> <dd>

One or more of the following flags.



| Value           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| file            | Specifies that the workspace is the presentation source. This is the default source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| input           | Specifies that the external input is the presentation source. If a [play](play.md) command is in progress, it is first paused. If [setvideo](setvideo.md) is "on", this flag displays a default hidden window. Devices might limit what other device instances can do while monitoring input.                                                                                                                                                                                                                                                                                                                                                                    |
| method *method* | When used with **monitor** "input", this flag selects the method of monitoring. The *method* is either "pre", "post", or "direct". Direct monitoring requests that the device be configured for optimum display quality during monitoring. The direct monitoring method might be incompatible with motion video recording.Pre- and post-monitoring allow motion video recording. Pre-monitoring shows the external input prior to compression, while post-monitoring shows the external input after compression. Typically, different monitoring methods have different hardware implications. The default monitoring method is selected by the device.<br/> |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The presentation source automatically switches to the workspace after a [play](play.md), [step](step.md), [pause](pause.md), [cue](cue.md) "output", or [seek](seek.md) command. The [record](record.md) command does not automatically switch presentation sources, which gives your application the option of not showing video while it is being recorded.

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

[cue](cue.md)
</dt> <dt>

[pause](pause.md)
</dt> <dt>

[play](play.md)
</dt> <dt>

[record](record.md)
</dt> <dt>

[seek](seek.md)
</dt> <dt>

[step](step.md)
</dt> </dl>

 

