---
title: Trace GetFile method
description: Returns the file name of the Trace.
ms.assetid: DD8383A6-DA9F-4257-BDBA-AD266B95AEE2
keywords:
- GetFile method Access Execution Engine
- GetFile method Access Execution Engine , Trace interface
- Trace interface Access Execution Engine , GetFile method
topic_type:
- apiref
api_name:
- Trace.GetFile
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

# Trace::GetFile method

Returns the file name of the **Trace**.

## Syntax


```C++
virtual HRESULT GetFile(
  [out] LPCWSTR *file
) const = 0;
```



## Parameters

<dl> <dt>

*file* \[out\]
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

 

 





