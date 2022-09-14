---
title: INapEnforcementClientBinding NotifyConnectionStateDown method (NapEnforcementClient.h)
description: Is used to inform the NapAgent that a connection to an enforcement client has gone down.
ms.assetid: 504c61c1-c8f9-46b8-87cd-c1f04846f0b3
keywords:
- NotifyConnectionStateDown method NAP
- NotifyConnectionStateDown method NAP , INapEnforcementClientBinding interface
- INapEnforcementClientBinding interface NAP , NotifyConnectionStateDown method
topic_type:
- apiref
api_name:
- INapEnforcementClientBinding.NotifyConnectionStateDown
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientBinding::NotifyConnectionStateDown method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientBinding::NotifyConnectionStateDown** method is used to inform the NapAgent that a connection to an enforcement client has gone down.

## Syntax


```C++
HRESULT NotifyConnectionStateDown(
  [in] INapEnforcementClientConnection *downCxn
);
```



## Parameters

<dl> <dt>

*downCxn* \[in\]
</dt> <dd>

A COM pointer to the [**INapEnforcementClientConnection**](inapenforcementclientconnection.md) interface of the down connection.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                             | Description                                                        |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                   | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>         | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>          | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**NAP\_E\_NOT\_INITIALIZED**</dt> </dl> | The enforcer has not been previously initialized.<br/>       |



 

## Remarks

When any of the connections established by an enforcement client go down, the enforcement client should remove the connection from its active list and inform the NapAgent using this method. As soon as this call returns, the connection object can be released and freed. The NapAgent will not hold references to the connection object.

As a result of this notification, the NapAgent updates its system NAP state as appropriate.

The enforcement client must call the [**INapEnforcementClientBinding::Initialize**](inapenforcementclientbinding-initialize-method.md) method before calling this or any other method of the [**INapEnforcementClientBinding**](inapenforcementclientbinding.md) interface.

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


</dt> <dt>

[**INapEnforcementClientBinding**](inapenforcementclientbinding.md)
</dt> </dl>

 

 





