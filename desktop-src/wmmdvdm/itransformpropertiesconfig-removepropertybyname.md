---
title: ITransformPropertiesConfig RemovePropertyByName method
description: The RemovePropertyByName method removes a property from the current property collection by name.
ms.assetid: c1b7b4ea-ce10-4baf-a3be-728c57cc6ae2
keywords:
- RemovePropertyByName method Windows Movie Maker and DVD Maker
- RemovePropertyByName method Windows Movie Maker and DVD Maker , ITransformPropertiesConfig interface
- ITransformPropertiesConfig interface Windows Movie Maker and DVD Maker , RemovePropertyByName method
topic_type:
- apiref
api_name:
- ITransformPropertiesConfig.RemovePropertyByName
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

# ITransformPropertiesConfig::RemovePropertyByName method

The **RemovePropertyByName** method removes a property from the current property collection by name.

## Syntax


```C++
HRESULT RemovePropertyByName(
  [in] LPCTSTR szName
);
```



## Parameters

<dl> <dt>

*szName* \[in\]
</dt> <dd>

A name that specifies the property to remove. Properties have unique names in a collection.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

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

 

 





