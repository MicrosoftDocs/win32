---
description: The CIM\_RemoteFileSystem class represents a remote file system that is accessed by way of a network-related service. In this case, the file store is hosted by a computer, which acts as a file server.
ms.assetid: 932970a8-0ab3-45d8-912d-c4ba7cf433b5
ms.tgt_platform: multiple
title: CIM_RemoteFileSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_RemoteFileSystem
- CIM_RemoteFileSystem.AvailableSpace
- CIM_RemoteFileSystem.BlockSize
- CIM_RemoteFileSystem.Caption
- CIM_RemoteFileSystem.CasePreserved
- CIM_RemoteFileSystem.CaseSensitive
- CIM_RemoteFileSystem.CodeSet
- CIM_RemoteFileSystem.CompressionMethod
- CIM_RemoteFileSystem.CreationClassName
- CIM_RemoteFileSystem.CSCreationClassName
- CIM_RemoteFileSystem.CSName
- CIM_RemoteFileSystem.Description
- CIM_RemoteFileSystem.EncryptionMethod
- CIM_RemoteFileSystem.FileSystemSize
- CIM_RemoteFileSystem.InstallDate
- CIM_RemoteFileSystem.MaxFileNameLength
- CIM_RemoteFileSystem.Name
- CIM_RemoteFileSystem.ReadOnly
- CIM_RemoteFileSystem.Root
- CIM_RemoteFileSystem.Status
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_RemoteFileSystem class

The **CIM\_RemoteFileSystem** class represents a remote file system that is accessed by way of a network-related service. In this case, the file store is hosted by a computer, which acts as a file server. For example, the file store for an NFS file system is typically not on a computer system's locally controlled media, nor is it directly accessed through a device driver. Subclasses of **CIM\_RemoteFileSystem** contain client-side configuration information related to the access of the file system.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{75BCF4F9-DB46-11D2-B4C8-80080C7B6371}"), AMENDMENT]
class CIM_RemoteFileSystem : CIM_FileSystem
{
  uint64   AvailableSpace;
  uint64   BlockSize;
  string   Caption;
  boolean  CasePreserved;
  boolean  CaseSensitive;
  uint16   CodeSet[];
  string   CompressionMethod;
  string   CreationClassName;
  string   CSCreationClassName;
  string   CSName;
  string   Description;
  string   EncryptionMethod;
  uint64   FileSystemSize;
  datetime InstallDate;
  uint32   MaxFileNameLength;
  string   Name;
  boolean  ReadOnly;
  string   Root;
  string   Status;
};
```

## Members

The **CIM\_RemoteFileSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RemoteFileSystem** class has these properties.

<dl> <dt>

**AvailableSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Partition\|002.4"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Amount of free space for the file system, in bytes. If unknown, enter 0.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Size, in bytes, of the blocks that form the storage extent. If unknown, or if a block concept is not valid, (for example, for aggregate extents, memory, or logical disks), enter a 1 (one).

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CasePreserved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the case of file names are preserved.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**CaseSensitive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, case-sensitive file names are supported.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**CodeSet**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Character sets or encoding supported by the file system. This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="ASCII"></span><span id="ascii"></span>

**ASCII** (2)


</dt> <dd></dd> <dt>

<span id="Unicode"></span><span id="unicode"></span><span id="UNICODE"></span>

**Unicode** (3)


</dt> <dd></dd> <dt>

<span id="ISO2022"></span><span id="iso2022"></span>

**ISO2022** (4)


</dt> <dd></dd> <dt>

<span id="ISO8859"></span><span id="iso8859"></span>

**ISO8859** (5)


</dt> <dd></dd> <dt>

<span id="Extended_UNIX_Code"></span><span id="extended_unix_code"></span><span id="EXTENDED_UNIX_CODE"></span>

**Extended UNIX Code** (6)


</dt> <dd></dd> <dt>

<span id="UTF-8"></span><span id="utf-8"></span>

**UTF-8** (7)


</dt> <dd></dd> <dt>

<span id="UCS-2"></span><span id="ucs-2"></span>

**UCS-2** (8)


</dt> <dd></dd> </dl>

</dd> <dt>

**CompressionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Partition\|002.7")
</dt> </dl>

Free-form string that indicates the algorithm or tool used to compress the logical file. If the compression scheme is unknown or not described, use "Unknown". If the logical file is compressed, but the compression scheme is unknown or not described, use "Compressed". If the logical file is not compressed, use "Not Compressed".

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**CreationClassName**")
</dt> </dl>

Scoping computer system's creation class name.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**Name**")
</dt> </dl>

Scoping computer system's name.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Partition\|002.8")
</dt> </dl>

Free-form string that identifies the algorithm or tool used to encrypt a logical file. If the encryption scheme is not indulged (for security reasons, for example), use "Unknown". If the file is encrypted, but either its encryption scheme is unknown or not disclosed, use "Encrypted". If the logical file is not encrypted, use "Not Encrypted". This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**FileSystemSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Total size of the file system, in bytes. If unknown, enter 0.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**MaxFileNameLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum length of a file name within the file system. A value of 0 indicates that file name length is unlimited.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ReadOnly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|HOST-RESOURCES-MIB.hrFSAccess")
</dt> </dl>

If **TRUE**, the file system is designated as read-only.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**Root**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|HOST-RESOURCES-MIB.hrFSMountPoint")
</dt> </dl>

Path name or other information that defines the root of the file system.

This property is inherited from [**CIM\_FileSystem**](cim-filesystem.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
</dt> </dl>

Current status of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **CIM\_RemoteFileSystem** class is derived from [**CIM\_FileSystem**](cim-filesystem.md).

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

[**CIM\_FileSystem**](cim-filesystem.md)
</dt> </dl>

 

