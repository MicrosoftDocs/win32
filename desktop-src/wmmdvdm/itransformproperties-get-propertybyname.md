---
title: ITransformProperties get\_PropertyByName method
description: The get\_PropertyByName method retrieves a property in the collection by name.
ms.assetid: '27a8fc6d-8710-4183-9ad6-8f77658407b1'
keywords: ["get_PropertyByName method Windows Movie Maker and DVD Maker", "get_PropertyByName method Windows Movie Maker and DVD Maker , ITransformProperties interface", "ITransformProperties interface Windows Movie Maker and DVD Maker , get_PropertyByName method"]
topic_type:
- apiref
api_name:
- ITransformProperties.get_PropertyByName
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformProperties::get\_PropertyByName method

The **get\_PropertyByName** method retrieves a property in the collection by name.

## Syntax


```C++
HRESULT get_PropertyByName(
  [in]  LPCTSTR            szName,
  [out] ITransformProperty **ppProperty
);
```



## Parameters

<dl> <dt>

*szName* \[in\]
</dt> <dd>

The name of the property to retrieve.

</dd> <dt>

*ppProperty* \[out\]
</dt> <dd>

Address of a pointer to the property that was requested. The caller must release this interface when it is no longer needed.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

You can query the returned property for **ITransformProperties** to examine any child properties that it may have.

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

 

 





