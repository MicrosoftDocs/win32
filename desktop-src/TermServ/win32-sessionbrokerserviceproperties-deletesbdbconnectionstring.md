---
title: DeleteSBDbConnectionString method of the Win32_SessionBrokerServiceProperties class
description: Deletes DB connection strings (primary or secondary) from the registry.
ms.assetid: 275dd790-bdc7-46d1-a07d-54ec6fa33e44
ms.tgt_platform: multiple
keywords:
- DeleteSBDbConnectionString method Remote Desktop Services
- DeleteSBDbConnectionString method Remote Desktop Services , Win32_SessionBrokerServiceProperties class
- Win32_SessionBrokerServiceProperties class Remote Desktop Services , DeleteSBDbConnectionString method
topic_type:
- apiref
api_name:
- Win32_SessionBrokerServiceProperties.DeleteSBDbConnectionString
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DeleteSBDbConnectionString method of the Win32\_SessionBrokerServiceProperties class

Deletes DB connection strings (primary or secondary) from the registry.

## Syntax


```mof
uint32 DeleteSBDbConnectionString(
  [in] boolean IsSecondaryConnString
);
```



## Parameters

<dl> <dt>

*IsSecondaryConnString* \[in\]
</dt> <dd>

If **True**, secondary connection string is removed. If **False**, primary connection string is removed.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SessionBrokerServiceProperties**](win32-sessionbrokerserviceproperties.md)
</dt> </dl>

 

 





