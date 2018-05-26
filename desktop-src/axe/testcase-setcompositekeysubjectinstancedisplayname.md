---
title: TestCase SetCompositeKeySubjectInstanceDisplayName method
description: Sets the composite key subject instance display name of the TestCase.
ms.assetid: A3C61A7A-3D9E-4606-A9FE-CD8871BD1266
keywords:
- SetCompositeKeySubjectInstanceDisplayName method Access Execution Engine
- SetCompositeKeySubjectInstanceDisplayName method Access Execution Engine , TestCase interface
- TestCase interface Access Execution Engine , SetCompositeKeySubjectInstanceDisplayName method
topic_type:
- apiref
api_name:
- TestCase.SetCompositeKeySubjectInstanceDisplayName
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

# TestCase::SetCompositeKeySubjectInstanceDisplayName method

Sets the composite key subject instance display name of the **TestCase.**

## Syntax


```C++
virtual HRESULT SetCompositeKeySubjectInstanceDisplayName(
  [in] LPCWSTR compositeKeySubjectInstanceDisplayName
) = 0;
```



## Parameters

<dl> <dt>

*compositeKeySubjectInstanceDisplayName* \[in\]
</dt> <dd>

The composite key subject instance display name.

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

 

 





