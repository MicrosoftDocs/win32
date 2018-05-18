---
title: ErrorWarning GetKind method
description: Gets the kind of item this is.
ms.assetid: '1757FA2A-4794-4FE5-A37E-2A5E8483CD71'
keywords: ["GetKind method Access Execution Engine", "GetKind method Access Execution Engine , ErrorWarning interface", "ErrorWarning interface Access Execution Engine , GetKind method"]
topic_type:
- apiref
api_name:
- ErrorWarning.GetKind
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorWarning::GetKind method

Gets the kind of item this is.

## Syntax


```C++
virtual HRESULT GetKind(
  [out] IssueType *issueType
) const = 0;
```



## Parameters

<dl> <dt>

*issueType* \[out\]
</dt> <dd>

The kind of item.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ErrorWarning**](errorwarning.md)
</dt> </dl>

 

 





