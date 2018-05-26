---
title: BcdOSLoaderElementTypes enumeration
description: Specifies the operating system loader element types.
ms.assetid: 9c2987c4-50ea-42cd-bed4-6112035c698a
keywords:
- BcdOSLoaderElementTypes enumeration Boot Config
topic_type:
- apiref
api_name:
- BcdOSLoaderElementTypes
api_type:
- NA
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BcdOSLoaderElementTypes enumeration

Specifies the operating system loader element types.

## Syntax


```C++
typedef enum BcdOSLoaderElementTypes { 
  BcdOSLoaderDevice_OSDevice                        = 0x21000001,
  BcdOSLoaderString_SystemRoot                      = 0x22000002,
  BcdOSLoaderObject_AssociatedResumeObject          = 0x23000003,
  BcdOSLoaderBoolean_DetectKernelAndHal             = 0x26000010,
  BcdOSLoaderString_KernelPath                      = 0x22000011,
  BcdOSLoaderString_HalPath                         = 0x22000012,
  BcdOSLoaderString_DbgTransportPath                = 0x22000013,
  BcdOSLoaderInteger_NxPolicy                       = 0x25000020,
  BcdOSLoaderInteger_PAEPolicy                      = 0x25000021,
  BcdOSLoaderBoolean_WinPEMode                      = 0x26000022,
  BcdOSLoaderBoolean_DisableCrashAutoReboot         = 0x26000024,
  BcdOSLoaderBoolean_UseLastGoodSettings            = 0x26000025,
  BcdOSLoaderBoolean_AllowPrereleaseSignatures      = 0x26000027,
  BcdOSLoaderBoolean_NoLowMemory                    = 0x26000030,
  BcdOSLoaderInteger_RemoveMemory                   = 0x25000031,
  BcdOSLoaderInteger_IncreaseUserVa                 = 0x25000032,
  BcdOSLoaderBoolean_UseVgaDriver                   = 0x26000040,
  BcdOSLoaderBoolean_DisableBootDisplay             = 0x26000041,
  BcdOSLoaderBoolean_DisableVesaBios                = 0x26000042,
  BcdOSLoaderBoolean_DisableVgaMode                 = 0x26000043,
  BcdOSLoaderInteger_ClusterModeAddressing          = 0x25000050,
  BcdOSLoaderBoolean_UsePhysicalDestination         = 0x26000051,
  BcdOSLoaderInteger_RestrictApicCluster            = 0x25000052,
  BcdOSLoaderBoolean_UseLegacyApicMode              = 0x26000054,
  BcdOSLoaderInteger_X2ApicPolicy                   = 0x25000055,
  BcdOSLoaderBoolean_UseBootProcessorOnly           = 0x26000060,
  BcdOSLoaderInteger_NumberOfProcessors             = 0x25000061,
  BcdOSLoaderBoolean_ForceMaximumProcessors         = 0x26000062,
  BcdOSLoaderBoolean_ProcessorConfigurationFlags    = 0x25000063,
  BcdOSLoaderBoolean_MaximizeGroupsCreated          = 0x26000064,
  BcdOSLoaderBoolean_ForceGroupAwareness            = 0x26000065,
  BcdOSLoaderInteger_GroupSize                      = 0x25000066,
  BcdOSLoaderInteger_UseFirmwarePciSettings         = 0x26000070,
  BcdOSLoaderInteger_MsiPolicy                      = 0x25000071,
  BcdOSLoaderInteger_SafeBoot                       = 0x25000080,
  BcdOSLoaderBoolean_SafeBootAlternateShell         = 0x26000081,
  BcdOSLoaderBoolean_BootLogInitialization          = 0x26000090,
  BcdOSLoaderBoolean_VerboseObjectLoadMode          = 0x26000091,
  BcdOSLoaderBoolean_KernelDebuggerEnabled          = 0x260000a0,
  BcdOSLoaderBoolean_DebuggerHalBreakpoint          = 0x260000a1,
  BcdOSLoaderBoolean_UsePlatformClock               = 0x260000A2,
  BcdOSLoaderBoolean_ForceLegacyPlatform            = 0x260000A3,
  BcdOSLoaderInteger_TscSyncPolicy                  = 0x250000A6,
  BcdOSLoaderBoolean_EmsEnabled                     = 0x260000b0,
  BcdOSLoaderInteger_DriverLoadFailurePolicy        = 0x250000c1,
  BcdOSLoaderInteger_BootMenuPolicy                 = 0x250000C2,
  BcdOSLoaderBoolean_AdvancedOptionsOneTime         = 0x260000C3,
  BcdOSLoaderInteger_BootStatusPolicy               = 0x250000E0,
  BcdOSLoaderBoolean_DisableElamDrivers             = 0x260000E1,
  BcdOSLoaderInteger_HypervisorLaunchType           = 0x250000F0,
  BcdOSLoaderBoolean_HypervisorDebuggerEnabled      = 0x260000F2,
  BcdOSLoaderInteger_HypervisorDebuggerType         = 0x250000F3,
  BcdOSLoaderInteger_HypervisorDebuggerPortNumber   = 0x250000F4,
  BcdOSLoaderInteger_HypervisorDebuggerBaudrate     = 0x250000F5,
  BcdOSLoaderInteger_HypervisorDebugger1394Channel  = 0x250000F6,
  BcdOSLoaderInteger_BootUxPolicy                   = 0x250000F7,
  BcdOSLoaderString_HypervisorDebuggerBusParams     = 0x220000F9,
  BcdOSLoaderInteger_HypervisorNumProc              = 0x250000FA,
  BcdOSLoaderInteger_HypervisorRootProcPerNode      = 0x250000FB,
  BcdOSLoaderBoolean_HypervisorUseLargeVTlb         = 0x260000FC,
  BcdOSLoaderInteger_HypervisorDebuggerNetHostIp    = 0x250000FD,
  BcdOSLoaderInteger_HypervisorDebuggerNetHostPort  = 0x250000FE,
  BcdOSLoaderInteger_TpmBootEntropyPolicy           = 0x25000100,
  BcdOSLoaderString_HypervisorDebuggerNetKey        = 0x22000110,
  BcdOSLoaderBoolean_HypervisorDebuggerNetDhcp      = 0x26000114,
  BcdOSLoaderInteger_HypervisorIommuPolicy          = 0x25000115,
  BcdOSLoaderInteger_XSaveDisable                   = 0x2500012b
} BcdOSLoaderElementTypes;
```



