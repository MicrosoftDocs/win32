---
title: DAAppServerConnection class
description: DirectAccess application server connection class.
audience: developer
ms.assetid: a6898205-79db-4416-b10a-ead45eb53be5
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAAppServerConnection class
- DAAppServerConnection class, described
topic_type:
- apiref
api_name:
- DAAppServerConnection
- DAAppServerConnection.ConnectionType
- DAAppServerConnection.TrafficProtection
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DAAppServerConnection class

DirectAccess application server connection class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAAppServerConnection
{
  string ConnectionType;
  string TrafficProtection;
};
```

## Members

The **DAAppServerConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAAppServerConnection** class has these properties.

<dl> <dt>

**ConnectionType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of connection to the application servers

The possible values are.

<dt>

<span id="NoE2EAuth"></span><span id="noe2eauth"></span><span id="NOE2EAUTH"></span>

**NoE2EAuth** ("NoE2EAuth")


</dt> <dd></dd> <dt>

<span id="E2EAuthOnlyToAppServer"></span><span id="e2eauthonlytoappserver"></span><span id="E2EAUTHONLYTOAPPSERVER"></span>

**E2EAuthOnlyToAppServer** ("E2EAuthOnlyToAppServer")


</dt> <dd></dd> <dt>

<span id="E2EAuthRequiredToAllServers"></span><span id="e2eauthrequiredtoallservers"></span><span id="E2EAUTHREQUIREDTOALLSERVERS"></span>

**E2EAuthRequiredToAllServers** ("E2EAuthRequiredToAllServers")


</dt> <dd></dd> </dl>

</dd> <dt>

**TrafficProtection**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether Internet Protocol security protection is enabled

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



 

 





