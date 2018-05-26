---
title: Activity SetAttributeParentID method
description: Sets the parent ID of the Activity.
ms.assetid: E304EE50-2FBE-4617-8E45-808CD0E9F168
keywords:
- SetAttributeParentID method Access Execution Engine
- SetAttributeParentID method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetAttributeParentID method
topic_type:
- apiref
api_name:
- Activity.SetAttributeParentID
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

# Activity::SetAttributeParentID method

Sets the parent ID of the **Activity**.

## Syntax


```C++
virtual HRESULT SetAttributeParentID(
  [in] LPCWSTR attributeParentID
) = 0;
```



## Parameters

<dl> <dt>

*attributeParentID* \[in\]
</dt> <dd>

The parent ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The parent ID is the value of attribute **parentID** of element **Activity**.

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

 

 





