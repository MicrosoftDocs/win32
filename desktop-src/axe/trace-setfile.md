---
title: Trace SetFile method
description: Sets the file name of the Trace.
ms.assetid: 8A212615-4321-4745-9E8A-B15E17061FF3
keywords:
- SetFile method Access Execution Engine
- SetFile method Access Execution Engine , Trace interface
- Trace interface Access Execution Engine , SetFile method
topic_type:
- apiref
api_name:
- Trace.SetFile
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Trace::SetFile method

Sets the file name of the **Trace**.

## Syntax


```C++
virtual HRESULT SetFile(
  [in] LPCWSTR file
) = 0;
```



## Parameters

<dl> <dt>

*file* \[in\]
</dt> <dd>

The file name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Trace** objects hold data from **AssessmentResult/Traces/Trace**, **Iteration/Trace** and **Activity/Trace** elements.

The file name is the value of element **Trace/File**.

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

 

 





