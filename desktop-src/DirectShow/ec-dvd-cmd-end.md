---
Description: 'Signals that a particular DVD Navigator command has completed.'
ms.assetid: 'f460db8e-b966-41fa-bfa1-4ad3fa65c3e3'
title: 'EC\_DVD\_CMD\_END'
---

# EC\_DVD\_CMD\_END

Signals that a particular [DVD Navigator](dvd-navigator-filter.md) command has completed.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Command identifier. Pass this parameter to the [**IDvdInfo2::GetCmdFromEvent**](idvdinfo2-getcmdfromevent.md) method to retrieve an [**IDvdCmd**](idvdcmd.md) interface pointer.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

**HRESULT** value indicating the status of the command.

</dd> </dl>

## Remarks

This event is only fired if your application sets the DVD\_CMD\_FLAG\_SendEvents flag in an [**IDvdControl2**](idvdcontrol2.md) method that takes a [**DVD\_CMD\_FLAGS**](dvd-cmd-flags.md) flag.

This event is raised in the title domain.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdevcode.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> <dt>

[DVD Event Notification Codes](dvd-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> <dt>

[Synchronizing DVD Commands](synchronizing-dvd-commands.md)
</dt> </dl>

 

 




