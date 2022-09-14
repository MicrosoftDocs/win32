---
description: Specifies the time stamp for the most recent frame step.
ms.assetid: 2c2ef8b8-7bee-4cd8-ad87-b48d6a48aa0e
title: EC_SCRUB_TIME (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_SCRUB\_TIME

Specifies the time stamp for the most recent frame step.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**DWORD**) Lower 32 bits of the time stamp.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

(**DWORD**) Upper 32 bits of the time stamp.

</dd> </dl>

## Default Action

None.

## Remarks

The presenter for the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) filter sends this message to the EVR when it completes a frame step.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> </dl>

 

 




