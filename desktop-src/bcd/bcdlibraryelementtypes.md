---
title: BcdLibraryElementTypes enumeration
description: Specifies the library element types. Library elements are available to all objects.
ms.assetid: '042ad83d-d764-46db-b611-c51228dccdde'
keywords: ["BcdLibraryElementTypes enumeration Boot Config"]
topic_type:
- apiref
api_name:
- BcdLibraryElementTypes
api_type:
- NA
---

# BcdLibraryElementTypes enumeration

Specifies the library element types. Library elements are available to all objects.

## Syntax


```C++
typedef enum BcdLibraryElementTypes { 
  BcdLibraryDevice_ApplicationDevice                  = 0x11000001,
  BcdLibraryString_ApplicationPath                    = 0x12000002,
  BcdLibraryString_Description                        = 0x12000004,
  BcdLibraryString_PreferredLocale                    = 0x12000005,
  BcdLibraryObjectList_InheritedObjects               = 0x14000006,
  BcdLibraryInteger_TruncatePhysicalMemory            = 0x15000007,
  BcdLibraryObjectList_RecoverySequence               = 0x14000008,
  BcdLibraryBoolean_AutoRecoveryEnabled               = 0x16000009,
  BcdLibraryIntegerList_BadMemoryList                 = 0x1700000a,
  BcdLibraryBoolean_AllowBadMemoryAccess              = 0x1600000b,
  BcdLibraryInteger_FirstMegabytePolicy               = 0x1500000c,
  BcdLibraryInteger_RelocatePhysicalMemory            = 0x1500000D,
  BcdLibraryInteger_AvoidLowPhysicalMemory            = 0x1500000E,
  BcdLibraryBoolean_DebuggerEnabled                   = 0x16000010,
  BcdLibraryInteger_DebuggerType                      = 0x15000011,
  BcdLibraryInteger_SerialDebuggerPortAddress         = 0x15000012,
  BcdLibraryInteger_SerialDebuggerPort                = 0x15000013,
  BcdLibraryInteger_SerialDebuggerBaudRate            = 0x15000014,
  BcdLibraryInteger_1394DebuggerChannel               = 0x15000015,
  BcdLibraryString_UsbDebuggerTargetName              = 0x12000016,
  BcdLibraryBoolean_DebuggerIgnoreUsermodeExceptions  = 0x16000017,
  BcdLibraryInteger_DebuggerStartPolicy               = 0x15000018,
  BcdLibraryString_DebuggerBusParameters              = 0x12000019,
  BcdLibraryInteger_DebuggerNetHostIP                 = 0x1500001A,
  BcdLibraryInteger_DebuggerNetPort                   = 0x1500001B,
  BcdLibraryBoolean_DebuggerNetDhcp                   = 0x1600001C,
  BcdLibraryString_DebuggerNetKey                     = 0x1200001D,
  BcdLibraryBoolean_EmsEnabled                        = 0x16000020,
  BcdLibraryInteger_EmsPort                           = 0x15000022,
  BcdLibraryInteger_EmsBaudRate                       = 0x15000023,
  BcdLibraryString_LoadOptionsString                  = 0x12000030,
  BcdLibraryBoolean_DisplayAdvancedOptions            = 0x16000040,
  BcdLibraryBoolean_DisplayOptionsEdit                = 0x16000041,
  BcdLibraryDevice_BsdLogDevice                       = 0x11000043,
  BcdLibraryString_BsdLogPath                         = 0x12000044,
  BcdLibraryBoolean_GraphicsModeDisabled              = 0x16000046,
  BcdLibraryInteger_ConfigAccessPolicy                = 0x15000047,
  BcdLibraryBoolean_DisableIntegrityChecks            = 0x16000048,
  BcdLibraryBoolean_AllowPrereleaseSignatures         = 0x16000049,
  BcdLibraryString_FontPath                           = 0x1200004A,
  BcdLibraryInteger_SiPolicy                          = 0x1500004B,
  BcdLibraryInteger_FveBandId                         = 0x1500004C,
  BcdLibraryBoolean_ConsoleExtendedInput              = 0x16000050,
  BcdLibraryInteger_GraphicsResolution                = 0x15000052,
  BcdLibraryBoolean_RestartOnFailure                  = 0x16000053,
  BcdLibraryBoolean_GraphicsForceHighestMode          = 0x16000054,
  BcdLibraryBoolean_IsolatedExecutionContext          = 0x16000060,
  BcdLibraryBoolean_BootUxDisable                     = 0x1600006C,
  BcdLibraryBoolean_BootShutdownDisabled              = 0x16000074,
  BcdLibraryIntegerList_AllowedInMemorySettings       = 0x17000077,
  BcdLibraryBoolean_ForceFipsCrypto                   = 0x16000079
} BcdLibraryElementTypes;
```



