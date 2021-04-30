---
title: INapServerCallback interface (NapSystemHealthValidator.h)
description: SHVs use to signal asynchronous request completion.
ms.assetid: 0138767a-9553-4de0-87da-97dd92906406
keywords:
- INapServerCallback interface NAP
- INapServerCallback interface NAP , described
topic_type:
- apiref
api_name:
- INapServerCallback
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerCallback interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerCallback** provides a method that SHVs use to signal asynchronous request completion.

## Members

The **INapServerCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapServerCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapServerCallback** interface has these methods.



| Method                                                                         | Description                                                        |
|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------|
| [**INapServerCallback::OnComplete**](inapservercallback-oncomplete-method.md) | Used by SHVs to signal asynchronous request completion.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qshvhost.dll</dt> </dl>                 |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

