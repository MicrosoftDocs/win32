---
title: Activity GetActivityEndTime method
description: Returns the activity end time of the Activity.
ms.assetid: '7F7CEAD2-F3E0-43F8-BB5B-DA23366D9B52'
keywords: ["GetActivityEndTime method Access Execution Engine", "GetActivityEndTime method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , GetActivityEndTime method"]
topic_type:
- apiref
api_name:
- Activity.GetActivityEndTime
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::GetActivityEndTime method

Returns the activity end time of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityEndTime(
  [out] DOUBLE *activityEndTime
) const = 0;
```



## Parameters

<dl> <dt>

*activityEndTime* \[out\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





