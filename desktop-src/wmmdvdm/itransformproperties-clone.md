---
title: ITransformProperties Clone method
description: The Clone method creates a copy of the current ITransformProperties interface.
ms.assetid: e64d4fde-9308-496b-a10d-e3a3747e999f
keywords:
- Clone method Windows Movie Maker and DVD Maker
- Clone method Windows Movie Maker and DVD Maker , ITransformProperties interface
- ITransformProperties interface Windows Movie Maker and DVD Maker , Clone method
topic_type:
- apiref
api_name:
- ITransformProperties.Clone
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

# ITransformProperties::Clone method

The **Clone** method creates a copy of the current **ITransformProperties** interface.

## Syntax


```C++
HRESULT Clone(
  [out] ITransformProperties **ppNewProps
);
```



## Parameters

<dl> <dt>

*ppNewProps* \[out\]
</dt> <dd>

Address of a pointer to a copy of this collection. The caller must release the retrieved interface when done with it.

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

[**ITransformProperties Interface**](itransformproperties.md)
</dt> </dl>

 

 





