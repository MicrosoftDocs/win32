---
title: INapEnforcementClientConnection SetMaxSize method (NapEnforcementClient.h)
description: Sets the maximum size of the SoH packet for this client.
ms.assetid: 30d3747d-bcf8-41b3-b0af-29f20d48417b
keywords:
- SetMaxSize method NAP
- SetMaxSize method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , SetMaxSize method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.SetMaxSize
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection::SetMaxSize method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::SetMaxSize** method sets the maximum size of the SoH packet for this client.

## Syntax


```C++
HRESULT SetMaxSize(
  [in] ProtocolMaxSize maxSize
);
```



## Parameters

<dl> <dt>

*maxSize* \[in\]
</dt> <dd>

A [**ProtocolMaxSize**](nap-datatypes.md) structure that indicates the maximum size, in bytes, of the SoH packet.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

This value is set by the enforcement client.

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

 

 





