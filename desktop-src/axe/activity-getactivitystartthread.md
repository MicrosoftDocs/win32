---
title: Activity GetActivityStartThread method
description: Returns the activity start thread of the Activity.
ms.assetid: 93CB9CDC-5085-4308-9354-9433C9DD29B9
keywords:
- GetActivityStartThread method Access Execution Engine
- GetActivityStartThread method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetActivityStartThread method
topic_type:
- apiref
api_name:
- Activity.GetActivityStartThread
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

# Activity::GetActivityStartThread method

Returns the activity start thread of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityStartThread(
  [out] INT *activityStartThread
) const = 0;
```



## Parameters

<dl> <dt>

*activityStartThread* \[out\]
</dt> <dd>

The activity start thread.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity start thread is the value of element **Activity/ActivityStartThread**.

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

 

 





