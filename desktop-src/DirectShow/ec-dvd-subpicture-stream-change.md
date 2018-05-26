---
Description: Signals that the current subpicture stream number changed for the main title.
ms.assetid: b6da3201-55df-47dc-ad4f-5cd2e78073ee
title: EC\_DVD\_SUBPICTURE\_STREAM\_CHANGE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_DVD\_SUBPICTURE\_STREAM\_CHANGE

Signals that the current subpicture stream number changed for the main title.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**DWORD** value indicating the new user subpicture stream number. Subpicture stream numbers range from 0 to 31. Stream 0xFFFFFFFF indicates that no stream is selected.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Boolean value that indicates the subpicture's on/off state.

</dd> </dl>

## Remarks

The subpicture can change automatically with a navigation command authored on disc as well as through application control using [**IDvdControl2**](/windows/win32/Strmif/nn-strmif-idvdcontrol2?branch=master).

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

 

 