## Constants

<dl> <dt>

<span id="BcdLibraryDevice_ApplicationDevice"></span><span id="bcdlibrarydevice_applicationdevice"></span><span id="BCDLIBRARYDEVICE_APPLICATIONDEVICE"></span>**BcdLibraryDevice\_ApplicationDevice**
</dt> <dd>

Device on which a boot environment application resides. The element data format is [**BcdDeviceElement**](bcddeviceelement.md).

</dd> <dt>

<span id="BcdLibraryString_ApplicationPath"></span><span id="bcdlibrarystring_applicationpath"></span><span id="BCDLIBRARYSTRING_APPLICATIONPATH"></span>**BcdLibraryString\_ApplicationPath**
</dt> <dd>

Path to a boot environment application. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdLibraryString_Description"></span><span id="bcdlibrarystring_description"></span><span id="BCDLIBRARYSTRING_DESCRIPTION"></span>**BcdLibraryString\_Description**
</dt> <dd>

Display name of the boot environment application. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdLibraryString_PreferredLocale"></span><span id="bcdlibrarystring_preferredlocale"></span><span id="BCDLIBRARYSTRING_PREFERREDLOCALE"></span>**BcdLibraryString\_PreferredLocale**
</dt> <dd>

Preferred locale, in RFC 3066 format. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdLibraryObjectList_InheritedObjects"></span><span id="bcdlibraryobjectlist_inheritedobjects"></span><span id="BCDLIBRARYOBJECTLIST_INHERITEDOBJECTS"></span>**BcdLibraryObjectList\_InheritedObjects**
</dt> <dd>

