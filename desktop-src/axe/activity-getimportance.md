---
title: Activity GetImportance method
description: Returns the importance of the Activity.
ms.assetid: D499EDE4-7290-4675-A2F5-CAF14DDC077E
keywords:
- GetImportance method Access Execution Engine
- GetImportance method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetImportance method
topic_type:
- apiref
api_name:
- Activity.GetImportance
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

# Activity::GetImportance method

Returns the importance of the **Activity**.

## Syntax


```C++
virtual HRESULT GetImportance(
  [out] UINT *importance
) const = 0;
```



## Parameters

<dl> <dt>

*importance* \[out\]
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

 

 





