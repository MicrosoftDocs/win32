---
title: TestCaseCollection GetItem method
description: Returns a TestCase from the TestCaseCollection.
ms.assetid: 92E84358-7A97-49F0-AF4B-34C8C0CA4E29
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , TestCaseCollection interface
- TestCaseCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- TestCaseCollection.GetItem
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

# TestCaseCollection::GetItem method

Returns a [**TestCase**](testcase-struct.md) from the **TestCaseCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT      index,
  [out] TestCase **testCase
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **TestCase** identifier.

</dd> <dt>

*testCase* \[out\]
</dt> <dd>

The **TestCase**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 





