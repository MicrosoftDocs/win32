---
Description: Signals a DVD warning condition.
ms.assetid: d7221e8a-089f-4eaf-a193-548709c14336
title: EC\_DVD\_WARNING
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_DVD\_WARNING

Signals a DVD warning condition.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the warning condition. Member of the [**DVD\_WARNING**](/windows/win32/dvdevcod/ne-dvdevcod-_tagdvd_warning?branch=master) enumerated data type.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

If *pParam1* equals DVD\_WARNING\_Open, DVD\_WARNING\_Seek, or DVD\_WARNING\_Read, then *lParam2* contains the last error code returned from **GetLastError**.

</dd> </dl>

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

 

 




