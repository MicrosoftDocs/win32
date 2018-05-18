---
title: Activity SetActivityTitle method
description: Sets the activity title of the Activity.
ms.assetid: '2E11A3C5-5858-400E-BF3B-D18BA68CB18B'
keywords: ["SetActivityTitle method Access Execution Engine", "SetActivityTitle method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , SetActivityTitle method"]
topic_type:
- apiref
api_name:
- Activity.SetActivityTitle
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::SetActivityTitle method

Sets the activity title of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityTitle(
  [in] LPCWSTR activityTitle
) = 0;
```



## Parameters

<dl> <dt>

*activityTitle* \[in\]
</dt> <dd>

The activity title.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity title is the value of element **Activity/ActivityTitle**.

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

 

 





