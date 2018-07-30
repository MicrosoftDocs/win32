---
Description: Extensions to the IPixEngine4 interface containing additions for viewing textures.
MS-HAID: vspixengine.IPixEngine5
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine5 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixengine5"></span>IPixEngine5 interface

Extensions to the IPixEngine4 interface containing additions for viewing textures.

## Members

The **IPixEngine5** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPixEngine5** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPixEngine5** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;">[<strong>FreeTextureAsync</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432764)</td><td style="text-align: left;"><p>Frees a texture and notifies the host asynchronously.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>LoadHistogramAsync</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432765)</td><td style="text-align: left;"><p>An asynchronous request to load histogram data.</p></td></tr><tr class="odd"><td style="text-align: left;">[<strong>LoadTextureFromFileAsync</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432766)</td><td style="text-align: left;"><p>Loads a texture from a file and notifies the host asynchronously when it completes.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>LoadTextureSliceAsync</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432767)</td><td style="text-align: left;"><p>Loads a texture slice and notifies the host asynchrnously when it completes.</p></td></tr><tr class="odd"><td style="text-align: left;">[<strong>ReadTexelValueAsync</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432768)</td><td style="text-align: left;"><p>Reads a texel value and returns the result to the host asynchrnously.</p></td></tr><tr class="even"><td style="text-align: left;">[<strong>RenderTextureAsync</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432769)</td><td style="text-align: left;"><p>Renders a texture to a file and returns the result to the host asynchrnously.</p></td></tr><tr class="odd"><td style="text-align: left;">[<strong>SaveTextureAsync</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432770)</td><td style="text-align: left;"><p>Saves a texture.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



