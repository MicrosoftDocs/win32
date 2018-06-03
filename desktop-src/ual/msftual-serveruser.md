---
title: MsftUal\_ServerUser class
description: This is a class of property qualifiers that provides client access detail by user, for the local server as a whole.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d553803d-3436-4fd2-9299-bb7d7215c14c
ms.prod: windows-server-dev
ms.technology: user-access-logging
ms.tgt_platform: multiple
keywords:
- MsftUal_ServerUser class User Access Logging
- MsftUal_ServerUser class User Access Logging , described
topic_type:
- apiref
api_name:
- MsftUal_ServerUser
- MsftUal_ServerUser.ChassisSerialNumber
- MsftUal_ServerUser.UUID
- MsftUal_ServerUser.UserName
- MsftUal_ServerUser.ActivityCount
- MsftUal_ServerUser.FirstSeen
- MsftUal_ServerUser.LastSeen
api_location:
- UALProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftUal\_ServerUser class

This is a class of property qualifiers that provides client access detail by user, for the local server as a whole.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_ServerUser
{
  string   ChassisSerialNumber;
  string   UUID;
  string   UserName;
  uint32   ActivityCount;
  datetime FirstSeen;
  datetime LastSeen;
};
```

## Members

The **MsftUal\_ServerUser** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_ServerUser** class has these properties.

<dl> <dt>

**ActivityCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The incremental counter of client user accesses for a particular client user.

</dd> <dt>

**ChassisSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unit identification for the local server.

</dd> <dt>

**FirstSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a client user name is first seen by a server.

</dd> <dt>

**LastSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a client user name is last seen by a server.

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The client user name that accompanies the UAL payload from installed roles and products, if applicable.

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
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





