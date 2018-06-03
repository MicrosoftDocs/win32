---
Description: The Win32\_Trustee abstract WMI class specifies a trustee that can be a name or a security identifier (SID) byte array.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e5394068-f05b-44dc-9089-ff7ffaa72348
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_Trustee class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_Trustee class

The **Win32\_Trustee** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) specifies a trustee that can be a name or a security identifier (SID) byte array.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, UUID("{8502C589-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_Trustee : __Trustee
{
  uint64 TIME_CREATED;
  string Domain;
  string Name;
  uint8  SID[];
  uint32 SidLength;
  string SIDString;
};
```

## Members

The **Win32\_Trustee** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_Trustee** class has these properties.

<dl> <dt>

**Domain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Domain), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Domain to which a trustee belongs.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Name), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

A trustee can be a user account, group account, or logon session.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (SID), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

SID that uniquely identifies a user or group.

</dd> <dt>

**SidLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (SidLength), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Length of a SID in bytes.

</dd> <dt>

**SIDString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (SidString), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

SID of a trustee in string format. The format for a string value is the following:

1.  The "S" character identifies the series of digits as a SID.
2.  The revision level.
3.  Identifier authority value.
4.  One or more subauthority values.

Example: "S-1-1-0"

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in the [CIM\_DATETIME](https://msdn.microsoft.com/library/aa387237) format when the security descriptor was created.

This property is inherited from [**\_\_Trustee**](https://msdn.microsoft.com/library/aa394687).

</dd> </dl>

## Remarks

The **Win32\_Trustee** class is derived from the [**Win32\_MethodParameterClass**](https://msdn.microsoft.com/library/aa394200). For more information about how to provide SID data to an instance of this class, see [Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_Trustee**](https://msdn.microsoft.com/library/aa394687)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[**Win32\_SecurityDescriptor**](win32-securitydescriptor.md)
</dt> <dt>

[Maintaining WMI Security](https://msdn.microsoft.com/library/aa392291)
</dt> </dl>

 

 




