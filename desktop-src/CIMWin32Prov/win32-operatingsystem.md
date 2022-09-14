---
description: Represents a Windows-based operating system installed on a computer.
ms.assetid: eb6a8cff-20a0-4211-b46a-3084e9c39246
ms.tgt_platform: multiple
title: Win32_OperatingSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_OperatingSystem
- Win32_OperatingSystem.BootDevice
- Win32_OperatingSystem.BuildNumber
- Win32_OperatingSystem.BuildType
- Win32_OperatingSystem.Caption
- Win32_OperatingSystem.CodeSet
- Win32_OperatingSystem.CountryCode
- Win32_OperatingSystem.CreationClassName
- Win32_OperatingSystem.CSCreationClassName
- Win32_OperatingSystem.CSDVersion
- Win32_OperatingSystem.CSName
- Win32_OperatingSystem.CurrentTimeZone
- Win32_OperatingSystem.DataExecutionPrevention_Available
- Win32_OperatingSystem.DataExecutionPrevention_32BitApplications
- Win32_OperatingSystem.DataExecutionPrevention_Drivers
- Win32_OperatingSystem.DataExecutionPrevention_SupportPolicy
- Win32_OperatingSystem.Debug
- Win32_OperatingSystem.Description
- Win32_OperatingSystem.Distributed
- Win32_OperatingSystem.EncryptionLevel
- Win32_OperatingSystem.ForegroundApplicationBoost
- Win32_OperatingSystem.FreePhysicalMemory
- Win32_OperatingSystem.FreeSpaceInPagingFiles
- Win32_OperatingSystem.FreeVirtualMemory
- Win32_OperatingSystem.InstallDate
- Win32_OperatingSystem.LargeSystemCache
- Win32_OperatingSystem.LastBootUpTime
- Win32_OperatingSystem.LocalDateTime
- Win32_OperatingSystem.Locale
- Win32_OperatingSystem.Manufacturer
- Win32_OperatingSystem.MaxNumberOfProcesses
- Win32_OperatingSystem.MaxProcessMemorySize
- Win32_OperatingSystem.MUILanguages
- Win32_OperatingSystem.Name
- Win32_OperatingSystem.NumberOfLicensedUsers
- Win32_OperatingSystem.NumberOfProcesses
- Win32_OperatingSystem.NumberOfUsers
- Win32_OperatingSystem.OperatingSystemSKU
- Win32_OperatingSystem.Organization
- Win32_OperatingSystem.OSArchitecture
- Win32_OperatingSystem.OSLanguage
- Win32_OperatingSystem.OSProductSuite
- Win32_OperatingSystem.OSType
- Win32_OperatingSystem.OtherTypeDescription
- Win32_OperatingSystem.PAEEnabled
- Win32_OperatingSystem.PlusProductID
- Win32_OperatingSystem.PlusVersionNumber
- Win32_OperatingSystem.PortableOperatingSystem
- Win32_OperatingSystem.Primary
- Win32_OperatingSystem.ProductType
- Win32_OperatingSystem.RegisteredUser
- Win32_OperatingSystem.SerialNumber
- Win32_OperatingSystem.ServicePackMajorVersion
- Win32_OperatingSystem.ServicePackMinorVersion
- Win32_OperatingSystem.SizeStoredInPagingFiles
- Win32_OperatingSystem.Status
- Win32_OperatingSystem.SuiteMask
- Win32_OperatingSystem.SystemDevice
- Win32_OperatingSystem.SystemDirectory
- Win32_OperatingSystem.SystemDrive
- Win32_OperatingSystem.TotalSwapSpaceSize
- Win32_OperatingSystem.TotalVirtualMemorySize
- Win32_OperatingSystem.TotalVisibleMemorySize
- Win32_OperatingSystem.Version
- Win32_OperatingSystem.WindowsDirectory
- Win32_OperatingSystem.QuantumLength
- Win32_OperatingSystem.QuantumType
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_OperatingSystem class

