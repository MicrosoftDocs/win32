---
title: MsftUal\_Overview class
description: This is a class of property qualifiers that provides an overview of roles and products installed and registered with the User Access Logging feature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1ff5c589-b71e-4b8a-8c04-5f25cb407ab5'
ms.prod: 'windows-server-dev'
ms.technology: 'user-access-logging'
ms.tgt_platform: multiple
keywords: ["MsftUal_Overview class User Access Logging", "MsftUal_Overview class User Access Logging , described"]
topic_type:
- apiref
api_name:
- MsftUal_Overview
- MsftUal_Overview.ProductName
- MsftUal_Overview.RoleName
- MsftUal_Overview.GUID
- MsftUal_Overview.FirstSeen
- MsftUal_Overview.LastSeen
api_location:
- UALProv.dll
api_type:
- DllExport
---

# MsftUal\_Overview class

This is a class of property qualifiers that provides an overview of roles and products installed and registered with the User Access Logging feature.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_Overview
{
  string   ProductName;
  string   RoleName;
  GUID     GUID;
  datetime FirstSeen;
  datetime LastSeen;
};
```

## Members

The **MsftUal\_Overview** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_Overview** class has these properties.

<dl> <dt>

**FirstSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a role component or product, becomes operational through UAL.

</dd> <dt>

**GUID**
</dt> <dd> <dl> <dt>

Data type: **GUID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The UAL assigned, or registered, GUID representing the server role, or installed product. When a role or product reports its UAL data, this GUID accompanies the payload.

</dd> <dt>

**LastSeen**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when a role component, or product, was last operational through UAL.

</dd> <dt>

**ProductName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the software parent product, or product line, that is providing User Access Logging data. This is also associated with a RoleName, and a RoleGuid.

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
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





