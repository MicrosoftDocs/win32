---
title: GetSecondaryConnectionString method of the Win32_RDMSDeploymentSettings class
description: Retrieves the deployment-level database secondary connection string, which may be used to support password expiration.
ms.assetid: 0de02752-6cbf-4c21-b752-a57ed58aeef1
ms.tgt_platform: multiple
keywords:
- GetSecondaryConnectionString method Remote Desktop Services
- GetSecondaryConnectionString method Remote Desktop Services , Win32_RDMSDeploymentSettings class
- Win32_RDMSDeploymentSettings class Remote Desktop Services , GetSecondaryConnectionString method
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings.GetSecondaryConnectionString
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetSecondaryConnectionString method of the Win32\_RDMSDeploymentSettings class

Retrieves the deployment-level database secondary connection string, which may be used to support password expiration.

## Syntax


```mof
uint32 GetSecondaryConnectionString(
  [out] string SecondaryConnectionString
);
```



## Parameters

<dl> <dt>

*SecondaryConnectionString* \[out\]
</dt> <dd>

The connection string to retrieve

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSDeploymentSettings**](win32-rdmsdeploymentsettings.md)
</dt> </dl>

 

 





