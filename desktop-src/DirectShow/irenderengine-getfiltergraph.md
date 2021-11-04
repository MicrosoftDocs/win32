---
description: The GetFilterGraph method retrieves the filter graph that the render engine has constructed, if any.
ms.assetid: 509b2c9c-c21b-4855-880f-f09ad342e758
title: IRenderEngine::GetFilterGraph method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.GetFilterGraph
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IRenderEngine::GetFilterGraph method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetFilterGraph` method retrieves the filter graph that the render engine has constructed, if any.

## Syntax


```C++
HRESULT GetFilterGraph(
  [out] IGraphBuilder **ppFG
);
```



## Parameters

<dl> <dt>

*ppFG* \[out\]
</dt> <dd>

Receives a pointer to the filter graph's [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) interface. It receives the value **NULL** if there is no filter graph.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                            | Description                                    |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success.<br/>                            |
| <dl> <dt>**E\_MUST\_INIT\_RENDERER**</dt> </dl> | Render engine failed to initialize.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>              | Invalid pointer.<br/>                    |



 

## Remarks

Use the [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) method to build the front end of the filter graph. For preview, use the [**IRenderEngine::RenderOutputPins**](irenderengine-renderoutputpins.md) to complete the graph. For file output, connect the front end to a mux/file writer combination. For more information, see [Rendering a Project](rendering-a-project.md).

The resulting graph can be run, paused, stopped, and seeked; the playback rate cannot be changed, however.

On return, if the value of *\*ppFG* is non-**NULL**, the **IGraphBuilder** interface has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IRenderEngine Interface**](irenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




