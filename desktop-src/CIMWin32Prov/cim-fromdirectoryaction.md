---
description: The CIM\_FromDirectoryAction association identifies the source directory for the file action.
ms.assetid: 25d06dad-ae39-4cfc-9331-4be7ef02d87c
ms.tgt_platform: multiple
title: CIM_FromDirectoryAction class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_FromDirectoryAction
- CIM_FromDirectoryAction.FileName
- CIM_FromDirectoryAction.SourceDirectory
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_FromDirectoryAction class

The **CIM\_FromDirectoryAction** association identifies the source directory for the file action. When this association is used, the assumption is that the source directory was created by a previous action. This association cannot exist with a [**CIM\_FromDirectorySpecification**](cim-fromdirectoryspecification.md) association; a file action can only involve a single source directory.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{55D5B446-DB2A-11d2-85FC-0000F8102E5F}"), Association, AMENDMENT]
class CIM_FromDirectoryAction
{
  CIM_FileAction      REF FileName;
  CIM_DirectoryAction REF SourceDirectory;
};
```

## Members

The **CIM\_FromDirectoryAction** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_FromDirectoryAction** class has these properties.

<dl> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **CIM\_FileAction**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0)
</dt> </dl>

Reference to the file name.

</dd> <dt>

**SourceDirectory**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DirectoryAction**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0)
</dt> </dl>

Reference to the source directory.

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



 

