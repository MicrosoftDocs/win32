---
Description: The Win32\_SID&\#8194;WMI class represents an arbitrary security identifier (SID). This property cannot be enumerated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 33453b86-4aec-4c98-a9f8-a10efc981926
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SID class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_SID class

The **Win32\_SID** [WMI class](https://msdn.microsoft.com/library/aa393244) represents an arbitrary security identifier (SID). This property cannot be enumerated.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), UUID("{8502C581-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SID
{
  string AccountName;
  uint8  BinaryRepresentation[];
  string ReferencedDomainName;
  string SID;
  uint32 SidLength;
};
```

## Members

The **Win32\_SID** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SID** class has these properties.

<dl> <dt>

**AccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the account associated with the SID.

</dd> <dt>

**BinaryRepresentation**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

SID in binary format.

</dd> <dt>

**ReferencedDomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Domain of the account associated with the SID.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

SID in string format. The values of the string are as follows (in order).

1. The literal character "S" (identifies the string as a SID).

2. The revision level.

3. Identifier authority value.

4. One or more subauthority values.

</dd> <dt>

**SidLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("bytes")
</dt> </dl>

Length of the SID in bytes.

</dd> </dl>

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

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[**Win32\_SecurityDescriptor**](win32-securitydescriptor.md)
</dt> <dt>

[Maintaining WMI Security](https://msdn.microsoft.com/library/aa392291)
</dt> </dl>

 

 




