---
title: Win32\_SoftwareElement class
description: The Win32\_SoftwareElement WMI class represents a software element, part of a software feature (a distinct subset of a product which may contain one or more elements).
ms.assetid: 93f6168f-5198-47c3-be5c-002b14c31986
keywords:
- Win32_SoftwareElement class
- Win32_SoftwareElement class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareElement
- Win32_SoftwareElement.Attributes
- Win32_SoftwareElement.BuildNumber
- Win32_SoftwareElement.Caption
- Win32_SoftwareElement.CodeSet
- Win32_SoftwareElement.Description
- Win32_SoftwareElement.IdentificationCode
- Win32_SoftwareElement.InstallDate
- Win32_SoftwareElement.InstallState
- Win32_SoftwareElement.LanguageEdition
- Win32_SoftwareElement.Manufacturer
- Win32_SoftwareElement.Name
- Win32_SoftwareElement.OtherTargetOS
- Win32_SoftwareElement.Path
- Win32_SoftwareElement.SerialNumber
- Win32_SoftwareElement.SoftwareElementID
- Win32_SoftwareElement.SoftwareElementState
- Win32_SoftwareElement.Status
- Win32_SoftwareElement.TargetOperatingSystem
- Win32_SoftwareElement.Version
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

# Win32\_SoftwareElement class

