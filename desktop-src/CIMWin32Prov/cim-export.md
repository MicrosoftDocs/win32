---
description: The CIM\_Export class represents an association between a local file system and its directories, which indicate that the specified directories are available for mount.
ms.assetid: 4c43ba5a-e003-4985-85b3-68ecf13a4bf5
ms.tgt_platform: multiple
title: CIM_Export class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Export
- CIM_Export.Directory
- CIM_Export.ExportedDirectoryName
- CIM_Export.LocalFS
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_Export class

The **CIM\_Export** class represents an association between a local file system and its directories, which indicate that the specified directories are available for mount. When exporting an entire file system, the directory should reference the topmost directory of the file system.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{75BCF4F8-DB46-11D2-B4C8-80080C7B6371}"), AMENDMENT]
class CIM_Export
{
  CIM_Directory       REF Directory;
  string                  ExportedDirectoryName;
  CIM_LocalFileSystem REF LocalFS;
};
```

## Members

The **CIM\_Export** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Export** class has these properties.

<dl> <dt>

**Directory**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Directory**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the directory exported for network file system (NFS) mount.

</dd> <dt>

**ExportedDirectoryName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name under which the directory is exported.

</dd> <dt>

**LocalFS**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LocalFileSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

Reference to the local file system.

</dd> </dl>

## Remarks

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



 

