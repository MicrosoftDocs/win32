---
title: Activity SetActivityInstanceDisplayName method
description: Sets the activity instance display name of the Activity.
ms.assetid: AD59BDEA-0D18-4630-B0D7-669AD3A61A73
keywords:
- SetActivityInstanceDisplayName method Access Execution Engine
- SetActivityInstanceDisplayName method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetActivityInstanceDisplayName method
topic_type:
- apiref
api_name:
- Activity.SetActivityInstanceDisplayName
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Activity::SetActivityInstanceDisplayName method

Sets the activity instance display name of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityInstanceDisplayName(
  [in] LPCWSTR activityInstanceDisplayName
) = 0;
```



## Parameters

<dl> <dt>

*activityInstanceDisplayName* \[in\]
</dt> <dd>

The activity instance display name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity instance display name is the value of element **Activity/ActivityInstanceDisplayName**.

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

 

 





