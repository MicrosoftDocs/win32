---
title: ITransformPropertiesConfig AddProperty method
description: The AddProperty method adds a previously created property to the current collection.
ms.assetid: 72976722-b759-4bd5-8b42-3dd893adcfd8
keywords:
- AddProperty method Windows Movie Maker and DVD Maker
- AddProperty method Windows Movie Maker and DVD Maker , ITransformPropertiesConfig interface
- ITransformPropertiesConfig interface Windows Movie Maker and DVD Maker , AddProperty method
topic_type:
- apiref
api_name:
- ITransformPropertiesConfig.AddProperty
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITransformPropertiesConfig::AddProperty method

The **AddProperty** method adds a previously created property to the current collection.

## Syntax


```C++
HRESULT AddProperty(
  [in] ITransformProperty *pNewProperty
);
```



## Parameters

<dl> <dt>

*pNewProperty* \[in\]
</dt> <dd>

Pointer to an existing property to add to the current collection. You can get this value by calling [**ITransformProperties::get\_PropertyByIndex**](itransformproperties-get-propertybyindex.md), [**ITransformProperties::get\_PropertyByName**](itransformproperties-get-propertybyname.md), [**ITransformProperty::Clone**](itransformproperty-clone.md), [**ITransformPropertiesConfig::CreateProperty**](itransformpropertiesconfig-createproperty.md), or [**CreateTransformProperty**](createtransformproperty.md).

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

If a property already exists with the same name as the submitted property, this method will add a property with a duplicate name and the new value. The caller can still get duplicate properties by iterating through child properties using [**ITransformProperties::get\_PropertyByIndex**](itransformproperties-get-propertybyindex.md); however, when calling [**ITransformProperties::get\_PropertyByName**](itransformproperties-get-propertybyname.md), which duplicate property will be retrieved is undefined.

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

 

 





