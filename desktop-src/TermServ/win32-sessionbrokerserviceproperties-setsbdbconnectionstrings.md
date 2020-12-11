---
title: SetSBDbConnectionStrings method of the Win32_SessionBrokerServiceProperties class
description: Saves DB connection strings, both primary and secondary, in the registry.
ms.assetid: a9a20eca-22d9-495c-b976-2952c97be67e
ms.tgt_platform: multiple
keywords:
- SetSBDbConnectionStrings method Remote Desktop Services
- SetSBDbConnectionStrings method Remote Desktop Services , Win32_SessionBrokerServiceProperties class
- Win32_SessionBrokerServiceProperties class Remote Desktop Services , SetSBDbConnectionStrings method
topic_type:
- apiref
api_name:
- Win32_SessionBrokerServiceProperties.SetSBDbConnectionStrings
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSBDbConnectionStrings method of the Win32\_SessionBrokerServiceProperties class

Saves DB connection strings, both primary and secondary, in the registry.

## Syntax


```mof
uint32 SetSBDbConnectionStrings(
  [in] string connStringToCentralDBRdcms,
  [in] string secondaryConnStringToCentralDBRdcms
);
```



## Parameters

<dl> <dt>

*connStringToCentralDBRdcms* \[in\]
</dt> <dd>

The primary connection string.

</dd> <dt>

*secondaryConnStringToCentralDBRdcms* \[in\]
</dt> <dd>

The secondary connection string.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_SessionBrokerServiceProperties**](win32-sessionbrokerserviceproperties.md)
</dt> </dl>

 

 





