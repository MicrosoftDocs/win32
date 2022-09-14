---
title: INapClientManagement RegisterSystemHealthAgent method (NapManagement.h)
description: Registers an SHA with the NAP system.
ms.assetid: 37acfd11-8282-42ba-ae02-9a45c4509b8b
keywords:
- RegisterSystemHealthAgent method NAP
- RegisterSystemHealthAgent method NAP , INapClientManagement interface
- INapClientManagement interface NAP , RegisterSystemHealthAgent method
topic_type:
- apiref
api_name:
- INapClientManagement.RegisterSystemHealthAgent
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement::RegisterSystemHealthAgent method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **RegisterSystemHealthAgent** method registers an SHA with the NAP system.

## Syntax


```C++
HRESULT RegisterSystemHealthAgent(
  [in] const NapComponentRegistrationInfo *agent
);
```



## Parameters

<dl> <dt>

*agent* \[in\]
</dt> <dd>

A pointer to a [**NapComponentRegistrationInfo**](/windows/win32/api/naptypes/ns-naptypes-napcomponentregistrationinfo) structure that contains the registration information for the SHA.

</dd> </dl>

## Return value

The method returns an HRESULT status code including but not limited to one of the following.



| Return code                                                                                            | Description                                                        |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Operation successful.<br/>                                   |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>         | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>          | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**NAP\_E\_CONFLICTING\_ID**</dt> </dl> | An SHA that uses this ID is already registered.<br/>         |



 

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
</dt> </dl>

 

 





