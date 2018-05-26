---
title: Activity SetActivityStartTime method
description: Sets the activity start time of the Activity.
ms.assetid: DC7CF9A0-7BBA-4C15-962A-57149D589D5E
keywords:
- SetActivityStartTime method Access Execution Engine
- SetActivityStartTime method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetActivityStartTime method
topic_type:
- apiref
api_name:
- Activity.SetActivityStartTime
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

# Activity::SetActivityStartTime method

Sets the activity start time of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityStartTime(
  [in] DOUBLE activityStartTime
) = 0;
```



## Parameters

<dl> <dt>

*activityStartTime* \[in\]
</dt> <dd>

The activity start time.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity start time is the value of element **Activity/ActivityStartTime**.

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

 

 





