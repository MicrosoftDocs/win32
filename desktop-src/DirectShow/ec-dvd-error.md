---
Description: Signals a DVD error condition.
ms.assetid: 2cd3e0c4-e2b7-4aa1-9f3c-9003eabfb08a
title: EC\_DVD\_ERROR
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_DVD\_ERROR

Signals a DVD error condition.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the error condition. Member of the [**DVD\_ERROR**](/windows/win32/dvdevcod/ne-dvdevcod-_tagdvd_error?branch=master) enumerated data type.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Meaning depends on the value of *lParam1*. See [**DVD\_ERROR**](/windows/win32/dvdevcod/ne-dvdevcod-_tagdvd_error?branch=master) for more information.

</dd> </dl>

## Remarks

This event is raised in all domains.

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
</dt> </dl>

 

 




