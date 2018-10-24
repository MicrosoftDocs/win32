---
Description: Callback to write a texture as a DDS file.
MS-HAID: vspixengine.ITextureCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ITextureCallback interface
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.itexturecallback"></span>ITextureCallback interface

Callback to write a texture as a DDS file.

## Members

The **ITextureCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITextureCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **ITextureCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432816"><strong>ResultCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host that the .DDS (DirectDraw Surface) file containing results from the associated request are ready.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



