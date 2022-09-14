---
title: mark command
description: The mark command controls recording and erasing of marks on the videotape. VCR devices recognize this command.
ms.assetid: d5f7a546-dc46-459c-b5dc-0651bca842cb
keywords:
- mark command Windows Multimedia
topic_type:
- apiref
api_name:
- mark
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# mark command

The mark command controls recording and erasing of marks on the videotape. VCR devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("mark %s %s %s"), 
  lpszDeviceID, 
  lpszMark, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszMark"></span><span id="lpszmark"></span><span id="LPSZMARK"></span>*lpszMark*
</dt> <dd>

One of the following flags.



| Value | Meaning                                                                                                                                |
|-------|----------------------------------------------------------------------------------------------------------------------------------------|
| erase | Erases a mark at the current position, if one exists. To erase a mark, first seek to the mark and then issue the mark "erase" command. |
| write | Writes a mark at the current position. The VCR might need to be in play or record mode for this command to succeed.                    |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or "test". For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Marks are special signals written to the content that can be detected by the VCR during high-speed searches. Marks are VCR specific.

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

 

