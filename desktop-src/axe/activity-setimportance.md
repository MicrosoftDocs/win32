---
title: Activity SetImportance method
description: Sets the importance of the Activity.
ms.assetid: 063F78D7-071F-44B9-BF5E-04C6A7C5B246
keywords:
- SetImportance method Access Execution Engine
- SetImportance method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetImportance method
topic_type:
- apiref
api_name:
- Activity.SetImportance
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

# Activity::SetImportance method

Sets the importance of the **Activity**.

## Syntax


```C++
virtual HRESULT SetImportance(
  [in] UINT importance
) = 0;
```



## Parameters

<dl> <dt>

*importance* \[in\]
</dt> <dd>

The importance.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The importance is the value of element **Activity/Importance**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





