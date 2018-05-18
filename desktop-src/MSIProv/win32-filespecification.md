---
title: Win32\_FileSpecification class
description: The Win32\_FileSpecification WMI class represents a source file with its various attributes, ordered by a unique, nonlocalized identifier.
ms.assetid: '89dbcb09-a29e-41d9-a21a-bc419947b3e3'
keywords: ["Win32_FileSpecification class", "Win32_FileSpecification class, described"]
topic_type:
- apiref
api_name:
- Win32_FileSpecification
- Win32_FileSpecification.Attributes
- Win32_FileSpecification.Caption
- Win32_FileSpecification.CheckID
- Win32_FileSpecification.CheckMode
- Win32_FileSpecification.CheckSum
- Win32_FileSpecification.CRC1
- Win32_FileSpecification.CRC2
- Win32_FileSpecification.CreateTimeStamp
- Win32_FileSpecification.Description
- Win32_FileSpecification.FileID
- Win32_FileSpecification.FileSize
- Win32_FileSpecification.Language
- Win32_FileSpecification.MD5CheckSum
- Win32_FileSpecification.Name
- Win32_FileSpecification.Sequence
- Win32_FileSpecification.SoftwareElementID
- Win32_FileSpecification.SoftwareElementState
- Win32_FileSpecification.TargetOperatingSystem
- Win32_FileSpecification.Version
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_FileSpecification class

