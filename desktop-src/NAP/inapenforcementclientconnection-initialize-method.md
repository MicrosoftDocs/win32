---
title: INapEnforcementClientConnection Initialize method (NapEnforcementClient.h)
description: Initializes the client connection.
ms.assetid: da72bfc3-9551-4fb0-b9a5-2931c14f618f
keywords:
- Initialize method NAP
- Initialize method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , Initialize method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.Initialize
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection::Initialize method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::Initialize** method initializes the client connection.

## Syntax


```C++
HRESULT Initialize(
  [in] EnforcementEntityId id
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

A pointer to an [**EnforementEntityId**](nap-datatypes.md) that identifies the enforcement client requesting the connection. This value is set by the NapAgent during connection creation.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapEnforcementClient.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapEnforcementClient.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagent.dll</dt> </dl>               |



## See also

<dl> <dt>

[**INapEnforcementClientConnection**](inapenforcementclientconnection.md)
</dt> </dl>

 

 





