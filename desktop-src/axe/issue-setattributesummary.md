---
title: Issue SetAttributeSummary method
description: Sets the summary of the Issue.
ms.assetid: 3A4FEC5D-A788-4335-B5C4-454863AE1651
keywords:
- SetAttributeSummary method Access Execution Engine
- SetAttributeSummary method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetAttributeSummary method
topic_type:
- apiref
api_name:
- Issue.SetAttributeSummary
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

# Issue::SetAttributeSummary method

Sets the summary of the **Issue**.

## Syntax


```C++
virtual HRESULT SetAttributeSummary(
  [in] LPCWSTR attributeSummary
) = 0;
```



## Parameters

<dl> <dt>

*attributeSummary* \[in\]
</dt> <dd>

The summary.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The summary is attribute **Summary** of element **Issue**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





