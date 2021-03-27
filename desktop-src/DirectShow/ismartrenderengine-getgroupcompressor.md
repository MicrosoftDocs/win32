---
description: The GetGroupCompressor method retrieves the compression filter for the specified group.
ms.assetid: 9d71e659-7abb-48c6-b9bd-5239560dc150
title: ISmartRenderEngine::GetGroupCompressor method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISmartRenderEngine.GetGroupCompressor
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISmartRenderEngine::GetGroupCompressor method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetGroupCompressor` method retrieves the compression filter for the specified group.

## Syntax


```C++
HRESULT GetGroupCompressor(
   long        Group,
   IBaseFilter **pCompressor
);
```



## Parameters

<dl> <dt>

*Group* 
</dt> <dd>

Zero-based index of the group.

</dd> <dt>

*pCompressor* 
</dt> <dd>

Receives a pointer to the [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface of the compression filter. It receives the value **NULL** if there is no compression filter.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Use this method to set properties on the compression filter, such as the key-frame rate. Call this method after calling [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md), but before rendering the project. Then query the compression filter's output pin for the [**IAMVideoCompression**](/windows/desktop/api/Strmif/nn-strmif-iamvideocompression) interface, which contains methods for setting compression parameters. Release the interface when you are done. If you make any subsequent changes to the timeline, call **ConnectFrontEnd**, and then call **GetGroupCompressor** again to reset the compression parameters.

On return, if the value of \**pCompressor* is non-**NULL**, the [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface has an outstanding reference count. Be sure to release the interface when you are done using it.

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

[**ISmartRenderEngine Interface**](ismartrenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




