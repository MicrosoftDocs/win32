---
title: Issue GetAttributeKnown method
description: Returns the value of attribute Known of the Issue.
ms.assetid: '4D69C4D5-B1D9-44DF-A725-8894C9B2F052'
keywords: ["GetAttributeKnown method Access Execution Engine", "GetAttributeKnown method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , GetAttributeKnown method"]
topic_type:
- apiref
api_name:
- Issue.GetAttributeKnown
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::GetAttributeKnown method

Returns the value of attribute **Known** of the **Issue**.

## Syntax


```C++
virtual HRESULT GetAttributeKnown(
  [out] LPCWSTR *attributeKnown
) const = 0;
```



## Parameters

<dl> <dt>

*attributeKnown* \[out\]
</dt> <dd>

The value of attribute **Known**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

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

 

 





