---
title: Issue SetAttributeID method
description: Sets the ID of the Issue.
ms.assetid: 91FEEA1D-406D-4DED-A19E-12BE8D586FE1
keywords:
- SetAttributeID method Access Execution Engine
- SetAttributeID method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetAttributeID method
topic_type:
- apiref
api_name:
- Issue.SetAttributeID
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

# Issue::SetAttributeID method

Sets the ID of the **Issue**.

## Syntax


```C++
virtual HRESULT SetAttributeID(
  [in] LPCWSTR attributeID
) = 0;
```



## Parameters

<dl> <dt>

*attributeID* \[in\]
</dt> <dd>

The ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The ID is attribute **ID** of element **Issue**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





