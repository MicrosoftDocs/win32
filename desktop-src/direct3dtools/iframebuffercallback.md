---
Description: Callback to return a render target. The format of the returned render target is R8G8B8A8\_UNORM regardless of the format of the in-engine rendertarget.
MS-HAID: vspixengine.IFrameBufferCallback
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameBufferCallback interface
ms.topic: interface
ms.date: 05/31/2018
---

# <span id="vspixengine.iframebuffercallback"></span>IFrameBufferCallback interface

Callback to return a render target. The format of the returned render target is R8G8B8A8\_UNORM regardless of the format of the in-engine rendertarget.

## Members

The **IFrameBufferCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IFrameBufferCallback** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IFrameBufferCallback** interface has these methods.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th style="text-align: left;">Method</th><th style="text-align: left;">Description</th></tr></thead><tbody><tr class="odd"><td style="text-align: left;"><a href="https://msdn.microsoft.com/library/windows/desktop/mt422669"><strong>ResultCallback</strong></a></td><td style="text-align: left;"><p>A callback that notifies the host of framebuffer information returned by the associated request.</p></td></tr></tbody></table>

 

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



