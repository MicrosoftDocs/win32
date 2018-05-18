---
title: Win32\_IniFileSpecification class
description: The Win32\_IniFileSpecification \ 8194;WMI class contains the .INI information that an application needs to set in an .INI file.
ms.assetid: 'a686f926-2677-4473-8176-0d56d7c6ec96'
keywords: ["Win32_IniFileSpecification class", "Win32_IniFileSpecification class, described"]
topic_type:
- apiref
api_name:
- Win32_IniFileSpecification
- Win32_IniFileSpecification.Action
- Win32_IniFileSpecification.Caption
- Win32_IniFileSpecification.CheckID
- Win32_IniFileSpecification.CheckMode
- Win32_IniFileSpecification.CheckSum
- Win32_IniFileSpecification.CRC1
- Win32_IniFileSpecification.CRC2
- Win32_IniFileSpecification.CreateTimeStamp
- Win32_IniFileSpecification.Description
- Win32_IniFileSpecification.FileSize
- Win32_IniFileSpecification.IniFile
- Win32_IniFileSpecification.Key
- Win32_IniFileSpecification.MD5Checksum
- Win32_IniFileSpecification.Name
- Win32_IniFileSpecification.Section
- Win32_IniFileSpecification.SoftwareElementID
- Win32_IniFileSpecification.SoftwareElementState
- Win32_IniFileSpecification.TargetOperatingSystem
- Win32_IniFileSpecification.Value
- Win32_IniFileSpecification.Version
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_IniFileSpecification class

