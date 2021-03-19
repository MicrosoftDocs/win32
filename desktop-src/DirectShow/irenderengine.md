---
description: The IRenderEngine interface renders a DirectShow Editing Services (DES) project by constructing a filter graph from a timeline.DES provides two components that implement this interface:The basic render engine creates uncompressed output.
ms.assetid: e2a91b34-ee4d-405e-81bf-29d15ea6342a
title: IRenderEngine interface (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IRenderEngine interface

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IRenderEngine` interface renders a [DirectShow Editing Services](directshow-editing-services.md) (DES) project by constructing a filter graph from a timeline.

DES provides two components that implement this interface:

-   The *basic render engine* creates uncompressed output. You can use the output for preview, or route it through compression filters and write it to a file.
-   The *smart render engine* creates compressed output, using *smart recompression*. With smart recompression, a source file is recompressed only if its format differs from the output format. A source with a matching format is written directly to the output file. Depending on the scenario, smart recompression can greatly improve rendering time.

The smart render engine also supports the [**ISmartRenderEngine**](ismartrenderengine.md) interface.

Although an application can create a filter graph and pass it to a render engine, the typical scenario is for the render engine to create the filter graph. Building the graph is a two-stage process. First, build the front end by calling the [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) method. Then connect the output pins on the front end to the desired rendering filters:

-   Video and audio renderers for preview, or
-   Compressors, multiplexers, and file writers to generate the final output.

## Members

The **IRenderEngine** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IRenderEngine** also has these types of members:

-   [Methods](#methods)

### Methods

The **IRenderEngine** interface has these methods.



| Method                                                                             | Description                                                                           |
|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**Commit**](irenderengine-commit.md)                                             | Not implemented.<br/>                                                           |
| [**ConnectFrontEnd**](irenderengine-connectfrontend.md)                           | Builds the front end of the filter graph from the current timeline.<br/>        |
| [**Decommit**](irenderengine-decommit.md)                                         | Not implemented.<br/>                                                           |
| [**DoSmartRecompression**](irenderengine-dosmartrecompression.md)                 | Not supported.<br/>                                                             |
| [**GetCaps**](irenderengine-getcaps.md)                                           | Not implemented.<br/>                                                           |
| [**GetFilterGraph**](irenderengine-getfiltergraph.md)                             | Retrieves the filter graph that the render engine has constructed, if any.<br/> |
| [**GetGroupOutputPin**](irenderengine-getgroupoutputpin.md)                       | Retrieves the output pin for the specified group.<br/>                          |
| [**GetTimelineObject**](irenderengine-gettimelineobject.md)                       | Retrieves the timeline that the render engine is currently using.<br/>          |
| [**GetVendorString**](irenderengine-getvendorstring.md)                           | Retrieves the vendor string.<br/>                                               |
| [**RenderOutputPins**](irenderengine-renderoutputpins.md)                         | Creates the previewing portion of the filter graph.<br/>                        |
| [**ScrapIt**](irenderengine-scrapit.md)                                           | Discards the render engine's filter graph and all associated objects.<br/>      |
| [**SetDynamicReconnectLevel**](irenderengine-setdynamicreconnectlevel.md)         | Sets the level of dynamic reconnection during rendering.<br/>                   |
| [**SetFilterGraph**](irenderengine-setfiltergraph.md)                             | Specifies a filter graph for the render engine to use.<br/>                     |
| [**SetInterestRange**](irenderengine-setinterestrange.md)                         | Not supported.<br/>                                                             |
| [**SetInterestRange2**](irenderengine-setinterestrange2.md)                       | Not supported.<br/>                                                             |
| [**SetRenderRange**](irenderengine-setrenderrange.md)                             | Sets the range of time to be rendered.<br/>                                     |
| [**SetRenderRange2**](irenderengine-setrenderrange2.md)                           | Sets the range of time to be rendered, as a **double**.<br/>                    |
| [**SetSourceConnectCallback**](irenderengine-setsourceconnectcallback.md)         | Not supported.<br/>                                                             |
| [**SetSourceNameValidation**](irenderengine-setsourcenamevalidation.md)           | Specifies how the render engine validates file names.<br/>                      |
| [**SetTimelineObject**](irenderengine-settimelineobject.md)                       | Sets the timeline for the render engine to use.<br/>                            |
| [**UseInSmartRecompressionGraph**](irenderengine-useinsmartrecompressiongraph.md) | Not supported.<br/>                                                             |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Rendering a Project](rendering-a-project.md)
</dt> </dl>

 

 
