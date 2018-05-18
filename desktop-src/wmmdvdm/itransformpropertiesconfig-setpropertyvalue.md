---
title: ITransformPropertiesConfig SetPropertyValue method
description: The SetPropertyValue method assigns a property with a time point to a collection.
ms.assetid: '84a8c993-fba4-46f7-bd2a-ebe7c86991ca'
keywords: ["SetPropertyValue method Windows Movie Maker and DVD Maker", "SetPropertyValue method Windows Movie Maker and DVD Maker , ITransformPropertiesConfig interface", "ITransformPropertiesConfig interface Windows Movie Maker and DVD Maker , SetPropertyValue method"]
topic_type:
- apiref
api_name:
- ITransformPropertiesConfig.SetPropertyValue
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformPropertiesConfig::SetPropertyValue method

The **SetPropertyValue** method assigns a property with a time point to a collection.

## Syntax


```C++
HRESULT SetPropertyValue(
  [in] LPCTSTR     szName,
  [in] double      dblTime,
  [in] PROPVARIANT varValue
);
```



## Parameters

<dl> <dt>

*szName* \[in\]
</dt> <dd>

The name of the new property.

</dd> <dt>

*dblTime* \[in\]
</dt> <dd>

A time value for a time point to assign to the property. This should be from 0.0 (the start of the effect or transition) to 1.0 (the end of the effect or transition).

</dd> <dt>

*varValue* \[in\]
</dt> <dd>

The value to assign to the property at time *dblTime*.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

If a property with the specified name already exists, this method will modify the existing property. If no property with this name exists, this method will create and add a new property.

An alternate way of creating a new property is [**ITransformPropertiesConfig::CreateProperty**](itransformpropertiesconfig-createproperty.md).

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ITransformPropertiesConfig Interface**](itransformpropertiesconfig.md)
</dt> </dl>

 

 





