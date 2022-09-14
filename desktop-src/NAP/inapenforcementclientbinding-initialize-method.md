---
title: INapEnforcementClientBinding Initialize method (NapEnforcementClient.h)
description: Starts up the NapAgent service automatically.
ms.assetid: 6b51043d-a8e7-41e4-9da9-e7f18f9bd068
keywords:
- Initialize method NAP
- Initialize method NAP , INapEnforcementClientBinding interface
- INapEnforcementClientBinding interface NAP , Initialize method
topic_type:
- apiref
api_name:
- INapEnforcementClientBinding.Initialize
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientBinding::Initialize method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientBinding::Initialize** method starts up the NapAgent service automatically.

## Syntax


```C++
HRESULT Initialize(
  [in] EnforcementEntityId           id,
  [in] INapEnforcementClientCallback *callback
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

An [**EnforcementEntityId**](nap-datatypes.md) that identifies the enforcement client and its version.

</dd> <dt>

*callback* \[in\]
</dt> <dd>

A COM pointer to an [**INapEnforcementClientCallback**](inapenforcementclientcallback.md) interface used by the NapAgent to callback the enforcement clients with notify/process. The NapAgent holds a reference to the object associated with this interface until [**INapEnforcementClientBinding::Uninitialize**](inapenforcementclientbinding-uninitialize-method.md) is called.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                                         | Description                                                                              |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                               | The operation is successful.<br/>                                                  |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>                     | Permissions error, access denied.<br/>                                             |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>                      | System resource limit, could not perform the operation.<br/>                       |
| <dl> <dt>**HRESULT(ERROR\_ALREADY\_INITIALIZED)**</dt> </dl> | If the enforcer has initialized previously, then this error code is returned.<br/> |
| <dl> <dt>**NAP\_E\_NOT\_REGISTERED**</dt> </dl>              | If the enforcer has not registered earlier, this error code is returned.<br/>      |



 

## Remarks

The enforcement client must call the **INapEnforcementClientBinding::Initialize** method before calling any other method of the [**INapEnforcementClientBinding**](inapenforcementclientbinding.md) interface.

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

[**INapEnforcementClientBinding::Uninitialize**](inapenforcementclientbinding-uninitialize-method.md)
</dt> </dl>

 

 





