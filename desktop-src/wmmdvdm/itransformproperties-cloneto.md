---
title: ITransformProperties CloneTo method
description: The CloneTo method copies the current ITransformProperties interface into a submitted ITransformProperties interface.
ms.assetid: 03aa1c23-547a-42dc-b1b4-22b93ea6fdd3
keywords:
- CloneTo method Windows Movie Maker and DVD Maker
- CloneTo method Windows Movie Maker and DVD Maker , ITransformProperties interface
- ITransformProperties interface Windows Movie Maker and DVD Maker , CloneTo method
topic_type:
- apiref
api_name:
- ITransformProperties.CloneTo
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITransformProperties::CloneTo method

The **CloneTo** method copies the current **ITransformProperties** interface into a submitted **ITransformProperties** interface.

## Syntax


```C++
HRESULT CloneTo(
  [in, out] ITransformProperties *pDestProps
);
```



## Parameters

<dl> <dt>

*pDestProps* \[in, out\]
</dt> <dd>

Pointer to the properties collection where the current values should be copied to. The caller must allocate and release this interface.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

This method does not clear any existing properties in the destination collection, but adds the new values to them. If the destination collection has properties with identical names to the source collection, the identically named properties will still be copied to the destination. How identically named properties are retrieved from a collection is undefined.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ITransformProperties Interface**](itransformproperties.md)
</dt> </dl>

 

 





