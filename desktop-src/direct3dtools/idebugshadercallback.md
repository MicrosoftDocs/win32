---
Description: Callback to return the instructions generated from creating a shader trace.
MS-HAID: vspixengine.IDebugShaderCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IDebugShaderCallback interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.idebugshadercallback"></span>IDebugShaderCallback interface

Callback to return the instructions generated from creating a shader trace.

## Members

The **IDebugShaderCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IDebugShaderCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IDebugShaderCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>ResultInstructions</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422657)</td><td style="text-align: left;"><p>A callback that notifies the host of instructrion information returned by the associated request.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



