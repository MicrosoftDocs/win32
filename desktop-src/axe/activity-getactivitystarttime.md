---
title: Activity GetActivityStartTime method
description: Returns the activity start time of the Activity.
ms.assetid: '1427EAE5-4E6E-41C1-8771-2FBA1E91BC18'
keywords: ["GetActivityStartTime method Access Execution Engine", "GetActivityStartTime method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , GetActivityStartTime method"]
topic_type:
- apiref
api_name:
- Activity.GetActivityStartTime
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::GetActivityStartTime method

Returns the activity start time of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityStartTime(
  [out] DOUBLE *activityStartTime
) const = 0;
```



## Parameters

<dl> <dt>

*activityStartTime* \[out\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