## Constants

<dl> <dt>

<span id="BcdOSLoaderDevice_OSDevice"></span><span id="bcdosloaderdevice_osdevice"></span><span id="BCDOSLOADERDEVICE_OSDEVICE"></span>**BcdOSLoaderDevice\_OSDevice**
</dt> <dd>

The device on which the operating system resides. The element data format is [**BcdDeviceElement**](bcddeviceelement.md).

</dd> <dt>

<span id="BcdOSLoaderString_SystemRoot"></span><span id="bcdosloaderstring_systemroot"></span><span id="BCDOSLOADERSTRING_SYSTEMROOT"></span>**BcdOSLoaderString\_SystemRoot**
</dt> <dd>

The file path to the operating system (%SystemRoot% minus the volume.) The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdOSLoaderObject_AssociatedResumeObject"></span><span id="bcdosloaderobject_associatedresumeobject"></span><span id="BCDOSLOADEROBJECT_ASSOCIATEDRESUMEOBJECT"></span>**BcdOSLoaderObject\_AssociatedResumeObject**
</dt> <dd>

The resume application associated with the operating system. The element data format is [**BcdObjectElement**](bcdobjectelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_DetectKernelAndHal"></span><span id="bcdosloaderboolean_detectkernelandhal"></span><span id="BCDOSLOADERBOOLEAN_DETECTKERNELANDHAL"></span>**BcdOSLoaderBoolean\_DetectKernelAndHal**
</dt> <dd>

Indicates whether the operating system loader should determine the kernel and HAL to load based on the platform features. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderString_KernelPath"></span><span id="bcdosloaderstring_kernelpath"></span><span id="BCDOSLOADERSTRING_KERNELPATH"></span>**BcdOSLoaderString\_KernelPath**
</dt> <dd>

The kernel to be loaded by the operating system loader. This value overrides the default kernel. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdOSLoaderString_HalPath"></span><span id="bcdosloaderstring_halpath"></span><span id="BCDOSLOADERSTRING_HALPATH"></span>**BcdOSLoaderString\_HalPath**
</dt> <dd>

The HAL to be loaded by the operating system loader. This value overrides the default HAL. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdOSLoaderString_DbgTransportPath"></span><span id="bcdosloaderstring_dbgtransportpath"></span><span id="BCDOSLOADERSTRING_DBGTRANSPORTPATH"></span>**BcdOSLoaderString\_DbgTransportPath**
</dt> <dd>

The transport DLL to be loaded by the operating system loader. This value overrides the default Kdcom.dll. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_NxPolicy"></span><span id="bcdosloaderinteger_nxpolicy"></span><span id="BCDOSLOADERINTEGER_NXPOLICY"></span>**BcdOSLoaderInteger\_NxPolicy**
</dt> <dd>

The no-execute page protection policy. The element data format is [**BcdIntegerElement**](bcdintegerelement.md) and the **Integer** property is one of the values from the [**BcdOSLoader\_NxPolicy**](bcdosloader-nxpolicy.md) enumeration.

If this value is not specified, the default is **NxPolicyAlwaysOff**.

</dd> <dt>

<span id="BcdOSLoaderInteger_PAEPolicy"></span><span id="bcdosloaderinteger_paepolicy"></span><span id="BCDOSLOADERINTEGER_PAEPOLICY"></span>**BcdOSLoaderInteger\_PAEPolicy**
</dt> <dd>

The Physical Address Extension (PAE) policy. The element data format is [**BcdIntegerElement**](bcdintegerelement.md) and the **Integer** property is one of the values from the [**BcdOSLoader\_PAEPolicy**](bcdosloader-paepolicy.md) enumeration.

If this value is not specified, the default is **PaePolicyDefault**.

</dd> <dt>

<span id="BcdOSLoaderBoolean_WinPEMode"></span><span id="bcdosloaderboolean_winpemode"></span><span id="BCDOSLOADERBOOLEAN_WINPEMODE"></span>**BcdOSLoaderBoolean\_WinPEMode**
</dt> <dd>

Indicates that the system should be started in Windows Preinstallation Environment (Windows PE) mode. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_DisableCrashAutoReboot"></span><span id="bcdosloaderboolean_disablecrashautoreboot"></span><span id="BCDOSLOADERBOOLEAN_DISABLECRASHAUTOREBOOT"></span>**BcdOSLoaderBoolean\_DisableCrashAutoReboot**
</dt> <dd>

Indicates that the system should not automatically reboot when it crashes. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_UseLastGoodSettings"></span><span id="bcdosloaderboolean_uselastgoodsettings"></span><span id="BCDOSLOADERBOOLEAN_USELASTGOODSETTINGS"></span>**BcdOSLoaderBoolean\_UseLastGoodSettings**
</dt> <dd>

Indicates that the system should use the last-known good settings. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_AllowPrereleaseSignatures"></span><span id="bcdosloaderboolean_allowprereleasesignatures"></span><span id="BCDOSLOADERBOOLEAN_ALLOWPRERELEASESIGNATURES"></span>**BcdOSLoaderBoolean\_AllowPrereleaseSignatures**
</dt> <dd>

Indicates whether the test code signing certificate is supported. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is not supported in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderBoolean_NoLowMemory"></span><span id="bcdosloaderboolean_nolowmemory"></span><span id="BCDOSLOADERBOOLEAN_NOLOWMEMORY"></span>**BcdOSLoaderBoolean\_NoLowMemory**
</dt> <dd>

Indicates whether the system should utilize the first 4GB of physical memory. This option requires 5GB of physical memory, and on x86 systems it requires PAE to be enabled. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_RemoveMemory"></span><span id="bcdosloaderinteger_removememory"></span><span id="BCDOSLOADERINTEGER_REMOVEMEMORY"></span>**BcdOSLoaderInteger\_RemoveMemory**
</dt> <dd>

The amount of memory the system should ignore. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_IncreaseUserVa"></span><span id="bcdosloaderinteger_increaseuserva"></span><span id="BCDOSLOADERINTEGER_INCREASEUSERVA"></span>**BcdOSLoaderInteger\_IncreaseUserVa**
</dt> <dd>

The amount of memory that should be utilized by the process address space, in bytes. This value should be between 2GB and 3GB. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

Increasing this value from the default 2GB decreases the amount of virtual address space available to the system and device drivers.

</dd> <dt>

<span id="BcdOSLoaderBoolean_UseVgaDriver"></span><span id="bcdosloaderboolean_usevgadriver"></span><span id="BCDOSLOADERBOOLEAN_USEVGADRIVER"></span>**BcdOSLoaderBoolean\_UseVgaDriver**
</dt> <dd>

Indicates whether the system should use the standard VGA display driver instead of a high-performance display driver. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_DisableBootDisplay"></span><span id="bcdosloaderboolean_disablebootdisplay"></span><span id="BCDOSLOADERBOOLEAN_DISABLEBOOTDISPLAY"></span>**BcdOSLoaderBoolean\_DisableBootDisplay**
</dt> <dd>

Indicates whether the system should initialize the VGA driver responsible for displaying simple graphics during the boot process. If not, there is no display is presented during the boot process. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value should not be used in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderBoolean_DisableVesaBios"></span><span id="bcdosloaderboolean_disablevesabios"></span><span id="BCDOSLOADERBOOLEAN_DISABLEVESABIOS"></span>**BcdOSLoaderBoolean\_DisableVesaBios**
</dt> <dd>

Indicates whether the VGA driver should avoid VESA BIOS calls. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is ignored by Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderBoolean_DisableVgaMode"></span><span id="bcdosloaderboolean_disablevgamode"></span><span id="BCDOSLOADERBOOLEAN_DISABLEVGAMODE"></span>**BcdOSLoaderBoolean\_DisableVgaMode**
</dt> <dd>

Disables the use of VGA modes in the OS. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_ClusterModeAddressing"></span><span id="bcdosloaderinteger_clustermodeaddressing"></span><span id="BCDOSLOADERINTEGER_CLUSTERMODEADDRESSING"></span>**BcdOSLoaderInteger\_ClusterModeAddressing**
</dt> <dd>

Indicates that cluster-mode APIC addressing should be utilized, and the value is the maximum number of processors per cluster. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_UsePhysicalDestination"></span><span id="bcdosloaderboolean_usephysicaldestination"></span><span id="BCDOSLOADERBOOLEAN_USEPHYSICALDESTINATION"></span>**BcdOSLoaderBoolean\_UsePhysicalDestination**
</dt> <dd>

Indicates whether to enable physical-destination mode for all APIC messages. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_RestrictApicCluster"></span><span id="bcdosloaderinteger_restrictapiccluster"></span><span id="BCDOSLOADERINTEGER_RESTRICTAPICCLUSTER"></span>**BcdOSLoaderInteger\_RestrictApicCluster**
</dt> <dd>

The maximum number of APIC clusters that should be used by cluster-mode addressing. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_UseLegacyApicMode"></span><span id="bcdosloaderboolean_uselegacyapicmode"></span><span id="BCDOSLOADERBOOLEAN_USELEGACYAPICMODE"></span>**BcdOSLoaderBoolean\_UseLegacyApicMode**
</dt> <dd>

Used to force legacy APIC mode, even if the processors and chipset support extended APIC mode. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_X2ApicPolicy"></span><span id="bcdosloaderinteger_x2apicpolicy"></span><span id="BCDOSLOADERINTEGER_X2APICPOLICY"></span>**BcdOSLoaderInteger\_X2ApicPolicy**
</dt> <dd>

Enables the use of extended APIC mode, if supported. Zero (0) indicates default behavior, one (1) indicates that extended APIC mode is disabled, and two (2) indicates that extended APIC mode is enabled. The system defaults to using extended APIC mode if available. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_UseBootProcessorOnly"></span><span id="bcdosloaderboolean_usebootprocessoronly"></span><span id="BCDOSLOADERBOOLEAN_USEBOOTPROCESSORONLY"></span>**BcdOSLoaderBoolean\_UseBootProcessorOnly**
</dt> <dd>

Indicates whether the operating system should initialize or start non-boot processors. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_NumberOfProcessors"></span><span id="bcdosloaderinteger_numberofprocessors"></span><span id="BCDOSLOADERINTEGER_NUMBEROFPROCESSORS"></span>**BcdOSLoaderInteger\_NumberOfProcessors**
</dt> <dd>

The maximum number of processors that can be utilized by the system; all other processors are ignored. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_ForceMaximumProcessors"></span><span id="bcdosloaderboolean_forcemaximumprocessors"></span><span id="BCDOSLOADERBOOLEAN_FORCEMAXIMUMPROCESSORS"></span>**BcdOSLoaderBoolean\_ForceMaximumProcessors**
</dt> <dd>

Indicates whether the system should use the maximum number of processors. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_ProcessorConfigurationFlags"></span><span id="bcdosloaderboolean_processorconfigurationflags"></span><span id="BCDOSLOADERBOOLEAN_PROCESSORCONFIGURATIONFLAGS"></span>**BcdOSLoaderBoolean\_ProcessorConfigurationFlags**
</dt> <dd>

Indicates whether processor specific configuration flags are to be used. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_MaximizeGroupsCreated"></span><span id="bcdosloaderboolean_maximizegroupscreated"></span><span id="BCDOSLOADERBOOLEAN_MAXIMIZEGROUPSCREATED"></span>**BcdOSLoaderBoolean\_MaximizeGroupsCreated**
</dt> <dd>

Maximizes the number of groups created when assigning nodes to processor groups. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_ForceGroupAwareness"></span><span id="bcdosloaderboolean_forcegroupawareness"></span><span id="BCDOSLOADERBOOLEAN_FORCEGROUPAWARENESS"></span>**BcdOSLoaderBoolean\_ForceGroupAwareness**
</dt> <dd>

This setting makes drivers group aware and can be used to determine improper group usage. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_GroupSize"></span><span id="bcdosloaderinteger_groupsize"></span><span id="BCDOSLOADERINTEGER_GROUPSIZE"></span>**BcdOSLoaderInteger\_GroupSize**
</dt> <dd>

Specifies the size of all processor groups. Must be set to a power of 2. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_UseFirmwarePciSettings"></span><span id="bcdosloaderinteger_usefirmwarepcisettings"></span><span id="BCDOSLOADERINTEGER_USEFIRMWAREPCISETTINGS"></span>**BcdOSLoaderInteger\_UseFirmwarePciSettings**
</dt> <dd>

Indicates whether the system should use I/O and IRQ resources created by the system firmware instead of using dynamically configured resources. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_MsiPolicy"></span><span id="bcdosloaderinteger_msipolicy"></span><span id="BCDOSLOADERINTEGER_MSIPOLICY"></span>**BcdOSLoaderInteger\_MsiPolicy**
</dt> <dd>

The PCI Message Signaled Interrupt (MSI) policy. Zero (0) indicates default, and one (1) indicates that MSI interrupts are disabled. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_SafeBoot"></span><span id="bcdosloaderinteger_safeboot"></span><span id="BCDOSLOADERINTEGER_SAFEBOOT"></span>**BcdOSLoaderInteger\_SafeBoot**
</dt> <dd>

The element data format is [**BcdIntegerElement**](bcdintegerelement.md) and the **Integer** property is one of the values from the [**BcdLibrary\_SafeBoot**](bcdlibrary-safeboot.md) enumeration.

</dd> <dt>

<span id="BcdOSLoaderBoolean_SafeBootAlternateShell"></span><span id="bcdosloaderboolean_safebootalternateshell"></span><span id="BCDOSLOADERBOOLEAN_SAFEBOOTALTERNATESHELL"></span>**BcdOSLoaderBoolean\_SafeBootAlternateShell**
</dt> <dd>

Indicates whether the system should use the shell specified under the following registry key instead of the default shell: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\AlternateShell**. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_BootLogInitialization"></span><span id="bcdosloaderboolean_bootloginitialization"></span><span id="BCDOSLOADERBOOLEAN_BOOTLOGINITIALIZATION"></span>**BcdOSLoaderBoolean\_BootLogInitialization**
</dt> <dd>

Indicates whether the system should write logging information to %SystemRoot%\\Ntbtlog.txt during initialization. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_VerboseObjectLoadMode"></span><span id="bcdosloaderboolean_verboseobjectloadmode"></span><span id="BCDOSLOADERBOOLEAN_VERBOSEOBJECTLOADMODE"></span>**BcdOSLoaderBoolean\_VerboseObjectLoadMode**
</dt> <dd>

Indicates whether the system should display verbose information. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_KernelDebuggerEnabled"></span><span id="bcdosloaderboolean_kerneldebuggerenabled"></span><span id="BCDOSLOADERBOOLEAN_KERNELDEBUGGERENABLED"></span>**BcdOSLoaderBoolean\_KernelDebuggerEnabled**
</dt> <dd>

Indicates whether the kernel debugger should be enabled using the settings in the inherited debugger object. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_DebuggerHalBreakpoint"></span><span id="bcdosloaderboolean_debuggerhalbreakpoint"></span><span id="BCDOSLOADERBOOLEAN_DEBUGGERHALBREAKPOINT"></span>**BcdOSLoaderBoolean\_DebuggerHalBreakpoint**
</dt> <dd>

Indicates whether the HAL should call **DbgBreakPoint** at the start of **HalInitSystem** for phase 0 initialization of the kernel. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_UsePlatformClock"></span><span id="bcdosloaderboolean_useplatformclock"></span><span id="BCDOSLOADERBOOLEAN_USEPLATFORMCLOCK"></span>**BcdOSLoaderBoolean\_UsePlatformClock**
</dt> <dd>

Forces the use of the platform clock as the system's performance counter. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

> [!Note]  
> This value should only be used for debugging.

 

</dd> <dt>

<span id="BcdOSLoaderBoolean_ForceLegacyPlatform"></span><span id="bcdosloaderboolean_forcelegacyplatform"></span><span id="BCDOSLOADERBOOLEAN_FORCELEGACYPLATFORM"></span>**BcdOSLoaderBoolean\_ForceLegacyPlatform**
</dt> <dd>

Forces the OS to assume the presence of legacy PC devices like CMOS and keyboard controllers. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

> [!Note]  
> This value should only be used for debugging.

 

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_TscSyncPolicy"></span><span id="bcdosloaderinteger_tscsyncpolicy"></span><span id="BCDOSLOADERINTEGER_TSCSYNCPOLICY"></span>**BcdOSLoaderInteger\_TscSyncPolicy**
</dt> <dd>

> [!Note]  
> This value should only be used for debugging.

 

Controls the TSC synchronization policy. Possible values include default (0), legacy (1), or enhanced (2). The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderBoolean_EmsEnabled"></span><span id="bcdosloaderboolean_emsenabled"></span><span id="BCDOSLOADERBOOLEAN_EMSENABLED"></span>**BcdOSLoaderBoolean\_EmsEnabled**
</dt> <dd>

Indicates whether EMS should be enabled in the kernel. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_DriverLoadFailurePolicy"></span><span id="bcdosloaderinteger_driverloadfailurepolicy"></span><span id="BCDOSLOADERINTEGER_DRIVERLOADFAILUREPOLICY"></span>**BcdOSLoaderInteger\_DriverLoadFailurePolicy**
</dt> <dd>

Indicates the driver load failure policy. Zero (0) indicates that a failed driver load is fatal and the boot will not continue, one (1) indicates that the standard error control is used. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_BootMenuPolicy"></span><span id="bcdosloaderinteger_bootmenupolicy"></span><span id="BCDOSLOADERINTEGER_BOOTMENUPOLICY"></span>**BcdOSLoaderInteger\_BootMenuPolicy**
</dt> <dd>

Defines the type of boot menus the system will use. Possible values include **menupolicylegacy (0)** or **menupolicystandard (1)**. The default value is **menupolicylegacy (0)**. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderBoolean_AdvancedOptionsOneTime"></span><span id="bcdosloaderboolean_advancedoptionsonetime"></span><span id="BCDOSLOADERBOOLEAN_ADVANCEDOPTIONSONETIME"></span>**BcdOSLoaderBoolean\_AdvancedOptionsOneTime**
</dt> <dd>

Controls whether the system boots to the legacy menu (F8 menu) on the next boot. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_BootStatusPolicy"></span><span id="bcdosloaderinteger_bootstatuspolicy"></span><span id="BCDOSLOADERINTEGER_BOOTSTATUSPOLICY"></span>**BcdOSLoaderInteger\_BootStatusPolicy**
</dt> <dd>

The boot status policy. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).



