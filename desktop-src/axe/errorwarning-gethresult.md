---
title: ErrorWarning GetHresult method
description: Gets the HRESULT value of this item.
ms.assetid: CAD1750F-15EF-475A-825F-6BFB26722C51
keywords:
- GetHresult method Access Execution Engine
- GetHresult method Access Execution Engine , ErrorWarning interface
- ErrorWarning interface Access Execution Engine , GetHresult method
topic_type:
- apiref
api_name:
- ErrorWarning.GetHresult
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ErrorWarning::GetHresult method

Gets the **HRESULT** value of this item.

## Syntax


```C++
virtual HRESULT GetHresult(
  [out] INT *hresult
) const = 0;
```



## Parameters

<dl> <dt>

*hresult* \[out\]
</dt> <dd>

The **HRESULT** value of this item.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ErrorWarning**](errorwarning.md)
</dt> </dl>

 

 





