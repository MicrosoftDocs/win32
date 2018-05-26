---
Description: Signals that a particular DVD Navigator command has completed.
ms.assetid: f460db8e-b966-41fa-bfa1-4ad3fa65c3e3
title: EC\_DVD\_CMD\_END
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_DVD\_CMD\_END

Signals that a particular [DVD Navigator](dvd-navigator-filter.md) command has completed.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Command identifier. Pass this parameter to the [**IDvdInfo2::GetCmdFromEvent**](/windows/win32/Strmif/nf-strmif-idvdinfo2-getcmdfromevent?branch=master) method to retrieve an [**IDvdCmd**](/windows/win32/Strmif/nn-strmif-idvdcmd?branch=master) interface pointer.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

**HRESULT** value indicating the status of the command.

</dd> </dl>

## Remarks

This event is only fired if your application sets the DVD\_CMD\_FLAG\_SendEvents flag in an [**IDvdControl2**](/windows/win32/Strmif/nn-strmif-idvdcontrol2?branch=master) method that takes a [**DVD\_CMD\_FLAGS**](/windows/win32/strmif/ne-strmif-__midl___midl_itf_strmif_0000_0132_0002?branch=master) flag.

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

 

 




