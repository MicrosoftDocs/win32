---
description: The Win32\_Directory&\#32;WMI class represents a directory entry on a computer system running Windows.
ms.assetid: d61cb5ee-8e87-4604-95e6-325c9b543411
ms.tgt_platform: multiple
title: Win32_Directory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Directory
- Win32_Directory.Caption
- Win32_Directory.Description
- Win32_Directory.InstallDate
- Win32_Directory.Name
- Win32_Directory.Status
- Win32_Directory.AccessMask
- Win32_Directory.Archive
- Win32_Directory.Compressed
- Win32_Directory.CompressionMethod
- Win32_Directory.CreationClassName
- Win32_Directory.CreationDate
- Win32_Directory.CSCreationClassName
- Win32_Directory.CSName
- Win32_Directory.Drive
- Win32_Directory.EightDotThreeFileName
- Win32_Directory.Encrypted
- Win32_Directory.EncryptionMethod
- Win32_Directory.Extension
- Win32_Directory.FileName
- Win32_Directory.FileSize
- Win32_Directory.FileType
- Win32_Directory.FSCreationClassName
- Win32_Directory.FSName
- Win32_Directory.Hidden
- Win32_Directory.InUseCount
- Win32_Directory.LastAccessed
- Win32_Directory.LastModified
- Win32_Directory.Path
- Win32_Directory.Readable
- Win32_Directory.System
- Win32_Directory.Writeable
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_Directory class

