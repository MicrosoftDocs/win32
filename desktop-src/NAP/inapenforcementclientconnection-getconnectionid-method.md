---
title: INapEnforcementClientConnection GetConnectionId method (NapEnforcementClient.h)
description: Is used to get the unique connection ID of the client.
ms.assetid: bf744aa6-5786-473f-9508-db4ee0c75578
keywords:
- GetConnectionId method NAP
- GetConnectionId method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , GetConnectionId method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.GetConnectionId
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection::GetConnectionId method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::GetConnectionId** method is used to get the unique connection ID of the client.

## Syntax


```C++
HRESULT GetConnectionId(
  [out] ConnectionId **connectionId
);
```



## Parameters

<dl> <dt>

*connectionId* \[out\]
</dt> <dd>

A pointer to a pointer to a [**ConnectionId**](nap-datatypes.md) that uniquely identifies this connection.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

The connection ID is primarily used for logging purposes.

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

 

 





