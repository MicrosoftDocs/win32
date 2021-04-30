---
title: GetClientAccessName method of the Win32_RDMSEnvironment class
description: Retrieves the Domain Name System (DNS) resource record (RR) name of the Remote Desktop Management Services (RDMS) environment.
ms.assetid: 16f9d00d-a398-4a73-a641-ac552ba6a9d3
ms.tgt_platform: multiple
keywords:
- GetClientAccessName method Remote Desktop Services
- GetClientAccessName method Remote Desktop Services , Win32_RDMSEnvironment class
- Win32_RDMSEnvironment class Remote Desktop Services , GetClientAccessName method
topic_type:
- apiref
api_name:
- Win32_RDMSEnvironment.GetClientAccessName
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetClientAccessName method of the Win32\_RDMSEnvironment class

Retrieves the Domain Name System (DNS) resource record (RR) name of the Remote Desktop Management Services (RDMS) environment.

## Syntax


```mof
uint32 GetClientAccessName(
  [out] string ClientAccessName
);
```



## Parameters

<dl> <dt>

*ClientAccessName* \[out\]
</dt> <dd>

Receives the retrieved RR name.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSEnvironment**](win32-rdmsenvironment.md)
</dt> </dl>

 

 





