---
title: ITransformPropertiesConfig CreateProperty method
description: The CreateProperty method creates a new property and adds it to the current property collection.
ms.assetid: a8091f90-7a23-4f18-91f2-2206c9770a9f
keywords:
- CreateProperty method Windows Movie Maker and DVD Maker
- CreateProperty method Windows Movie Maker and DVD Maker , ITransformPropertiesConfig interface
- ITransformPropertiesConfig interface Windows Movie Maker and DVD Maker , CreateProperty method
topic_type:
- apiref
api_name:
- ITransformPropertiesConfig.CreateProperty
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

# ITransformPropertiesConfig::CreateProperty method

The **CreateProperty** method creates a new property and adds it to the current property collection.

## Syntax


```C++
HRESULT CreateProperty(
  [in]  LPCTSTR            szPropertyName,
  [in]  PROPVARIANT        varValue,
  [out] ITransformProperty **ppNewProperty
);
```



## Parameters

<dl> <dt>

*szPropertyName* \[in\]
</dt> <dd>

A pointer to a **NULL**-terminated string that specifies the name for the new property.

</dd> <dt>

*varValue* \[in\]
</dt> <dd>

A **PROPVARIANT** that specifies the value of the new property.

</dd> <dt>

*ppNewProperty* \[out\]
</dt> <dd>

Address of a pointer to the newly created property.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

An alternate way of creating a new property is to call [**ITransformPropertiesConfig::SetPropertyValue**](itransformpropertiesconfig-setpropertyvalue.md); however, if the property with the specified name already exists, that method will overwrite the existing property.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ITransformPropertiesConfig Interface**](itransformpropertiesconfig.md)
</dt> </dl>

 

 