The **Win32\_FileSpecification** [WMI class](https://msdn.microsoft.com/library/aa393244) represents a source file with its various attributes, ordered by a unique, nonlocalized identifier. For uncompressed files, the **File** property is ignored, and the **FileName** property is used for both source and destination file name. You must set the Uncompressed bit of the **Attributes** property for any file that is not compressed in a cabinet.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_FileSpecification : CIM_FileSpecification
{
  uint16   Attributes;
  string   Caption;
  string   CheckID;
  boolean  CheckMode;
  uint32   CheckSum;
  uint32   CRC1;
  uint32   CRC2;
  datetime CreateTimeStamp;
  string   Description;
  string   FileID;
  uint64   FileSize;
  string   Language;
  string   MD5CheckSum;
  string   Name;
  uint16   Sequence;
  string   SoftwareElementID;
  uint16   SoftwareElementState;
  uint16   TargetOperatingSystem;
  string   Version;
};
```

## Members

The **Win32\_FileSpecification** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_FileSpecification** class has these methods.



| Method                                                           | Description                                                                                                                                                                                            |
|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Invoke**](invoke-method-in-class-win32-filespecification.md) | Evaluates a particular check. The details of how the method evaluates a particular check in a CIM context are described by the nonabstract [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) subclasses.<br/> |



 

### Properties

The **Win32\_FileSpecification** class has these properties.

<dl> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Integer that contains bit flags representing file attributes.



| Value                                                                                     | Meaning                                                                                                 |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| <dl> <dt>1 (0x1)</dt> </dl>        | Read Only.<br/>                                                                                   |
| <dl> <dt>2 (0x2)</dt> </dl>        | Hidden.<br/>                                                                                      |
| <dl> <dt>4 (0x4)</dt> </dl>        | System.<br/>                                                                                      |
| <dl> <dt>256 (0x100)</dt> </dl>    | Split - the file is split between two or more compression cabinets.<br/>                          |
| <dl> <dt>512 (0x200)</dt> </dl>    | Vital - the file is vital for the proper operation of the component to which it belongs.<br/>     |
| <dl> <dt>4096 (0x1000)</dt> </dl>  | Permanent - the file is not removed on uninstall.<br/>                                            |
| <dl> <dt>8192 (0x2000)</dt> </dl>  | Uncompressed - the file is uncompressed on the source media.<br/>                                 |
| <dl> <dt>16384 (0x4000)</dt> </dl> | Patch (reserved for future use).<br/>                                                             |
| <dl> <dt>32768 (0x8000)</dt> </dl> | PatchSourceIgnore - the file can be ignored during a patch upgrade if it is run-from-source.<br/> |



 

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object.

</dd> <dt>

**CheckID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier used in conjunction with other keys to uniquely identify the check.

</dd> <dt>

**CheckMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Condition is expected to exist in the environment. When **True**, the condition is expected to exist (for example, a file is expected to be on a system), so the [**Invoke**](invoke-method-in-class-win32-filespecification.md) method is expected to return **True**.

</dd> <dt>

**CheckSum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Checksum calculated as the 16-bit sum of the first 32 bytes of the file.

</dd> <dt>

**CRC1**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CRC value calculated using the middle 512 kilobytes.

</dd> <dt>

**CRC2**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CRC value for the middle 512 kilobytes with a offset modulo 3 to the start of the file of zero.

</dd> <dt>

**CreateTimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date the file was created.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

</dd> <dt>

**FileID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique key that identifies a file within the scope of a product.

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the file.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**Language**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Decimal language identifiers that are comma-separated if there is more than one.

</dd> <dt>

**MD5CheckSum**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Algorithm for computing a 128-bit checksum for any file or object. The probability of two different files producing the same MD5 checksum is small (about 1 in 2^64), and the MD5 checksum of a file can be used to construct a reliable content identifier that is likely to uniquely identify the file. The reverse is also true. If two files have the same MD5 checksum, it is likely that the files are identical. For purposes of MOF specification of the MD5 property, the MD5 algorithm always generates a 32 character string. For example, the string "abcdefghijklmnopqrstuvwxyz" generates the string "c3fcd3d76192e4007dfb496cca67e13b".

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of a file or the name of a file with a directory prefix.

</dd> <dt>

**Sequence**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Sequence with respect to the media images. Order must track the cabinet order.

</dd> <dt>

**SoftwareElementID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier for the software element.

</dd> <dt>

**SoftwareElementState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State of a software element.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Deployable<br/>  |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Installable<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Executable<br/>  |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Running<br/>     |



 

</dd> <dt>

**TargetOperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Target operating system of the software element. The following list identifies the list of possible values for this property.



| Value                                                                                                  | Meaning                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl>   | Unknown<br/>          |
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Other<br/>            |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | MACOS<br/>            |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | ATTUNIX<br/>          |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | DGUX<br/>             |
| <span id="5"></span><dl> <dt>**5**</dt> </dl>   | DECNT<br/>            |
| <span id="6"></span><dl> <dt>**6**</dt> </dl>   | Digital Unix<br/>     |
| <span id="7"></span><dl> <dt>**7**</dt> </dl>   | OpenVMS<br/>          |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | HPUX<br/>             |
| <span id="9"></span><dl> <dt>**9**</dt> </dl>   | AIX<br/>              |
| <span id="10"></span><dl> <dt>**10**</dt> </dl> | MVS<br/>              |
| <span id="11"></span><dl> <dt>**11**</dt> </dl> | OS400<br/>            |
| <span id="12"></span><dl> <dt>**12**</dt> </dl> | OS/2<br/>             |
| <span id="13"></span><dl> <dt>**13**</dt> </dl> | JavaVM<br/>           |
| <span id="14"></span><dl> <dt>**14**</dt> </dl> | MSDOS<br/>            |
| <span id="15"></span><dl> <dt>**15**</dt> </dl> | WIN3x<br/>            |
| <span id="16"></span><dl> <dt>**16**</dt> </dl> | WIN95<br/>            |
| <span id="17"></span><dl> <dt>**17**</dt> </dl> | WIN98<br/>            |
| <span id="18"></span><dl> <dt>**18**</dt> </dl> | WINNT<br/>            |
| <span id="19"></span><dl> <dt>**19**</dt> </dl> | WINCE<br/>            |
| <span id="20"></span><dl> <dt>**20**</dt> </dl> | NCR3000<br/>          |
| <span id="21"></span><dl> <dt>**21**</dt> </dl> | NetWare<br/>          |
| <span id="22"></span><dl> <dt>**22**</dt> </dl> | OSF<br/>              |
| <span id="23"></span><dl> <dt>**23**</dt> </dl> | DC/OS<br/>            |
| <span id="24"></span><dl> <dt>**24**</dt> </dl> | Reliant UNIX<br/>     |
| <span id="25"></span><dl> <dt>**25**</dt> </dl> | SCO UnixWare<br/>     |
| <span id="26"></span><dl> <dt>**26**</dt> </dl> | SCO OpenServer<br/>   |
| <span id="27"></span><dl> <dt>**27**</dt> </dl> | Sequent<br/>          |
| <span id="28"></span><dl> <dt>**28**</dt> </dl> | IRIX<br/>             |
| <span id="29"></span><dl> <dt>**29**</dt> </dl> | Solaris<br/>          |
| <span id="30"></span><dl> <dt>**30**</dt> </dl> | SunOS<br/>            |
| <span id="31"></span><dl> <dt>**31**</dt> </dl> | U6000<br/>            |
| <span id="32"></span><dl> <dt>**32**</dt> </dl> | ASERIES<br/>          |
| <span id="33"></span><dl> <dt>**33**</dt> </dl> | TandemNSK<br/>        |
| <span id="34"></span><dl> <dt>**34**</dt> </dl> | TandemNT<br/>         |
| <span id="35"></span><dl> <dt>**35**</dt> </dl> | BS2000<br/>           |
| <span id="36"></span><dl> <dt>**36**</dt> </dl> | LINUX<br/>            |
| <span id="37"></span><dl> <dt>**37**</dt> </dl> | Lynx<br/>             |
| <span id="38"></span><dl> <dt>**38**</dt> </dl> | XENIX<br/>            |
| <span id="39"></span><dl> <dt>**39**</dt> </dl> | VM/ESA<br/>           |
| <span id="40"></span><dl> <dt>**40**</dt> </dl> | Interactive UNIX<br/> |
| <span id="41"></span><dl> <dt>**41**</dt> </dl> | BSDUNIX<br/>          |
| <span id="42"></span><dl> <dt>**42**</dt> </dl> | FreeBSD<br/>          |
| <span id="43"></span><dl> <dt>**43**</dt> </dl> | NetBSD<br/>           |
| <span id="44"></span><dl> <dt>**44**</dt> </dl> | GNU Hurd<br/>         |
| <span id="45"></span><dl> <dt>**45**</dt> </dl> | OS9<br/>              |
| <span id="46"></span><dl> <dt>**46**</dt> </dl> | MACH Kernel<br/>      |
| <span id="47"></span><dl> <dt>**47**</dt> </dl> | Inferno<br/>          |
| <span id="48"></span><dl> <dt>**48**</dt> </dl> | QNX<br/>              |
| <span id="49"></span><dl> <dt>**49**</dt> </dl> | EPOC<br/>             |
| <span id="50"></span><dl> <dt>**50**</dt> </dl> | IxWorks<br/>          |
| <span id="51"></span><dl> <dt>**51**</dt> </dl> | VxWorks<br/>          |
| <span id="52"></span><dl> <dt>**52**</dt> </dl> | MiNT<br/>             |
| <span id="53"></span><dl> <dt>**53**</dt> </dl> | BeOS<br/>             |
| <span id="54"></span><dl> <dt>**54**</dt> </dl> | HP MPE<br/>           |
| <span id="55"></span><dl> <dt>**55**</dt> </dl> | NextStep<br/>         |
| <span id="56"></span><dl> <dt>**56**</dt> </dl> | PalmPilot<br/>        |
| <span id="57"></span><dl> <dt>**57**</dt> </dl> | Rhapsody<br/>         |



 

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of the software element. Values should be in the form \[Major\].\[Minor\].\[Revision\] or \[Major\].\[Minor\]\[letter\]\[revision\].

</dd> </dl>

## Remarks

The **Win32\_FileSpecification** class is derived from [**CIM\_FileSpecification**](https://msdn.microsoft.com/library/aa387271).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





