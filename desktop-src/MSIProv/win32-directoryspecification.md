---
title: Win32\_DirectorySpecification class
description: The Win32\_DirectorySpecification class represents the directory layout for the product. Each instance of the class represents a directory in both the source image and the destination image.
ms.assetid: c298bdba-342d-4330-9dd3-7b6aaec9b2d9
keywords:
- Win32_DirectorySpecification class
- Win32_DirectorySpecification class, described
topic_type:
- apiref
api_name:
- Win32_DirectorySpecification
- Win32_DirectorySpecification.Caption
- Win32_DirectorySpecification.CheckID
- Win32_DirectorySpecification.CheckMode
- Win32_DirectorySpecification.DefaultDir
- Win32_DirectorySpecification.Description
- Win32_DirectorySpecification.Directory
- Win32_DirectorySpecification.DirectoryPath
- Win32_DirectorySpecification.DirectoryType
- Win32_DirectorySpecification.Name
- Win32_DirectorySpecification.SoftwareElementID
- Win32_DirectorySpecification.SoftwareElementState
- Win32_DirectorySpecification.TargetOperatingSystem
- Win32_DirectorySpecification.Version
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_DirectorySpecification class

The **Win32\_DirectorySpecification** class represents the directory layout for the product. Each instance of the class represents a directory in both the source image and the destination image.

Directory resolution is performed as follows:

-   Root destination directories: The root directory entries are those with a null **Directory\_Parent** value or a **Directory\_Parent** value identical to the **Directory** value. The value in the **Directory** property is interpreted as the name of a property defining the location of the destination directory. If the property is defined, the destination directory is resolved to the property's value. If the property is undefined, the **ROOTDRIVE** property is used instead to resolve the path.
-   Root source directories: The value of the **DefaultDir** column for root entries is interpreted as the name of a property defining the source location of this directory. This property must be defined or an error will occur.
-   Nonroot destination directories: The **Directory** value for a nonroot directory is also interpreted as the name of a property defining the location of the destination. If the property is defined, the destination directory is resolved to the property's value. If the property is not defined, the destination directory is resolved to a subdirectory beneath the resolved destination directory for the Directory\_Parent entry. The DefaultDir value defines the name of the subdirectory.
-   Nonroot source directories: The source directory for a nonroot directory is resolved to a subdirectory of the resolved source directory for the Directory\_Parent entry. Again, the **DefaultDir** value defines the name of the subdirectory.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_DirectorySpecification : CIM_DirectorySpecification
{
  string  Caption;
  string  CheckID;
  boolean CheckMode;
  string  DefaultDir;
  string  Description;
  string  Directory;
  string  DirectoryPath;
  uint16  DirectoryType;
  string  Name;
  string  SoftwareElementID;
  uint16  SoftwareElementState;
  uint16  TargetOperatingSystem;
  string  Version;
};
```

## Members

The **Win32\_DirectorySpecification** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DirectorySpecification** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short description of the object.

</dd> <dt>

**CheckID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Identifier used in conjunction with other keys to uniquely identify the check.

</dd> <dt>

**CheckMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Condition is expected to exist or not exist in the environment. When **TRUE**, the condition is expected to exist (a file is expected to be on a system) so the **Invoke**() method is expected to return **TRUE**.

</dd> <dt>

**DefaultDir**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the objects.

</dd> <dt>

**Directory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

</dd> <dt>

**DirectoryPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of a directory. The value supplied by an application provider is actually a default or recommended path name and can be changed for a particular environment.

</dd> <dt>

**DirectoryType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of directory being described.



| Value                                                                                                  | Meaning                                   |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Product log directory<br/>          |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Shared base directory<br/>          |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | Shared executable directory<br/>    |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | Shared library directory<br/>       |
| <span id="5"></span><dl> <dt>**5**</dt> </dl>   | Shared include directory<br/>       |
| <span id="6"></span><dl> <dt>**6**</dt> </dl>   | System base directory<br/>          |
| <span id="7"></span><dl> <dt>**7**</dt> </dl>   | System executable directory<br/>    |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | System library directory<br/>       |
| <span id="9"></span><dl> <dt>**9**</dt> </dl>   | System configuration directory<br/> |
| <span id="10"></span><dl> <dt>**10**</dt> </dl> | System include directory<br/>       |
| <span id="11"></span><dl> <dt>**11**</dt> </dl> | System log directory<br/>           |
| <span id="12"></span><dl> <dt>**12**</dt> </dl> | Other<br/>                          |



 

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name used to identify this software element.

</dd> <dt>

**SoftwareElementID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier for this software element. Designed to be used in conjunction with other keys to create a unique representation of this [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) instance.

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
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Disabled<br/>    |
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

Target operating system of the owning software element. The possible values for this property are as follows.



| Value                                                                                                  | Meaning                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl>   | Unknown<br/>          |
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Other<br/>            |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | MACOS<br/>            |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | ATTUNIX<br/>          |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | DGUX<br/>             |
| <span id="5"></span><dl> <dt>**5**</dt> </dl>   | DECNT<br/>            |
| <span id="6"></span><dl> <dt>**6**</dt> </dl>   | Digital UNIX<br/>     |
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

Version of the software element. Version should be in the form &lt;Major&gt;.&lt;Minor&gt;.&lt;Revision&gt; or &lt;Major&gt;.&lt;Minor&gt;&lt;letter&gt;&lt;revision&gt;.

</dd> </dl>

## Remarks

The **Win32\_DirectorySpecification** class is derived from [**CIM\_DirectorySpecification**](https://msdn.microsoft.com/library/aa387251).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 





