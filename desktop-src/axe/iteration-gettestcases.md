---
title: Iteration GetTestCases method
description: Returns the TestCaseCollection for the Iteration.
ms.assetid: 8B377587-9150-49BA-AABC-E6DC219E2DD9
keywords:
- GetTestCases method Access Execution Engine
- GetTestCases method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , GetTestCases method
topic_type:
- apiref
api_name:
- Iteration.GetTestCases
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

# Iteration::GetTestCases method

Returns the [**TestCaseCollection**](testcasecollection.md) for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetTestCases(
  [out] TestCaseCollection **testCases
) = 0;
```



## Parameters

<dl> <dt>

*testCases* \[out\]
</dt> <dd>

The **TestCaseCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCaseCollection** holds information from element **Iteration/TestCases**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





