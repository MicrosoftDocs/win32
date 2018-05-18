---
title: Iteration SetTraceName method
description: Sets the trace name for the Iteration.
ms.assetid: 'AA373712-1292-478A-A479-8408C0747ABF'
keywords: ["SetTraceName method Access Execution Engine", "SetTraceName method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , SetTraceName method"]
topic_type:
- apiref
api_name:
- Iteration.SetTraceName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::SetTraceName method

Sets the trace name for the **Iteration**.

## Syntax


```C++
virtual HRESULT SetTraceName(
  [in] LPCWSTR traceName
) = 0;
```



## Parameters

<dl> <dt>

*traceName* \[in\]
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

 

 





