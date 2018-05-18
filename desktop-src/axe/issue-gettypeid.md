---
title: Issue GetTypeID method
description: Returns the type ID of the Issue.
ms.assetid: '8D478EF1-8FDA-4A9F-9FB9-75DBEB87E91A'
keywords: ["GetTypeID method Access Execution Engine", "GetTypeID method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , GetTypeID method"]
topic_type:
- apiref
api_name:
- Issue.GetTypeID
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::GetTypeID method

Returns the type ID of the **Issue**.

## Syntax


```C++
virtual HRESULT GetTypeID(
  [out] LPCWSTR *typeID
) const = 0;
```



## Parameters

<dl> <dt>

*typeID* \[out\]
</dt> <dd>

The type ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The type ID is the value of element **Issue/TypeID**.

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

 

 