List of BCD objects from which the current object should inherit elements. The element data format is [**BcdObjectListElement**](bcdobjectlistelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_TruncatePhysicalMemory"></span><span id="bcdlibraryinteger_truncatephysicalmemory"></span><span id="BCDLIBRARYINTEGER_TRUNCATEPHYSICALMEMORY"></span>**BcdLibraryInteger\_TruncatePhysicalMemory**
</dt> <dd>

Maximum physical address a boot environment application should recognize. All memory above this address is ignored. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryObjectList_RecoverySequence"></span><span id="bcdlibraryobjectlist_recoverysequence"></span><span id="BCDLIBRARYOBJECTLIST_RECOVERYSEQUENCE"></span>**BcdLibraryObjectList\_RecoverySequence**
</dt> <dd>

List of boot environment applications to be executed if the associated application fails. The applications are executed in the order they appear in this list. The element data format is [**BcdObjectListElement**](bcdobjectlistelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_AutoRecoveryEnabled"></span><span id="bcdlibraryboolean_autorecoveryenabled"></span><span id="BCDLIBRARYBOOLEAN_AUTORECOVERYENABLED"></span>**BcdLibraryBoolean\_AutoRecoveryEnabled**
</dt> <dd>

Indicates whether the recovery sequence executes automatically if the boot application fails. Otherwise, the recovery sequence only runs on demand. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryIntegerList_BadMemoryList"></span><span id="bcdlibraryintegerlist_badmemorylist"></span><span id="BCDLIBRARYINTEGERLIST_BADMEMORYLIST"></span>**BcdLibraryIntegerList\_BadMemoryList**
</dt> <dd>

List of page frame numbers describing faulty memory in the system. The element data format is [**BcdIntegerListElement**](bcdintegerlistelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_AllowBadMemoryAccess"></span><span id="bcdlibraryboolean_allowbadmemoryaccess"></span><span id="BCDLIBRARYBOOLEAN_ALLOWBADMEMORYACCESS"></span>**BcdLibraryBoolean\_AllowBadMemoryAccess**
</dt> <dd>

If **TRUE**, indicates that a boot application can use memory listed in the **BcdLibraryIntegerList\_BadMemoryList**. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_FirstMegabytePolicy"></span><span id="bcdlibraryinteger_firstmegabytepolicy"></span><span id="BCDLIBRARYINTEGER_FIRSTMEGABYTEPOLICY"></span>**BcdLibraryInteger\_FirstMegabytePolicy**
</dt> <dd>

Indicates how the first megabyte of memory is to be used. The element data format is [**BcdIntegerElement**](bcdintegerelement.md). The following are the possible values.



| Term                                                                                                                                                                                                     | Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="FirstMegabytePolicyUseNone__0_"></span><span id="firstmegabytepolicyusenone__0_"></span><span id="FIRSTMEGABYTEPOLICYUSENONE__0_"></span>FirstMegabytePolicyUseNone (0)<br/>             | Use none of the first megabyte of memory.<br/> |
| <span id="FirstMegabytePolicyUseAll__1_"></span><span id="firstmegabytepolicyuseall__1_"></span><span id="FIRSTMEGABYTEPOLICYUSEALL__1_"></span>FirstMegabytePolicyUseAll (1)<br/>                 | Use all of the first megabyte of memory.<br/>  |
| <span id="FirstMegabytePolicyUsePrivate__2_"></span><span id="firstmegabytepolicyuseprivate__2_"></span><span id="FIRSTMEGABYTEPOLICYUSEPRIVATE__2_"></span>FirstMegabytePolicyUsePrivate (2)<br/> | Reserved for future use.<br/>                  |



 

</dd> <dt>

<span id="BcdLibraryInteger_RelocatePhysicalMemory"></span><span id="bcdlibraryinteger_relocatephysicalmemory"></span><span id="BCDLIBRARYINTEGER_RELOCATEPHYSICALMEMORY"></span>**BcdLibraryInteger\_RelocatePhysicalMemory**
</dt> <dd>

Relocates physical memory on certain AMD processors. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

> [!Note]  
> This value is not used in Windows 8 or Windows Server 2012.

 

</dd> <dt>

<span id="BcdLibraryInteger_AvoidLowPhysicalMemory"></span><span id="bcdlibraryinteger_avoidlowphysicalmemory"></span><span id="BCDLIBRARYINTEGER_AVOIDLOWPHYSICALMEMORY"></span>**BcdLibraryInteger\_AvoidLowPhysicalMemory**
</dt> <dd>

Specifies a minimum physical address to use in the boot environment. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_DebuggerEnabled"></span><span id="bcdlibraryboolean_debuggerenabled"></span><span id="BCDLIBRARYBOOLEAN_DEBUGGERENABLED"></span>**BcdLibraryBoolean\_DebuggerEnabled**
</dt> <dd>

Indicates whether the boot debugger should be enabled. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_DebuggerType"></span><span id="bcdlibraryinteger_debuggertype"></span><span id="BCDLIBRARYINTEGER_DEBUGGERTYPE"></span>**BcdLibraryInteger\_DebuggerType**
</dt> <dd>

Debugger type. The element data format is [**BcdIntegerElement**](bcdintegerelement.md) and the [**Integer**](bcdintegerelement.md) property is one of the values from the [**BcdLibrary\_DebuggerType**](bcdlibrary-debuggertype.md) enumeration.

</dd> <dt>

<span id="BcdLibraryInteger_SerialDebuggerPortAddress"></span><span id="bcdlibraryinteger_serialdebuggerportaddress"></span><span id="BCDLIBRARYINTEGER_SERIALDEBUGGERPORTADDRESS"></span>**BcdLibraryInteger\_SerialDebuggerPortAddress**
</dt> <dd>

I/O port address for the serial debugger. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_SerialDebuggerPort"></span><span id="bcdlibraryinteger_serialdebuggerport"></span><span id="BCDLIBRARYINTEGER_SERIALDEBUGGERPORT"></span>**BcdLibraryInteger\_SerialDebuggerPort**
</dt> <dd>

Serial port number for serial debugging. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the default is specified by the DBGP ACPI table settings.

</dd> <dt>

<span id="BcdLibraryInteger_SerialDebuggerBaudRate"></span><span id="bcdlibraryinteger_serialdebuggerbaudrate"></span><span id="BCDLIBRARYINTEGER_SERIALDEBUGGERBAUDRATE"></span>**BcdLibraryInteger\_SerialDebuggerBaudRate**
</dt> <dd>

Baud rate for serial debugging. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the default is specified by the DBGP ACPI table settings.

</dd> <dt>

<span id="BcdLibraryInteger_1394DebuggerChannel"></span><span id="bcdlibraryinteger_1394debuggerchannel"></span><span id="BCDLIBRARYINTEGER_1394DEBUGGERCHANNEL"></span>**BcdLibraryInteger\_1394DebuggerChannel**
</dt> <dd>

Channel number for 1394 debugging. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryString_UsbDebuggerTargetName"></span><span id="bcdlibrarystring_usbdebuggertargetname"></span><span id="BCDLIBRARYSTRING_USBDEBUGGERTARGETNAME"></span>**BcdLibraryString\_UsbDebuggerTargetName**
</dt> <dd>

The target name for the USB debugger. The target name is arbitrary but must match between the debugger and the debug target. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_DebuggerIgnoreUsermodeExceptions"></span><span id="bcdlibraryboolean_debuggerignoreusermodeexceptions"></span><span id="BCDLIBRARYBOOLEAN_DEBUGGERIGNOREUSERMODEEXCEPTIONS"></span>**BcdLibraryBoolean\_DebuggerIgnoreUsermodeExceptions**
</dt> <dd>

If **TRUE**, the debugger will ignore user mode exceptions and only stop for kernel mode exceptions. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_DebuggerStartPolicy"></span><span id="bcdlibraryinteger_debuggerstartpolicy"></span><span id="BCDLIBRARYINTEGER_DEBUGGERSTARTPOLICY"></span>**BcdLibraryInteger\_DebuggerStartPolicy**
</dt> <dd>

Indicates the debugger start policy. The element data format is [**BcdIntegerElement**](bcdintegerelement.md). The following are the possible values.



| Term                                                                                                                                                                             | Description                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DebuggerStartActive__0_"></span><span id="debuggerstartactive__0_"></span><span id="DEBUGGERSTARTACTIVE__0_"></span>DebuggerStartActive (0)<br/>                 | The debugger will start active.<br/>                                                                                                                                     |
| <span id="DebuggerStartAutoEnable__1_"></span><span id="debuggerstartautoenable__1_"></span><span id="DEBUGGERSTARTAUTOENABLE__1_"></span>DebuggerStartAutoEnable (1)<br/> | The debugger will start in the auto-enabled state. If a debugger is attached it will be used; otherwise the debugger port will be available for other applications.<br/> |
| <span id="DebuggerStartDisable__2_"></span><span id="debuggerstartdisable__2_"></span><span id="DEBUGGERSTARTDISABLE__2_"></span>DebuggerStartDisable (2)<br/>             | The debugger will not start.<br/>                                                                                                                                        |



 

</dd> <dt>

<span id="BcdLibraryString_DebuggerBusParameters"></span><span id="bcdlibrarystring_debuggerbusparameters"></span><span id="BCDLIBRARYSTRING_DEBUGGERBUSPARAMETERS"></span>**BcdLibraryString\_DebuggerBusParameters**
</dt> <dd>

Defines the PCI bus, device, and function numbers of the debugging device. For example, 1.5.0 describes the debugging device on bus 1, device 5, function 0. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_DebuggerNetHostIP"></span><span id="bcdlibraryinteger_debuggernethostip"></span><span id="BCDLIBRARYINTEGER_DEBUGGERNETHOSTIP"></span>**BcdLibraryInteger\_DebuggerNetHostIP**
</dt> <dd>

Defines the host IP address for the network debugger. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_DebuggerNetPort"></span><span id="bcdlibraryinteger_debuggernetport"></span><span id="BCDLIBRARYINTEGER_DEBUGGERNETPORT"></span>**BcdLibraryInteger\_DebuggerNetPort**
</dt> <dd>

Defines the network port for the network debugger. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_DebuggerNetDhcp"></span><span id="bcdlibraryboolean_debuggernetdhcp"></span><span id="BCDLIBRARYBOOLEAN_DEBUGGERNETDHCP"></span>**BcdLibraryBoolean\_DebuggerNetDhcp**
</dt> <dd>

Controls the use of DHCP by the network debugger. Setting this to false causes the OS to only use link-local addresses. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryString_DebuggerNetKey"></span><span id="bcdlibrarystring_debuggernetkey"></span><span id="BCDLIBRARYSTRING_DEBUGGERNETKEY"></span>**BcdLibraryString\_DebuggerNetKey**
</dt> <dd>

Holds the key used to encrypt the network debug connection. The element data format is [**BcdStringElement**](bcdstringelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryBoolean_EmsEnabled"></span><span id="bcdlibraryboolean_emsenabled"></span><span id="BCDLIBRARYBOOLEAN_EMSENABLED"></span>**BcdLibraryBoolean\_EmsEnabled**
</dt> <dd>

Indicates whether EMS redirection should be enabled. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_EmsPort"></span><span id="bcdlibraryinteger_emsport"></span><span id="BCDLIBRARYINTEGER_EMSPORT"></span>**BcdLibraryInteger\_EmsPort**
</dt> <dd>

COM port number for EMS redirection. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the default is specified by the SPCR ACPI table settings.

</dd> <dt>

<span id="BcdLibraryInteger_EmsBaudRate"></span><span id="bcdlibraryinteger_emsbaudrate"></span><span id="BCDLIBRARYINTEGER_EMSBAUDRATE"></span>**BcdLibraryInteger\_EmsBaudRate**
</dt> <dd>

Baud rate for EMS redirection. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryString_LoadOptionsString"></span><span id="bcdlibrarystring_loadoptionsstring"></span><span id="BCDLIBRARYSTRING_LOADOPTIONSSTRING"></span>**BcdLibraryString\_LoadOptionsString**
</dt> <dd>

String that is appended to the load options string passed to the kernel to be consumed by kernel-mode components. This is useful for communicating with kernel-mode components that are not BCD-aware. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_DisplayAdvancedOptions"></span><span id="bcdlibraryboolean_displayadvancedoptions"></span><span id="BCDLIBRARYBOOLEAN_DISPLAYADVANCEDOPTIONS"></span>**BcdLibraryBoolean\_DisplayAdvancedOptions**
</dt> <dd>

Indicates whether the advanced options boot menu (F8) is displayed. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_DisplayOptionsEdit"></span><span id="bcdlibraryboolean_displayoptionsedit"></span><span id="BCDLIBRARYBOOLEAN_DISPLAYOPTIONSEDIT"></span>**BcdLibraryBoolean\_DisplayOptionsEdit**
</dt> <dd>

Indicates whether the boot options editor is enabled. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryDevice_BsdLogDevice"></span><span id="bcdlibrarydevice_bsdlogdevice"></span><span id="BCDLIBRARYDEVICE_BSDLOGDEVICE"></span>**BcdLibraryDevice\_BsdLogDevice**
</dt> <dd>

Allows a device override for the bootstat.dat log in the boot manager and winload.exe. The element data format is [**BcdDeviceElement**](bcddeviceelement.md).

</dd> <dt>

<span id="BcdLibraryString_BsdLogPath"></span><span id="bcdlibrarystring_bsdlogpath"></span><span id="BCDLIBRARYSTRING_BSDLOGPATH"></span>**BcdLibraryString\_BsdLogPath**
</dt> <dd>

Allows a path override for the bootstat.dat log file in the boot manager and winload.exe. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_GraphicsModeDisabled"></span><span id="bcdlibraryboolean_graphicsmodedisabled"></span><span id="BCDLIBRARYBOOLEAN_GRAPHICSMODEDISABLED"></span>**BcdLibraryBoolean\_GraphicsModeDisabled**
</dt> <dd>

Indicates whether graphics mode is disabled and boot applications must use text mode display. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_ConfigAccessPolicy"></span><span id="bcdlibraryinteger_configaccesspolicy"></span><span id="BCDLIBRARYINTEGER_CONFIGACCESSPOLICY"></span>**BcdLibraryInteger\_ConfigAccessPolicy**
</dt> <dd>

Indicates the access policy for PCI configuration space. The element data format is [**BcdIntegerElement**](bcdintegerelement.md). The following are the possible values.



| Term                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ConfigAccessPolicyDefault__0_"></span><span id="configaccesspolicydefault__0_"></span><span id="CONFIGACCESSPOLICYDEFAULT__0_"></span>ConfigAccessPolicyDefault (0)<br/>                                     | Access to PCI configuration space through the memory-mapped region is allowed.<br/>                                                                                                                                                                                                  |
| <span id="ConfigAccessPolicyDisallowMmConfig__1_"></span><span id="configaccesspolicydisallowmmconfig__1_"></span><span id="CONFIGACCESSPOLICYDISALLOWMMCONFIG__1_"></span>ConfigAccessPolicyDisallowMmConfig (1)<br/> | Access to PCI configuration space through the memory-mapped region is not allowed. This setting is used for platforms that implement memory-mapped configuration space incorrectly. The CFC/CF8 access mechanism can be used to access configuration space on these platforms. <br/> |



 

</dd> <dt>

<span id="BcdLibraryBoolean_DisableIntegrityChecks"></span><span id="bcdlibraryboolean_disableintegritychecks"></span><span id="BCDLIBRARYBOOLEAN_DISABLEINTEGRITYCHECKS"></span>**BcdLibraryBoolean\_DisableIntegrityChecks**
</dt> <dd>

Disables integrity checks. Cannot be set when secure boot is enabled. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

> [!Note]  
> This value is ignored by Windows 7 and Windows 8.

 

</dd> <dt>

<span id="BcdLibraryBoolean_AllowPrereleaseSignatures"></span><span id="bcdlibraryboolean_allowprereleasesignatures"></span><span id="BCDLIBRARYBOOLEAN_ALLOWPRERELEASESIGNATURES"></span>**BcdLibraryBoolean\_AllowPrereleaseSignatures**
</dt> <dd>

Indicates whether the test code signing certificate is supported. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryString_FontPath"></span><span id="bcdlibrarystring_fontpath"></span><span id="BCDLIBRARYSTRING_FONTPATH"></span>**BcdLibraryString\_FontPath**
</dt> <dd>

Overrides the default location of the boot fonts. The element data format is [**BcdStringElement**](bcdstringelement.md).

> [!Note]  
> Use caution when modifying this setting. Boot screens will not work if the correct fonts are not present.

 

</dd> <dt>

<span id="BcdLibraryInteger_SiPolicy"></span><span id="bcdlibraryinteger_sipolicy"></span><span id="BCDLIBRARYINTEGER_SIPOLICY"></span>**BcdLibraryInteger\_SiPolicy**
</dt> <dd>

The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryInteger_FveBandId"></span><span id="bcdlibraryinteger_fvebandid"></span><span id="BCDLIBRARYINTEGER_FVEBANDID"></span>**BcdLibraryInteger\_FveBandId**
</dt> <dd>

This value (if present) should not be modified. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryBoolean_ConsoleExtendedInput"></span><span id="bcdlibraryboolean_consoleextendedinput"></span><span id="BCDLIBRARYBOOLEAN_CONSOLEEXTENDEDINPUT"></span>**BcdLibraryBoolean\_ConsoleExtendedInput**
</dt> <dd>

Specifies that legacy BIOS systems should use INT 16h Function 10h for console input instead of INT 16h Function 0h. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value only applies to Windows Vista and Windows 7.

</dd> <dt>

<span id="BcdLibraryInteger_GraphicsResolution"></span><span id="bcdlibraryinteger_graphicsresolution"></span><span id="BCDLIBRARYINTEGER_GRAPHICSRESOLUTION"></span>**BcdLibraryInteger\_GraphicsResolution**
</dt> <dd>

Forces a specific graphics resolution at boot. Possible values include **GraphicsResolution1024x768 (0)**, **GraphicsResolution800x600 (1)**, and **GraphicsResolution1024x600 (2)**. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_RestartOnFailure"></span><span id="bcdlibraryboolean_restartonfailure"></span><span id="BCDLIBRARYBOOLEAN_RESTARTONFAILURE"></span>**BcdLibraryBoolean\_RestartOnFailure**
</dt> <dd>

If enabled, specifies that boot error screens are not shown when OS launch errors occur, and the system is reset rather than exiting directly back to the firmware. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdLibraryBoolean_GraphicsForceHighestMode"></span><span id="bcdlibraryboolean_graphicsforcehighestmode"></span><span id="BCDLIBRARYBOOLEAN_GRAPHICSFORCEHIGHESTMODE"></span>**BcdLibraryBoolean\_GraphicsForceHighestMode**
</dt> <dd>

Forces highest available graphics resolution at boot. This value can only be used on UEFI systems. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryBoolean_IsolatedExecutionContext"></span><span id="bcdlibraryboolean_isolatedexecutioncontext"></span><span id="BCDLIBRARYBOOLEAN_ISOLATEDEXECUTIONCONTEXT"></span>**BcdLibraryBoolean\_IsolatedExecutionContext**
</dt> <dd>

This setting is used to differentiate between the Windows 7 and Windows 8 implementations of UEFI. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

Do not modify this setting. If this setting is removed from a Windows 8 installation, it will not boot. If this setting is added to a Windows 7 installation, it will not boot.

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryBoolean_BootUxDisable"></span><span id="bcdlibraryboolean_bootuxdisable"></span><span id="BCDLIBRARYBOOLEAN_BOOTUXDISABLE"></span>**BcdLibraryBoolean\_BootUxDisable**
</dt> <dd>

This setting disables the progress bar and default Windows logo. If a custom text string has been defined, it is also disabled by this setting. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryBoolean_BootShutdownDisabled"></span><span id="bcdlibraryboolean_bootshutdowndisabled"></span><span id="BCDLIBRARYBOOLEAN_BOOTSHUTDOWNDISABLED"></span>**BcdLibraryBoolean\_BootShutdownDisabled**
</dt> <dd>

Disables the 1-minute timer that triggers shutdown on boot error screens, and the F8 menu, on UEFI systems. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryIntegerList_AllowedInMemorySettings"></span><span id="bcdlibraryintegerlist_allowedinmemorysettings"></span><span id="BCDLIBRARYINTEGERLIST_ALLOWEDINMEMORYSETTINGS"></span>**BcdLibraryIntegerList\_AllowedInMemorySettings**
</dt> <dd>

Indicates whether or not an in-memory BCD setting passed between boot apps will trigger BitLocker recovery. This value should not be modified as it could trigger a BitLocker recovery action. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdLibraryBoolean_ForceFipsCrypto"></span><span id="bcdlibraryboolean_forcefipscrypto"></span><span id="BCDLIBRARYBOOLEAN_FORCEFIPSCRYPTO"></span>**BcdLibraryBoolean\_ForceFipsCrypto**
</dt> <dd>

Force the use of FIPS cryptography checks on boot applications. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdBooleanElement**](bcdbooleanelement.md)
</dt> <dt>

[**BcdIntegerElement**](bcdintegerelement.md)
</dt> <dt>

[**BcdObjectListElement**](bcdobjectlistelement.md)
</dt> <dt>

[**BcdStringElement**](bcdstringelement.md)
</dt> <dt>

[**GetElement**](getelement-bcdobject.md)
</dt> <dt>

[**BcdElementType**](bcdelementtype.md)
</dt> </dl>

 

 





