---
title: MsftUal\_Dns class
description: This is a class of property qualifiers that provides client host and device data for the DNS role on the local server, if applicable.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c1469f7-0a94-491c-b5d0-1fe4fcf84760
ms.prod: windows-server-dev
ms.technology: user-access-logging
ms.tgt_platform: multiple
keywords:
- MsftUal_Dns class User Access Logging
- MsftUal_Dns class User Access Logging , described
topic_type:
- apiref
api_name:
- MsftUal_Dns
- MsftUal_Dns.ProductName
- MsftUal_Dns.RoleName
- MsftUal_Dns.RoleGuid
- MsftUal_Dns.IPAddress
- MsftUal_Dns.HostName
- MsftUal_Dns.LastSeen
api_location:
- UALProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftUal\_Dns class

This is a class of property qualifiers that provides client host and device data for the DNS role on the local server, if applicable.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_Dns
{
  string   ProductName;
  string   RoleName;
  string   RoleGuid;
  string   IPAddress;
  string   HostName;
  datetime LastSeen;
};
```

## Members

The **MsftUal\_Dns** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_Dns** class has these properties.

<dl> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The host name of the client. This is associated with IPAddress.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The IP address of a DNS client record. This is associated with hostname.

</dd> <dt>

**LastSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a DNS client record was last seen in DNS.

</dd> <dt>

**ProductName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the software parent product, or product line, that is providing User Access Logging data. This is also associated with a RoleName, and a RoleGuid.

</dd> <dt>

**RoleGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The UAL assigned, or registered, GUID representing the server role, or installed product. When a role or product reports its UAL data, this GUID accompanies the payload.

</dd> <dt>

**RoleName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the role, component, or sub-product that is providing User Access Logging data. This is also associated with a ProductName, and a RoleGuid.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





