---
title: ActivityReference SetAttributeActivityID method
description: Sets the activity ID of the ActivityReference.
ms.assetid: 2A255094-597D-4CB8-93E2-CB23CEABD6B5
keywords:
- SetAttributeActivityID method Access Execution Engine
- SetAttributeActivityID method Access Execution Engine , ActivityReference interface
- ActivityReference interface Access Execution Engine , SetAttributeActivityID method
topic_type:
- apiref
api_name:
- ActivityReference.SetAttributeActivityID
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

# ActivityReference::SetAttributeActivityID method

Sets the activity ID of the **ActivityReference**.

## Syntax


```C++
virtual HRESULT SetAttributeActivityID(
  [in] LPCWSTR attributeActivityID
) = 0;
```



## Parameters

<dl> <dt>

*attributeActivityID* \[in\]
</dt> <dd>

The activity ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

An **ActivityReference** holds data from an **Issue/Impact/RelatedActivities/ActivityReference** element.

The activity ID is the value of attribute **ActivityID** of element **ActivityReference**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ActivityReference**](activityreference-struct.md)
</dt> </dl>

 

 