The **Win32\_SoftwareElement** [WMI class](https://msdn.microsoft.com/library/aa393244) represents a software element, part of a software feature (a distinct subset of a product which may contain one or more elements). Each software element is defined in a **Win32\_SoftwareElement** instance, and the association between a feature and its [**Win32\_SoftwareFeature**](win32-softwarefeature.md) instance is defined in the [**Win32\_SoftwareFeatureSoftwareElements**](win32-softwarefeaturesoftwareelements.md) association class.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareElement : CIM_SoftwareElement
{
  uint16   Attributes;
  string   BuildNumber;
  string   Caption;
  string   CodeSet;
  string   Description;
  string   IdentificationCode;
  datetime InstallDate;
  sint16   InstallState;
  string   LanguageEdition;
  string   Manufacturer;
  string   Name;
  string   OtherTargetOS;
  string   Path;
  string   SerialNumber;
  string   SoftwareElementID;
  uint16   SoftwareElementState;
  string   Status;
  uint16   TargetOperatingSystem;
  string   Version;
};
```

## Members

The **Win32\_SoftwareElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareElement** class has these properties.

<dl> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bitmap that contains the remote execution options for the software element.

</dd> <dt>

**BuildNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of the build.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object.

</dd> <dt>

**CodeSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Code set used by the software element.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

</dd> <dt>

**IdentificationCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Manufacturer's identifier for this software element. Often this is a stock keeping unit (SKU) or part number.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object was installed. This property does not need a value to indicate that the object is installed.

</dd> <dt>

**InstallState**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current installed state for the software element.



| Value                                                                                                  | Meaning                      |
|--------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="-7"></span><dl> <dt>**-7**</dt> </dl> | Not Used<br/>          |
| <span id="-6"></span><dl> <dt>**-6**</dt> </dl> | Bad Configuration<br/> |
| <span id="-4"></span><dl> <dt>**-4**</dt> </dl> | Source Absent<br/>     |
| <span id="-1"></span><dl> <dt>**-1**</dt> </dl> | Error<br/>             |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Absent<br/>            |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | Local<br/>             |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | Source<br/>            |



 

</dd> <dt>

**LanguageEdition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Language edition of this software element. The language codes defined in ISO 639 should be used. Where the software element represents a multilingual or multiple international version of a product, the string "multilingual" should be used.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Manufacturer of the software element.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name used to identify the software element.

</dd> <dt>

**OtherTargetOS**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Records the manufacturer and operating system type for a software element when the **TargetOperatingSystem** property has a value of 1 (Other). When **TargetOperatingSystem** has a value of 1, **OtherTargetOS** must have a non-null value. For all other values of **TargetOperatingSystem**, **OtherTargetOS** is **NULL**.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path to the installed software element. If the component is a registry key, the registry roots are represented numerically. For example, a registry path of

```
HKEY_CURRENT_USER
   SOFTWARE
      Microsoft
```

would be returned as **01:\\SOFTWARE\\Microsoft**. The registry roots returned are defined as follows:



| Value                                                                                                  | Meaning                         |
|--------------------------------------------------------------------------------------------------------|---------------------------------|
| <span id="00"></span><dl> <dt>**00**</dt> </dl> | HKEY\_CLASSES\_ROOT<br/>  |
| <span id="01"></span><dl> <dt>**01**</dt> </dl> | HKEY\_CURRENT\_USER<br/>  |
| <span id="02"></span><dl> <dt>**02**</dt> </dl> | HKEY\_LOCAL\_MACHINE<br/> |
| <span id="03"></span><dl> <dt>**03**</dt> </dl> | HKEY\_USERS<br/>          |



 

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Assigned serial number of the software element.

</dd> <dt>

**SoftwareElementID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier for the software element and is designed to be used in conjunction with other keys to create a unique representation of this **Win32\_SoftwareElement** instance.

</dd> <dt>

**SoftwareElementState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Various states of a software element's life cycle. A software element in the deployable state describes the details necessary to successful distribute it and the details (conditions and actions) required to create a software element in the installable state (that is, the next state). A software element in the installable state describes the details necessary to successfully install it and details conditions and actions required to create a software element in the executable state (that is, the next state). A software element in the executable state describes the details necessary to successfully start it and details conditions and actions required to create a software element in the running state (that is, the next state). A software element in the running state describes the details necessary to monitor and operate on a start element.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Deployable<br/>  |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Installable<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Executable<br/>  |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Running<br/>     |



 

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. Various operational and non-operational statuses can be defined. Operational statuses include: OK, Degraded, and Pred Fail (an element, such as a SMART-enabled hard disk drive, can function properly but predict a failure in the near future). Non-operational statuses include: Error, Starting, Stopping, and Service. Examples of Service could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither OK nor in one of the other states.

Values are:

<dl><span id="_OK_"></span><span id="_ok_"></span><dt>

**"OK"**
</dt><span id="_Error_"></span><span id="_error_"></span><span id="_ERROR_"></span><dt>

**"Error"**
</dt><span id="_Degraded_"></span><span id="_degraded_"></span><span id="_DEGRADED_"></span><dt>

**"Degraded"**
</dt><span id="_Unknown_"></span><span id="_unknown_"></span><span id="_UNKNOWN_"></span><dt>

**"Unknown"**
</dt><span id="_Pred_Fail_"></span><span id="_pred_fail_"></span><span id="_PRED_FAIL_"></span><dt>

**"Pred Fail"**
</dt><span id="_Starting_"></span><span id="_starting_"></span><span id="_STARTING_"></span><dt>

**"Starting"**
</dt><span id="_Stopping_"></span><span id="_stopping_"></span><span id="_STOPPING_"></span><dt>

**"Stopping"**
</dt><span id="_Service_"></span><span id="_service_"></span><span id="_SERVICE_"></span><dt>

**"Service"**
</dt> </dl>

</dd> <dt>

**TargetOperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provider's choice of operating system environment. The value of this property does not ensure binary executable. Two other pieces of information are needed. First, the version of the operating system must be specified using the operating system version check. The second piece of information is the architecture the operating system runs on. The combination of these constructs allows the provider to clearly identify the level of operating system required for a particular software element. The possible values for this property are as follows.



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
| <span id="19"></span><dl> <dt>**19**</dt> </dl> | XP<br/>               |
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

Any component can be shared between two or more [**Win32\_SoftwareFeature**](win32-softwarefeature.md) instances. If two or more features reference the same component, that component is selected for installation if any of these features are selected.

The **Win32\_SoftwareElement** class is derived from [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467).

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

 

 





