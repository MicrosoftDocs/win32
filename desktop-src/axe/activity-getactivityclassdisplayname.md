---
title: Activity GetActivityClassDisplayName method
description: Returns the activity class display name of the Activity.
ms.assetid: C3956606-CEE5-47B4-9312-3DADEFAA088A
keywords:
- GetActivityClassDisplayName method Access Execution Engine
- GetActivityClassDisplayName method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetActivityClassDisplayName method
topic_type:
- apiref
api_name:
- Activity.GetActivityClassDisplayName
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

# Activity::GetActivityClassDisplayName method

Returns the activity class display name of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityClassDisplayName(
  [out] LPCWSTR *activityClassDisplayName
) const = 0;
```



## Parameters

<dl> <dt>

*activityClassDisplayName* \[out\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





