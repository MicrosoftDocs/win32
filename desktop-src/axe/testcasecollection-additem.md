---
title: TestCaseCollection AddItem method
description: Creates and adds a new TestCase to the TestCaseCollection.
ms.assetid: 3A9DB454-CCB8-4CD5-ABD3-594E07828AED
keywords:
- AddItem method Access Execution Engine
- AddItem method Access Execution Engine , TestCaseCollection interface
- TestCaseCollection interface Access Execution Engine , AddItem method
topic_type:
- apiref
api_name:
- TestCaseCollection.AddItem
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

# TestCaseCollection::AddItem method

Creates and adds a new [**TestCase**](testcase-struct.md) to the **TestCaseCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [out] TestCase **testCase
) = 0;
```



## Parameters

<dl> <dt>

*testCase* \[out\]
</dt> <dd>

The **TestCase** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**TestCaseCollection**](testcasecollection.md)
</dt> </dl>

 

 





