---
title: DAClientSettings class
description: DirectAccess Client Settings class.
audience: developer
ms.assetid: f0873820-5a90-4390-bdc8-001e1cedb785
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAClientSettings class
- DAClientSettings class, described
topic_type:
- apiref
api_name:
- DAClientSettings
- DAClientSettings.ForceTunnel
- DAClientSettings.ForceTunnelingNrptEntry
- DAClientSettings.OnlyRemoteComputers
- DAClientSettings.Downlevel
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DAClientSettings class

DirectAccess Client Settings class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAClientSettings
{
  string            ForceTunnel;
  DnsClientNrptRule ForceTunnelingNrptEntry;
  string            OnlyRemoteComputers;
  string            Downlevel;
};
```

## Members

The **DAClientSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAClientSettings** class has these properties.

<dl> <dt>

**Downlevel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether appropriate policies should be deployed on downlevel Windows 7 clients enabling them to connect to the Windows Server 2012 DA Server.

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**ForceTunnel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Force Tunneling status

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**ForceTunnelingNrptEntry**
</dt> <dd> <dl> <dt>

Data type: **DnsClientNrptRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsClientNrptRule**](dnsclientnrptrule.md)")
</dt> </dl>

Name Resolution Policy Table entry for force tunneling as a [**DnsClientNrptRule**](dnsclientnrptrule.md) embedded instance.

</dd> <dt>

**OnlyRemoteComputers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to deploy DA on laptops and notebooks and not on all computers in the domain

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





