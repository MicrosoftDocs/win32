---
Description: Callback to return the contents of an object in buffer form for those that support it (buffers, textures).
MS-HAID: vspixengine.IBufferObjectDataCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IBufferObjectDataCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ibufferobjectdatacallback"></span>IBufferObjectDataCallback interface

Callback to return the contents of an object in buffer form for those that support it (buffers, textures).

## Members

The **IBufferObjectDataCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBufferObjectDataCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IBufferObjectDataCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>ResultCallback</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422647)</td><td style="text-align: left;"><p>A callback that notifies the host of buffer information written to a file by the assocaited request.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



