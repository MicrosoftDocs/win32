---
title: RemoteAccessS2SConfiguration class
description: Retrieves and Updates a Remote Access site-to-site (S2S) interface configuration.
audience: developer
ms.assetid: '9d7a22a6-b489-4166-bf67-50da6fd2c043'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessS2SConfiguration class", "RemoteAccessS2SConfiguration class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessS2SConfiguration
- RemoteAccessS2SConfiguration.S2SInterfaceConfiguration
- RemoteAccessS2SConfiguration.Ipv4TransportInfo
- RemoteAccessS2SConfiguration.Ipv6TransportInfo
- RemoteAccessS2SConfiguration.SharedSecret
- RemoteAccessS2SConfiguration.Password
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessS2SConfiguration class

Retrieves and Updates a Remote Access site-to-site (S2S) interface configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessS2SConfiguration
{
  object S2SInterfaceConfiguration;
  uint8  Ipv4TransportInfo[];
  uint8  Ipv6TransportInfo[];
  string SharedSecret;
  string Password;
};
```

## Members

The **RemoteAccessS2SConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessS2SConfiguration** class has these properties.

<dl> <dt>

**Ipv4TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv4 transport information

</dd> <dt>

**Ipv6TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv6 transport information

</dd> <dt>

**Password**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The password of the S2S interface

</dd> <dt>

**S2SInterfaceConfiguration**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

The configuration of an S2S interface as an embedded object

</dd> <dt>

**SharedSecret**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The shared secret of the S2S interface

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





