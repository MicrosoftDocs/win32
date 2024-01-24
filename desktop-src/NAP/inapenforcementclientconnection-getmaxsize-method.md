---
title: INapEnforcementClientConnection GetMaxSize method (NapEnforcementClient.h)
description: Gets the maximum size of the SoH packet for this client.
ms.assetid: 054bc783-db5d-4801-8984-6b8a131744a2
keywords:
- GetMaxSize method NAP
- GetMaxSize method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , GetMaxSize method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.GetMaxSize
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection::GetMaxSize method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::GetMaxSize** method gets the maximum size of the SoH packet for this client.

## Syntax


```C++
HRESULT GetMaxSize(
  [out] ProtocolMaxSize *maxSize
);
```



## Parameters

<dl> <dt>

*maxSize* \[out\]
</dt> <dd>

A pointer to a [**ProtocolMaxSize**](nap-datatypes.md) that indicates the maximum size, in bytes, of the SoH packet.

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

 

 





