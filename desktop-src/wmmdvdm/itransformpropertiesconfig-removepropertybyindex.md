---
title: ITransformPropertiesConfig RemovePropertyByIndex method
description: The RemovePropertyByIndex method removes a property from the current collection by index number.
ms.assetid: e14abd6c-2a1a-459d-8f72-1ad62499d71a
keywords:
- RemovePropertyByIndex method Windows Movie Maker and DVD Maker
- RemovePropertyByIndex method Windows Movie Maker and DVD Maker , ITransformPropertiesConfig interface
- ITransformPropertiesConfig interface Windows Movie Maker and DVD Maker , RemovePropertyByIndex method
topic_type:
- apiref
api_name:
- ITransformPropertiesConfig.RemovePropertyByIndex
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

# ITransformPropertiesConfig::RemovePropertyByIndex method

The **RemovePropertyByIndex** method removes a property from the current collection by index number.

## Syntax


```C++
HRESULT RemovePropertyByIndex(
  [in] long nIndex
);
```



## Parameters

<dl> <dt>

*nIndex* \[in\]
</dt> <dd>

Zero-based index of the property to remove.

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

 

 





