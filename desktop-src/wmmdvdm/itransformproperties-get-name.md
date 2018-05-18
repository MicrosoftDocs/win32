---
title: ITransformProperties get\_Name method
description: The get\_Name method gets the name of the current property holding the collection of child properties. This is equivalent to ITransformProperty get\_Name.
ms.assetid: '1c3eb98c-3da7-481f-84dd-63f4fd6a6a7b'
keywords: ["get_Name method Windows Movie Maker and DVD Maker", "get_Name method Windows Movie Maker and DVD Maker , ITransformProperties interface", "ITransformProperties interface Windows Movie Maker and DVD Maker , get_Name method"]
topic_type:
- apiref
api_name:
- ITransformProperties.get_Name
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformProperties::get\_Name method

The **get\_Name** method gets the name of the current property holding the collection of child properties. This is equivalent to [**ITransformProperty::get\_Name**](itransformproperty-get-name.md).

## Syntax


```C++
HRESULT get_Name(
  [in]      LPTSTR szBuffer,
  [in, out] long   *plSizeBufferChars
);
```



## Parameters

<dl> <dt>

*szBuffer* \[in\]
</dt> <dd>

A caller-allocated buffer holding the name of the property. To learn the size that is required, call this method with this parameter set to **NULL** and the required size will be returned in *plSizeBufferChars*.

</dd> <dt>

*plSizeBufferChars* \[in, out\]
</dt> <dd>

Pointer to the size of the buffer in characters, including the termination character. On input, this is the size allocated by the caller. On output, this is the size required (if *szBuffer* is **NULL**) or the size of the returned buffer.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ITransformProperties Interface**](itransformproperties.md)
</dt> </dl>

 

 





