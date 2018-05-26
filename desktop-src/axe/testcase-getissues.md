---
title: TestCase GetIssues method
description: Returns the IssueCollection for the TestCase.
ms.assetid: 09B899D4-B720-41AB-BC02-42E5066A5C8B
keywords:
- GetIssues method Access Execution Engine
- GetIssues method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , GetIssues method
topic_type:
- apiref
api_name:
- TestCase.GetIssues
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

# TestCase::GetIssues method

Returns the [**IssueCollection**](issuecollection.md) for the **TestCase**.

## Syntax


```C++
virtual HRESULT GetIssues(
  [out] IssueCollection **issues
) = 0;
```



## Parameters

<dl> <dt>

*issues* \[out\]
</dt> <dd>

The **IssueCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

The **IssueCollection** holds information from element **TestCase/Issues**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCase**](testcase-struct.md)
</dt> </dl>

 

 





