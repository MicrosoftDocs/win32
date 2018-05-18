---
title: Activity GetActivityDescription method
description: Returns the activity description of the Activity.
ms.assetid: 'AF8A09B3-256F-4C91-97FD-4415DFF4A4E0'
keywords: ["GetActivityDescription method Access Execution Engine", "GetActivityDescription method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , GetActivityDescription method"]
topic_type:
- apiref
api_name:
- Activity.GetActivityDescription
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::GetActivityDescription method

Returns the activity description of the **Activity**.

## Syntax


```C++
virtual HRESULT GetActivityDescription(
  [out] LPCWSTR *activityDescription
) const = 0;
```



## Parameters

<dl> <dt>

*activityDescription* \[out\]
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

 

 





