---
title: Iteration GetOrdinal method
description: Returns the ordinal value of the Iteration.
ms.assetid: '7F9071CD-E451-4A6C-8DDA-0AE9E38D0D05'
keywords: ["GetOrdinal method Access Execution Engine", "GetOrdinal method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , GetOrdinal method"]
topic_type:
- apiref
api_name:
- Iteration.GetOrdinal
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::GetOrdinal method

Returns the ordinal value of the **Iteration**.

## Syntax


```C++
virtual HRESULT GetOrdinal(
  [out] UINT *ordinal
) const = 0;
```



## Parameters

<dl> <dt>

*ordinal* \[out\]
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

 

 