The **Win32\_OperatingSystem** [WMI class](../wmisdk/retrieving-a-class.md) represents a Windows-based operating system installed on a computer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Singleton, Dynamic, Provider("CIMWin32"), SupportsUpdate, UUID("{8502C4DE-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_OperatingSystem : CIM_OperatingSystem
{
  string   BootDevice;
  string   BuildNumber;
  string   BuildType;
  string   Caption;
  string   CodeSet;
  string   CountryCode;
  string   CreationClassName;
  string   CSCreationClassName;
  string   CSDVersion;
  string   CSName;
  sint16   CurrentTimeZone;
  boolean  DataExecutionPrevention_Available;
  boolean  DataExecutionPrevention_32BitApplications;
  boolean  DataExecutionPrevention_Drivers;
  uint8    DataExecutionPrevention_SupportPolicy;
  boolean  Debug;
  string   Description;
  boolean  Distributed;
  uint32   EncryptionLevel;
  uint8    ForegroundApplicationBoost = 2;
  uint64   FreePhysicalMemory;
  uint64   FreeSpaceInPagingFiles;
  uint64   FreeVirtualMemory;
  datetime InstallDate;
  uint32   LargeSystemCache;
  datetime LastBootUpTime;
  datetime LocalDateTime;
  string   Locale;
  string   Manufacturer;
  uint32   MaxNumberOfProcesses;
  uint64   MaxProcessMemorySize;
  string   MUILanguages[];
  string   Name;
  uint32   NumberOfLicensedUsers;
  uint32   NumberOfProcesses;
  uint32   NumberOfUsers;
  uint32   OperatingSystemSKU;
  string   Organization;
  string   OSArchitecture;
  uint32   OSLanguage;
  uint32   OSProductSuite;
  uint16   OSType;
  string   OtherTypeDescription;
  Boolean  PAEEnabled;
  string   PlusProductID;
  string   PlusVersionNumber;
  boolean  PortableOperatingSystem;
  boolean  Primary;
  uint32   ProductType;
  string   RegisteredUser;
  string   SerialNumber;
  uint16   ServicePackMajorVersion;
  uint16   ServicePackMinorVersion;
  uint64   SizeStoredInPagingFiles;
  string   Status;
  uint32   SuiteMask;
  string   SystemDevice;
  string   SystemDirectory;
  string   SystemDrive;
  uint64   TotalSwapSpaceSize;
  uint64   TotalVirtualMemorySize;
  uint64   TotalVisibleMemorySize;
  string   Version;
  string   WindowsDirectory;
  uint8    QuantumLength;
  uint8    QuantumType;
};
```

## Members

The **Win32\_OperatingSystem** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_OperatingSystem** class has these methods.



| Method                                                                                     | Description                                                                                                                                                                                                                                                            |
|:-------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Reboot**](reboot-method-in-class-win32-operatingsystem.md)                             | Shuts down and then restarts the computer system.<br/>                                                                                                                                                                                                           |
| [**SetDateTime**](setdatetime-method-in-class-win32-operatingsystem.md)                   | Allows the computer date and time to be set.<br/>                                                                                                                                                                                                                |
| [**Shutdown**](shutdown-method-in-class-win32-operatingsystem.md)                         | Unloads programs and DLLs to the point where it is safe to turn off the computer.<br/>                                                                                                                                                                           |
| [**Win32Shutdown**](win32shutdown-method-in-class-win32-operatingsystem.md)               | Provides the full set of shutdown options supported by Windows operating systems.<br/>                                                                                                                                                                           |
| [**Win32ShutdownTracker**](win32shutdowntracker-method-in-class-win32-operatingsystem.md) | Provides the same set of shutdown options supported by the [**Win32Shutdown**](win32shutdown-method-in-class-win32-operatingsystem.md) method in **Win32\_OperatingSystem**, but also allows you to specify comments, a reason for shutdown, or a timeout.<br/> |



 

### Properties

The **Win32\_OperatingSystem** class has these properties.

<dl> <dt>

**BootDevice**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|DRIVE\_MAP\_INFO\|btInt13Unit")
</dt> </dl>

Name of the disk drive from which the Windows operating system starts.

Example: "\\\\Device\\Harddisk0"

</dd> <dt>

**BuildNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|System Information Structures\|[**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa)\|dwBuildNumber")
</dt> </dl>

Build number of an operating system. It can be used for more precise version information than product release version numbers.

Example: "1381"

</dd> <dt>

**BuildType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\|CurrentType")
</dt> </dl>

Type of build used for an operating system.

Examples: ""retail build"", ""checked build""

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

Short description of the object—a one-line string. The string includes the operating system version. For example, "Microsoft Windows 7 Enterprise ". This property can be localized.

**Windows Vista and Windows 7:** This property may contain trailing characters. For example, the string "Microsoft Windows 7 Enterprise " (trailing space included) may be necessary to retrieve information using this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CodeSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (6), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|National Language Support Functions\|[**GetLocaleInfo**](/windows/win32/api/winnls/nf-winnls-getlocaleinfoa)\|LOCALE\_IDEFAULTANSICODEPAGE")
</dt> </dl>

Code page value an operating system uses. A code page contains a character table that an operating system uses to translate strings for different languages. The American National Standards Institute (ANSI) lists values that represent defined code pages. If an operating system does not use an ANSI code page, this member is set to 0 (zero). The **CodeSet** string can use a maximum of six characters to define the code page value.

Example: "1255"

</dd> <dt>

**CountryCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|National Language Support Functions\|[**GetLocaleInfo**](/windows/win32/api/winnls/nf-winnls-getlocaleinfoa)\|LOCALE\_ICOUNTRY")
</dt> </dl>

Code for the country/region that an operating system uses. Values are based on international phone dialing prefixes—also referred to as IBM country/region codes. This property can use a maximum of six characters to define the country/region code value.

Example: "1" (United States)

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the first concrete class that appears in the inheritance chain used in the creation of an instance. When used with other key properties of the class, this property allows all instances of this class and its subclasses to be identified uniquely.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**CreationClassName**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Creation class name of the scoping computer system.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**CSDVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|System Information Structures\|[**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa)\|**szCSDVersion**")
</dt> </dl>

**NULL**-terminated string that indicates the latest service pack installed on a computer. If no service pack is installed, the string is **NULL**.

Example: "Service Pack 3"

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**Name**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the scoping computer system.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**CurrentTimeZone**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("minutes")
</dt> </dl>

Number, in minutes, an operating system is offset from Greenwich mean time (GMT). The number is positive, negative, or zero.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**DataExecutionPrevention\_32BitApplications**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

When the data execution prevention hardware feature is available, this property indicates that the feature is set to work for 32-bit applications if **True**. On 64-bit computers, the data execution prevention feature is configured in the [Boot Configuration Data (BCD)](/previous-versions/windows/desktop/bcd/boot-configuration-data-portal) store and the properties in **Win32\_OperatingSystem** are set accordingly.

</dd> <dt>

**DataExecutionPrevention\_Available**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Data execution prevention is a hardware feature to prevent buffer overrun attacks by stopping the execution of code on data-type memory pages. If **True**, then this feature is available. On 64-bit computers, the data execution prevention feature is configured in the BCD store and the properties in **Win32\_OperatingSystem** are set accordingly.

</dd> <dt>

**DataExecutionPrevention\_Drivers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

When the data execution prevention hardware feature is available, this property indicates that the feature is set to work for drivers if **True**. On 64-bit computers, the data execution prevention feature is configured in the BCD store and the properties in **Win32\_OperatingSystem** are set accordingly.

</dd> <dt>

**DataExecutionPrevention\_SupportPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Indicates which Data Execution Prevention (DEP) setting is applied. The DEP setting specifies the extent to which DEP applies to 32-bit applications on the system. DEP is always applied to the Windows kernel.

<dt>

<span id="Always_Off"></span><span id="always_off"></span><span id="ALWAYS_OFF"></span>

<span id="Always_Off"></span><span id="always_off"></span><span id="ALWAYS_OFF"></span>**Always Off** (0)


</dt> <dd>

DEP is turned off for all 32-bit applications on the computer with no exceptions. This setting is not available for the user interface.

</dd> <dt>

<span id="Always_On"></span><span id="always_on"></span><span id="ALWAYS_ON"></span>

<span id="Always_On"></span><span id="always_on"></span><span id="ALWAYS_ON"></span>**Always On** (1)


</dt> <dd>

DEP is enabled for all 32-bit applications on the computer. This setting is not available for the user interface.

</dd> <dt>

<span id="Opt_In"></span><span id="opt_in"></span><span id="OPT_IN"></span>

<span id="Opt_In"></span><span id="opt_in"></span><span id="OPT_IN"></span>**Opt In** (2)


</dt> <dd>

DEP is enabled for a limited number of binaries, the kernel, and all Windows-based services. However, it is off by default for all 32-bit applications. A user or administrator must explicitly choose either the **Always On** or the **Opt Out** setting before DEP can be applied to 32-bit applications.

</dd> <dt>

<span id="Opt_Out"></span><span id="opt_out"></span><span id="OPT_OUT"></span>

<span id="Opt_Out"></span><span id="opt_out"></span><span id="OPT_OUT"></span>**Opt Out** (3)


</dt> <dd>

DEP is enabled by default for all 32-bit applications. A user or administrator can explicitly remove support for a 32-bit application by adding the application to an exceptions list.

</dd> </dl>

</dd> <dt>

**Debug**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|[**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics)\|SM\_DEBUG")
</dt> </dl>

Operating system is a checked (debug) build. If **True**, the debugging version is installed. Checked builds provide error checking, argument verification, and system debugging code. Additional code in a checked binary generates a kernel debugger error message and breaks into the debugger. This helps immediately determine the cause and location of the error. Performance may be affected in a checked build due to the additional code that is executed.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Description"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Description of the Windows operating system. Some user interfaces for example, those that allow editing of this description, limit its length to 48 characters.

</dd> <dt>

**Distributed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the operating system is distributed across several computer system nodes. If so, these nodes should be grouped as a cluster.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**EncryptionLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Encryption level for secure transactions: 40-bit, 128-bit, or *n*-bit.

<dt>

<span id="40-bit"></span><span id="40-BIT"></span>

**40-bit** (0)


</dt> <dd></dd> <dt>

<span id="128-bit"></span><span id="128-BIT"></span>

**128-bit** (1)


</dt> <dd></dd> <dt>

<span id="n-bit"></span><span id="N-BIT"></span>

**n-bit** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ForegroundApplicationBoost**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\PriorityControl\|Win32PrioritySeparation")
</dt> </dl>

Increase in priority is given to the foreground application. Application boost is implemented by giving an application more execution time slices (quantum lengths).

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

The system boosts the quantum length by 6.

</dd> <dt>

<span id="Minimum"></span><span id="minimum"></span><span id="MINIMUM"></span>

<span id="Minimum"></span><span id="minimum"></span><span id="MINIMUM"></span>**Minimum** (1)


</dt> <dd>

The system boosts the quantum length by 12.

</dd> <dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>**Maximum** (2)


</dt> <dd>

The system boosts the quantum length by 18.

</dd> </dl>

</dd> <dt>

**FreePhysicalMemory**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Number, in kilobytes, of physical memory currently unused and available.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**FreeSpaceInPagingFiles**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|System Memory Settings\|001.4"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Number, in kilobytes, that can be mapped into the operating system paging files without causing any other pages to be swapped out.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**FreeVirtualMemory**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Number, in kilobytes, of virtual memory currently unused and available.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Date object was installed. This property does not require a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**LargeSystemCache**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

This property is obsolete and not supported.

<dt>

<span id="Optimize_for_Applications"></span><span id="optimize_for_applications"></span><span id="OPTIMIZE_FOR_APPLICATIONS"></span>

<span id="Optimize_for_Applications"></span><span id="optimize_for_applications"></span><span id="OPTIMIZE_FOR_APPLICATIONS"></span>**Optimize for Applications** (0)


</dt> <dd>

Optimize memory for applications.

</dd> <dt>

<span id="Optimize_for_System_Performance"></span><span id="optimize_for_system_performance"></span><span id="OPTIMIZE_FOR_SYSTEM_PERFORMANCE"></span>

<span id="Optimize_for_System_Performance"></span><span id="optimize_for_system_performance"></span><span id="OPTIMIZE_FOR_SYSTEM_PERFORMANCE"></span>**Optimize for System Performance** (1)


</dt> <dd>

Optimize memory for system performance.

</dd> </dl>

</dd> <dt>

**LastBootUpTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the operating system was last restarted.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**LocalDateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIB.IETF\|HOST-RESOURCES-MIB.hrSystemDate", "MIF.DMTF\|General Information\|001.6")
</dt> </dl>

Operating system version of the local date and time-of-day.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**Locale**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|National Language Support Functions\|[**GetLocaleInfo**](/windows/win32/api/winnls/nf-winnls-getlocaleinfoa)\|LOCALE\_ILANGUAGE")
</dt> </dl>

Language identifier used by the operating system. A language identifier is a standard international numeric abbreviation for a country/region. Each language has a unique language identifier (LANGID), a 16-bit value that consists of a primary language identifier and a secondary language identifier.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Name of the operating system manufacturer. For Windows-based systems, this value is "Microsoft Corporation".

</dd> <dt>

**MaxNumberOfProcesses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIB.IETF\|HOST-RESOURCES-MIB.hrSystemMaxProcesses")
</dt> </dl>

Maximum number of process contexts the operating system can support. The default value set by the provider is 4294967295 (0xFFFFFFFF). If there is no fixed maximum, the value should be 0 (zero). On systems that have a fixed maximum, this object can help diagnose failures that occur when the maximum is reached—if unknown, enter 4294967295 (0xFFFFFFFF).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**MaxProcessMemorySize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Maximum number, in kilobytes, of memory that can be allocated to a process. For operating systems with no virtual memory, typically this value is equal to the total amount of physical memory minus the memory used by the BIOS and the operating system. For some operating systems, this value may be infinity, in which case 0 (zero) should be entered. In other cases, this value could be a constant, for example, 2G or 4G.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**MUILanguages**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Multilingual User Interface Pack (MUI Pack ) languages installed on the computer. For example, "en-us". MUI Pack languages are resource files that can be installed on the English version of the operating system. When an MUI Pack is installed, you can can change the user interface language to one of 33 supported languages.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Operating system instance within a computer system.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**NumberOfLicensedUsers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of user licenses for the operating system. If unlimited, enter 0 (zero). If unknown, enter -1.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**NumberOfProcesses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIB.IETF\|HOST-RESOURCES-MIB.hrSystemProcesses")
</dt> </dl>

Number of process contexts currently loaded or running on the operating system.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**NumberOfUsers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIB.IETF\|HOST-RESOURCES-MIB.hrSystemNumUsers")
</dt> </dl>

Number of user sessions for which the operating system is storing state information currently.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**OperatingSystemSKU**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Stock Keeping Unit (SKU) number for the operating system. These values are the same as the **PRODUCT\_\*** constants defined in WinNT.h that are used with the [**GetProductInfo**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo) function.

The following list lists possible SKU values.

<dt>

<span id="PRODUCT_UNDEFINED"></span><span id="product_undefined"></span>

<span id="PRODUCT_UNDEFINED"></span><span id="product_undefined"></span>**PRODUCT\_UNDEFINED** (0)


</dt> <dd>

Undefined

</dd> <dt>

<span id="PRODUCT_ULTIMATE"></span><span id="product_ultimate"></span>

<span id="PRODUCT_ULTIMATE"></span><span id="product_ultimate"></span>**PRODUCT\_ULTIMATE** (1)


</dt> <dd>

Ultimate Edition, e.g. Windows Vista Ultimate.

</dd> <dt>

<span id="PRODUCT_HOME_BASIC"></span><span id="product_home_basic"></span>

<span id="PRODUCT_HOME_BASIC"></span><span id="product_home_basic"></span>**PRODUCT\_HOME\_BASIC** (2)


</dt> <dd>

Home Basic Edition

</dd> <dt>

<span id="PRODUCT_HOME_PREMIUM"></span><span id="product_home_premium"></span>

<span id="PRODUCT_HOME_PREMIUM"></span><span id="product_home_premium"></span>**PRODUCT\_HOME\_PREMIUM** (3)


</dt> <dd>

Home Premium Edition

</dd> <dt>

<span id="PRODUCT_ENTERPRISE"></span><span id="product_enterprise"></span>

<span id="PRODUCT_ENTERPRISE"></span><span id="product_enterprise"></span>**PRODUCT\_ENTERPRISE** (4)


</dt> <dd>

Enterprise Edition

</dd> <dt>

<span id="PRODUCT_BUSINESS"></span><span id="product_business"></span>

<span id="PRODUCT_BUSINESS"></span><span id="product_business"></span>**PRODUCT\_BUSINESS** (6)


</dt> <dd>

Business Edition

</dd> <dt>

<span id="PRODUCT_STANDARD_SERVER"></span><span id="product_standard_server"></span>

<span id="PRODUCT_STANDARD_SERVER"></span><span id="product_standard_server"></span>**PRODUCT\_STANDARD\_SERVER** (7)


</dt> <dd>

Windows Server Standard Edition (Desktop Experience installation)

</dd> <dt>

<span id="PRODUCT_DATACENTER_SERVER"></span><span id="product_datacenter_server"></span>

<span id="PRODUCT_DATACENTER_SERVER"></span><span id="product_datacenter_server"></span>**PRODUCT\_DATACENTER\_SERVER** (8)


</dt> <dd>

Windows Server Datacenter Edition (Desktop Experience installation)

</dd> <dt>

<span id="PRODUCT_SMALLBUSINESS_SERVER"></span><span id="product_smallbusiness_server"></span>

<span id="PRODUCT_SMALLBUSINESS_SERVER"></span><span id="product_smallbusiness_server"></span>**PRODUCT\_SMALLBUSINESS\_SERVER** (9)


</dt> <dd>

Small Business Server Edition

</dd> <dt>

<span id="PRODUCT_ENTERPRISE_SERVER"></span><span id="product_enterprise_server"></span>

<span id="PRODUCT_ENTERPRISE_SERVER"></span><span id="product_enterprise_server"></span>**PRODUCT\_ENTERPRISE\_SERVER** (10)


</dt> <dd>

Enterprise Server Edition

</dd> <dt>

<span id="PRODUCT_STARTER"></span><span id="product_starter"></span>

<span id="PRODUCT_STARTER"></span><span id="product_starter"></span>**PRODUCT\_STARTER** (11)


</dt> <dd>

Starter Edition

</dd> <dt>

<span id="PRODUCT_DATACENTER_SERVER_CORE"></span><span id="product_datacenter_server_core"></span>

<span id="PRODUCT_DATACENTER_SERVER_CORE"></span><span id="product_datacenter_server_core"></span>**PRODUCT\_DATACENTER\_SERVER\_CORE** (12)


</dt> <dd>

Datacenter Server Core Edition

</dd> <dt>

<span id="PRODUCT_STANDARD_SERVER_CORE"></span><span id="product_standard_server_core"></span>

<span id="PRODUCT_STANDARD_SERVER_CORE"></span><span id="product_standard_server_core"></span>**PRODUCT\_STANDARD\_SERVER\_CORE** (13)


</dt> <dd>

Standard Server Core Edition

</dd> <dt>

<span id="PRODUCT_ENTERPRISE_SERVER_CORE"></span><span id="product_enterprise_server_core"></span>

<span id="PRODUCT_ENTERPRISE_SERVER_CORE"></span><span id="product_enterprise_server_core"></span>**PRODUCT\_ENTERPRISE\_SERVER\_CORE** (14)


</dt> <dd>

Enterprise Server Core Edition

</dd> <dt>

<span id="PRODUCT_WEB_SERVER"></span><span id="product_web_server"></span>

<span id="PRODUCT_WEB_SERVER"></span><span id="product_web_server"></span>**PRODUCT\_WEB\_SERVER** (17)


</dt> <dd>

Web Server Edition

</dd> <dt>

<span id="PRODUCT_HOME_SERVER"></span><span id="product_home_server"></span>

<span id="PRODUCT_HOME_SERVER"></span><span id="product_home_server"></span>**PRODUCT\_HOME\_SERVER** (19)


</dt> <dd>

Home Server Edition

</dd> <dt>

<span id="PRODUCT_STORAGE_EXPRESS_SERVER"></span><span id="product_storage_express_server"></span>

<span id="PRODUCT_STORAGE_EXPRESS_SERVER"></span><span id="product_storage_express_server"></span>**PRODUCT\_STORAGE\_EXPRESS\_SERVER** (20)


</dt> <dd>

Storage Express Server Edition

</dd> <dt>

<span id="PRODUCT_STORAGE_STANDARD_SERVER"></span><span id="product_storage_standard_server"></span>

<span id="PRODUCT_STORAGE_STANDARD_SERVER"></span><span id="product_storage_standard_server"></span>**PRODUCT\_STORAGE\_STANDARD\_SERVER** (21)


</dt> <dd>

Windows Storage Server Standard Edition (Desktop Experience installation)

</dd> <dt>

<span id="PRODUCT_STORAGE_WORKGROUP_SERVER"></span><span id="product_storage_workgroup_server"></span>

<span id="PRODUCT_STORAGE_WORKGROUP_SERVER"></span><span id="product_storage_workgroup_server"></span>**PRODUCT\_STORAGE\_WORKGROUP\_SERVER** (22)


</dt> <dd>

Windows Storage Server Workgroup Edition (Desktop Experience installation)

</dd> <dt>

<span id="PRODUCT_STORAGE_ENTERPRISE_SERVER"></span><span id="product_storage_enterprise_server"></span>

<span id="PRODUCT_STORAGE_ENTERPRISE_SERVER"></span><span id="product_storage_enterprise_server"></span>**PRODUCT\_STORAGE\_ENTERPRISE\_SERVER** (23)


</dt> <dd>

Storage Enterprise Server Edition

</dd> <dt>

<span id="PRODUCT_SERVER_FOR_SMALLBUSINESS"></span><span id="product_server_for_smallbusiness"></span>

<span id="PRODUCT_SERVER_FOR_SMALLBUSINESS"></span><span id="product_server_for_smallbusiness"></span>**PRODUCT\_SERVER\_FOR\_SMALLBUSINESS** (24)


</dt> <dd>

Server For Small Business Edition

</dd> <dt>

<span id="PRODUCT_SMALLBUSINESS_SERVER_PREMIUM"></span><span id="product_smallbusiness_server_premium"></span>

<span id="PRODUCT_SMALLBUSINESS_SERVER_PREMIUM"></span><span id="product_smallbusiness_server_premium"></span>**PRODUCT\_SMALLBUSINESS\_SERVER\_PREMIUM** (25)


</dt> <dd>

Small Business Server Premium Edition

</dd> <dt>

<span id="PRODUCT_ENTERPRISE_N"></span><span id="product_enterprise_n"></span>

<span id="PRODUCT_ENTERPRISE_N"></span><span id="product_enterprise_n"></span>**PRODUCT\_ENTERPRISE\_N** (27)


</dt> <dd>

Windows Enterprise Edition

</dd> <dt>

<span id="PRODUCT_ULTIMATE_N"></span><span id="product_ultimate_n"></span>

<span id="PRODUCT_ULTIMATE_N"></span><span id="product_ultimate_n"></span>**PRODUCT\_ULTIMATE\_N** (28)


</dt> <dd>

Windows Ultimate Edition

</dd> <dt>

<span id="PRODUCT_WEB_SERVER_CORE"></span><span id="product_web_server_core"></span>

<span id="PRODUCT_WEB_SERVER_CORE"></span><span id="product_web_server_core"></span>**PRODUCT\_WEB\_SERVER\_CORE** (29)


</dt> <dd>

Windows Server Web Server Edition (Server Core installation)

</dd> <dt>

<span id="PRODUCT_STANDARD_SERVER_V"></span><span id="product_standard_server_v"></span>

<span id="PRODUCT_STANDARD_SERVER_V"></span><span id="product_standard_server_v"></span>**PRODUCT\_STANDARD\_SERVER\_V** (36)


</dt> <dd>

Windows Server Standard Edition without Hyper-V

</dd> <dt>

<span id="PRODUCT_DATACENTER_SERVER_V"></span><span id="product_datacenter_server_v"></span>

<span id="PRODUCT_DATACENTER_SERVER_V"></span><span id="product_datacenter_server_v"></span>**PRODUCT\_DATACENTER\_SERVER\_V** (37)


</dt> <dd>

Windows Server Datacenter Edition without Hyper-V (full installation)

</dd> <dt>

<span id="PRODUCT_ENTERPRISE_SERVER_V"></span><span id="product_enterprise_server_v"></span>

<span id="PRODUCT_ENTERPRISE_SERVER_V"></span><span id="product_enterprise_server_v"></span>**PRODUCT\_ENTERPRISE\_SERVER\_V** (38)


</dt> <dd>

Windows Server Enterprise Edition without Hyper-V (full installation)

</dd> <dt>

<span id="PRODUCT_DATACENTER_SERVER_CORE_V"></span><span id="product_datacenter_server_core_v"></span>

<span id="PRODUCT_DATACENTER_SERVER_CORE_V"></span><span id="product_datacenter_server_core_v"></span>**PRODUCT\_DATACENTER\_SERVER\_CORE\_V** (39)


</dt> <dd>

Windows Server Datacenter Edition without Hyper-V (Server Core installation)

</dd> <dt>

<span id="PRODUCT_STANDARD_SERVER_CORE_V"></span><span id="product_standard_server_core_v"></span>

<span id="PRODUCT_STANDARD_SERVER_CORE_V"></span><span id="product_standard_server_core_v"></span>**PRODUCT\_STANDARD\_SERVER\_CORE\_V** (40)


</dt> <dd>

Windows Server Standard Edition without Hyper-V (Server Core installation)

</dd> <dt>

<span id="PRODUCT_ENTERPRISE_SERVER_CORE_V"></span><span id="product_enterprise_server_core_v"></span>

<span id="PRODUCT_ENTERPRISE_SERVER_CORE_V"></span><span id="product_enterprise_server_core_v"></span>**PRODUCT\_ENTERPRISE\_SERVER\_CORE\_V** (41)


</dt> <dd>

Windows Server Enterprise Edition without Hyper-V (Server Core installation)

</dd> <dt>

<span id="PRODUCT_HYPERV"></span><span id="product_hyperv"></span>

<span id="PRODUCT_HYPERV"></span><span id="product_hyperv"></span>**PRODUCT\_HYPERV** (42)


</dt> <dd>

Microsoft Hyper-V Server

</dd> <dt>

<span id="PRODUCT_STORAGE_EXPRESS_SERVER_CORE"></span><span id="product_storage_express_server_core"></span>

<span id="PRODUCT_STORAGE_EXPRESS_SERVER_CORE"></span><span id="product_storage_express_server_core"></span>**PRODUCT\_STORAGE\_EXPRESS\_SERVER\_CORE** (43)


</dt> <dd>

Storage Server Express Edition (Server Core installation)

</dd> <dt>

<span id="PRODUCT_STORAGE_STANDARD_SERVER_CORE"></span><span id="product_storage_standard_server_core"></span>

<span id="PRODUCT_STORAGE_STANDARD_SERVER_CORE"></span><span id="product_storage_standard_server_core"></span>**PRODUCT\_STORAGE\_STANDARD\_SERVER\_CORE** (44)


</dt> <dd>

Storage Server Standard Edition (Server Core installation)

</dd> <dt>

<span id="PRODUCT_STORAGE_WORKGROUP_SERVER_CORE"></span><span id="product_storage_workgroup_server_core"></span>

<span id="PRODUCT_STORAGE_WORKGROUP_SERVER_CORE"></span><span id="product_storage_workgroup_server_core"></span>**PRODUCT\_STORAGE\_WORKGROUP\_SERVER\_CORE** (45)


</dt> <dd>

Storage Server Workgroup Edition (Server Core installation)

</dd> <dt>

<span id="PRODUCT_STORAGE_ENTERPRISE_SERVER_CORE"></span><span id="product_storage_enterprise_server_core"></span>

<span id="PRODUCT_STORAGE_ENTERPRISE_SERVER_CORE"></span><span id="product_storage_enterprise_server_core"></span>**PRODUCT\_STORAGE\_ENTERPRISE\_SERVER\_CORE** (46)


</dt> <dd>

Storage Server Workgroup Edition (Server Core installation)

</dd> <dt>

<span id="PRODUCT_PROFESSIONAL"></span><span id="product_professional"></span>

<span id="PRODUCT_PROFESSIONAL"></span><span id="product_professional"></span>**PRODUCT\_PROFESSIONAL** (48)


</dt> <dd>

Windows Professional

</dd> <dt>

<span id="PRODUCT_SB_SOLUTION_SERVER"></span><span id="product_sb_solution_server"></span>

<span id="PRODUCT_SB_SOLUTION_SERVER"></span><span id="product_sb_solution_server"></span>**PRODUCT\_SB\_SOLUTION\_SERVER** (50)


</dt> <dd>

Windows Server Essentials (Desktop Experience installation)

</dd> <dt>

<span id="PRODUCT_SMALLBUSINESS_SERVER_PREMIUM_CORE"></span><span id="product_smallbusiness_server_premium_core"></span>

<span id="PRODUCT_SMALLBUSINESS_SERVER_PREMIUM_CORE"></span><span id="product_smallbusiness_server_premium_core"></span>**PRODUCT\_SMALLBUSINESS\_SERVER\_PREMIUM\_CORE** (63)


</dt> <dd>

Small Business Server Premium (Server Core installation)

</dd> <dt>

<span id="PRODUCT_CLUSTER_SERVER_V"></span><span id="product_cluster_server_v"></span>

<span id="PRODUCT_CLUSTER_SERVER_V"></span><span id="product_cluster_server_v"></span>**PRODUCT\_CLUSTER\_SERVER\_V** (64)


</dt> <dd>

Windows Compute Cluster Server without Hyper-V

</dd> <dt>

<span id="PRODUCT_CORE_ARM"></span><span id="product_core_arm"></span>

<span id="PRODUCT_CORE_ARM"></span><span id="product_core_arm"></span>**PRODUCT\_CORE\_ARM** (97)


</dt> <dd>

Windows RT

</dd> <dt>

<span id="PRODUCT_CORE"></span><span id="product_core"></span>

<span id="PRODUCT_CORE"></span><span id="product_core"></span>**PRODUCT\_CORE** (101)


</dt> <dd>

Windows Home

</dd> <dt>

<span id="PRODUCT_PROFESSIONAL_WMC"></span><span id="product_professional_wmc"></span>

<span id="PRODUCT_PROFESSIONAL_WMC"></span><span id="product_professional_wmc"></span>**PRODUCT\_PROFESSIONAL\_WMC** (103)


</dt> <dd>

Windows Professional with Media Center

</dd> <dt>

<span id="PRODUCT_MOBILE_CORE"></span><span id="product_mobile_core"></span>

<span id="PRODUCT_MOBILE_CORE"></span><span id="product_mobile_core"></span>**PRODUCT\_MOBILE\_CORE** (104)


</dt> <dd>

Windows Mobile

</dd> <dt>

<span id="PRODUCT_IOTUAP"></span><span id="product_iotuap"></span>

<span id="PRODUCT_IOTUAP"></span><span id="product_iotuap"></span>**PRODUCT\_IOTUAP** (123)


</dt> <dd>

Windows IoT (Internet of Things) Core

</dd> <dt>

<span id="PRODUCT_DATACENTER_NANO_SERVER"></span><span id="product_datacenter_nano_server"></span>

<span id="PRODUCT_DATACENTER_NANO_SERVER"></span><span id="product_datacenter_nano_server"></span>**PRODUCT\_DATACENTER\_NANO\_SERVER** (143)


</dt> <dd>

Windows Server Datacenter Edition (Nano Server installation)

</dd> <dt>

<span id="PRODUCT_STANDARD_NANO_SERVER"></span><span id="product_standard_nano_server"></span>

<span id="PRODUCT_STANDARD_NANO_SERVER"></span><span id="product_standard_nano_server"></span>**PRODUCT\_STANDARD\_NANO\_SERVER** (144)


</dt> <dd>

Windows Server Standard Edition (Nano Server installation)

</dd> <dt>

<span id="PRODUCT_DATACENTER_WS_SERVER_CORE"></span><span id="product_datacenter_ws_server_core"></span>

<span id="PRODUCT_DATACENTER_WS_SERVER_CORE"></span><span id="product_datacenter_ws_server_core"></span>**PRODUCT\_DATACENTER\_WS\_SERVER\_CORE** (147)


</dt> <dd>

Windows Server Datacenter Edition (Server Core installation)

</dd> <dt>

<span id="PRODUCT_STANDARD_WS_SERVER_CORE"></span><span id="product_standard_ws_server_core"></span>

<span id="PRODUCT_STANDARD_WS_SERVER_CORE"></span><span id="product_standard_ws_server_core"></span>**PRODUCT\_STANDARD\_WS\_SERVER\_CORE** (148)


</dt> <dd>

Windows Server Standard Edition (Server Core installation)

</dd> </dl>

</dd> <dt>
  
<span id="PRODUCT_ENTERPRISE_FOR_VIRTUAL_DESKTOPS"></span><span id="product_enterprise_for_virtual_desktops"></span>

<span id="PRODUCT_ENTERPRISE_FOR_VIRTUAL_DESKTOPS"></span><span id="product_enterprise_for_virtual_desktops"></span>**PRODUCT\_ENTERPRISE\_FOR\_VIRTUAL\_DESKTOPS** (175)

</dt> <dd>

Windows Enterprise for Virtual Desktops (Azure Virtual Desktop)

</dd> </dl>

</dd> <dt>

**Organization**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\|RegisteredOrganization")
</dt> </dl>

Company name for the registered user of the operating system.

Example: "Microsoft Corporation"

</dd> <dt>

**OSArchitecture**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Architecture of the operating system, as opposed to the processor. This property can be localized.

Example: 32-bit

</dd> <dt>

**OSLanguage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|DEFAULT\\\\Control Panel\\\\International\|Locale")
</dt> </dl>

Language version of the operating system installed. The following list lists the possible values. Example: 0x0807 (German, Switzerland).

<dt>

1 (0x1)
</dt> <dd>

Arabic

</dd> <dt>

4 (0x4)
</dt> <dd>

Chinese (Simplified)– China

</dd> <dt>

9 (0x9)
</dt> <dd>

English

</dd> <dt>

1025 (0x401)
</dt> <dd>

Arabic – Saudi Arabia

</dd> <dt>

1026 (0x402)
</dt> <dd>

Bulgarian

</dd> <dt>

1027 (0x403)
</dt> <dd>

Catalan

</dd> <dt>

1028 (0x404)
</dt> <dd>

Chinese (Traditional) – Taiwan

</dd> <dt>

1029 (0x405)
</dt> <dd>

Czech

</dd> <dt>

1030 (0x406)
</dt> <dd>

Danish

</dd> <dt>

1031 (0x407)
</dt> <dd>

German – Germany

</dd> <dt>

1032 (0x408)
</dt> <dd>

Greek

</dd> <dt>

1033 (0x409)
</dt> <dd>

English – United States

</dd> <dt>

1034 (0x40A)
</dt> <dd>

Spanish – Traditional Sort

</dd> <dt>

1035 (0x40B)
</dt> <dd>

Finnish

</dd> <dt>

1036 (0x40C)
</dt> <dd>

French – France

</dd> <dt>

1037 (0x40D)
</dt> <dd>

Hebrew

</dd> <dt>

1038 (0x40E)
</dt> <dd>

Hungarian

</dd> <dt>

1039 (0x40F)
</dt> <dd>

Icelandic

</dd> <dt>

1040 (0x410)
</dt> <dd>

Italian – Italy

</dd> <dt>

1041 (0x411)
</dt> <dd>

Japanese

</dd> <dt>

1042 (0x412)
</dt> <dd>

Korean

</dd> <dt>

1043 (0x413)
</dt> <dd>

Dutch – Netherlands

</dd> <dt>

1044 (0x414)
</dt> <dd>

Norwegian – Bokmal

</dd> <dt>

1045 (0x415)
</dt> <dd>

Polish

</dd> <dt>

1046 (0x416)
</dt> <dd>

Portuguese – Brazil

</dd> <dt>

1047 (0x417)
</dt> <dd>

Rhaeto-Romanic

</dd> <dt>

1048 (0x418)
</dt> <dd>

Romanian

</dd> <dt>

1049 (0x419)
</dt> <dd>

Russian

</dd> <dt>

1050 (0x41A)
</dt> <dd>

Croatian

</dd> <dt>

1051 (0x41B)
</dt> <dd>

Slovak

</dd> <dt>

1052 (0x41C)
</dt> <dd>

Albanian

</dd> <dt>

1053 (0x41D)
</dt> <dd>

Swedish

</dd> <dt>

1054 (0x41E)
</dt> <dd>

Thai

</dd> <dt>

1055 (0x41F)
</dt> <dd>

Turkish

</dd> <dt>

1056 (0x420)
</dt> <dd>

Urdu

</dd> <dt>

1057 (0x421)
</dt> <dd>

Indonesian

</dd> <dt>

1058 (0x422)
</dt> <dd>

Ukrainian

</dd> <dt>

1059 (0x423)
</dt> <dd>

Belarusian

</dd> <dt>

1060 (0x424)
</dt> <dd>

Slovenian

</dd> <dt>

1061 (0x425)
</dt> <dd>

Estonian

</dd> <dt>

1062 (0x426)
</dt> <dd>

Latvian

</dd> <dt>

1063 (0x427)
</dt> <dd>

Lithuanian

</dd> <dt>

1065 (0x429)
</dt> <dd>

Persian

</dd> <dt>

1066 (0x42A)
</dt> <dd>

Vietnamese

</dd> <dt>

1069 (0x42D)
</dt> <dd>

Basque (Basque)

</dd> <dt>

1070 (0x42E)
</dt> <dd>

Serbian

</dd> <dt>

1071 (0x42F)
</dt> <dd>

Macedonian (North Macedonia)

</dd> <dt>

1072 (0x430)
</dt> <dd>

Sutu

</dd> <dt>

1073 (0x431)
</dt> <dd>

Tsonga

</dd> <dt>

1074 (0x432)
</dt> <dd>

Tswana

</dd> <dt>

1076 (0x434)
</dt> <dd>

Xhosa

</dd> <dt>

1077 (0x435)
</dt> <dd>

Zulu

</dd> <dt>

1078 (0x436)
</dt> <dd>

Afrikaans

</dd> <dt>

1080 (0x438)
</dt> <dd>

Faeroese

</dd> <dt>

1081 (0x439)
</dt> <dd>

Hindi

</dd> <dt>

1082 (0x43A)
</dt> <dd>

Maltese

</dd> <dt>

1084 (0x43C)
</dt> <dd>

Scottish Gaelic (United Kingdom)

</dd> <dt>

1085 (0x43D)
</dt> <dd>

Yiddish

</dd> <dt>

1086 (0x43E)
</dt> <dd>

Malay – Malaysia

</dd> <dt>

2049 (0x801)
</dt> <dd>

Arabic – Iraq

</dd> <dt>

2052 (0x804)
</dt> <dd>

Chinese (Simplified) – PRC

</dd> <dt>

2055 (0x807)
</dt> <dd>

German – Switzerland

</dd> <dt>

2057 (0x809)
</dt> <dd>

English – United Kingdom

</dd> <dt>

2058 (0x80A)
</dt> <dd>

Spanish – Mexico

</dd> <dt>

2060 (0x80C)
</dt> <dd>

French – Belgium

</dd> <dt>

2064 (0x810)
</dt> <dd>

Italian – Switzerland

</dd> <dt>

2067 (0x813)
</dt> <dd>

Dutch – Belgium

</dd> <dt>

2068 (0x814)
</dt> <dd>

Norwegian – Nynorsk

</dd> <dt>

2070 (0x816)
</dt> <dd>

Portuguese – Portugal

</dd> <dt>

2072 (0x818)
</dt> <dd>

Romanian – Moldova

</dd> <dt>

2073 (0x819)
</dt> <dd>

Russian – Moldova

</dd> <dt>

2074 (0x81A)
</dt> <dd>

Serbian – Latin

</dd> <dt>

2077 (0x81D)
</dt> <dd>

Swedish – Finland

</dd> <dt>

3073 (0xC01)
</dt> <dd>

Arabic – Egypt

</dd> <dt>

3076 (0xC04)
</dt> <dd>

Chinese (Traditional) – Hong Kong SAR

</dd> <dt>

3079 (0xC07)
</dt> <dd>

German – Austria

</dd> <dt>

3081 (0xC09)
</dt> <dd>

English – Australia

</dd> <dt>

3082 (0xC0A)
</dt> <dd>

Spanish – International Sort

</dd> <dt>

3084 (0xC0C)
</dt> <dd>

French – Canada

</dd> <dt>

3098 (0xC1A)
</dt> <dd>

Serbian – Cyrillic

</dd> <dt>

4097 (0x1001)
</dt> <dd>

Arabic – Libya

</dd> <dt>

4100 (0x1004)
</dt> <dd>

Chinese (Simplified) – Singapore

</dd> <dt>

4103 (0x1007)
</dt> <dd>

German – Luxembourg

</dd> <dt>

4105 (0x1009)
</dt> <dd>

English – Canada

</dd> <dt>

4106 (0x100A)
</dt> <dd>

Spanish – Guatemala

</dd> <dt>

4108 (0x100C)
</dt> <dd>

French – Switzerland

</dd> <dt>

5121 (0x1401)
</dt> <dd>

Arabic – Algeria

</dd> <dt>

5127 (0x1407)
</dt> <dd>

German – Liechtenstein

</dd> <dt>

5129 (0x1409)
</dt> <dd>

English – New Zealand

</dd> <dt>

5130 (0x140A)
</dt> <dd>

Spanish – Costa Rica

</dd> <dt>

5132 (0x140C)
</dt> <dd>

French – Luxembourg

</dd> <dt>

6145 (0x1801)
</dt> <dd>

Arabic – Morocco

</dd> <dt>

6153 (0x1809)
</dt> <dd>

English – Ireland

</dd> <dt>

6154 (0x180A)
</dt> <dd>

Spanish – Panama

</dd> <dt>

7169 (0x1C01)
</dt> <dd>

Arabic – Tunisia

</dd> <dt>

7177 (0x1C09)
</dt> <dd>

English – South Africa

</dd> <dt>

7178 (0x1C0A)
</dt> <dd>

Spanish – Dominican Republic

</dd> <dt>

8193 (0x2001)
</dt> <dd>

Arabic – Oman

</dd> <dt>

8201 (0x2009)
</dt> <dd>

English – Jamaica

</dd> <dt>

8202 (0x200A)
</dt> <dd>

Spanish – Venezuela

</dd> <dt>

9217 (0x2401)
</dt> <dd>

Arabic – Yemen

</dd> <dt>

9226 (0x240A)
</dt> <dd>

Spanish – Colombia

</dd> <dt>

10241 (0x2801)
</dt> <dd>

Arabic – Syria

</dd> <dt>

10249 (0x2809)
</dt> <dd>

English – Belize

</dd> <dt>

10250 (0x280A)
</dt> <dd>

Spanish – Peru

</dd> <dt>

11265 (0x2C01)
</dt> <dd>

Arabic – Jordan

</dd> <dt>

11273 (0x2C09)
</dt> <dd>

English – Trinidad

</dd> <dt>

11274 (0x2C0A)
</dt> <dd>

Spanish – Argentina

</dd> <dt>

12289 (0x3001)
</dt> <dd>

Arabic – Lebanon

</dd> <dt>

12298 (0x300A)
</dt> <dd>

Spanish – Ecuador

</dd> <dt>

13313 (0x3401)
</dt> <dd>

Arabic – Kuwait

</dd> <dt>

13322 (0x340A)
</dt> <dd>

Spanish – Chile

</dd> <dt>

14337 (0x3801)
</dt> <dd>

Arabic – U.A.E.

</dd> <dt>

14346 (0x380A)
</dt> <dd>

Spanish – Uruguay

</dd> <dt>

15361 (0x3C01)
</dt> <dd>

Arabic – Bahrain

</dd> <dt>

15370 (0x3C0A)
</dt> <dd>

Spanish – Paraguay

</dd> <dt>

16385 (0x4001)
</dt> <dd>

Arabic – Qatar

</dd> <dt>

16394 (0x400A)
</dt> <dd>

Spanish – Bolivia

</dd> <dt>

17418 (0x440A)
</dt> <dd>

Spanish – El Salvador

</dd> <dt>

18442 (0x480A)
</dt> <dd>

Spanish – Honduras

</dd> <dt>

19466 (0x4C0A)
</dt> <dd>

Spanish – Nicaragua

</dd> <dt>

20490 (0x500A)
</dt> <dd>

Spanish – Puerto Rico

</dd> </dl>

</dd> <dt>

**OSProductSuite**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\ProductOptions\|ProductSuite"), [**BitValues**](../wmisdk/standard-qualifiers.md) ("Small Business", "Enterprise", "BackOffice", "Communication Server", "Terminal Server", "Small Business(Restricted)", "Embedded NT", "Data Center")
</dt> </dl>

Installed and licensed system product additions to the operating system. For example, the value of 146 (0x92) for **OSProductSuite** indicates Enterprise, Terminal Services, and Data Center (bits one, four, and seven set). The following list lists possible values.

<dt>

1 (0x1)
</dt> <dd>

Microsoft Small Business Server was once installed, but may have been upgraded to another version of Windows.

</dd> <dt>

2 (0x2)
</dt> <dd>

Windows Server 2008 Enterprise is installed.

</dd> <dt>

4 (0x4)
</dt> <dd>

Windows BackOffice components are installed.

</dd> <dt>

8 (0x8)
</dt> <dd>

Communication Server is installed.

</dd> <dt>

16 (0x10)
</dt> <dd>

Terminal Services is installed.

</dd> <dt>

32 (0x20)
</dt> <dd>

Microsoft Small Business Server is installed with the restrictive client license.

</dd> <dt>

64 (0x40)
</dt> <dd>

Windows Embedded is installed.

</dd> <dt>

128 (0x80)
</dt> <dd>

A Datacenter edition is installed.

</dd> <dt>

256 (0x100)
</dt> <dd>

Terminal Services is installed, but only one interactive session is supported.

</dd> <dt>

512 (0x200)
</dt> <dd>

Windows Home Edition is installed.

</dd> <dt>

1024 (0x400)
</dt> <dd>

Web Server Edition is installed.

</dd> <dt>

8192 (0x2000)
</dt> <dd>

Storage Server Edition is installed.

</dd> <dt>

16384 (0x4000)
</dt> <dd>

Compute Cluster Edition is installed.

</dd> </dl>

</dd> <dt>

**OSType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](../wmisdk/standard-qualifiers.md) ("[**CIM\_OperatingSystem**](cim-operatingsystem.md).**OtherTypeDescription**")
</dt> </dl>

Type of operating system. The following list identifies the possible values.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="MACOS"></span><span id="macos"></span>

<span id="MACOS"></span><span id="macos"></span>**MACOS** (2)


</dt> <dd>

MACROS

</dd> <dt>

<span id="ATTUNIX"></span><span id="attunix"></span>

<span id="ATTUNIX"></span><span id="attunix"></span>**ATTUNIX** (3)


</dt> <dd></dd> <dt>

<span id="DGUX"></span><span id="dgux"></span>

<span id="DGUX"></span><span id="dgux"></span>**DGUX** (4)


</dt> <dd></dd> <dt>

<span id="DECNT"></span><span id="decnt"></span>

<span id="DECNT"></span><span id="decnt"></span>**DECNT** (5)


</dt> <dd></dd> <dt>

<span id="Digital_Unix"></span><span id="digital_unix"></span><span id="DIGITAL_UNIX"></span>

<span id="Digital_Unix"></span><span id="digital_unix"></span><span id="DIGITAL_UNIX"></span>**Digital Unix** (6)


</dt> <dd></dd> <dt>

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>**OpenVMS** (7)


</dt> <dd></dd> <dt>

<span id="HPUX"></span><span id="hpux"></span>

<span id="HPUX"></span><span id="hpux"></span>**HPUX** (8)


</dt> <dd></dd> <dt>

<span id="AIX"></span><span id="aix"></span>

<span id="AIX"></span><span id="aix"></span>**AIX** (9)


</dt> <dd></dd> <dt>

<span id="MVS"></span><span id="mvs"></span>

<span id="MVS"></span><span id="mvs"></span>**MVS** (10)


</dt> <dd></dd> <dt>

<span id="OS400"></span><span id="os400"></span>

<span id="OS400"></span><span id="os400"></span>**OS400** (11)


</dt> <dd></dd> <dt>

<span id="OS_2"></span><span id="os_2"></span>

<span id="OS_2"></span><span id="os_2"></span>**OS/2** (12)


</dt> <dd></dd> <dt>

<span id="JavaVM"></span><span id="javavm"></span><span id="JAVAVM"></span>

<span id="JavaVM"></span><span id="javavm"></span><span id="JAVAVM"></span>**JavaVM** (13)


</dt> <dd></dd> <dt>

<span id="MSDOS"></span><span id="msdos"></span>

<span id="MSDOS"></span><span id="msdos"></span>**MSDOS** (14)


</dt> <dd></dd> <dt>

<span id="WIN3x"></span><span id="win3x"></span><span id="WIN3X"></span>

<span id="WIN3x"></span><span id="win3x"></span><span id="WIN3X"></span>**WIN3x** (15)


</dt> <dd></dd> <dt>

<span id="WIN95"></span><span id="win95"></span>

<span id="WIN95"></span><span id="win95"></span>**WIN95** (16)


</dt> <dd></dd> <dt>

<span id="WIN98"></span><span id="win98"></span>

<span id="WIN98"></span><span id="win98"></span>**WIN98** (17)


</dt> <dd></dd> <dt>

<span id="WINNT"></span><span id="winnt"></span>

<span id="WINNT"></span><span id="winnt"></span>**WINNT** (18)


</dt> <dd></dd> <dt>

<span id="WINCE"></span><span id="wince"></span>

<span id="WINCE"></span><span id="wince"></span>**WINCE** (19)


</dt> <dd></dd> <dt>

<span id="NCR3000"></span><span id="ncr3000"></span>

<span id="NCR3000"></span><span id="ncr3000"></span>**NCR3000** (20)


</dt> <dd></dd> <dt>

<span id="NetWare"></span><span id="netware"></span><span id="NETWARE"></span>

<span id="NetWare"></span><span id="netware"></span><span id="NETWARE"></span>**NetWare** (21)


</dt> <dd></dd> <dt>

<span id="OSF"></span><span id="osf"></span>

<span id="OSF"></span><span id="osf"></span>**OSF** (22)


</dt> <dd></dd> <dt>

<span id="DC_OS"></span><span id="dc_os"></span>

<span id="DC_OS"></span><span id="dc_os"></span>**DC/OS** (23)


</dt> <dd></dd> <dt>

<span id="Reliant_UNIX"></span><span id="reliant_unix"></span><span id="RELIANT_UNIX"></span>

<span id="Reliant_UNIX"></span><span id="reliant_unix"></span><span id="RELIANT_UNIX"></span>**Reliant UNIX** (24)


</dt> <dd></dd> <dt>

<span id="SCO_UnixWare"></span><span id="sco_unixware"></span><span id="SCO_UNIXWARE"></span>

<span id="SCO_UnixWare"></span><span id="sco_unixware"></span><span id="SCO_UNIXWARE"></span>**SCO UnixWare** (25)


</dt> <dd></dd> <dt>

<span id="SCO_OpenServer"></span><span id="sco_openserver"></span><span id="SCO_OPENSERVER"></span>

<span id="SCO_OpenServer"></span><span id="sco_openserver"></span><span id="SCO_OPENSERVER"></span>**SCO OpenServer** (26)


</dt> <dd></dd> <dt>

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>**Sequent** (27)


</dt> <dd></dd> <dt>

<span id="IRIX"></span><span id="irix"></span>

<span id="IRIX"></span><span id="irix"></span>**IRIX** (28)


</dt> <dd></dd> <dt>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>**Solaris** (29)


</dt> <dd>

Solaris

</dd> <dt>

<span id="SunOS"></span><span id="sunos"></span><span id="SUNOS"></span>

<span id="SunOS"></span><span id="sunos"></span><span id="SUNOS"></span>**SunOS** (30)


</dt> <dd></dd> <dt>

<span id="U6000"></span><span id="u6000"></span>

<span id="U6000"></span><span id="u6000"></span>**U6000** (31)


</dt> <dd></dd> <dt>

<span id="ASERIES"></span><span id="aseries"></span>

<span id="ASERIES"></span><span id="aseries"></span>**ASERIES** (32)


</dt> <dd></dd> <dt>

<span id="TandemNSK"></span><span id="tandemnsk"></span><span id="TANDEMNSK"></span>

<span id="TandemNSK"></span><span id="tandemnsk"></span><span id="TANDEMNSK"></span>**TandemNSK** (33)


</dt> <dd></dd> <dt>

<span id="TandemNT"></span><span id="tandemnt"></span><span id="TANDEMNT"></span>

<span id="TandemNT"></span><span id="tandemnt"></span><span id="TANDEMNT"></span>**TandemNT** (34)


</dt> <dd></dd> <dt>

<span id="BS2000"></span><span id="bs2000"></span>

<span id="BS2000"></span><span id="bs2000"></span>**BS2000** (35)


</dt> <dd></dd> <dt>

<span id="LINUX"></span><span id="linux"></span>

<span id="LINUX"></span><span id="linux"></span>**LINUX** (36)


</dt> <dd></dd> <dt>

<span id="Lynx"></span><span id="lynx"></span><span id="LYNX"></span>

<span id="Lynx"></span><span id="lynx"></span><span id="LYNX"></span>**Lynx** (37)


</dt> <dd></dd> <dt>

<span id="XENIX"></span><span id="xenix"></span>

<span id="XENIX"></span><span id="xenix"></span>**XENIX** (38)


</dt> <dd></dd> <dt>

<span id="VM_ESA"></span><span id="vm_esa"></span>

<span id="VM_ESA"></span><span id="vm_esa"></span>**VM/ESA** (39)


</dt> <dd></dd> <dt>

<span id="Interactive_UNIX"></span><span id="interactive_unix"></span><span id="INTERACTIVE_UNIX"></span>

<span id="Interactive_UNIX"></span><span id="interactive_unix"></span><span id="INTERACTIVE_UNIX"></span>**Interactive UNIX** (40)


</dt> <dd></dd> <dt>

<span id="BSDUNIX"></span><span id="bsdunix"></span>

<span id="BSDUNIX"></span><span id="bsdunix"></span>**BSDUNIX** (41)


</dt> <dd></dd> <dt>

<span id="FreeBSD"></span><span id="freebsd"></span><span id="FREEBSD"></span>

<span id="FreeBSD"></span><span id="freebsd"></span><span id="FREEBSD"></span>**FreeBSD** (42)


</dt> <dd></dd> <dt>

<span id="NetBSD"></span><span id="netbsd"></span><span id="NETBSD"></span>

<span id="NetBSD"></span><span id="netbsd"></span><span id="NETBSD"></span>**NetBSD** (43)


</dt> <dd></dd> <dt>

<span id="GNU_Hurd"></span><span id="gnu_hurd"></span><span id="GNU_HURD"></span>

<span id="GNU_Hurd"></span><span id="gnu_hurd"></span><span id="GNU_HURD"></span>**GNU Hurd** (44)


</dt> <dd></dd> <dt>

<span id="OS9"></span><span id="os9"></span>

<span id="OS9"></span><span id="os9"></span>**OS9** (45)


</dt> <dd></dd> <dt>

<span id="MACH_Kernel"></span><span id="mach_kernel"></span><span id="MACH_KERNEL"></span>

<span id="MACH_Kernel"></span><span id="mach_kernel"></span><span id="MACH_KERNEL"></span>**MACH Kernel** (46)


</dt> <dd></dd> <dt>

<span id="Inferno"></span><span id="inferno"></span><span id="INFERNO"></span>

<span id="Inferno"></span><span id="inferno"></span><span id="INFERNO"></span>**Inferno** (47)


</dt> <dd></dd> <dt>

<span id="QNX"></span><span id="qnx"></span>

<span id="QNX"></span><span id="qnx"></span>**QNX** (48)


</dt> <dd></dd> <dt>

<span id="EPOC"></span><span id="epoc"></span>

<span id="EPOC"></span><span id="epoc"></span>**EPOC** (49)


</dt> <dd></dd> <dt>

<span id="IxWorks"></span><span id="ixworks"></span><span id="IXWORKS"></span>

<span id="IxWorks"></span><span id="ixworks"></span><span id="IXWORKS"></span>**IxWorks** (50)


</dt> <dd></dd> <dt>

<span id="VxWorks"></span><span id="vxworks"></span><span id="VXWORKS"></span>

<span id="VxWorks"></span><span id="vxworks"></span><span id="VXWORKS"></span>**VxWorks** (51)


</dt> <dd></dd> <dt>

<span id="MiNT"></span><span id="mint"></span><span id="MINT"></span>

<span id="MiNT"></span><span id="mint"></span><span id="MINT"></span>**MiNT** (52)


</dt> <dd></dd> <dt>

<span id="BeOS"></span><span id="beos"></span><span id="BEOS"></span>

<span id="BeOS"></span><span id="beos"></span><span id="BEOS"></span>**BeOS** (53)


</dt> <dd></dd> <dt>

<span id="HP_MPE"></span><span id="hp_mpe"></span>

<span id="HP_MPE"></span><span id="hp_mpe"></span>**HP MPE** (54)


</dt> <dd></dd> <dt>

<span id="NextStep"></span><span id="nextstep"></span><span id="NEXTSTEP"></span>

<span id="NextStep"></span><span id="nextstep"></span><span id="NEXTSTEP"></span>**NextStep** (55)


</dt> <dd></dd> <dt>

<span id="PalmPilot"></span><span id="palmpilot"></span><span id="PALMPILOT"></span>

<span id="PalmPilot"></span><span id="palmpilot"></span><span id="PALMPILOT"></span>**PalmPilot** (56)


</dt> <dd></dd> <dt>

<span id="Rhapsody"></span><span id="rhapsody"></span><span id="RHAPSODY"></span>

<span id="Rhapsody"></span><span id="rhapsody"></span><span id="RHAPSODY"></span>**Rhapsody** (57)


</dt> <dd></dd> <dt>

<span id="Windows_2000"></span><span id="windows_2000"></span><span id="WINDOWS_2000"></span>

<span id="Windows_2000"></span><span id="windows_2000"></span><span id="WINDOWS_2000"></span>**Windows 2000** (58)


</dt> <dd></dd> <dt>

<span id="Dedicated"></span><span id="dedicated"></span><span id="DEDICATED"></span>

<span id="Dedicated"></span><span id="dedicated"></span><span id="DEDICATED"></span>**Dedicated** (59)


</dt> <dd></dd> <dt>

<span id="OS_390"></span><span id="os_390"></span>

<span id="OS_390"></span><span id="os_390"></span>**OS/390** (60)


</dt> <dd></dd> <dt>

<span id="VSE"></span><span id="vse"></span>

<span id="VSE"></span><span id="vse"></span>**VSE** (61)


</dt> <dd></dd> <dt>

<span id="TPF"></span><span id="tpf"></span>

<span id="TPF"></span><span id="tpf"></span>**TPF** (62)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**ModelCorrespondence**](../wmisdk/standard-qualifiers.md) ("[**CIM\_OperatingSystem**](cim-operatingsystem.md).**OSType**")
</dt> </dl>

Additional description for the current operating system version.

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**PAEEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the physical address extensions (PAE) are enabled by the operating system running on Intel processors. PAE allows applications to address more than 4 GB of physical memory. When PAE is enabled, the operating system uses three-level linear address translation rather than two-level. Providing more physical memory to an application reduces the need to swap memory to the page file and increases performance. To enable, PAE, use the "/PAE" switch in the Boot.ini file. For more information about the Physical Address Extension feature, see <https://Go.Microsoft.Com/FWLink/p/?LinkID=45912>.

</dd> <dt>

**PlusProductID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\|Plus! ProductId")
</dt> </dl>

Not supported.

</dd> <dt>

**PlusVersionNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\|Plus! VersionNumber")
</dt> </dl>

Not supported.

</dd> <dt>

**PortableOperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the operating system booted from an external USB device. If true, the operating system has detected it is booting on a supported locally connected storage device.

**Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows 8 and Windows Server 2012.

</dd> <dt>

**Primary**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Specifies whether this is the primary operating system.

</dd> <dt>

**ProductType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional system information.

<dt>

<span id="Work_Station"></span><span id="work_station"></span><span id="WORK_STATION"></span>

**Work Station** (1)


</dt> <dd></dd> <dt>

<span id="Domain_Controller"></span><span id="domain_controller"></span><span id="DOMAIN_CONTROLLER"></span>

**Domain Controller** (2)


</dt> <dd></dd> <dt>

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>

**Server** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**QuantumLength**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\PriorityControl\|Win32PrioritySeparation")
</dt> </dl>

Not supported

**Windows Server 2008 and Windows Vista:  **

The **QuantumLength** property defines the number of clock ticks per quantum. A quantum is a unit of execution time that the scheduler is allowed to give to an application before switching to other applications. When a thread runs one quantum, the kernel preempts it and moves it to the end of a queue for applications with equal priorities. The actual length of a thread's quantum varies across different Windows platforms. For Windows NT/Windows 2000 only.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="One_tick"></span><span id="one_tick"></span><span id="ONE_TICK"></span>

**One tick** (1)


</dt> <dd></dd> <dt>

<span id="Two_ticks"></span><span id="two_ticks"></span><span id="TWO_TICKS"></span>

**Two ticks** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**QuantumType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not supported

**Windows Server 2008 and Windows Vista:  **

The **QuantumType** property specifies either fixed or variable length quantums. Windows defaults to variable length quantums where the foreground application has a longer quantum than the background applications. Windows Server defaults to fixed-length quantums. A quantum is a unit of execution time that the scheduler is allowed to give to an application before switching to another application. When a thread runs one quantum, the kernel preempts it and moves it to the end of a queue for applications with equal priorities. The actual length of a thread's quantum varies across different Windows platforms.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>

**Fixed** (1)


</dt> <dd></dd> <dt>

<span id="Variable"></span><span id="variable"></span><span id="VARIABLE"></span>

**Variable** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**RegisteredUser**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\|RegisteredOwner")
</dt> </dl>

Name of the registered user of the operating system.

Example: "Ben Smith"

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\|ProductId")
</dt> </dl>

Operating system product serial identification number.

Example: "10497-OEM-0031416-71674"

</dd> <dt>

**ServicePackMajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|System Information Structures\|[**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa)\|**wServicePackMajor**")
</dt> </dl>

Major version number of the service pack installed on the computer system. If no service pack has been installed, the value is 0 (zero).

</dd> <dt>

**ServicePackMinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|System Information Structures\|[**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa)\|**wServicePackMinor**")
</dt> </dl>

Minor version number of the service pack installed on the computer system. If no service pack has been installed, the value is 0 (zero).

</dd> <dt>

**SizeStoredInPagingFiles**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|System Memory Settings\|001.3"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Total number of kilobytes that can be stored in the operating system paging files—0 (zero) indicates that there are no paging files. Be aware that this number does not represent the actual physical size of the paging file on disk.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive may function properly, but predicts a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The Service status applies to administrative work, such as mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

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

**SuiteMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitMap**](../wmisdk/standard-qualifiers.md) ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), [**BitValues**](../wmisdk/standard-qualifiers.md) ("Windows Server, Small Business Edition", "Windows Server, Enterprise Edition", "Windows Server, Backoffice Edition", "Windows Server, Communications Edition", "Microsoft Terminal Services", "Windows Server, Small Business Edition Restricted", "Windows Embedded", "Windows Server, Datacenter Edition", "Single User", "Windows Home Edition", "Windows Server, Web Edition")
</dt> </dl>

Bit flags that identify the product suites available on the system.

For example, to specify both Personal and BackOffice, set **SuiteMask** to `4 | 512` or `516`.

<dt>

1
</dt> <dd>

Small Business

</dd> <dt>

2
</dt> <dd>

Enterprise

</dd> <dt>

4
</dt> <dd>

BackOffice

</dd> <dt>

8
</dt> <dd>

Communications

</dd> <dt>

16
</dt> <dd>

Terminal Services

</dd> <dt>

32
</dt> <dd>

Small Business Restricted

</dd> <dt>

64
</dt> <dd>

Embedded Edition

</dd> <dt>

128
</dt> <dd>

Datacenter Edition

</dd> <dt>

256
</dt> <dd>

Single User

</dd> <dt>

512
</dt> <dd>

Home Edition

</dd> <dt>

1024
</dt> <dd>

Web Server Edition

</dd> </dl>

</dd> <dt>

**SystemDevice**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Registry Functions\|[**GetPrivateProfileString**](/windows/win32/api/winbase/nf-winbase-getprivateprofilestring)\|Paths\|TargetDevice")
</dt> </dl>

Physical disk partition on which the operating system is installed.

</dd> <dt>

**SystemDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|System Information Functions[**GetSystemDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya))
</dt> </dl>

System directory of the operating system.

Example: "C:\\WINDOWS\\SYSTEM32"

</dd> <dt>

**SystemDrive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Letter of the disk drive on which the operating system resides. Example: "C:"

</dd> <dt>

**TotalSwapSpaceSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Total swap space in kilobytes. This value may be **NULL** (unspecified) if the swap space is not distinguished from page files. However, some operating systems distinguish these concepts. For example, in UNIX, whole processes can be swapped out when the free page list falls and remains below a specified amount.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**TotalVirtualMemorySize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Number, in kilobytes, of virtual memory. For example, this may be calculated by adding the amount of total RAM to the amount of paging space, that is, adding the amount of memory in or aggregated by the computer system to the property, **SizeStoredInPagingFiles**.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**TotalVisibleMemorySize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Total amount, in kilobytes, of physical memory available to the operating system. This value does not necessarily indicate the true amount of physical memory, but what is reported to the operating system as available to it.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Version"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|System Information Structures\|[**OSVERSIONINFOEX**](/windows/win32/api/winnt/ns-winnt-osversioninfoexa)\|dwMajorVersion, dwMinorVersion")
</dt> </dl>

Version number of the operating system.

Example: "4.0"

</dd> <dt>

**WindowsDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|System Information Functions\|[**GetWindowsDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya)")
</dt> </dl>

Windows directory of the operating system.

Example: "C:\\WINDOWS"

</dd> </dl>

## Remarks

The **Win32\_OperatingSystem** class is derived from [**CIM\_OperatingSystem**](cim-operatingsystem.md).

Any operating system that can be installed on a computer that can run a Windows-based operating system is a descendant or member of this class. **Win32\_OperatingSystem** is a singleton class. To get the single instance, use "@" for the key.

Unlike most of the other WMI classes generated by MgmtClassGen, the **OperatingSystem.CreateInstance**() method will return a blank **OperatingSystem** object. Therefore, if you are using C\# with MgmtClassGen, you can use the following code:


```CSharp
WMI.OperatingSystem os = new ROOT.CIMV2.win32.OperatingSystem();
```



## Examples

You can find a VBScript example that obtains operating system and processor data from [**Win32\_ComputerSystem**](win32-computersystem.md), [**Win32\_Processor**](win32-processor.md), and **Win32\_OperatingSystem** in the [**Win32\_Processor**](win32-processor.md) topic examples.

The [Generate Exchange Environment Reports using Powershell](https://Gallery.TechNet.Microsoft.Com/scriptcenter/Generate-Exchange-2388e7c9) PowerShell sample on TechNet Gallery uses a **Win32\_OperatingSystem** class as part of a larger application to generate exchange environment reports.

The [Get Server Uptime Using WMI](https://Gallery.TechNet.Microsoft.Com/Get-Server-Uptime-Using-WMI-15aaa8ac) sample in the TechNet Gallery uses the **LastBootupTime** property to determine how long the server has been active. The sample also uses the timeout option to ensure that the WMI call does not hang.

The [WMI Information Retriever](https://Gallery.TechNet.Microsoft.Com/e493376c-1286-456b-bd4b-4ac3b0e9bb45) VBScript code example on the TechNet Gallery uses the **Win32\_OperatingSystem** class to retrieve OS information from a number of remote computers.

The following script obtains the instances of **Win32\_OperatingSystem** in the default "Root\\CIMv2" namespace, and then displays information about the operating system.


```VB
On Error Resume Next
' Connect to WMI and obtain instances of Win32_OperatingSystem
For Each objOS in GetObject( _
    "winmgmts:").InstancesOf ("Win32_OperatingSystem")

WScript.Echo "Name = " & objOS.Caption & "Version = " & objOS.Version &VBCR _
           & "Registered User = " & objOS.RegisteredUser &VBCR _
           & "Manufacturer = " & objOS.Manufacturer      
Next

if Err <> 0 Then
    WScript.Echo Err.Description
    Err.Clear
End if
```



The following PowerShell code sample displays all the operating information about the current OS.


```PowerShell
# get instance
$os = Get-WmiObject Win32_OperatingSystem

# output information:
"The class has {0} properties" -f $os.properties.count
"Details on this class:"
$os | Format-List *
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_OperatingSystem**](cim-operatingsystem.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> <dt>

[WMI Tasks: Operating Systems](../wmisdk/wmi-tasks--operating-systems.md)
</dt> <dt>

[WMI Tasks: Computer Hardware](../wmisdk/wmi-tasks--computer-hardware.md)
</dt> <dt>

[WMI Tasks: Desktop Management](../wmisdk/wmi-tasks--desktop-management.md)
</dt> </dl>

 

 
