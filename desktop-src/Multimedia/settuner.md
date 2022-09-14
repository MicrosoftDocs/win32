---
title: settuner command
description: The settuner command changes the current tuner or the channel setting of the current tuner. VCR devices recognize this command.
ms.assetid: '76d05210-3c2a-4d00-b3eb-c912c1deabf7'
keywords:
- settuner command Windows Multimedia
topic_type:
- apiref
api_name:
- settuner
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# settuner command

The settuner command changes the current tuner or the channel setting of the current tuner. VCR devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("settuner %s %s %s"), 
  lpszDeviceID, 
  lpszTuner, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszTuner"></span><span id="lpsztuner"></span><span id="LPSZTUNER"></span>*lpszTuner*
</dt> <dd>

One of the following flags.



| Value                            | Meaning                                                                                                                                                                                                                                                                                                     |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| channel *channel*                | Sets the tuner to *channel*. You might not be able to change the channel while recording, depending on the VCR. A channel larger than the maximum sets the tuner to the maximum channel.                                                                                                                    |
| channel seek upchannel seek down | Seeks the next channel with a valid signal. "Seek up" increments the channel number in its search. "Seek down" decrements the channel number in its search. The tuner wraps to channel 1 when the maximum channel number is exceeded. Similarly, when seeking down, the tuner wraps to the maximum channel. |
| channel upchannel down           | Increments or decrements the tuner channel. You might not be able to change the channel while recording, depending on the VCR. The tuner wraps to channel 1 when the maximum channel number is exceeded. Similarly, when seeking down, the tuner wraps to the maximum channel.                              |
| number *number*                  | Specifies the tuner to be affected by the settuner command. If *number* is not given, the default value of 1 is assumed.                                                                                                                                                                                    |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

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
</dt> </dl>

 