The **Win32\_IniFileSpecification** [WMI class](https://msdn.microsoft.com/library/aa393244) contains the .INI information that an application needs to set in an .INI file. The .INI file information is written out when the corresponding component is selected for installation—locally or from the source.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_IniFileSpecification : CIM_FileSpecification
{
  uint16   Action;
  string   Caption;
  string   CheckID;
  boolean  CheckMode;
  uint32   CheckSum;
  uint32   CRC1;
  uint32   CRC2;
  datetime CreateTimeStamp;
  string   Description;
  uint64   FileSize;
  string   IniFile;
  string   Key;
  string   MD5Checksum;
  string   Name;
  string   Section;
  string   SoftwareElementID;
  uint16   SoftwareElementState;
  uint16   TargetOperatingSystem;
  string   Value;
  string   Version;
};
```

## Members

The **Win32\_IniFileSpecification** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_IniFileSpecification** class has these methods.



| Method                                                              | Description                                                                                                                                                                                        |
|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Invoke**](invoke-method-in-class-win32-inifilespecification.md) | Evaluates a specific check. The details of how the method evaluates a specific check in a CIM context are described by the nonabstract [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) subclasses.<br/> |



 

### Properties

The **Win32\_IniFileSpecification** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of modification made.



| Value                                                                              | Meaning                                                                                     |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Creates or updates an .ini entry.<br/>                                                |
| <dl> <dt>1 (0x1)</dt> </dl> | Creates an .ini entry only if the entry does not already exist.<br/>                  |
| <dl> <dt>3 (0x3)</dt> </dl> | Creates a new entry or appends a new comma-separated value to an existing entry.<br/> |



 

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of an object—a one-line string.

</dd> <dt>

**CheckID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier used together with other keys to uniquely identify a check.

</dd> <dt>

**CheckMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Condition is expected to exist in the environment. When **True**, the condition is expected to exist. For example, a file is expected to be on a system, so the Invoke method is expected to return **True**.

</dd> <dt>

**CheckSum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Checksum calculated as the 16-bit sum of the first 32 bytes of a file.

</dd> <dt>

**CRC1**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Cyclic Redundancy Check (CRC) value calculated by using the middle 512K bytes.

</dd> <dt>

**CRC2**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CRC value for the middle 512K bytes with an offset of modulo 3 to the start of a file of 0 (zero).

</dd> <dt>

**CreateTimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date the file is created.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of an object.

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of a file.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**IniFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique key that identifies an .ini file specification within its product.

</dd> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Key of the .ini file within a section.

</dd> <dt>

**MD5Checksum**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**MD5Checksum** algorithm is a well-known algorithm for computing a 128-bit checksum for a file or object. The likelihood of two different files producing the same MD5 checksum is very small (about 1 in 2^64). The MD5 checksum of a file can be used to construct a reliable content identifier that uniquely identifies a file. If two files have the same MD5 checksum, it is very likely that the files are identical. For purposes of MOF specification of the MD5 property, the MD5 algorithm always generates a 32-character string. For example: The string "abcdefghijklmnopqrstuvwxyz" generates the string "c3fcd3d76192e4007dfb496cca67e13b".

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the file or the name of the file with a directory prefix.

</dd> <dt>

**Section**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Section of an .ini file.

</dd> <dt>

**SoftwareElementID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier for a software element.

</dd> <dt>

**SoftwareElementState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State of a software element.



| Value                                                                              | Meaning                |
|------------------------------------------------------------------------------------|------------------------|
| <dl> <dt>1 (0x1)</dt> </dl> | Deployable<br/>  |
| <dl> <dt>2 (0x2)</dt> </dl> | Installable<br/> |
| <dl> <dt>3 (0x3)</dt> </dl> | Executable<br/>  |
| <dl> <dt>4 (0x4)</dt> </dl> | Running<br/>     |



 

</dd> <dt>

**TargetOperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Target operating system of a software element.

The values are:



| Value                                                                                | Meaning                     |
|--------------------------------------------------------------------------------------|-----------------------------|
| <dl> <dt>0 (0x0)</dt> </dl>   | Unknown<br/>          |
| <dl> <dt>1 (0x1)</dt> </dl>   | Other<br/>            |
| <dl> <dt>2 (0x2)</dt> </dl>   | MACOS<br/>            |
| <dl> <dt>3 (0x3)</dt> </dl>   | ATTUNIX<br/>          |
| <dl> <dt>4 (0x4)</dt> </dl>   | DGUX<br/>             |
| <dl> <dt>5 (0x5)</dt> </dl>   | DECNT<br/>            |
| <dl> <dt>6 (0x6)</dt> </dl>   | Digital UNIX<br/>     |
| <dl> <dt>7 (0x7)</dt> </dl>   | OpenVMS<br/>          |
| <dl> <dt>8 (0x8)</dt> </dl>   | HPUX<br/>             |
| <dl> <dt>9 (0x9)</dt> </dl>   | AIX<br/>              |
| <dl> <dt>10 (0xA)</dt> </dl>  | MVS<br/>              |
| <dl> <dt>11 (0xB)</dt> </dl>  | OS400<br/>            |
| <dl> <dt>12 (0xC)</dt> </dl>  | OS/2<br/>             |
| <dl> <dt>13 (0xD)</dt> </dl>  | JavaVM<br/>           |
| <dl> <dt>14 (0xE)</dt> </dl>  | MSDOS<br/>            |
| <dl> <dt>15 (0xF)</dt> </dl>  | WIN3x<br/>            |
| <dl> <dt>16 (0x10)</dt> </dl> | WIN95<br/>            |
| <dl> <dt>17 (0x11)</dt> </dl> | WIN98<br/>            |
| <dl> <dt>18 (0x12)</dt> </dl> | WINNT<br/>            |
| <dl> <dt>19 (0x13)</dt> </dl> | WINCE<br/>            |
| <dl> <dt>20 (0x14)</dt> </dl> | NCR3000<br/>          |
| <dl> <dt>21 (0x15)</dt> </dl> | NetWare<br/>          |
| <dl> <dt>22 (0x16)</dt> </dl> | OSF<br/>              |
| <dl> <dt>23 (0x17)</dt> </dl> | DC/OS<br/>            |
| <dl> <dt>24 (0x18)</dt> </dl> | Reliant UNIX<br/>     |
| <dl> <dt>25 (0x19)</dt> </dl> | SCO UnixWare<br/>     |
| <dl> <dt>26 (0x1A)</dt> </dl> | SCO OpenServer<br/>   |
| <dl> <dt>27 (0x1B)</dt> </dl> | Sequent<br/>          |
| <dl> <dt>28 (0x1C)</dt> </dl> | IRIX<br/>             |
| <dl> <dt>29 (0x1D)</dt> </dl> | Solaris<br/>          |
| <dl> <dt>30 (0x1E)</dt> </dl> | SunOS<br/>            |
| <dl> <dt>31 (0x1F)</dt> </dl> | U6000<br/>            |
| <dl> <dt>32 (0x20)</dt> </dl> | ASERIES<br/>          |
| <dl> <dt>33 (0x21)</dt> </dl> | TandemNSK<br/>        |
| <dl> <dt>34 (0x22)</dt> </dl> | TandemNT<br/>         |
| <dl> <dt>35 (0x23)</dt> </dl> | BS2000<br/>           |
| <dl> <dt>36 (0x24)</dt> </dl> | LINUX<br/>            |
| <dl> <dt>37 (0x25)</dt> </dl> | Lynx<br/>             |
| <dl> <dt>38 (0x26)</dt> </dl> | XENIX<br/>            |
| <dl> <dt>39 (0x27)</dt> </dl> | VM/ESA<br/>           |
| <dl> <dt>40 (0x28)</dt> </dl> | Interactive UNIX<br/> |
| <dl> <dt>41 (0x29)</dt> </dl> | BSDUNIX<br/>          |
| <dl> <dt>42 (0x2A)</dt> </dl> | FreeBSD<br/>          |
| <dl> <dt>43 (0x2B)</dt> </dl> | NetBSD<br/>           |
| <dl> <dt>44 (0x2C)</dt> </dl> | GNU Hurd<br/>         |
| <dl> <dt>45 (0x2D)</dt> </dl> | OS9<br/>              |
| <dl> <dt>46 (0x2E)</dt> </dl> | MACH Kernel<br/>      |
| <dl> <dt>47 (0x2F)</dt> </dl> | Inferno<br/>          |
| <dl> <dt>48 (0x30)</dt> </dl> | QNX<br/>              |
| <dl> <dt>49 (0x31)</dt> </dl> | EPOC<br/>             |
| <dl> <dt>50 (0x32)</dt> </dl> | IxWorks<br/>          |
| <dl> <dt>51 (0x33)</dt> </dl> | VxWorks<br/>          |
| <dl> <dt>52 (0x34)</dt> </dl> | MiNT<br/>             |
| <dl> <dt>53 (0x35)</dt> </dl> | BeOS<br/>             |
| <dl> <dt>54 (0x36)</dt> </dl> | HP MPE<br/>           |
| <dl> <dt>55 (0x37)</dt> </dl> | NextStep<br/>         |
| <dl> <dt>56 (0x38)</dt> </dl> | PalmPilot<br/>        |
| <dl> <dt>57 (0x39)</dt> </dl> | Rhapsody<br/>         |



 

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Value to be written.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of a software element. Values should be in the form \[Major\].\[Minor\].\[Revision\] or \[Major\].\[Minor\]\[letter\]\[revision\].

</dd> </dl>

## Remarks

The **Win32\_IniFileSpecification** class is derived from [**CIM\_FileSpecification**](https://msdn.microsoft.com/library/aa387271).

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

 

 





