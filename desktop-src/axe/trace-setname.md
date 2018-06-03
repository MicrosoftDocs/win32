---
title: Trace SetName method
description: Sets the name of the Trace.
ms.assetid: 32B040E9-06D6-4D98-8B82-69574087290F
keywords:
- SetName method Access Execution Engine
- SetName method Access Execution Engine , Trace interface
- Trace interface Access Execution Engine , SetName method
topic_type:
- apiref
api_name:
- Trace.SetName
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

# Trace::SetName method

Sets the name of the **Trace**.

## Syntax


```C++
virtual HRESULT SetName(
  [in] LPCWSTR name
) = 0;
```



## Parameters

<dl> <dt>

*name* \[in\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Trace**](trace-struct.md)
</dt> </dl>

 

 





