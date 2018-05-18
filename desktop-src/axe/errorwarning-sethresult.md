---
title: ErrorWarning SetHresult method
description: Sets the HRESULT value of this item.
ms.assetid: 'EB6C614D-900F-4734-A607-98C1140693AD'
keywords: ["SetHresult method Access Execution Engine", "SetHresult method Access Execution Engine , ErrorWarning interface", "ErrorWarning interface Access Execution Engine , SetHresult method"]
topic_type:
- apiref
api_name:
- ErrorWarning.SetHresult
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorWarning::SetHresult method

Sets the **HRESULT** value of this item.

## Syntax


```C++
virtual HRESULT SetHresult(
  [in] INT hresult
) = 0;
```



## Parameters

<dl> <dt>

*hresult* \[in\]
</dt> <dd>

The **HRESULT** value.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ErrorWarning**](errorwarning.md)
</dt> </dl>

 

 





