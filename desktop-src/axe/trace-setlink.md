---
title: Trace SetLink method
description: Sets the link of the Trace.
ms.assetid: F2EC24CA-4407-4C61-9019-97DEEA14727A
keywords:
- SetLink method Access Execution Engine
- SetLink method Access Execution Engine , Trace interface
- Trace interface Access Execution Engine , SetLink method
topic_type:
- apiref
api_name:
- Trace.SetLink
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

# Trace::SetLink method

Sets the link of the **Trace**.

## Syntax


```C++
virtual HRESULT SetLink(
  [in] LPCWSTR link
) = 0;
```



## Parameters

<dl> <dt>

*link* \[in\]
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

 

 