| Term                                                                                                                                                                                                                                                     | Description                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <span id="BootStatusPolicyDisplayAllFailures__0_"></span><span id="bootstatuspolicydisplayallfailures__0_"></span><span id="BOOTSTATUSPOLICYDISPLAYALLFAILURES__0_"></span>BootStatusPolicyDisplayAllFailures (0)<br/>                             | Display all boot failures.<br/>    |
| <span id="BootStatusPolicyIgnoreAllFailures__1_"></span><span id="bootstatuspolicyignoreallfailures__1_"></span><span id="BOOTSTATUSPOLICYIGNOREALLFAILURES__1_"></span>BootStatusPolicyIgnoreAllFailures (1)<br/>                                 | Ignore all boot failures.<br/>     |
| <span id="BootStatusPolicyIgnoreShutdownFailures__2_"></span><span id="bootstatuspolicyignoreshutdownfailures__2_"></span><span id="BOOTSTATUSPOLICYIGNORESHUTDOWNFAILURES__2_"></span>BootStatusPolicyIgnoreShutdownFailures (2)<br/>             | Ignore all shutdown failures.<br/> |
| <span id="BootStatusPolicyIgnoreBootFailures__3_"></span><span id="bootstatuspolicyignorebootfailures__3_"></span><span id="BOOTSTATUSPOLICYIGNOREBOOTFAILURES__3_"></span>BootStatusPolicyIgnoreBootFailures (3)<br/>                             | Ignore all boot failures.<br/>     |
| <span id="BootStatusPolicyIgnoreCheckpointFailures__4_"></span><span id="bootstatuspolicyignorecheckpointfailures__4_"></span><span id="BOOTSTATUSPOLICYIGNORECHECKPOINTFAILURES__4_"></span>BootStatusPolicyIgnoreCheckpointFailures (4)<br/>     | Ignore checkpoint failures.<br/>   |
| <span id="BootStatusPolicyDisplayShutdownFailures__5_"></span><span id="bootstatuspolicydisplayshutdownfailures__5_"></span><span id="BOOTSTATUSPOLICYDISPLAYSHUTDOWNFAILURES__5_"></span>BootStatusPolicyDisplayShutdownFailures (5)<br/>         | Display shutdown failures.<br/>    |
| <span id="BootStatusPolicyDisplayBootFailures__6_"></span><span id="bootstatuspolicydisplaybootfailures__6_"></span><span id="BOOTSTATUSPOLICYDISPLAYBOOTFAILURES__6_"></span>BootStatusPolicyDisplayBootFailures (6)<br/>                         | Display boot failures.<br/>        |
| <span id="BootStatusPolicyDisplayCheckpointFailures__7_"></span><span id="bootstatuspolicydisplaycheckpointfailures__7_"></span><span id="BOOTSTATUSPOLICYDISPLAYCHECKPOINTFAILURES__7_"></span>BootStatusPolicyDisplayCheckpointFailures (7)<br/> | Display checkpoint failures.<br/>  |



 

