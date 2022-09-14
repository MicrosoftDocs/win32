---
description: A stream-control stop command has taken effect.
ms.assetid: a2f7a959-fafd-47ff-9b3d-1a898fdb1f81
title: EC_STREAM_CONTROL_STOPPED (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_STREAM\_CONTROL\_STOPPED

A stream-control stop command has taken effect.

## Parameters

<dl> <dt>

<span id="pSender"></span><span id="psender"></span><span id="PSENDER"></span>*pSender*
</dt> <dd>

(**IUnknown**\*) Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface of the pin that stopped the stream.

</dd> <dt>

<span id="dwCookie"></span><span id="dwcookie"></span><span id="DWCOOKIE"></span>*dwCookie*
</dt> <dd>

(**DWORD**) User-defined value.

</dd> </dl>

## Default Action

None.

## Remarks

Filters send this event in response to the [**IAMStreamControl::StopAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-stopat) method. The **StopAt** method specifies a reference time for a pin to stop streaming. When streaming does halt, the filter sends this event.

The *pSender* parameter specifies the pin that executes the stop command. Depending on the implementation, it might not be the pin that received the [**StopAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-stopat) call.

The *dwCookie* parameter is specified by the application in the [**StopAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-stopat) method. This parameter enables the application to track multiple calls to the method.

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

 

 




