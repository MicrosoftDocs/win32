---
title: Activity SetActivityClassDisplayName method
description: Sets the activity class display name of the Activity.
ms.assetid: 'B0E943A6-68E8-4F5C-B1A6-4CB38E74074E'
keywords: ["SetActivityClassDisplayName method Access Execution Engine", "SetActivityClassDisplayName method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , SetActivityClassDisplayName method"]
topic_type:
- apiref
api_name:
- Activity.SetActivityClassDisplayName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::SetActivityClassDisplayName method

Sets the activity class display name of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityClassDisplayName(
  [in] LPCWSTR activityClassDisplayName
) = 0;
```



## Parameters

<dl> <dt>

*activityClassDisplayName* \[in\]
</dt> <dd>

The activity class display name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity class display name is the value of element **Activity/ActivityClassDisplayName**.

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

 

 





