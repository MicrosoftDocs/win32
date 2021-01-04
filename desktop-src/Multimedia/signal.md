---
title: signal command
description: The signal command identifies a specified position in the workspace by sending the application an MM\_MCISIGNAL message. Digital-video devices recognize this command. MCIAVI supports only one active signal at a time.
ms.assetid: '3d10eac0-fd1a-41ee-98fa-2518642c7339'
keywords:
- signal command Windows Multimedia
topic_type:
- apiref
api_name:
- signal
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# signal command

The signal command identifies a specified position in the workspace by sending the application an [MM\_MCISIGNAL](mm-mcisignal.md) message. Digital-video devices recognize this command. MCIAVI supports only one active signal at a time.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("signal %s %s %s"), 
  lpszDeviceID, 
  lpszSignalFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszSignalFlags"></span><span id="lpszsignalflags"></span><span id="LPSZSIGNALFLAGS"></span>*lpszSignalFlags*
</dt> <dd>

One of the following flags.



| Value            | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at position      | Specifies the frame to invoke a signal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| cancel           | Removes signals from the workspace. An individual signal is specified by using the "uservalue" flag. If the "uservalue" flag is not specified by using "cancel", the device cancels all signals. The "cancel" flag is incompatible with the "at", "every", and "return position" flags.                                                                                                                                                                                                                                                                                          |
| every *interval* | Specifies the period of the signals. The *interval* value is specified in the current time format.If used with "at" *position*, signals are placed throughout the workspace with one signal mark placed at *position*.<br/> Without the "at" flag, signals are placed throughout the workspace with one signal at the current position.<br/> If this flag is omitted, only the position indicated by the "at" flag is marked.<br/> If the *interval* value is less than the minimum frequency supported by a device, it will use its minimum value.<br/> |
| return position  | Indicates the device should send the position value instead of the "uservalue" identifier in the signaling message. The "uservalue" identifier can still be used to cancel or to redefine the signal marks.                                                                                                                                                                                                                                                                                                                                                                      |
| uservalue *id*   | Specifies an identifier that is reported back with the signaling message. This identifier acts as an identifier that can be used with other **signal** commands to reference this **signal** setting. If omitted, the default value is zero.                                                                                                                                                                                                                                                                                                                                     |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The window handle used for notification of command completion messages is also used for signaling.

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

[MM\_MCISIGNAL](mm-mcisignal.md)
</dt> </dl>

 

