---
title: MsftUal\_ServerDevice class
description: This is a class of property qualifiers that provides client access detail by device, for the local server as a whole.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9cbc2a37-c50c-475a-89be-ba4f69aa7541'
ms.prod: 'windows-server-dev'
ms.technology: 'user-access-logging'
ms.tgt_platform: multiple
keywords: ["MsftUal_ServerDevice class User Access Logging", "MsftUal_ServerDevice class User Access Logging , described"]
topic_type:
- apiref
api_name:
- MsftUal_ServerDevice
- MsftUal_ServerDevice.ChassisSerialNumber
- MsftUal_ServerDevice.UUID
- MsftUal_ServerDevice.IPAddress
- MsftUal_ServerDevice.ActivityCount
- MsftUal_ServerDevice.FirstSeen
- MsftUal_ServerDevice.LastSeen
api_location:
- UALProv.dll
api_type:
- DllExport
---

# MsftUal\_ServerDevice class

This is a class of property qualifiers that provides client access detail by device, for the local server as a whole.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_ServerDevice
{
  string   ChassisSerialNumber;
  string   UUID;
  string   IPAddress;
  uint32   ActivityCount;
  datetime FirstSeen;
  datetime LastSeen;
};
```

## Members

The **MsftUal\_ServerDevice** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_ServerDevice** class has these properties.

<dl> <dt>

**ActivityCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The incremental counter of client device accesses for a particular client device.

</dd> <dt>

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

The date and time when a client IP address is first seen by a server.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The IP address of the client that accompanies the UAL payload from installed roles and products.

</dd> <dt>

**LastSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a client IP address is last seen by a server.

</dd> <dt>

**UUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SMBIOS reported universally unique identifier for this server unit.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





