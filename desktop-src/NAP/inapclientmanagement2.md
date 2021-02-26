---
title: INapClientManagement2 interface (NapManagement.h)
description: Provides methods for NAP client management. | INapClientManagement2 interface (NapManagement.h)
ms.assetid: 3cf29bfe-471a-481a-903d-bf0479c57a08
keywords:
- INapClientManagement2 interface NAP
- INapClientManagement2 interface NAP , described
topic_type:
- apiref
api_name:
- INapClientManagement2
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement2 interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapClientManagement2** interface provides methods for NAP client management.

> [!Note]  
> This interface inherits all the methods of [**INapClientManagement**](inapclientmanagement.md) and should be used instead.

 

## Members

The **INapClientManagement2** interface inherits from [**INapClientManagement**](inapclientmanagement.md). **INapClientManagement2** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapClientManagement2** interface has these methods.



| Method                                                                                                    | Description                                                                                                |
|:----------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**INapClientManagement2::GetSystemIsolationInfoEx**](inapclientmanagement2-getsystemisolationinfoex.md) | Retrieves information about the isolation state and extended isolation state of the Nap client.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>NapManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagent.dll</dt> </dl>        |



## See also

<dl> <dt>

[**INapClientManagement**](inapclientmanagement.md)
</dt> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

 





