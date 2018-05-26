---
title: DAClientDnsConfiguration class
description: Direct Access Client DNS Configuration class.
audience: developer
ms.assetid: 601a82cd-1997-422c-ae9e-11f04c075133
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAClientDnsConfiguration class
- DAClientDnsConfiguration class, described
topic_type:
- apiref
api_name:
- DAClientDnsConfiguration
- DAClientDnsConfiguration.NrptEntry
- DAClientDnsConfiguration.NrptGlobalSettings
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DAClientDnsConfiguration class

Direct Access Client DNS Configuration class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAClientDnsConfiguration
{
  DnsClientNrptRule   NrptEntry[];
  DnsClientNrptGlobal NrptGlobalSettings;
};
```

## Members

The **DAClientDnsConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAClientDnsConfiguration** class has these properties.

<dl> <dt>

**NrptEntry**
</dt> <dd> <dl> <dt>

Data type: **DnsClientNrptRule** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsClientNrptRule**](dnsclientnrptrule.md)")
</dt> </dl>

A [**DnsClientNrptRule**](dnsclientnrptrule.md) embedded instance listing entries in the client GPO

</dd> <dt>

**NrptGlobalSettings**
</dt> <dd> <dl> <dt>

Data type: **DnsClientNrptGlobal**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsClientNrptGlobal**](dnsclientnrptglobal.md)")
</dt> </dl>

A [**DnsClientNrptGlobal**](dnsclientnrptglobal.md) embedded instance of the local name resolution setting

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





