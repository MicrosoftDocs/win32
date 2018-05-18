---
title: Activity SetActivityDescription method
description: Sets the activity description of the Activity.
ms.assetid: '459DCBE3-4E97-4078-B447-75CF26EFA98C'
keywords: ["SetActivityDescription method Access Execution Engine", "SetActivityDescription method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , SetActivityDescription method"]
topic_type:
- apiref
api_name:
- Activity.SetActivityDescription
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::SetActivityDescription method

Sets the activity description of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityDescription(
  [in] LPCWSTR activityDescription
) = 0;
```



## Parameters

<dl> <dt>

*activityDescription* \[in\]
</dt> <dd>

The activity description.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity description is the value of element **Activity/ActivityDescription**.

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

 

 





