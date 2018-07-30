---
Description: Callback to return the versions of all the interfaces supported. This allows the consumer to be out of sync with the capture engine.
MS-HAID: vspixengine.IVersionCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IVersionCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.iversioncallback"></span>IVersionCallback interface

Callback to return the versions of all the interfaces supported. This allows the consumer to be out of sync with the capture engine.

## Members

The **IVersionCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IVersionCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IVersionCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>VersionTableReady</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432827)</td><td style="text-align: left;"><p>A callback function used to notify the host of which interfaces are supported.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



