---
title: ErrorWarning SetMessage method
description: Sets the text message of this item.
ms.assetid: '75B741DF-AA45-42E2-BB1C-376D4621C74C'
keywords: ["SetMessage method Access Execution Engine", "SetMessage method Access Execution Engine , ErrorWarning interface", "ErrorWarning interface Access Execution Engine , SetMessage method"]
topic_type:
- apiref
api_name:
- ErrorWarning.SetMessage
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorWarning::SetMessage method

Sets the text message of this item.

## Syntax


```C++
virtual HRESULT SetMessage(
  [in] LPCWSTR message
) = 0;
```



## Parameters

<dl> <dt>

*message* \[in\]
</dt> <dd>

The text message.

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

 

 





