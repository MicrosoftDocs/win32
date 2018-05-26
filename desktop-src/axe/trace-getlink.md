---
title: Trace GetLink method
description: Returns the link of the Trace.
ms.assetid: 02893DA2-E0E3-424D-A29B-302451C516B1
keywords:
- GetLink method Access Execution Engine
- GetLink method Access Execution Engine , Trace interface
- Trace interface Access Execution Engine , GetLink method
topic_type:
- apiref
api_name:
- Trace.GetLink
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

# Trace::GetLink method

Returns the link of the **Trace**.

## Syntax


```C++
virtual HRESULT GetLink(
  [out] LPCWSTR *link
) const = 0;
```



## Parameters

<dl> <dt>

*link* \[out\]
</dt> <dd>

The link.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Trace** objects hold data from **AssessmentResult/Traces/Trace**, **Iteration/Trace** and **Activity/Trace** elements.

The link is the value of element **Trace/Link**.

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

 

 





