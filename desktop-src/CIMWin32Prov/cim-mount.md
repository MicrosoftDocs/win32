---
description: The CIM\_Mount class represents an association between a file system and a directory to which it is attached.
ms.assetid: abf1833b-9b39-45c0-8400-2be2bf3a1c3c
ms.tgt_platform: multiple
title: CIM_Mount class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Mount
- CIM_Mount.Dependent
- CIM_Mount.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_Mount class

The **CIM\_Mount** class represents an association between a file system and a directory to which it is attached.

The semantics of this relationship require that the mounted directory be contained by a file system (via the file storage association) that is different from the file system referenced as the dependent. The directory's containing file system can be local or remote. For example, a local file system on a Solaris computer system can mount a directory from the file system accessed via the computer's CDROM drive (that is, another local file system). On the other hand, in a "remote" case, the directory is first exported by its file system, which is hosted on another computer system acting, for example, as a file server. To distinguish the two mounts, a [**CIM\_Export**](cim-export.md) association should always be defined for the remotely accessed/mounted directories.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{75BCF4F6-DB46-11D2-B4C8-80080C7B6371}"), AMENDMENT]
class CIM_Mount : CIM_Dependency
{
  CIM_NFS       REF Dependent;
  CIM_Directory REF Antecedent;
};
```

## Members

The **CIM\_Mount** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Mount** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Directory**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_Directory**](cim-directory.md) describing the directory mounted.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NFS**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_NFS**](cim-nfs.md) describing the FileSystem the Directory is mounted on.

</dd> </dl>

## Remarks

**CIM\_Mount** is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

