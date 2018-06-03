---
title: DANetworkLocationServer class
description: DirectAccess Network Location Server settings.
audience: developer
ms.assetid: cef31f02-5ad8-420f-9a5a-6ed54caa73f5
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DANetworkLocationServer class
- DANetworkLocationServer class, described
topic_type:
- apiref
api_name:
- DANetworkLocationServer
- DANetworkLocationServer.NlsLocation
- DANetworkLocationServer.Url
- DANetworkLocationServer.Certificate
- DANetworkLocationServer.Reachability
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DANetworkLocationServer class

DirectAccess Network Location Server settings

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DANetworkLocationServer
{
  string  NlsLocation;
  string  Url;
  uint8   Certificate[];
  boolean Reachability;
};
```

## Members

The **DANetworkLocationServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **DANetworkLocationServer** class has these properties.

<dl> <dt>

**Certificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

NLS certificate present on the DA server

</dd> <dt>

**NlsLocation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network Location Server (NLS) location information

The possible values are.

<dt>

<span id="DirectAccessServer"></span><span id="directaccessserver"></span><span id="DIRECTACCESSSERVER"></span>

**DirectAccessServer** ("DirectAccessServer")


</dt> <dd></dd> <dt>

<span id="ExternalServer"></span><span id="externalserver"></span><span id="EXTERNALSERVER"></span>

**ExternalServer** ("ExternalServer")


</dt> <dd></dd> </dl>

</dd> <dt>

**Reachability**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether NLS URL is reachable

</dd> <dt>

**Url**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

NLS URL which is deployed on a Highly Available Server

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





