---
title: INapSystemHealthValidator interface
description: Must be implemented by SHV developers to enable the NAP system to communicate with an SHV.
ms.assetid: 0366d919-39b9-4961-9b8b-c4313448391f
keywords:
- INapSystemHealthValidator interface NAP
- INapSystemHealthValidator interface NAP , described
topic_type:
- apiref
api_name:
- INapSystemHealthValidator
api_location:
- NapSystemHealthValidator.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# INapSystemHealthValidator interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidator** provides methods that must be implemented by SHV developers to enable the NAP system to communicate with an SHV.

## Members

The **INapSystemHealthValidator** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **INapSystemHealthValidator** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSystemHealthValidator** interface has these methods.



| Method                                                                                   | Description                                                                                                                               |
|:-----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [**INapSystemHealthValidator::Validate**](inapsystemhealthvalidator-validate-method.md) | The NAP system calls this application defined method to validate the [**SoHRequest**](/windows/desktop/api/NapTypes/ns-naptypes-tagsoh) received from a client. <br/> |



 

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

 





