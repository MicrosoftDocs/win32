---
title: Activity SetActivityStartThread method
description: Sets the activity start thread of the Activity.
ms.assetid: 'BD3360CF-A73C-49E0-BC0E-F00460B0A922'
keywords: ["SetActivityStartThread method Access Execution Engine", "SetActivityStartThread method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , SetActivityStartThread method"]
topic_type:
- apiref
api_name:
- Activity.SetActivityStartThread
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::SetActivityStartThread method

Sets the activity start thread of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityStartThread(
  [in] INT activityStartThread
) = 0;
```



## Parameters

<dl> <dt>

*activityStartThread* \[in\]
</dt> <dd>

The activity start thread.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity start thread is the value of element **Activity/ActivityStartThread**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





