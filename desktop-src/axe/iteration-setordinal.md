---
title: Iteration SetOrdinal method
description: Sets the ordinal value of the Iteration.
ms.assetid: '57138FC3-B6F1-443E-B852-891EFA840450'
keywords: ["SetOrdinal method Access Execution Engine", "SetOrdinal method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , SetOrdinal method"]
topic_type:
- apiref
api_name:
- Iteration.SetOrdinal
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::SetOrdinal method

Sets the ordinal value of the **Iteration**.

## Syntax


```C++
virtual HRESULT SetOrdinal(
  [in] UINT ordinal
) = 0;
```



## Parameters

<dl> <dt>

*ordinal* \[in\]
</dt> <dd>

The ordinal value.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The ordinal value is the value of element **Iteration/Ordinal**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





