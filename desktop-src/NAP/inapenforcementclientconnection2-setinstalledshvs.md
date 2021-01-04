---
title: INapEnforcementClientConnection2 SetInstalledShvs method (NapEnforcementClient.h)
description: Used by the NAP Agent to set the installed System Health Validators (SHVs) on the client.
ms.assetid: 38aa99b9-a15a-414d-91fc-128de8f5a654
keywords:
- SetInstalledShvs method NAP
- SetInstalledShvs method NAP , INapEnforcementClientConnection2 interface
- INapEnforcementClientConnection2 interface NAP , SetInstalledShvs method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection2.SetInstalledShvs
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection2::SetInstalledShvs method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **SetInstalledShvs** method is used by the NAP Agent to set the installed System Health Validators (SHVs) on the client.

## Syntax


```C++
HRESULT SetInstalledShvs(
  [in] SystemHealthEntityCount count,
  [in] SystemHealthEntityId    *ids
);
```



## Parameters

<dl> <dt>

*count* \[in\]
</dt> <dd>

A [SystemHealthEntityCount](nap-datatypes.md) value that specifies the number of SHVs to install in *ids*.

</dd> <dt>

*ids* \[in\]
</dt> <dd>

A pointer to a [SystemHealthEntityId](nap-datatypes.md) value that contains a list of SHV IDs to install.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                  | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>        | The method was successful.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *count* parameter was 0 (zero).<br/> |



 

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

[**INapEnforcementClientConnection2**](inapenforcementclientconnection2.md)
</dt> </dl>

 

 





