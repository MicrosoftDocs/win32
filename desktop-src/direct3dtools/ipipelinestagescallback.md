---
Description: Not used. Formerly a callback for pipeline stages data.
MS-HAID: vspixengine.IPipeLineStagesCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPipeLineStagesCallback interface
ms.topic: interface
ms.date: 05/31/2018
ms.assetid: 2F5B84DB-3D06-4D82-BF1D-E5853CC4B835
api_name: 
 - IPipeLineStagesCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipipelinestagescallback"></span>IPipeLineStagesCallback interface

Not used. Formerly a callback for pipeline stages data.

## Members

The **IPipeLineStagesCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPipeLineStagesCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPipeLineStagesCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432722"><strong>GetSupportedStages</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of which pipeline stages are used by the draw call of the assocaited request.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432723"><strong>MeshDataNotAvailableCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of which pipeline stages are not able to return mesh data for the event specified in the associated request.</p></td></tr><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432724"><strong>MeshDataVertCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of pipeline stages mesh information returned by the assocaited request.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432725"><strong>ResultCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of pipeline stages image information returned by the assocaited request.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