</dd> <dt>

<span id="BcdOSLoaderBoolean_DisableElamDrivers"></span><span id="bcdosloaderboolean_disableelamdrivers"></span><span id="BCDOSLOADERBOOLEAN_DISABLEELAMDRIVERS"></span>**BcdOSLoaderBoolean\_DisableElamDrivers**
</dt> <dd>

The OS loader removes this entry for security reasons. This option can only be triggered by using the F8 menu; a user must be physically present to trigger this option. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorLaunchType"></span><span id="bcdosloaderinteger_hypervisorlaunchtype"></span><span id="BCDOSLOADERINTEGER_HYPERVISORLAUNCHTYPE"></span>**BcdOSLoaderInteger\_HypervisorLaunchType**
</dt> <dd>

Controls the hypervisor launch type. Options are **HyperVisorLaunchOff (0)** and **HypervisorLaunchAuto (1)**. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderBoolean_HypervisorDebuggerEnabled"></span><span id="bcdosloaderboolean_hypervisordebuggerenabled"></span><span id="BCDOSLOADERBOOLEAN_HYPERVISORDEBUGGERENABLED"></span>**BcdOSLoaderBoolean\_HypervisorDebuggerEnabled**
</dt> <dd>

Controls whether the hypervisor debugger is enabled. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorDebuggerType"></span><span id="bcdosloaderinteger_hypervisordebuggertype"></span><span id="BCDOSLOADERINTEGER_HYPERVISORDEBUGGERTYPE"></span>**BcdOSLoaderInteger\_HypervisorDebuggerType**
</dt> <dd>

