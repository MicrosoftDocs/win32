---
title: undo command
description: The undo command reverses the action taken by the most recent successful copy, cut, delete, undo, or paste command. Digital-video devices recognize this command.
ms.assetid: 1593457a-e680-4732-a89e-00f4eff7605a
keywords:
- undo command Windows Multimedia
topic_type:
- apiref
api_name:
- undo
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# undo command

The undo command reverses the action taken by the most recent successful [copy](copy.md), [cut](cut.md), [delete](delete.md), undo, or [paste](paste.md) command. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/windows/win32/Mmsystem/?branch=master) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("undo %s %s"), 
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

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Command Strings](mci-command-strings.md)
</dt> <dt>

[copy](copy.md)
</dt> <dt>

[cut](cut.md)
</dt> <dt>

[delete](delete.md)
</dt> <dt>

[paste](paste.md)
</dt> </dl>

 

 





