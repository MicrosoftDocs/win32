---
title: RemoteAccessCore class
description: Remote Access Core Configuration.
audience: developer
ms.assetid: 93665663-4bad-4a2b-96d2-780f85f122cd
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessCore class
- RemoteAccessCore class, described
topic_type:
- apiref
api_name:
- RemoteAccessCore
- RemoteAccessCore.InternetInterface
- RemoteAccessCore.InternalInterface
- RemoteAccessCore.SslCertificate
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessCore class

Remote Access Core Configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessCore
{
  string InternetInterface;
  string InternalInterface;
  uint8  SslCertificate[];
};
```

## Members

The **RemoteAccessCore** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessCore** class has these properties.

<dl> <dt>

**InternalInterface**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Intranet facing interface

</dd> <dt>

**InternetInterface**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Internet facing interface

</dd> <dt>

**SslCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of IP-HTTPS/SSL certificates

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





