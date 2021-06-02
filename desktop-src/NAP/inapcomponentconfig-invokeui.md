---
title: INapComponentConfig InvokeUI method (NapCommon.h)
description: Launches a customized user interface for a system health validator (SHV) component.
ms.assetid: da2a5e3e-bc17-4984-bdbe-b72e9e710a9d
keywords:
- InvokeUI method NAP
- InvokeUI method NAP , INapComponentConfig interface
- INapComponentConfig interface NAP , InvokeUI method
topic_type:
- apiref
api_name:
- INapComponentConfig.InvokeUI
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig::InvokeUI method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **InvokeUI** method launches a customized user interface for a system health validator (SHV) component.

## Syntax


```C++
HRESULT InvokeUI(
  [in] HWND hwndParent
) const;
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

A handle to the parent or owner window. A valid window handle must be supplied.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>       | The SHV does not support a customized UI.<br/>               |



 

## Remarks

This method call should block until the SHV user interface exits.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig**](inapcomponentconfig.md)
</dt> <dt>

[**INapComponentConfig::IsUISupported**](inapcomponentconfig-isuisupported.md)
</dt> </dl>

 

 





