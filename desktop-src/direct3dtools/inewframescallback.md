---
Description: Callback from engine indicating that it is done parsing any new frames added to the log.
MS-HAID: vspixengine.INewFramesCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: INewFramesCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.inewframescallback"></span>INewFramesCallback interface

Callback from engine indicating that it is done parsing any new frames added to the log.

## Members

The **INewFramesCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **INewFramesCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **INewFramesCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>CancelAll</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422691)</td><td style="text-align: left;"><p>A callback that notifies the host that all requests have been cancelled.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>CancelUsingCallback</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422692)</td><td style="text-align: left;"><p>A callback that notifies the host of a canceled request.</p></td></tr><tr class="odd"><td style="text-align: left;">[<strong>CancelUsingCookie</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422693)</td><td style="text-align: left;"><p>A callback that notifies the host of a canceled request by using a cookie that uniquely identifies the request.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>NewFramesAvailable</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422694)</td><td style="text-align: left;"><p>A callback that notifies the host that new frames are available to be processed.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



