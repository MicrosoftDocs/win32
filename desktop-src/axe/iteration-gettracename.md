---
title: Iteration GetTraceName method
description: Returns the trace name for the Iteration.
ms.assetid: '2188963E-554D-4D6C-9F81-19D4A78C58F1'
keywords: ["GetTraceName method Access Execution Engine", "GetTraceName method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , GetTraceName method"]
topic_type:
- apiref
api_name:
- Iteration.GetTraceName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::GetTraceName method

Returns the trace name for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetTraceName(
  [out] LPCWSTR *traceName
) const = 0;
```



## Parameters

<dl> <dt>

*traceName* \[out\]
</dt> <dd>

The trace name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The trace name is the value of element **Iteration/Trace/Description/Name**.

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

 

 





