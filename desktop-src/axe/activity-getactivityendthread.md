---
title: Activity GetActivityEndThread method
description: Returns the activity end thread of the Activity.
ms.assetid: '1F3AE636-3997-455C-92E8-85EA01B35FC0'
keywords: ["GetActivityEndThread method Access Execution Engine", "GetActivityEndThread method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , GetActivityEndThread method"]
topic_type:
- apiref
api_name:
- Activity.GetActivityEndThread
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::GetActivityEndThread method

Returns the activity end thread of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityEndThread(
  [out] INT *activityEndThread
) const = 0;
```



## Parameters

<dl> <dt>

*activityEndThread* \[out\]
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

 

 





