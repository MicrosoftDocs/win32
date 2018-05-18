---
title: DirectAccessConfiguration class
description: Remote Access DirectAccess Configuration.
audience: developer
ms.assetid: '21ba030c-bd5c-47c6-a856-cfa8e507a024'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DirectAccessConfiguration class", "DirectAccessConfiguration class, described"]
topic_type:
- apiref
api_name:
- DirectAccessConfiguration
- DirectAccessConfiguration.AppServerPolicy
- DirectAccessConfiguration.ClientPolicy
- DirectAccessConfiguration.ServerConfiguration
- DirectAccessConfiguration.NetworkLocationServerPolicy
- DirectAccessConfiguration.ClientDnsConfiguration
- DirectAccessConfiguration.MgmtServer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DirectAccessConfiguration class

Remote Access DirectAccess Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DirectAccessConfiguration
{
  DAAppServer              AppServerPolicy;
  DAClient                 ClientPolicy;
  DAServerConfiguration    ServerConfiguration;
  DANetworkLocationServer  NetworkLocationServerPolicy;
  DAClientDnsConfiguration ClientDnsConfiguration;
  string                   MgmtServer[];
};
```

## Members

The **DirectAccessConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **DirectAccessConfiguration** class has these properties.

<dl> <dt>

**AppServerPolicy**
</dt> <dd> <dl> <dt>

Data type: **DAAppServer**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAAppServer**](daappserver.md)")
</dt> </dl>

DirectAccess App Server Policy as a [**DAAppServer**](daappserver.md) embedded instance

</dd> <dt>

**ClientDnsConfiguration**
</dt> <dd> <dl> <dt>

Data type: **DAClientDnsConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAClientDnsConfiguration**](daclientdnsconfiguration.md)")
</dt> </dl>

Client DNS configuration as a [**DAClientDnsConfiguration**](daclientdnsconfiguration.md) embedded instance

</dd> <dt>

**ClientPolicy**
</dt> <dd> <dl> <dt>

Data type: **DAClient**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAClient**](daclient.md)")
</dt> </dl>

DirectAccess client policy as a [**DAClient**](daclient.md) embedded instance

</dd> <dt>

**MgmtServer**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of management servers

</dd> <dt>

**NetworkLocationServerPolicy**
</dt> <dd> <dl> <dt>

Data type: **DANetworkLocationServer**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DANetworkLocationServer**](danetworklocationserver.md)")
</dt> </dl>

NLS policy as a [**DANetworkLocationServer**](danetworklocationserver.md) embedded instance

</dd> <dt>

**ServerConfiguration**
</dt> <dd> <dl> <dt>

Data type: **DAServerConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAServerConfiguration**](daserverconfiguration.md)")
</dt> </dl>

DirectAccess server configuration as a [**DAServerConfiguration**](daserverconfiguration.md) embedded instance

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





