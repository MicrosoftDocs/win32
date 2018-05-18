---
title: Trace GetName method
description: Returns the name of the Trace.
ms.assetid: '588736AE-225E-4892-A5FE-4AA9B01AA186'
keywords: ["GetName method Access Execution Engine", "GetName method Access Execution Engine , Trace interface", "Trace interface Access Execution Engine , GetName method"]
topic_type:
- apiref
api_name:
- Trace.GetName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Trace::GetName method

Returns the name of the **Trace**.

## Syntax


```C++
virtual HRESULT GetName(
  [out] LPCWSTR *name
) const = 0;
```



## Parameters

<dl> <dt>

*name* \[out\]
</dt> <dd>

The name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Trace** objects hold data from **AssessmentResult/Traces/Trace**, **Iteration/Trace** and **Activity/Trace** elements.

The name is the value of element **Trace/Description/Name**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Trace**](trace-struct.md)
</dt> </dl>

 

 





