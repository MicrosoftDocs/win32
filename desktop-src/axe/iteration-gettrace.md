---
title: Iteration GetTrace method
description: Returns the Trace object of the Iteration.
ms.assetid: '7D132651-0F80-4351-B6E1-06B37C66E7E3'
keywords: ["GetTrace method Access Execution Engine", "GetTrace method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , GetTrace method"]
topic_type:
- apiref
api_name:
- Iteration.GetTrace
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::GetTrace method

Returns the [**Trace**](trace-struct.md) object of the **Iteration**.

## Syntax


```C++
virtual HRESULT GetTrace(
  [out] Trace **trace
) = 0;
```



## Parameters

<dl> <dt>

*trace* \[out\]
</dt> <dd>

The **Trace** object.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Trace** object holds information from element **Iteration/Trace**.

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

 

 





