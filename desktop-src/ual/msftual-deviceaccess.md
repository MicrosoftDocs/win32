---
title: MsftUal\_DeviceAccess class
description: This is a class of property qualifiers that provides client device access details for roles and products installed on the local server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b6a15b0a-330a-4469-bb81-45d06c5ab449
ms.prod: windows-server-dev
ms.technology: user-access-logging
ms.tgt_platform: multiple
keywords:
- MsftUal_DeviceAccess class User Access Logging
- MsftUal_DeviceAccess class User Access Logging , described
topic_type:
- apiref
api_name:
- MsftUal_DeviceAccess
- MsftUal_DeviceAccess.ProductName
- MsftUal_DeviceAccess.RoleName
- MsftUal_DeviceAccess.RoleGuid
- MsftUal_DeviceAccess.IPAddress
- MsftUal_DeviceAccess.TenantIdentifier
- MsftUal_DeviceAccess.ActivityCount
- MsftUal_DeviceAccess.FirstSeen
- MsftUal_DeviceAccess.LastSeen
api_location:
- UALProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftUal\_DeviceAccess class

This is a class of property qualifiers that provides client device access details for roles and products installed on the local server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_DeviceAccess
{
  string   ProductName;
  string   RoleName;
  string   RoleGuid;
  string   IPAddress;
  string   TenantIdentifier;
  uint32   ActivityCount;
  datetime FirstSeen;
  datetime LastSeen;
};
```

## Members

The **MsftUal\_DeviceAccess** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_DeviceAccess** class has these properties.

<dl> <dt>

**ActivityCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The incremental counter of device accesses for a particular client device.

</dd> <dt>

**FirstSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a client IP address is first seen by a role or product.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The IP address of a client device that accompanies the UAL payload from installed roles and products.

</dd> <dt>

**LastSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a client IP address is last seen by a role or product.

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
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
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

</dd> <dt>

**TenantIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A unique GUID for a tenant client of an installed role or product which accompanies the UAL data payload, if applicable.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





