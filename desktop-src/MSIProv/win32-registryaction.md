---
title: Win32\_RegistryAction class
description: The Win32\_RegistryAction WMI class sets up registry information that the application requires in the system registry.
ms.assetid: 5c389d37-de62-4bc3-8aa9-91dc3802e5c1
keywords:
- Win32_RegistryAction class
- Win32_RegistryAction class, described
topic_type:
- apiref
api_name:
- Win32_RegistryAction
- Win32_RegistryAction.ActionID
- Win32_RegistryAction.Caption
- Win32_RegistryAction.Description
- Win32_RegistryAction.Direction
- Win32_RegistryAction.EntryName
- Win32_RegistryAction.EntryValue
- Win32_RegistryAction.Key
- Win32_RegistryAction.Name
- Win32_RegistryAction.Registry
- Win32_RegistryAction.Root
- Win32_RegistryAction.SoftwareElementID
- Win32_RegistryAction.SoftwareElementState
- Win32_RegistryAction.TargetOperatingSystem
- Win32_RegistryAction.Version
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_RegistryAction class

The **Win32\_RegistryAction** [WMI class](https://msdn.microsoft.com/library/aa393244) sets up registry information that the application requires in the system registry. The registry information is gated by the component class. A registry value is written to the system registry if the corresponding component has been set to be installed either locally or run from source.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_RegistryAction : CIM_Action
{
  string ActionID;
  string Caption;
  string Description;
  uint16 Direction;
  string EntryName;
  string EntryValue;
  string Key;
  string Name;
  string Registry;
  sint16 Root;
  string SoftwareElementID;
  uint16 SoftwareElementState;
  uint16 TargetOperatingSystem;
  string Version;
};
```

## Members

The **Win32\_RegistryAction** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_RegistryAction** class has these methods.



| Method                                                        | Description                                                                                                          |
|:--------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**Invoke**](invoke-method-in-class-win32-registryaction.md) | Takes a particular action. The details of how the method performs the action are implementation-specific.<br/> |



 

### Properties

The **Win32\_RegistryAction** class has these properties.

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

**EntryName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Property is written to the default registry key.

</dd> <dt>

**EntryValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Registry value.

</dd> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Key for the registry value.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name used to identify the software element.

</dd> <dt>

**Registry**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Registry value name. If the **EntryValue** property is null, then the following strings in the **Name** property have special significance.



| String                                                                                                | Meaning                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="_"></span><dl> <dt>**+**</dt> </dl>  | The key is to be created, if absent upon the installation of the component.<br/>                                                                                                                    |
| <span id="-"></span><dl> <dt>**-**</dt> </dl>  | The key is to be deleted, if present, with all its values and subkeys upon the uninstallation of the component.<br/>                                                                                |
| <span id="_"></span><dl> <dt>**\***</dt> </dl> | The key is to be created, if absent upon the installation of the component AND the key is to be deleted, if present, with all its values and subkeys upon the uninstallation of the component.<br/> |



 

</dd> <dt>

**Root**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State of a software element.



| Value                                                                                                 | Meaning                             |
|-------------------------------------------------------------------------------------------------------|-------------------------------------|
| <span id="1"></span><dl> <dt>** 1**</dt> </dl> | **HKEY\_CURRENT\_USER**<br/>  |
| <span id="1"></span><dl> <dt>** 1**</dt> </dl> | **HKEY\_LOCAL\_MACHINE**<br/> |
| <span id="0"></span><dl> <dt>**0**</dt> </dl>  | **HKEY\_CLASSES\_ROOT**<br/>  |
| <span id="1"></span><dl> <dt>**1**</dt> </dl>  | **HKEY\_CURRENT\_USER**<br/>  |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>  | **HKEY\_LOCAL\_MACHINE**<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>  | **HKEY\_USERS**<br/>          |



 

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

Version of the software element. Values should be in the form \[Major\].\[Minor\].\[Revision\] or \[Major\].\[Minor\]\[letter\]\[revision\].

</dd> </dl>

## Remarks

The **Win32\_RegistryAction** class is derived from [**CIM\_Action**](https://msdn.microsoft.com/library/aa386541).

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

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





