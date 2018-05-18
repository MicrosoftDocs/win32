---
title: Issue GetClassDisplayName method
description: Returns the display name of the class of the Issue.
ms.assetid: '1896F555-18BD-4B7C-A6B4-1D40126AC617'
keywords: ["GetClassDisplayName method Access Execution Engine", "GetClassDisplayName method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , GetClassDisplayName method"]
topic_type:
- apiref
api_name:
- Issue.GetClassDisplayName
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::GetClassDisplayName method

Returns the display name of the class of the **Issue**.

## Syntax


```C++
virtual HRESULT GetClassDisplayName(
  [out] LPCWSTR *classDisplayName
) const = 0;
```



## Parameters

<dl> <dt>

*classDisplayName* \[out\]
</dt> <dd>

The display name of the class.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The display name of the class is the value of element **Issue/Class/DisplayName**.

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

 

 





