---
title: Activity GetActivityTitle method
description: Returns the activity title of the Activity.
ms.assetid: '3E8EA8A8-4B9B-4297-A964-D9877CCD7A1D'
keywords: ["GetActivityTitle method Access Execution Engine", "GetActivityTitle method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , GetActivityTitle method"]
topic_type:
- apiref
api_name:
- Activity.GetActivityTitle
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::GetActivityTitle method

Returns the activity title of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityTitle(
  [out] LPCWSTR *activityTitle
) const = 0;
```



## Parameters

<dl> <dt>

*activityTitle* \[out\]
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

 

 





