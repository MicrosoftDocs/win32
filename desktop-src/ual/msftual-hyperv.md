---
title: MsftUal\_HyperV class
description: This is a class of property qualifiers that provides virtual machine details for the Hyper-V role on the local server, if applicable.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7eb9720d-54c1-4839-8f51-bc6848fc837d
ms.prod: windows-server-dev
ms.technology: user-access-logging
ms.tgt_platform: multiple
keywords:
- MsftUal_HyperV class User Access Logging
- MsftUal_HyperV class User Access Logging , described
topic_type:
- apiref
api_name:
- MsftUal_HyperV
- MsftUal_HyperV.ProductName
- MsftUal_HyperV.RoleName
- MsftUal_HyperV.RoleGuid
- MsftUal_HyperV.UUID
- MsftUal_HyperV.ChassisSerialNumber
- MsftUal_HyperV.FirstSeen
- MsftUal_HyperV.LastSeen
api_location:
- UALProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MsftUal\_HyperV class

This is a class of property qualifiers that provides virtual machine details for the Hyper-V role on the local server, if applicable.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_HyperV
{
  string   ProductName;
  string   RoleName;
  string   RoleGuid;
  string   UUID;
  string   ChassisSerialNumber;
  datetime FirstSeen;
  datetime LastSeen;
};
```

## Members

The **MsftUal\_HyperV** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_HyperV** class has these properties.

<dl> <dt>

**ChassisSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unit identification for the local server.

</dd> <dt>

**FirstSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a VM is first seen.

</dd> <dt>

**LastSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a VM is last seen.

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

</dd> <dt>

**UUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The hypervisor assigned GUID for identifying a virtual machine.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





