---
Description: Callback to returns offline analysis data.
MS-HAID: vspixengine.IOfflineAnalysisCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IOfflineAnalysisCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.iofflineanalysiscallback"></span>IOfflineAnalysisCallback interface

Callback to returns offline analysis data.

## Members

The **IOfflineAnalysisCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IOfflineAnalysisCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IOfflineAnalysisCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>OfflineAnalysisComplete</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432707)</td><td style="text-align: left;"><p>A callback function used to notify the host that offline analysis has completed.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>OfflineAnalysisProgress</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432708)</td><td style="text-align: left;"><p>A callback function used to notify the host of offline analysis progress.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



