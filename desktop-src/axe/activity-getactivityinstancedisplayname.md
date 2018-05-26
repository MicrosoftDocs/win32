---
title: Activity GetActivityInstanceDisplayName method
description: Returns the activity instance display name of the Activity.
ms.assetid: 0E6BF330-478D-4A2D-B413-14ABB94E281C
keywords:
- GetActivityInstanceDisplayName method Access Execution Engine
- GetActivityInstanceDisplayName method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetActivityInstanceDisplayName method
topic_type:
- apiref
api_name:
- Activity.GetActivityInstanceDisplayName
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

# Activity::GetActivityInstanceDisplayName method

Returns the activity instance display name of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityInstanceDisplayName(
  [out] LPCWSTR *activityInstanceDisplayName
) const = 0;
```



## Parameters

<dl> <dt>

*activityInstanceDisplayName* \[out\]
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

 

 





