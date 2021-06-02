---
description: Sent when an application uses the WM ASF Writer filter to index Windows Media Video files.
ms.assetid: e5f69aa1-f9b0-4403-acab-25d1f971a876
title: EC_WMT_INDEX_EVENT (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC_WMT_INDEX_EVENT (Dshow.h)

Sent when an application uses the [WM ASF Writer](wm-asf-writer-filter.md) filter to index Windows Media Video files.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Can be one of the following **WMT\_STATUS** messages.



| Value                | Description              |
|----------------------|--------------------------|
| WMT\_STARTED         | Indexing has begun.      |
| WMT\_CLOSED          | Indexing has completed.  |
| WMT\_INDEX\_PROGRESS | Indexing is in progress. |



 

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

If *lParam1* is WMT\_CLOSED or WMT\_STARTED, then *lParam2* is zero. If *lParam1* is WMT\_INDEX\_PROGRESS, then *lParam2* is a **DWORD** that specifies the current progress as a percentage of the total download size.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