Controls the hypervisor debugger type. Can be set to **SERIAL (0)**, **1394 (1)**, or **NET (2)**. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorDebuggerPortNumber"></span><span id="bcdosloaderinteger_hypervisordebuggerportnumber"></span><span id="BCDOSLOADERINTEGER_HYPERVISORDEBUGGERPORTNUMBER"></span>**BcdOSLoaderInteger\_HypervisorDebuggerPortNumber**
</dt> <dd>

Specifies the serial port number for serial debugging. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the default is specified by the DBGP ACPI table settings.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorDebuggerBaudrate"></span><span id="bcdosloaderinteger_hypervisordebuggerbaudrate"></span><span id="BCDOSLOADERINTEGER_HYPERVISORDEBUGGERBAUDRATE"></span>**BcdOSLoaderInteger\_HypervisorDebuggerBaudrate**
</dt> <dd>

Specifies the baud rate for serial debugging. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the default is specified by the DBGP ACPI table settings.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorDebugger1394Channel"></span><span id="bcdosloaderinteger_hypervisordebugger1394channel"></span><span id="BCDOSLOADERINTEGER_HYPERVISORDEBUGGER1394CHANNEL"></span>**BcdOSLoaderInteger\_HypervisorDebugger1394Channel**
</dt> <dd>

