---
title: spin command
description: The spin command starts spinning a disc or stops the disc from spinning. Videodisc devices recognize this command.
ms.assetid: '1fdf4d09-fafd-4245-ad92-397114d0f473'
keywords:
- spin command Windows Multimedia
topic_type:
- apiref
api_name:
- spin
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# spin command

The spin command starts spinning a disc or stops the disc from spinning. Videodisc devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("spin %s %s %s"), 
  lpszDeviceID, 
  lpszUpDown, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszUpDown"></span><span id="lpszupdown"></span><span id="LPSZUPDOWN"></span>*lpszUpDown*
</dt> <dd>

One of the following flags.



| Value | Meaning                       |
|-------|-------------------------------|
| down  | Stops the disc from spinning. |
| up    | Starts spinning the disc.     |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Examples

The following command starts spinning a videodisc device.

``` syntax
spin videodisc up
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
</dt> </dl>

 

