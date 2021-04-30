---
title: SetClientAccessName method of the Win32_RDMSEnvironment class
description: Updates the Domain Name System (DNS) resource record (RR) name of an Remote Desktop Management Services (RDMS) environment.
ms.assetid: bbce3fc1-d2c5-4874-bdd0-be27fb5981d1
ms.tgt_platform: multiple
keywords:
- SetClientAccessName method Remote Desktop Services
- SetClientAccessName method Remote Desktop Services , Win32_RDMSEnvironment class
- Win32_RDMSEnvironment class Remote Desktop Services , SetClientAccessName method
topic_type:
- apiref
api_name:
- Win32_RDMSEnvironment.SetClientAccessName
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetClientAccessName method of the Win32\_RDMSEnvironment class

Updates the Domain Name System (DNS) resource record (RR) name of an Remote Desktop Management Services (RDMS) environment.

## Syntax


```mof
uint32 SetClientAccessName(
  [in] string ClientAccessName
);
```



## Parameters

<dl> <dt>

*ClientAccessName* \[in\]
</dt> <dd>

The new RR name.

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

 

 





