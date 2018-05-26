---
Description: The video renderer was destroyed or removed from the graph.
ms.assetid: facf35c2-d6a2-4373-bce5-171fd9325116
title: EC\_WINDOW\_DESTROYED
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EC\_WINDOW\_DESTROYED

The video renderer was destroyed or removed from the graph.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**IUnknown**\*) Pointer to the video renderer's [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master) interface.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

The filter graph manager releases this window as the focus, through the [**IResourceManager**](/windows/win32/Strmif/nn-strmif-iresourcemanager?branch=master) interface. It does not send the event notification to the application.

## Remarks

The video renderer sends this event when it leaves the filter graph, in its [**IBaseFilter::JoinFilterGraph**](/windows/win32/Strmif/nf-strmif-ibasefilter-joinfiltergraph?branch=master) method. (Sending the event when the filter is destroyed might be too late, because at that point the filter graph manager might also be destroyed.)

This event enables other filters to acquire resources that depend on window focus, such as audio devices.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




