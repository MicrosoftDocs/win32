---
title: INapEnforcementClientConnection2 GetInstalledShvs method (NapEnforcementClient.h)
description: Used by the NAP Agent to query the installed System Health Validators (SHVs) on the client.
ms.assetid: b2e3ab29-90bf-4117-bc2e-2ff2827ee15c
keywords:
- GetInstalledShvs method NAP
- GetInstalledShvs method NAP , INapEnforcementClientConnection2 interface
- INapEnforcementClientConnection2 interface NAP , GetInstalledShvs method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection2.GetInstalledShvs
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection2::GetInstalledShvs method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetInstalledShvs** method is used by the NAP Agent to query the installed System Health Validators (SHVs) on the client.

## Syntax


```C++
HRESULT GetInstalledShvs(
  [out] SystemHealthEntityCount *count,
  [out] SystemHealthEntityId    **ids
) const;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

A pointer to a [SystemHealthEntityCount](nap-datatypes.md) value that specifies the number of installed SHVs in *ids*.

</dd> <dt>

*ids* \[out\]
</dt> <dd>

A pointer to an array of [SystemHealthEntityId](nap-datatypes.md) values that contain the installed SHV IDs.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                   | Description                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>         | Operation succeeded.<br/>                          |
| <dl> <dt>**E\_INVALIDARG** </dt> </dl> | An invalid argument was passed to the method.<br/> |



 

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

 

 





