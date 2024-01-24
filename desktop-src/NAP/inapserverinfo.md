---
title: INapServerInfo interface (NapServerManagement.h)
description: Management clients (for example, WMI providers or command-line tools) use to query the status of the NAP server system.
ms.assetid: 3c6d3f76-ea63-4cb2-bac7-e5668e50b7a7
keywords:
- INapServerInfo interface NAP
- INapServerInfo interface NAP , described
topic_type:
- apiref
api_name:
- INapServerInfo
api_location:
- qsvrmgmt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerInfo interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerInfo** provides methods that Management clients (for example, WMI providers or command-line tools) use to query the status of the NAP server system.

## Members

The **INapServerInfo** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapServerInfo** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapServerInfo** interface has these methods.



| Method                                                                                                                   | Description                                                             |
|:-------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**INapServerInfo::GetFailureCategoryMappings**](inapserverinfo-getfailurecategorymappings-method.md)                   | Retrieves the failure category mappings for a specified SHV.<br/> |
| [**INapServerInfo::GetNapServerInfo**](inapserverinfo-getnapserverinfo-method.md)                                       | Retrieves information about the NAP server.<br/>                  |
| [**INapServerInfo::GetRegisteredSystemHealthValidators**](inapserverinfo-getregisteredsystemhealthvalidators-method.md) | Retrieves a list of registered SHVs.<br/>                         |



 

## Remarks

These methods provide only static information about the NAP Server and its components on the system.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>NapServerManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapServerManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qsvrmgmt.dll</dt> </dl>            |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

