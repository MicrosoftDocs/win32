---
title: Issue SetAttributeParentID method
description: Sets the parent ID of the Issue.
ms.assetid: 'D77991CD-9BEE-4BD4-9F42-3E02F3C1C190'
keywords: ["SetAttributeParentID method Access Execution Engine", "SetAttributeParentID method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , SetAttributeParentID method"]
topic_type:
- apiref
api_name:
- Issue.SetAttributeParentID
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::SetAttributeParentID method

Sets the parent ID of the **Issue**.

## Syntax


```C++
virtual HRESULT SetAttributeParentID(
  [in] LPCWSTR attributeParentID
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

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The parent ID is attribute **parentID** of element **Issue**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





