---
title: Activity SetActivityClass method
description: Sets the activity class of the Activity.
ms.assetid: 09D6668B-8591-4433-B677-AEDBC8E9FA72
keywords:
- SetActivityClass method Access Execution Engine
- SetActivityClass method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetActivityClass method
topic_type:
- apiref
api_name:
- Activity.SetActivityClass
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

# Activity::SetActivityClass method

Sets the activity class of the **Activity**.

## Syntax


```C++
virtual HRESULT SetActivityClass(
  [in] LPCWSTR activityClass
) = 0;
```



## Parameters

<dl> <dt>

*activityClass* \[in\]
</dt> <dd>

The activity class.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity class is the value of element **Activity/ActivityClass**.

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

 

 





