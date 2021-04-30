---
description: Specifies a compression filter to use when rendering the specified group.
ms.assetid: ba717cac-c5a8-4821-a5f0-dd9d5fe4834e
title: ISmartRenderEngine::SetGroupCompressor method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISmartRenderEngine.SetGroupCompressor
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISmartRenderEngine::SetGroupCompressor method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Specifies a compression filter to use when rendering the specified group.

## Syntax


```C++
HRESULT SetGroupCompressor(
   long        Group,
   IBaseFilter *pCompressor
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

Pointer to the [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface of the compression filter.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

[**ISmartRenderEngine Interface**](ismartrenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




