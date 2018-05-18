---
title: ErrorWarning SetKind method
description: Sets the kind of item for this item.
ms.assetid: 'AEFC44CB-D34C-4DC3-A1A0-1271332E0992'
keywords: ["SetKind method Access Execution Engine", "SetKind method Access Execution Engine , ErrorWarning interface", "ErrorWarning interface Access Execution Engine , SetKind method"]
topic_type:
- apiref
api_name:
- ErrorWarning.SetKind
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorWarning::SetKind method

Sets the kind of item for this item.

## Syntax


```C++
virtual HRESULT SetKind(
  [in] IssueType issueType
) = 0;
```



## Parameters

<dl> <dt>

*issueType* \[in\]
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

 

 





