---
title: Activity SetActivityInstance method
description: Sets the activity instance of the Activity.
ms.assetid: 20117190-89C8-449A-BA12-A7F49128F5CA
keywords:
- SetActivityInstance method Access Execution Engine
- SetActivityInstance method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetActivityInstance method
topic_type:
- apiref
api_name:
- Activity.SetActivityInstance
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

# Activity::SetActivityInstance method

Sets the activity instance of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityInstance(
  [in] LPCWSTR activityInstance
) = 0;
```



## Parameters

<dl> <dt>

*activityInstance* \[in\]
</dt> <dd>

The activity instance.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity instance is the value of element **Activity/ActivityInstance**.

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

 

 





