---
title: Activity SetActivityEndTime method
description: Sets the activity end time of the Activity.
ms.assetid: 909BCED1-5969-4758-84A7-E47816091FF3
keywords:
- SetActivityEndTime method Access Execution Engine
- SetActivityEndTime method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetActivityEndTime method
topic_type:
- apiref
api_name:
- Activity.SetActivityEndTime
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

# Activity::SetActivityEndTime method

Sets the activity end time of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityEndTime(
  [in] DOUBLE activityEndTime
) = 0;
```



## Parameters

<dl> <dt>

*activityEndTime* \[in\]
</dt> <dd>

The activity end time.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity end time is the value of element **Activity/ActivityEndTime**.

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

 

 





