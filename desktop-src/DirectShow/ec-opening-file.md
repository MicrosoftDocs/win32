---
description: The graph is opening a file, or has finished opening a file.
ms.assetid: 352867e1-025f-4adb-be32-f7941c0ec8cf
title: EC_OPENING_FILE (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_OPENING\_FILE

The graph is opening a file, or has finished opening a file.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

**TRUE** if the graph is starting to open a file, or **FALSE** if the graph is no longer opening the file.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

None.

## Remarks

A filter can send this event if it spends significant time opening a file. (For example, the file might be located on a network.) The application can use this event to adjust its user interface.

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

 

 




