---
description: The source file has changed. The application should rebuild the filter graph.
ms.assetid: f99df68f-d7e8-4dbf-b958-84fe3f0821f0
title: EC_PLEASE_REOPEN (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_PLEASE\_REOPEN

The source file has changed. The application should rebuild the filter graph.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Zero.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

None.

## Remarks

The legacy [Windows Media Source](windows-media-source-filter.md) filter sends this event. New filters should not send this event.

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

 

 




