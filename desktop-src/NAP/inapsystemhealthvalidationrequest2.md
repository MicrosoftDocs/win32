---
title: INapSystemHealthValidationRequest2 interface (NapSystemHealthValidator.h)
description: Provides methods that are used to support system health validators which are defined by the application developer.
ms.assetid: 12094203-bb6c-4028-9baf-a2a9b124ce6d
keywords:
- INapSystemHealthValidationRequest2 interface NAP
- INapSystemHealthValidationRequest2 interface NAP , described
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest2
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest2 interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest2** interface provides methods that are used to support system health validators which are defined by the application developer.

> [!Note]  
> This interface inherits all the methods of [**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md) and should be used instead.

 

## Members

The **INapSystemHealthValidationRequest2** interface inherits from [**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md). **INapSystemHealthValidationRequest2** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSystemHealthValidationRequest2** interface has these methods.



| Method                                                                                                    | Description                                                        |
|:----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|
| [**INapSystemHealthValidationRequest2::GetConfigId**](inapsystemhealthvalidationrequest2-getconfigid.md) | Retrieves the configuration id in a validation request.<br/> |



 

## Remarks

If an SHV doesn t support [**INapComponentConfig3**](inapcomponentconfig3.md), this interface doesn t apply.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qshvhost.dll</dt> </dl>                 |



## See also

<dl> <dt>

[**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md)
</dt> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

 





