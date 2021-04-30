---
title: escape command
description: The escape command sends device-specific information to a device. Videodisc devices recognize this command.
ms.assetid: 16e0e2b6-6d98-440a-86c1-eca8201ad61a
keywords:
- escape command Windows Multimedia
topic_type:
- apiref
api_name:
- escape
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# escape command

The escape command sends device-specific information to a device. Videodisc devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("escape %s %s %s"), 
  lpszDeviceID, 
  lpszEscape, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszEscape"></span><span id="lpszescape"></span><span id="LPSZESCAPE"></span>*lpszEscape*
</dt> <dd>

Custom information to send to the device.

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Examples

The following command sends the escape string "SA" to the videodisc device.

``` syntax
escape videodisc SA
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

 

