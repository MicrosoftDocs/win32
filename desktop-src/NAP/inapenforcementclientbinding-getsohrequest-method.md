---
title: INapEnforcementClientBinding GetSoHRequest method (NapEnforcementClient.h)
description: Is used by the enforcement client to retrieve an SoH-request for a particular connection.
ms.assetid: 6fce6e84-ce03-48f2-957b-a41efe044fc5
keywords:
- GetSoHRequest method NAP
- GetSoHRequest method NAP , INapEnforcementClientBinding interface
- INapEnforcementClientBinding interface NAP , GetSoHRequest method
topic_type:
- apiref
api_name:
- INapEnforcementClientBinding.GetSoHRequest
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientBinding::GetSoHRequest method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientBinding::GetSoHRequest** method is used by the enforcement client to retrieve an SoH-request for a particular connection.

## Syntax


```C++
HRESULT GetSoHRequest(
  [in]  INapEnforcementClientConnection *connection,
  [out] BOOL                            *retriggerHint
);
```



## Parameters

<dl> <dt>

*connection* \[in\]
</dt> <dd>

A COM pointer to an [**INapEnforcementClientConnection**](inapenforcementclientconnection.md) interface. The NapAgent does not hold references to the object associated with this interface after the method completes.

</dd> <dt>

*retriggerHint* \[out\]
</dt> <dd>

A pointer to a **BOOL** that indicates if the connection should be re-triggered. It is **TRUE** if the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) has changed since this function was last called or if [**ProbationTime**](nap-datatypes.md) has expired. Otherwise, **FALSE** is returned.

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

The NapAgent sets the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) on the connection object.

If an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) was outstanding on this connection, then it is discarded, and the SHAs are notified of orphaned **SoHRequests**.

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

 

 





