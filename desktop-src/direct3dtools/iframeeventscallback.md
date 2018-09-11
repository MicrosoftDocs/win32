---
Description: Callback to return the list of events in a frame.
MS-HAID: vspixengine.IFrameEventsCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameEventsCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.iframeeventscallback"></span>IFrameEventsCallback interface

Callback to return the list of events in a frame.

## Members

The **IFrameEventsCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IFrameEventsCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IFrameEventsCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt422673"><strong>GetSupportedEventColumns</strong></a></td><td style="text-align: left;"><p>Gets information about which columns (types of event data) are supported by the event list.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt422674"><strong>ResultCallback</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host of information about events in the event list.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



