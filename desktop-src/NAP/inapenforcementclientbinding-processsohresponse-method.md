---
title: INapEnforcementClientBinding ProcessSoHResponse method (NapEnforcementClient.h)
description: Is used by enforcement clients to process an SoHResponse whenever they receive an SoHResponse data blob from the enforcement server.
ms.assetid: 6ff6d2c5-9ebe-4d8c-aa27-03147e2e1122
keywords:
- ProcessSoHResponse method NAP
- ProcessSoHResponse method NAP , INapEnforcementClientBinding interface
- INapEnforcementClientBinding interface NAP , ProcessSoHResponse method
topic_type:
- apiref
api_name:
- INapEnforcementClientBinding.ProcessSoHResponse
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientBinding::ProcessSoHResponse method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientBinding::ProcessSoHResponse** method is used by enforcement clients to process an SoHResponse whenever they receive an SoHResponse data blob from the enforcement server.

## Syntax


```C++
HRESULT ProcessSoHResponse(
  [in] INapEnforcementClientConnection *connection
);
```



## Parameters

<dl> <dt>

*connection* \[in\]
</dt> <dd>

A COM pointer to the [**INapEnforcementClientConnection**](inapenforcementclientconnection.md) interface of the client connection. The NapAgent does not hold references to the object associated with this interface after this method call completes.

You must use a previously established connection for processing SOHResponse data blobs.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                             | Description                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                   | The operation is successful.<br/>                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | No connections have previously been created on the enforcement client. <br/>                                                                                                                                                                                                                                                 |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>         | Permissions error, access denied.<br/>                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>          | System resource limit, could not perform the operation.<br/>                                                                                                                                                                                                                                                                 |
| <dl> <dt>**NAP\_E\_INVALID\_PACKET**</dt> </dl>  | If this value is returned the enforcement client must drop the packet if the NapAgent returns NAP\_E\_INVALID\_PACKET. In this case, the enforcer must assume that the server it is talking to is not NAP-enabled and remove the connection from the active list (i.e. notify the NapAgent of a connection state down).<br/> |
| <dl> <dt>**NAP\_E\_MISMATCHED\_ID**</dt> </dl>   | If this value is returned it indicates that the correlation id in the SoH-Response packet did not match the outstanding SoH-Response. In this case, the enforcer should drop the packet and wait for another newer SoH-Response packet.<br/> This may be caused by a response to an older request message.<br/>        |
| <dl> <dt>**NAP\_E\_NOT\_INITIALIZED**</dt> </dl> | The enforcer has not been previously initialized.<br/>                                                                                                                                                                                                                                                                       |



 

## Remarks

The NapAgent queries the SoH-Response data blob from the connection object, processes it, and sets the resulting decision (eg. full/restricted access/etc) on the connection object.

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
</dt> <dt>

[**INapEnforcementClientConnection**](inapenforcementclientconnection.md)
</dt> </dl>

 

 





