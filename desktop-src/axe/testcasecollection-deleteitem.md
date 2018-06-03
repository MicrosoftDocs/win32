---
title: TestCaseCollection DeleteItem method
description: Deletes a TestCase from the TestCaseCollection.
ms.assetid: D4AE2F75-EC03-4269-8A02-92CDA44F245D
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , TestCaseCollection interface
- TestCaseCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- TestCaseCollection.DeleteItem
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

# TestCaseCollection::DeleteItem method

Deletes a [**TestCase**](testcase-struct.md) from the **TestCaseCollection**.

## Syntax


```C++
virtual HRESULT DeleteItem(
  [in] INT index
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **TestCase** identifier.

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

 

 





