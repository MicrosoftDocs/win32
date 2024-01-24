---
title: INapEnforcementClientConnection SetConnectionId method (NapEnforcementClient.h)
description: Is used to set the unique ID of the connection and must be set by the enforcement client as soon as the connection is created.
ms.assetid: 69d1a891-bc86-4c8a-b614-ebcdaa4a9057
keywords:
- SetConnectionId method NAP
- SetConnectionId method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , SetConnectionId method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.SetConnectionId
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection::SetConnectionId method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::SetConnectionId** method is used to set the unique ID of the connection and must be set by the enforcement client as soon as the connection is created.

## Syntax


```C++
HRESULT SetConnectionId(
  [in] const ConnectionId *connectionId
);
```



## Parameters

<dl> <dt>

*connectionId* \[in\]
</dt> <dd>

A pointer to a [**ConnectionId**](nap-datatypes.md) that uniquely identifies a connection.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

This ConnectionID is primarily used for logging purposes.

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

 

 





