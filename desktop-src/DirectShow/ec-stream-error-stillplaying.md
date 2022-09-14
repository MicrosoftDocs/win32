---
description: An error occurred in a stream, but the stream is still playing.
ms.assetid: ff155c01-22ba-46dd-85b8-05eabf956908
title: EC_STREAM_ERROR_STILLPLAYING (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_STREAM\_ERROR\_STILLPLAYING

An error occurred in a stream, but the stream is still playing.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**HRESULT**) Failure code of the operation that failed.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

(**DWORD**) Minor error code. This value is usually zero.

</dd> </dl>

## Default Action

None. The application must decide whether to stop the graph.

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

 

 




