---
Description: Callback to return object table data.
MS-HAID: vspixengine.IObjectTableCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IObjectTableCallback interface
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.iobjecttablecallback"></span>IObjectTableCallback interface

Callback to return object table data.

## Members

The **IObjectTableCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IObjectTableCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IObjectTableCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt422697"><strong>GetSupportedColumns</strong></a></td><td style="text-align: left;"><p>Gets information about which columns (types of object data) are supported by the object table.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt422698"><strong>ResultCallback</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host of object table information.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



