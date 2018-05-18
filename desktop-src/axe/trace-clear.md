---
title: Trace Clear method
description: Clears the settings of the Trace.
ms.assetid: '336D1C8E-101A-4CA8-8EAA-2E76936ED7BD'
keywords: ["Clear method Access Execution Engine", "Clear method Access Execution Engine , Trace interface", "Trace interface Access Execution Engine , Clear method"]
topic_type:
- apiref
api_name:
- Trace.Clear
api_location:
- AxeCore.dll
api_type:
- COM
---

# Trace::Clear method

Clears the settings of the **Trace**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Trace** objects hold data from **AssessmentResult/Traces/Trace**, **Iteration/Trace** and **Activity/Trace** elements.

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

 

 