The **Win32\_Directory** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) represents a directory entry on a computer system running Windows. A directory is a type of file that logically groups data files and provides path information for the grouped files. Example: C:\\TEMP. **Win32\_Directory** does not include directories of network drives.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4C7-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_Directory : CIM_Directory
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  uint32   AccessMask;
  boolean  Archive;
  boolean  Compressed;
  string   CompressionMethod;
  string   CreationClassName;
  datetime CreationDate;
  string   CSCreationClassName;
  string   CSName;
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
  uint64   InUseCount;
  datetime LastAccessed;
  datetime LastModified;
  string   Path;
  boolean  Readable;
  boolean  System;
  boolean  Writeable;
};
```

## Members

The **Win32\_Directory** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_Directory** class has these methods.



| Method                                                                                             | Description                                                                                                                                                                                                                             |
|:---------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeSecurityPermissions**](changesecuritypermissions-method-in-class-win32-directory.md)     | Class method that changes the security permissions for the logical file specified in the object path.<br/>                                                                                                                        |
| [**ChangeSecurityPermissionsEx**](changesecuritypermissionsex-method-in-class-win32-directory.md) | Class method that changes the security permissions for the logical file specified in the object path.<br/>                                                                                                                        |
| [**Compress**](compress-method-in-class-win32-directory.md)                                       | Class method that compresses the logical file (or directory) specified in the object path.<br/>                                                                                                                                   |
| [**CompressEx**](compressex-method-in-class-win32-directory.md)                                   | Class method that compresses the logical file (or directory) specified in the object path.<br/>                                                                                                                                   |
| [**Copy**](copy-method-in-class-win32-directory.md)                                               | Class method that copies the logical file or directory specified in the object path to the location specified by the input parameter.<br/>                                                                                        |
| [**CopyEx**](copyex-method-in-class-win32-directory.md)                                           | Class method that copies the logical file or directory specified in the object path to the location specified by the *FileName* parameter.<br/>                                                                                   |
| [**Delete**](delete-method-in-class-win32-directory.md)                                           | Class method that deletes the logical file (or directory) specified in the object path.<br/>                                                                                                                                      |
| [**DeleteEx**](deleteex-method-in-class-win32-directory.md)                                       | Class method that deletes the logical file (or directory) specified in the object path.<br/>                                                                                                                                      |
| [**GetEffectivePermission**](geteffectivepermission-method-in-class-win32-directory.md)           | Class method that determines whether the caller has the aggregated permissions specified by the *Permissions* argument not only on the file object, but on the share the file or directory resides on (if it is on a share).<br/> |
| [**Rename**](rename-method-in-class-win32-directory.md)                                           | Class method that renames the logical file (or directory) specified in the object path.<br/>                                                                                                                                      |
| [**TakeOwnerShip**](takeownership-method-in-class-win32-directory.md)                             | Class method that obtains ownership of the logical file specified in the object path.<br/>                                                                                                                                        |
| [**TakeOwnerShipEx**](takeownershipex-method-in-class-win32-directory.md)                         | Class method that obtains ownership of the logical file specified in the object path.<br/>                                                                                                                                        |
| [**Uncompress**](uncompress-method-in-class-win32-directory.md)                                   | Class method that uncompresses the logical file (or directory) specified in the object path.<br/>                                                                                                                                 |
| [**UncompressEx**](uncompressex-method-in-class-win32-directory.md)                               | Class method that uncompresses the logical file (or directory) specified in the object path.<br/>                                                                                                                                 |



 

### Properties

The **Win32\_Directory** class has these properties.

<dl> <dt>

**AccessMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Access Rights")
</dt> </dl>

Bitmask that represents the access rights required to access or perform specific operations on the directory. For bit values, see [**File and Directory Access Rights Constants**](/windows/desktop/WmiSdk/file-and-directory-access-rights-constants).

> [!Note]  
> On FAT volumes, the **FULL\_ACCESS** value is returned instead, which indicates no security has been set on the object.

 

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

<dt>

<span id="FILE_READ_DATA__file__or_FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__or_file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__OR_FILE_LIST_DIRECTORY__DIRECTORY_"></span>

<span id="FILE_READ_DATA__file__or_FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__or_file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__OR_FILE_LIST_DIRECTORY__DIRECTORY_"></span>**FILE\_READ\_DATA (file) or FILE\_LIST\_DIRECTORY (directory)** (1)


</dt> <dd>

Grants the right to read data from the file. For a directory, this value grants the right to list the contents of the directory.

</dd> <dt>

<span id="FILE_WRITE_DATA__file__or_FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__or_file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__OR_FILE_ADD_FILE__DIRECTORY_"></span>

<span id="FILE_WRITE_DATA__file__or_FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__or_file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__OR_FILE_ADD_FILE__DIRECTORY_"></span>**FILE\_WRITE\_DATA (file) or FILE\_ADD\_FILE (directory)** (2)


</dt> <dd>

Grants the right to write data to the file. For a directory, this value grants the right to create a file in the directory.

</dd> <dt>

<span id="FILE_APPEND_DATA__file__or_FILE_ADD_SUBDIRECTORY"></span><span id="file_append_data__file__or_file_add_subdirectory"></span><span id="FILE_APPEND_DATA__FILE__OR_FILE_ADD_SUBDIRECTORY"></span>

<span id="FILE_APPEND_DATA__file__or_FILE_ADD_SUBDIRECTORY"></span><span id="file_append_data__file__or_file_add_subdirectory"></span><span id="FILE_APPEND_DATA__FILE__OR_FILE_ADD_SUBDIRECTORY"></span>**FILE\_APPEND\_DATA (file) or FILE\_ADD\_SUBDIRECTORY** (4)


</dt> <dd>

Grants the right to append data to the file. For a directory, this value grants the right to create a subdirectory.

</dd> <dt>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>**FILE\_READ\_EA** (8)


</dt> <dd>

Grants the right to read extended attributes.

</dd> <dt>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>**FILE\_WRITE\_EA** (16)


</dt> <dd>

Grants the right to write extended attributes.

</dd> <dt>

<span id="FILE_EXECUTE__file__or_FILE_TRAVERSE__directory_"></span><span id="file_execute__file__or_file_traverse__directory_"></span><span id="FILE_EXECUTE__FILE__OR_FILE_TRAVERSE__DIRECTORY_"></span>

<span id="FILE_EXECUTE__file__or_FILE_TRAVERSE__directory_"></span><span id="file_execute__file__or_file_traverse__directory_"></span><span id="FILE_EXECUTE__FILE__OR_FILE_TRAVERSE__DIRECTORY_"></span>**FILE\_EXECUTE (file) or FILE\_TRAVERSE (directory)** (32)


</dt> <dd>

Grants the right to execute a file. For a directory, the directory can be traversed.

</dd> <dt>

<span id="FILE_DELETE_CHILD__directory_"></span><span id="file_delete_child__directory_"></span><span id="FILE_DELETE_CHILD__DIRECTORY_"></span>

<span id="FILE_DELETE_CHILD__directory_"></span><span id="file_delete_child__directory_"></span><span id="FILE_DELETE_CHILD__DIRECTORY_"></span>**FILE\_DELETE\_CHILD (directory)** (64)


</dt> <dd>

Grants the right to delete a directory and all of the files it contains (its children), even if the files are read-only.

</dd> <dt>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>**FILE\_READ\_ATTRIBUTES** (128)


</dt> <dd>

Grants the right to read file attributes.

</dd> <dt>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>**FILE\_WRITE\_ATTRIBUTES** (256)


</dt> <dd>

Grants the right to change file attributes.

</dd> <dt>

<span id="DELETE"></span><span id="delete"></span>

<span id="DELETE"></span><span id="delete"></span>**DELETE** (65536)


</dt> <dd>

Grants delete access.

</dd> <dt>

<span id="READ_CONTROL"></span><span id="read_control"></span>

<span id="READ_CONTROL"></span><span id="read_control"></span>**READ\_CONTROL** (131072)


</dt> <dd>

Grants read access to the security descriptor and owner.

</dd> <dt>

<span id="WRITE_DAC"></span><span id="write_dac"></span>

<span id="WRITE_DAC"></span><span id="write_dac"></span>**WRITE\_DAC** (262144)


</dt> <dd>

Grants write access to the discretionary ACL.

</dd> <dt>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>**WRITE\_OWNER** (524288)


</dt> <dd>

Assigns the write owner.

</dd> <dt>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>**SYNCHRONIZE** (1048576)


</dt> <dd>

Synchronizes access and allows a process to wait for an object to enter the signaled state.

</dd> <dt>

<span id="ACCESS_SYSTEM_SECURITY"></span><span id="access_system_security"></span>

<span id="ACCESS_SYSTEM_SECURITY"></span><span id="access_system_security"></span>**ACCESS\_SYSTEM\_SECURITY** (18809343)


</dt> <dd>

Controls the ability to get or set the SACL in an object's security descriptor.

</dd> </dl>

</dd> <dt>

**Archive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Should Be Archived")
</dt> </dl>

Indicates whether the archive bit on the folder has been set. The archive bit is used by backup programs to identify files that should be backed up. If **True**, the file should be archived.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Compressed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Compressed")
</dt> </dl>

Indicates whether or not the folder has been compressed. WMI recognizes folders compressed using WMI itself or using the graphical user interface; it does not, however, recognize .ZIP files as being compressed. If **True**, the file is compressed.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CompressionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Compression Method")
</dt> </dl>

Algorithm or tool (usually a method) used to compress the logical file. If it is not possible (or not desired) to describe the compression scheme (perhaps because it is not known), use the following words: "Unknown" to represent that it is not known whether the logical file is compressed; "Compressed" to represent that the file is compressed, but either its compression scheme is not known or not disclosed; and "Not Compressed" to represent that the logical file is not compressed.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Class Name")
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CreationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Creation Date")
</dt> </dl>

Date that the file system object was created. For more information on working with WMI date and time formats, see [WMI Tasks: Dates and Times](/windows/desktop/WmiSdk/wmi-tasks--dates-and-times).

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_FileSystem**](cim-filesystem.md).**CSCreationClassName**"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Computer System Class Name")
</dt> </dl>

Creation class name of the scoping computer system.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_FileSystem**](cim-filesystem.md).**CSName**"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Computer System Name")
</dt> </dl>

Name of the computer where the file system object is stored.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Drive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Drive")
</dt> </dl>

Drive letter of the drive (including colon) where the file system object is stored.

Example: "c:"

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**EightDotThreeFileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Eight Dot Three File Name")
</dt> </dl>

MS-DOS -compatible name for the folder.

Example: "c:\\progra~1"

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Encrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Encrypted")
</dt> </dl>

Indicates whether or not the folder has been encrypted. If **True**, the folder is encrypted.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Encryption Method")
</dt> </dl>

Algorithm or tool used to encrypt the logical file. If it is not possible (or not desired) to describe the encryption scheme (perhaps for security reasons), use the following words: "Unknown" to represent that it is not known whether the logical file is encrypted; "Encrypted" to represent that the file is encrypted, but either its encryption scheme is not known or not disclosed; and "Not Encrypted" to represent that the logical file is not encrypted.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Extension**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("File Extension")
</dt> </dl>

File name extension for the file system object, not including the dot (.) that separates the extension from the file name.

Examples: "txt", "mof", "mdb"

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("File Name")
</dt> </dl>

File name (without the dot or extension) of the file.

Example: "autoexec"

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Size"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Size of the file system object, in bytes. Although folders possess a **FileSize** property, the value 0 is always returned. To determine the size of a folder, use the FileSystemObject or add up the size of all the files stored in the folder.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**FileType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("File Type")
</dt> </dl>

File type (indicated by the **Extension** property).

For example, an .mdb file is likely to have the file type Microsoft Access Application. An .asp file likely has the file type HTML Document. Folders are typically reported simply as Folder.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**FSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_FileSystem**](cim-filesystem.md).**CreationClassName**"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("File System Class Name")
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

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_FileSystem**](cim-filesystem.md).**Name**"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("File System Name")
</dt> </dl>

Type of file system (NTFS, FAT, FAT32) installed on the drive where the file or folder is located.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Hidden**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Hidden")
</dt> </dl>

Indicates whether the file system object is hidden. If **True**, the file is hidden.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InUseCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Current File Open Count")
</dt> </dl>

Number of "file opens" that are currently active against the file.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**LastAccessed**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Last Accessed")
</dt> </dl>

Date the file was last accessed. For more information on working with WMI date and time formats, see [WMI Tasks: Dates and Times](/windows/desktop/WmiSdk/wmi-tasks--dates-and-times).

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**LastModified**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Last Modified")
</dt> </dl>

Date the file was last modified. For more information on working with WMI date and time formats, see [WMI Tasks: Dates and Times](/windows/desktop/WmiSdk/wmi-tasks--dates-and-times).

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The Name property is a string representing the inherited name that serves as a key of a logical file instance within a file system. Full path names should be provided. Example: C:\\Windows\\system\\win.ini

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Path")
</dt> </dl>

Path for the file. The path includes the leading and trailing backslashes, but not the drive letter or the folder name.

For the folder c:\\windows\\system32\\wbem, the path is \\windows\\system32\\. For the folder c:\\scripts, the path is \\.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Readable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Readable")
</dt> </dl>

Indicates whether you can read items in the folder. If **True**, the file can be read.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
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

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("System File")
</dt> </dl>

Indicates whether the object is a system file. If **True**, the file is a system file

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> <dt>

**Writeable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Writeable")
</dt> </dl>

If **True**, the file can be written.

This property is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

</dd> </dl>

## Remarks

The **Win32\_Directory** class is derived from [**CIM\_Directory**](cim-directory.md).

**Overview**

Folders are file system objects designed to contain other file system objects. This does not mean that all folders are alike, however. Instead, folders can vary considerably. Some folders are operating system folders, which generally should not be modified by a script. Some folders are read-only, which means that users can access the contents of that folder but cannot add to, delete from, or modify those contents. Some folders are compressed for optimal storage, while others are hidden and not visible to users.

WMI uses the **Win32\_Directory** class to manage folders. Significantly, the properties and methods available in this class are identical to the properties and methods available in the [**CIM\_DataFile**](cim-datafile.md) class, the class used to manage files. This means that after you have learned how to manage folders using WMI, you will, without any extra work, also know how to manage files.

The [**Win32\_Subdirectory**](win32-subdirectory.md) association class is also used to manage files and folders. The **Win32\_Subdirectory** class relates a folder and its immediate subfolders. For example, in the folder structure C:\\Scripts\\Logs, Logs is a subfolder of Scripts, and Scripts is a subfolder of the root folder C:\\. However, Logs is not considered a subfolder of C:\\.

You can retrieve the properties of any folder in the file system using the **Win32\_Directory** class. The properties available using this class are shown in Table 11.1. To retrieve the properties for a single folder, construct a Windows Query Language (WQL) query for the **Win32\_Directory** class, making sure that you include the name of the folder. For example, this query binds to the folder D:\\Archive:

`        Copy     "SELECT * FROM Win32_Directory WHERE Name = 'D:\\Archive'"`

When specifying a file or folder name in a WQL query, be sure you use two backslashes (\\\\) to separate path components.

If you want to limit data retrieval to a single disk drive, include a Where clause specifying the drive letter. For example, this query returns a list of all the folders on drive C:

`"SELECT * FROM Win32_Directory WHERE Drive = 'C:'"`

If you need to enumerate all the folders on a computer, be aware that this query can take an extended time to complete.

## Examples

The following VBScript sample retrieves properties for the folder C:\\Scripts.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colFolders = objWMIService.ExecQuery("SELECT * FROM Win32_Directory WHERE Name = 'c:\\Scripts'")
For Each objFolder in colFolders
 Wscript.Echo "Archive: " & objFolder.Archive
 Wscript.Echo "Caption: " & objFolder.Caption
 Wscript.Echo "Compressed: " & objFolder.Compressed
 Wscript.Echo "Compression method: " & objFolder.CompressionMethod
 Wscript.Echo "Creation date: " & objFolder.CreationDate
 Wscript.Echo "Encrypted: " & objFolder.Encrypted
 Wscript.Echo "Encryption method: " & objFolder.EncryptionMethod
 Wscript.Echo "Hidden: " & objFolder.Hidden
 Wscript.Echo "In use count: " & objFolder.InUseCount
 Wscript.Echo "Last accessed: " & objFolder.LastAccessed
 Wscript.Echo "Last modified: " & objFolder.LastModified
 Wscript.Echo "Name: " & objFolder.Name
 Wscript.Echo "Path: " & objFolder.Path
 Wscript.Echo "Readable: " & objFolder.Readable
 Wscript.Echo "System: " & objFolder.System
 Wscript.Echo "Writeable: " & objFolder.Writeable
Next
```



The following VBScript sample returns a list of all the hidden folders on a computer.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colFiles = objWMIService.ExecQuery("SELECT * FROM Win32_Directory WHERE Hidden = True")
For Each objFile in colFiles
 Wscript.Echo objFile.Name
Next
```



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

[**CIM\_Directory**](cim-directory.md)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> </dl>

 

