---
title: SetBrokerHAMode method of the Win32_SessionBrokerServiceProperties class
description: Migrates data from a local WID database to the new SQL server-based database. It also configures the broker server to use the central SQL server.
ms.assetid: 8f14590d-3042-403c-a1cb-a3b257866284
ms.tgt_platform: multiple
keywords:
- SetBrokerHAMode method Remote Desktop Services
- SetBrokerHAMode method Remote Desktop Services , Win32_SessionBrokerServiceProperties class
- Win32_SessionBrokerServiceProperties class Remote Desktop Services , SetBrokerHAMode method
topic_type:
- apiref
api_name:
- Win32_SessionBrokerServiceProperties.SetBrokerHAMode
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetBrokerHAMode method of the Win32\_SessionBrokerServiceProperties class

Migrates data from a local WID database to the new SQL server-based database. It also configures the broker server to use the central SQL server.

## Syntax


```mof
uint32 SetBrokerHAMode(
  [in] string connStringToCentralDBRdcms,
  [in] string secondaryConnStringToCentralDBRdcms,
  [in] string brokerDnsRRName,
  [in] string activeBrokerName
);
```



## Parameters

<dl> <dt>

*connStringToCentralDBRdcms* \[in\]
</dt> <dd>

Connection string to the central database.

</dd> <dt>

*secondaryConnStringToCentralDBRdcms* \[in\]
</dt> <dd>

Secondary connection string to the central database.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*brokerDnsRRName* \[in\]
</dt> <dd>

Broker DNS name.

</dd> <dt>

*activeBrokerName* \[in\]
</dt> <dd>

Active broker name.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not available before Windows Server 2016.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SessionBrokerServiceProperties**](win32-sessionbrokerserviceproperties.md)
</dt> </dl>

 

 





