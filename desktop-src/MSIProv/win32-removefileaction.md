---
title: Win32\_RemoveFileAction class
description: The Win32\_RemoveFileAction WMI class represents files previously installed which are to be removed.
ms.assetid: 'db174d8a-0afb-4938-ac28-1bdbe1d20e36'
keywords: ["Win32_RemoveFileAction class", "Win32_RemoveFileAction class, described"]
topic_type:
- apiref
api_name:
- Win32_RemoveFileAction
- Win32_RemoveFileAction.ActionID
- Win32_RemoveFileAction.Caption
- Win32_RemoveFileAction.Description
- Win32_RemoveFileAction.Direction
- Win32_RemoveFileAction.DirProperty
- Win32_RemoveFileAction.File
- Win32_RemoveFileAction.FileKey
- Win32_RemoveFileAction.FileName
- Win32_RemoveFileAction.InstallMode
- Win32_RemoveFileAction.Name
- Win32_RemoveFileAction.SoftwareElementID
- Win32_RemoveFileAction.SoftwareElementState
- Win32_RemoveFileAction.TargetOperatingSystem
- Win32_RemoveFileAction.Version
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_RemoveFileAction class

The **Win32\_RemoveFileAction** [WMI class](https://msdn.microsoft.com/library/aa393244) represents files previously installed which are to be removed. The class can also remove specific author-specified files that were not installed by the installer. Each of these files is gated by a link to an entry in the software element class; those files whose components are resolved to any active Action state (that is, not in the off or **NULL** state) are removed if the file exists in the specified directory. This implies that removal of files is attempted when the gating software element is first installed, during a reinstall, and again when the gating software element is removed.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_RemoveFileAction : CIM_RemoveFileAction
{
  string ActionID;
  string Caption;
  string Description;
  uint16 Direction;
  string DirProperty;
  string File;
  string FileKey;
  string FileName;
  uint16 InstallMode;
  string Name;
  string SoftwareElementID;
  uint16 SoftwareElementState;
  uint16 TargetOperatingSystem;
  string Version;
};
```

## Members

The **Win32\_RemoveFileAction** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_RemoveFileAction** class has these methods.



| Method                                                          | Description                                                                                                          |
|:----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**Invoke**](invoke-method-in-class-win32-removefileaction.md) | Takes a particular action. The details of how the method performs the action are implementation-specific.<br/> |



 

### Properties

The **Win32\_RemoveFileAction** class has these properties.

<dl> <dt>

**ActionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier assigned to a particular action for a software element.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

</dd> <dt>

**Direction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether a particular [**CIM\_Action**](https://msdn.microsoft.com/library/aa386541) object is part of a sequence of actions to transition the current software element to its next state (Install) or to remove the current software element (Uninstall).



| Value                                                                                                | Meaning              |
|------------------------------------------------------------------------------------------------------|----------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Install<br/>   |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Uninstall<br/> |



 

</dd> <dt>

**DirProperty**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

[**Win32\_Property**](win32-property.md) instance whose value is assumed to resolve to the full path to the folder of the file to be removed. The property can be the name of a directory property for a [**Win32\_DirectorySpecification**](win32-directoryspecification.md) instance or any other property that represents a full path.

</dd> <dt>

**File**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File name.

</dd> <dt>

**FileKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique key identifying this remove file action within its product.

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the file to be removed. If this column is **NULL**, then the specified folder is removed if it is empty. All of the files that match the wildcard are removed from the specified directory.

</dd> <dt>

**InstallMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bitmap that identifies when this remove file action is performed.



| Value                                                                                                                                            | Meaning                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| <span id="0x001__1_"></span><span id="0X001__1_"></span><dl> <dt>**0x001 (1)**</dt> </dl> | Remove only when the associated component is being installed (msiInstallStateLocal or msiInstallStateSource).<br/> |
| <span id="0x002__2_"></span><span id="0X002__2_"></span><dl> <dt>**0x002 (2)**</dt> </dl> | Remove only when the associated component is being removed (msiInstallStateAbsent)<br/>                            |
| <span id="0x003__3_"></span><span id="0X003__3_"></span><dl> <dt>**0x003 (3)**</dt> </dl> | Remove in either of the above cases.<br/>                                                                          |



 

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name used to identify the software element.

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

Target operating system of the owning software element. The possible values for this property are as follows.



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

Version should be in the form \[Major\].\[Minor\].\[Revision\] or \[Major\].\[Minor\]\[letter\]\[revision\].

</dd> </dl>

## Remarks

The **Win32\_RemoveFileAction** class is derived from [**CIM\_RemoveFileAction**](https://msdn.microsoft.com/library/aa388420).

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

 

 





