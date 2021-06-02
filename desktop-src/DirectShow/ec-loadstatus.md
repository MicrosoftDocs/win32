---
description: Notifies the application of progress when opening a network file.
ms.assetid: 022b87e5-76af-4253-9485-97140f294938
title: EC_LOADSTATUS (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_LOADSTATUS

Notifies the application of progress when opening a network file.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Status code. See Remarks.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

None.

## Remarks

The [WM ASF Reader](wm-asf-reader-filter.md) filter and the legacy [Windows Media Source](windows-media-source-filter.md) filter send this event. The first event parameter has one of the following values.



| Value                        | Description                                    |
|------------------------------|------------------------------------------------|
| AM\_LOADSTATUS\_CLOSED       | The source filter has closed the file.         |
| AM\_LOADSTATUS\_CONNECTING   | The source filter is connecting to the server. |
| AM\_LOADSTATUS\_LOADINGDESCR | Not used.                                      |
| AM\_LOADSTATUS\_LOADINGMCAST | Not used                                       |
| AM\_LOADSTATUS\_LOCATING     | The source filter is locating requested data.  |
| AM\_LOADSTATUS\_OPEN         | The source filter has opened the file.         |
| AM\_LOADSTATUS\_OPENING      | The source filter is opening the file.         |



 

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

 

 




