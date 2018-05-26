---
title: DAServer class
description: DirectAccess Server Settings.
audience: developer
ms.assetid: a9b283c6-e576-48af-b0df-a98dd38e54a2
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAServer class
- DAServer class, described
topic_type:
- apiref
api_name:
- DAServer
- DAServer.InternetInterface
- DAServer.InternalInterface
- DAServer.SslCertificate
- DAServer.ServerConfiguration
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DAServer class

DirectAccess Server Settings

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAServer : RemoteAccessCore
{
  string                InternetInterface;
  string                InternalInterface;
  uint8                 SslCertificate[];
  DAServerConfiguration ServerConfiguration;
};
```

## Members

The **DAServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAServer** class has these properties.

<dl> <dt>

**InternalInterface**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Intranet facing interface

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**InternetInterface**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Internet facing interface

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**ServerConfiguration**
</dt> <dd> <dl> <dt>

Data type: **DAServerConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAServerConfiguration**](daserverconfiguration.md)")
</dt> </dl>

A [**DAServerConfiguration**](daserverconfiguration.md) embedded instance

</dd> <dt>

**SslCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of IP-HTTPS/SSL certificates

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





