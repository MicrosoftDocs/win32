---
title: TestCase SetCompositeKeySubjectClassDisplayName method
description: Sets the composite key subject class display name of the TestCase.
ms.assetid: DE5AE466-8058-40E0-B731-177B2526B3B7
keywords:
- SetCompositeKeySubjectClassDisplayName method Access Execution Engine
- SetCompositeKeySubjectClassDisplayName method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , SetCompositeKeySubjectClassDisplayName method
topic_type:
- apiref
api_name:
- TestCase.SetCompositeKeySubjectClassDisplayName
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

# TestCase::SetCompositeKeySubjectClassDisplayName method

Sets the composite key subject class display name of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetCompositeKeySubjectClassDisplayName(
  [in] LPCWSTR compositeKeySubjectClassDisplayName
) = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectClassDisplayName* \[in\]
</dt> <dd>

The composite key subject class display name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

This method is deprecated.

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

 

 





