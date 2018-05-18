---
Description: 'Signals that a DVD Navigator command has begun.'
ms.assetid: '230116b4-23f1-4c37-a781-da2c5aa20a1f'
title: 'EC\_DVD\_CMD\_START'
---

# EC\_DVD\_CMD\_START

Signals that a [DVD Navigator](dvd-navigator-filter.md) command has begun.

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

This event is only fired if your application sets the **DVD\_CMD\_FLAG\_SendEvents** flag in an [**IDvdControl2**](idvdcontrol2.md) method that takes a [**DVD\_CMD\_FLAGS**](dvd-cmd-flags.md) flag.

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

 

 




