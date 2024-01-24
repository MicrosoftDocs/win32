---
title: INapEnforcementClientBinding NotifySoHChangeFailure method (NapEnforcementClient.h)
description: Is used by the enforcement client to inform the NapAgent that it could not process a previous INapEnforcementClientCallback NotifySoHChange.
ms.assetid: 2de1626c-ffda-4191-90c4-72d0275965d9
keywords:
- NotifySoHChangeFailure method NAP
- NotifySoHChangeFailure method NAP , INapEnforcementClientBinding interface
- INapEnforcementClientBinding interface NAP , NotifySoHChangeFailure method
topic_type:
- apiref
api_name:
- INapEnforcementClientBinding.NotifySoHChangeFailure
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientBinding::NotifySoHChangeFailure method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientBinding::NotifySoHChangeFailure** method is used by the enforcement client to inform the NapAgent that it could not process a previous [**INapEnforcementClientCallback::NotifySoHChange**](inapenforcementclientcallback-notifysohchange-method.md).

## Syntax


```C++
HRESULT NotifySoHChangeFailure();
```



## Parameters

This method has no parameters.

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                             | Description                                                        |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                   | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>         | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>          | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**NAP\_E\_NOT\_INITIALIZED**</dt> </dl> | The enforcer has not been previously initialized.<br/>       |



 

## Remarks

As a result of this method call the NapAgent retries applying the SoH change at a later time by calling [**INapEnforcementClientCallback::NotifySoHChange**](inapenforcementclientcallback-notifysohchange-method.md) again. Once the enforcement client has called [**INapEnforcementClientBinding::GetSoHRequest**](inapenforcementclientbinding-getsohrequest-method.md), it then must apply the change, i.e. no failures are handled by the NapAgent after this point.

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

[**INapEnforcementClientBinding::GetSoHRequest**](inapenforcementclientbinding-getsohrequest-method.md)
</dt> <dt>

[**INapEnforcementClientCallback::NotifySoHChange**](inapenforcementclientcallback-notifysohchange-method.md)
</dt> </dl>

 

 





