---
Description: The CIM\_Directory class represents a file type that logically groups the data files that it contains and provides path information for the grouped files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a9594f53-08f0-4a47-9edc-51686c80c5ea
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_Directory class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_Directory class

The **CIM\_Directory** class represents a file type that logically groups the data files that it contains and provides path information for the grouped files.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{8502C55F-5FBB-11D2-AAC1-006008C78BC7}"), DisplayName("Directories (CIM)"), AMENDMENT]
class CIM_Directory : CIM_LogicalFile
{
  uint32   AccessMask;
  boolean  Archive;
  string   Caption;
  boolean  Compressed;
  string   CompressionMethod;
  string   CreationClassName;
  datetime CreationDate;
  string   CSCreationClassName;
  string   CSName;
  string   Description;
  string   Drive;
  string   EightDotThreeFileName;
  boolean  Encrypted;
  string   EncryptionMethod;
  string   Extension;
  string   FileName;
  uint64   FileSize;
  string   FileType;
  string   FSCreationClassName;
  string   FSName;
  boolean  Hidden;
  datetime InstallDate;
  uint64   InUseCount;
  datetime LastAccessed;
  datetime LastModified;
  string   Name;
  string   Path;
  boolean  Readable;
  string   Status;
  boolean  System;
  boolean  Writeable;
};
```

## Members

The **CIM\_Directory** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_Directory** class has these methods.



| Method                                                                                           | Description                                                                                                                                              |
|:-------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeSecurityPermissions**](changesecuritypermissions-method-in-class-cim-directory.md)     | Changes the security permissions for the logical file specified in the object path. Not implemented by WMI.<br/>                                   |
| [**ChangeSecurityPermissionsEx**](changesecuritypermissionsex-method-in-class-cim-directory.md) | Changes the security permissions for the logical file specified in the object path. Not implemented by WMI.<br/>                                   |
| [**Compress**](compress-method-in-class-cim-directory.md)                                       | Compresses the logical file (or directory) specified in the object path. Not implemented by WMI.<br/>                                              |
| [**CompressEx**](compressex-method-in-class-cim-directory.md)                                   | Compresses the logical file (or directory) specified in the object path. Not implemented by WMI.<br/>                                              |
| [**Copy**](copy-method-in-class-cim-directory.md)                                               | Copies the logical file (or directory) specified in the object path to the location specified by the input parameter. Not implemented by WMI.<br/> |
| [**CopyEx**](copyex-method-in-class-cim-directory.md)                                           | Copies the logical file (or directory) specified in the object path to the location specified by the input parameter. Not implemented by WMI.<br/> |
| [**Delete**](delete-method-in-class-cim-directory.md)                                           | Deletes the logical file (or directory) specified in the object path. Not implemented by WMI.<br/>                                                 |
| [**DeleteEx**](deleteex-method-in-class-cim-directory.md)                                       | Deletes the logical file (or directory) specified in the object path. Not implemented by WMI.<br/>                                                 |
| [**GetEffectivePermission**](geteffectivepermission-method-in-class-cim-directory.md)           | Determines whether the caller has the aggregated permissions specified by the **Permission** argument. Not implemented by WMI.<br/>                |
| [**Rename**](rename-method-in-class-cim-directory.md)                                           | Renames the logical file (or directory) specified in the object path. Not implemented by WMI.<br/>                                                 |
| [**TakeOwnerShip**](takeownership-method-in-class-cim-directory.md)                             | Obtains ownership of the logical file specified in the object path. Not implemented by WMI.<br/>                                                   |
| [**TakeOwnerShipEx**](takeownershipex-method-in-class-cim-directory.md)                         | Obtains ownership of the logical file specified in the object path. Not implemented by WMI.<br/>                                                   |
| [**Uncompress**](uncompress-method-in-class-cim-directory.md)                                   | Uncompresses the logical file (or directory) specified in the object path. Not implemented by WMI.<br/>                                            |
| [**UncompressEx**](uncompressex-method-in-class-cim-directory.md)                               | Uncompresses the logical file (or directory) specified in the object path. Not implemented by WMI.<br/>                                            |



 

### Properties

The **CIM\_Directory** class has these properties.

<dl> <dt>

**AccessMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Access Rights")
</dt> </dl>

Bitmask that represents the access rights required to access or perform specific operations on the directory. For values, see [**File and Directory Access Rights Constants**](https://msdn.microsoft.com/library/aa822867).

> [!Note]  
> On FAT volumes, the **FULL\_ACCESS** value is returned instead, which indicates no security has been set on the object.

 

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

<dt>

<span id="FILE_READ_DATA__file__or_FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__or_file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__OR_FILE_LIST_DIRECTORY__DIRECTORY_"></span>

**FILE\_READ\_DATA (file) or FILE\_LIST\_DIRECTORY (directory)** (1)


</dt> <dd></dd> <dt>

<span id="FILE_WRITE_DATA__file__or_FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__or_file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__OR_FILE_ADD_FILE__DIRECTORY_"></span>

**FILE\_WRITE\_DATA (file) or FILE\_ADD\_FILE (directory)** (2)


</dt> <dd></dd> <dt>

<span id="FILE_APPEND_DATA__file__or_FILE_ADD_SUBDIRECTORY__directory_"></span><span id="file_append_data__file__or_file_add_subdirectory__directory_"></span><span id="FILE_APPEND_DATA__FILE__OR_FILE_ADD_SUBDIRECTORY__DIRECTORY_"></span>

**FILE\_APPEND\_DATA (file) or FILE\_ADD\_SUBDIRECTORY (directory)** (4)


</dt> <dd></dd> <dt>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>

**FILE\_READ\_EA** (8)


</dt> <dd></dd> <dt>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>

**FILE\_WRITE\_EA** (16)


</dt> <dd></dd> <dt>

<span id="FILE_EXECUTE__file__or_FILE_TRAVERSE__directory_"></span><span id="file_execute__file__or_file_traverse__directory_"></span><span id="FILE_EXECUTE__FILE__OR_FILE_TRAVERSE__DIRECTORY_"></span>

**FILE\_EXECUTE (file) or FILE\_TRAVERSE (directory)** (32)


</dt> <dd></dd> <dt>

<span id="FILE_DELETE_CHILD__directory_"></span><span id="file_delete_child__directory_"></span><span id="FILE_DELETE_CHILD__DIRECTORY_"></span>

**FILE\_DELETE\_CHILD (directory)** (64)


</dt> <dd></dd> <dt>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>

**FILE\_READ\_ATTRIBUTES** (128)


</dt> <dd></dd> <dt>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>

**FILE\_WRITE\_ATTRIBUTES** (256)


</dt> <dd></dd> <dt>

<span id="DELETE"></span><span id="delete"></span>

**DELETE** (65536)


</dt> <dd></dd> <dt>

<span id="READ_CONTROL"></span><span id="read_control"></span>

**READ\_CONTROL** (131072)


</dt> <dd></dd> <dt>

<span id="WRITE_DAC"></span><span id="write_dac"></span>

**WRITE\_DAC** (262144)


</dt> <dd></dd> <dt>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>

**WRITE\_OWNER** (524288)


</dt> <dd></dd> <dt>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>

**SYNCHRONIZE** (1048576)


</dt> <dd></dd> </dl>

</dd> <dt>

**Archive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Should Be Archived")
</dt> </dl>

If **True**, the file should be archived.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Caption")
</dt> </dl>

Short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Compressed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Compressed")
</dt> </dl>

If **True**, the file is compressed.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CompressionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Compression Method")
</dt> </dl>

Free-form string that indicates the algorithm or tool used to compress the logical file. If the compression scheme is unknown or not described, use "Unknown". If the logical file is compressed, but the compression scheme is unknown or not described, use "Compressed". If the logical file is not compressed, use "Not Compressed".

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Class Name")
</dt> </dl>

Name of the class.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CreationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Creation Date")
</dt> </dl>

Date and time that the file was created.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_FileSystem**](cim-filesystem.md).**CSCreationClassName**"), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Computer System Class Name")
</dt> </dl>

Class of the computer system.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_FileSystem**](cim-filesystem.md).**CSName**"), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Computer System Name")
</dt> </dl>

Name of the computer system.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Description")
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Drive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](https://msdn.microsoft.com/library/aa393651), [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Drive")
</dt> </dl>

Drive letter (including the colon that follows the drive letter) of the file. This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

Example: "c:"

</dd> <dt>

**EightDotThreeFileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Eight Dot Three File Name")
</dt> </dl>

DOS-compatible file name. This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

Example: "c:\\progra~1"

</dd> <dt>

**Encrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Encrypted")
</dt> </dl>

If **True**, the file is encrypted.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Encryption Method")
</dt> </dl>

Free-form string that identifies the algorithm or tool used to encrypt a logical file. If the encryption scheme is not indulged (for security reasons, for example), use "Unknown". If the file is encrypted, but either its encryption scheme is unknown or not disclosed, use "Encrypted". If the logical file is not encrypted, use "Not Encrypted".

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Extension**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](https://msdn.microsoft.com/library/aa393651), [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Extension")
</dt> </dl>

File name extension without the preceding period (dot).

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

Example: "txt", "mof", "mdb"

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](https://msdn.microsoft.com/library/aa393651), [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Name")
</dt> </dl>

File name without the file name extension.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

Example: "MyDataFile"

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Size"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("bytes")
</dt> </dl>

Size of the file, in bytes.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**FileType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Type")
</dt> </dl>

Descriptor that represents the file type (indicated by the **Extension** property).

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**FSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_FileSystem**](cim-filesystem.md).**CreationClassName**"), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File System Class Name")
</dt> </dl>

Class of the file system.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**FSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_FileSystem**](cim-filesystem.md).**Name**"), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File System Name")
</dt> </dl>

Name of the file system.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Hidden**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Hidden")
</dt> </dl>

If **True**, the file is hidden.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Install Date")
</dt> </dl>

Date and time when the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InUseCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Current File Open Count")
</dt> </dl>

Number of "file opens" that are currently active against the file.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**LastAccessed**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Accessed")
</dt> </dl>

Date and time that the file was last accessed.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**LastModified**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Modified")
</dt> </dl>

Date and time that the file was last modified.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Inherited name that serves as a key of a logical file instance within a file system (provide full path names).

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Example: "C:\\Windows\\system\\win.ini"

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](https://msdn.microsoft.com/library/aa393651), [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Path")
</dt> </dl>

Path of the file including the leading and trailing backslashes. This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

Example: "\\windows\\system\\"

</dd> <dt>

**Readable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Readable")
</dt> </dl>

If **True**, the file can be read.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Status")
</dt> </dl>

String that indicates the current status of the object.

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

</dd> <dt>

**System**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](https://msdn.microsoft.com/library/aa393650) ("Win32"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("System File")
</dt> </dl>

If **True**, the file is a system file.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Writeable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Writeable")
</dt> </dl>

If **True**, the file can be written.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> </dl>

## Remarks

The **CIM\_Directory** class is derived from [**CIM\_LogicalFile**](cim-logicalfile.md).

WMI does not implement this class. For more information about classes derived from **CIM\_Directory**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalFile**](cim-logicalfile.md)
</dt> </dl>

 

 




