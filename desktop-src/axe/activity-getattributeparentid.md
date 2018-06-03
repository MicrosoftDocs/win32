---
title: Activity GetAttributeParentID method
description: Returns the parent ID of the Activity.
ms.assetid: 1845EFB8-6FBB-4FED-93EE-314B078C9490
keywords:
- GetAttributeParentID method Access Execution Engine
- GetAttributeParentID method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetAttributeParentID method
topic_type:
- apiref
api_name:
- Activity.GetAttributeParentID
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

# Activity::GetAttributeParentID method

Returns the parent ID of the **Activity**.

## Syntax


```C++
virtual HRESULT GetAttributeParentID(
  [out] LPCWSTR *attributeParentID
) const = 0;
```



## Parameters

<dl> <dt>

*attributeParentID* \[out\]
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

 

 





