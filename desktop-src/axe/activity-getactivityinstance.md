---
title: Activity GetActivityInstance method
description: Returns the activity instance of the Activity.
ms.assetid: A460C111-74B9-41FC-BE4B-28D41FC97C93
keywords:
- GetActivityInstance method Access Execution Engine
- GetActivityInstance method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetActivityInstance method
topic_type:
- apiref
api_name:
- Activity.GetActivityInstance
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

# Activity::GetActivityInstance method

Returns the activity instance of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityInstance(
  [out] LPCWSTR *activityInstance
) const = 0;
```



## Parameters

<dl> <dt>

*activityInstance* \[out\]
</dt> <dd>

The activity instance.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The activity instance is the value of element **Activity/ActivityInstance**.

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

 

 





