---
title: Activity SetActivityEndThread method
description: Sets the activity end thread of the Activity.
ms.assetid: '43C62E26-F22B-421D-AA4B-01175D961D96'
keywords: ["SetActivityEndThread method Access Execution Engine", "SetActivityEndThread method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , SetActivityEndThread method"]
topic_type:
- apiref
api_name:
- Activity.SetActivityEndThread
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::SetActivityEndThread method

Sets the activity end thread of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityEndThread(
  [in] INT activityEndThread
) = 0;
```



## Parameters

<dl> <dt>

*activityEndThread* \[in\]
</dt> <dd>

The activity end thread.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity end thread is the value of element **Activity/ActivityEndThread**.

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

 

 





