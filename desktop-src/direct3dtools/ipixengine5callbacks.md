---
Description: Callbacks used for viewing textures.
MS-HAID: vspixengine.IPixEngine5Callbacks
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine5Callbacks interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixengine5callbacks"></span>IPixEngine5Callbacks interface

Callbacks used for viewing textures.

## Members

The **IPixEngine5Callbacks** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPixEngine5Callbacks** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixEngine5Callbacks** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432757"><strong>FreeTextureComplete</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host when a texture has been freed.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432758"><strong>LoadHistogramComplete</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host when a histogram load has been completed.</p></td></tr><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432759"><strong>LoadTextureFromFileComplete</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host when a texture load has been completed.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432760"><strong>LoadTextureSliceComplete</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host when a texture slice load has been completed.</p></td></tr><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432761"><strong>ReadTexelValueComplete</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host when a texel value read has been completed.</p></td></tr><tr class="even"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432762"><strong>RenderTextureComplete</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host when a texture render has been completed.</p></td></tr><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt432763"><strong>SaveTextureComplete</strong></a></td><td style="text-align: left;"><p>A callback function used to notify the host when saving a texture has been completed.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