Specifies the channel number for 1394 debugging. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdOSLoaderInteger_BootUxPolicy"></span><span id="bcdosloaderinteger_bootuxpolicy"></span><span id="BCDOSLOADERINTEGER_BOOTUXPOLICY"></span>**BcdOSLoaderInteger\_BootUxPolicy**
</dt> <dd>

Values are Disabled (0), Basic (1), and Standard (2). The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is no longer used in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderString_HypervisorDebuggerBusParams"></span><span id="bcdosloaderstring_hypervisordebuggerbusparams"></span><span id="BCDOSLOADERSTRING_HYPERVISORDEBUGGERBUSPARAMS"></span>**BcdOSLoaderString\_HypervisorDebuggerBusParams**
</dt> <dd>

Defines the PCI bus, device, and function numbers of the debugging device used with the hypervisor. For example, 1.5.0 describes the debugging device on bus 1, device 5, function 0. The element data format is [**BcdStringElement**](bcdstringelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorNumProc"></span><span id="bcdosloaderinteger_hypervisornumproc"></span><span id="BCDOSLOADERINTEGER_HYPERVISORNUMPROC"></span>**BcdOSLoaderInteger\_HypervisorNumProc**
</dt> <dd>

Specifies the total number of logical processors that can be started in the hypervisor. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorRootProcPerNode"></span><span id="bcdosloaderinteger_hypervisorrootprocpernode"></span><span id="BCDOSLOADERINTEGER_HYPERVISORROOTPROCPERNODE"></span>**BcdOSLoaderInteger\_HypervisorRootProcPerNode**
</dt> <dd>

Specifies the total number of virtual processors in the root partition that can be started within a pre-split Non-Uniform Memory Architecture (NUMA) node. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderBoolean_HypervisorUseLargeVTlb"></span><span id="bcdosloaderboolean_hypervisoruselargevtlb"></span><span id="BCDOSLOADERBOOLEAN_HYPERVISORUSELARGEVTLB"></span>**BcdOSLoaderBoolean\_HypervisorUseLargeVTlb**
</dt> <dd>

Increases virtual Translation Lookaside Buffer (TLB) size. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorDebuggerNetHostIp"></span><span id="bcdosloaderinteger_hypervisordebuggernethostip"></span><span id="BCDOSLOADERINTEGER_HYPERVISORDEBUGGERNETHOSTIP"></span>**BcdOSLoaderInteger\_HypervisorDebuggerNetHostIp**
</dt> <dd>

Defines the host IPv4 address for the network debugger. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorDebuggerNetHostPort"></span><span id="bcdosloaderinteger_hypervisordebuggernethostport"></span><span id="BCDOSLOADERINTEGER_HYPERVISORDEBUGGERNETHOSTPORT"></span>**BcdOSLoaderInteger\_HypervisorDebuggerNetHostPort**
</dt> <dd>

Defines the network UDP port for the network debugger. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_TpmBootEntropyPolicy"></span><span id="bcdosloaderinteger_tpmbootentropypolicy"></span><span id="BCDOSLOADERINTEGER_TPMBOOTENTROPYPOLICY"></span>**BcdOSLoaderInteger\_TpmBootEntropyPolicy**
</dt> <dd>

Determines whether entropy is gathered from the trusted platform module (TPM) to help seed the random number generator in the OS. The element data format is [**BcdIntegerElement**](bcdintegerelement.md). Possible values are **default (0)**, **forcedisable (1)**, and **forceenable (2)**.

</dd> <dt>

<span id="BcdOSLoaderString_HypervisorDebuggerNetKey"></span><span id="bcdosloaderstring_hypervisordebuggernetkey"></span><span id="BCDOSLOADERSTRING_HYPERVISORDEBUGGERNETKEY"></span>**BcdOSLoaderString\_HypervisorDebuggerNetKey**
</dt> <dd>

Holds the key used to encrypt the network debug connection used with the hypervisor. The element data format is [**BcdStringElement**](bcdstringelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderBoolean_HypervisorDebuggerNetDhcp"></span><span id="bcdosloaderboolean_hypervisordebuggernetdhcp"></span><span id="BCDOSLOADERBOOLEAN_HYPERVISORDEBUGGERNETDHCP"></span>**BcdOSLoaderBoolean\_HypervisorDebuggerNetDhcp**
</dt> <dd>

Controls use of DHCP by the network debugger used with the hypervisor. Setting this to false forces local link only address. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_HypervisorIommuPolicy"></span><span id="bcdosloaderinteger_hypervisoriommupolicy"></span><span id="BCDOSLOADERINTEGER_HYPERVISORIOMMUPOLICY"></span>**BcdOSLoaderInteger\_HypervisorIommuPolicy**
</dt> <dd>

Controls whether the hypervisor uses an Input Output Memory Management Unit (IOMMU). The element data format is [**BcdIntegerElement**](bcdintegerelement.md). Possible values are **default (0)**, **enable (1)**, and **disable (2)**.

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdOSLoaderInteger_XSaveDisable"></span><span id="bcdosloaderinteger_xsavedisable"></span><span id="BCDOSLOADERINTEGER_XSAVEDISABLE"></span>**BcdOSLoaderInteger\_XSaveDisable**
</dt> <dd>

When set to a value other than zero (0), disables XSAVE functionality in the kernel. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdBooleanElement**](bcdbooleanelement.md)
</dt> <dt>

[**BcdIntegerElement**](bcdintegerelement.md)
</dt> <dt>

[**BcdStringElement**](bcdstringelement.md)
</dt> <dt>

[**GetElement**](getelement-bcdobject.md)
</dt> <dt>

[**BcdElementType**](bcdelementtype.md)
</dt> </dl>

 

 





