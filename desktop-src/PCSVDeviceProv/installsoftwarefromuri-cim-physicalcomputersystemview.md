---
Description: An extrinsic method for installing software on this physical computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c58e60cb-d065-40b5-87ad-d2eaddc702ac
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: InstallSoftwareFromURI method of the CIM\_PhysicalComputerSystemView class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# InstallSoftwareFromURI method of the CIM\_PhysicalComputerSystemView class

An extrinsic method for installing software on this physical computer system. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. The return value shall be 1 if the request is not supported, and 2 if an error occurred. If 4096 is returned, a ConcreteJob will be started to to perform the install. The Job's reference will be returned in the output parameter Job.

## Syntax


```mof
uint32 InstallSoftwareFromURI(
  [in, out] CIM_ConcreteJob REF Job,
  [in]      uint16              Classifications[],
  [in]      string              URI,
  [in]      uint16              InstallOptions[],
  [in]      string              InstallOptionsValues[]
);
```



## Parameters

<dl> <dt>

*Job* \[in, out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*Classifications* \[in\]
</dt> <dd>

See CIM\_SoftwareIdentity.Classifications for details.

<dt>

<span id="Firmware"></span><span id="firmware"></span><span id="FIRMWARE"></span>

**Firmware** (10)


</dt> <dd></dd> <dt>

<span id="BIOS_FCode"></span><span id="bios_fcode"></span><span id="BIOS_FCODE"></span>

**BIOS/FCode** (11)


</dt> <dd></dd> <dt>

<span id="Software_Bundle"></span><span id="software_bundle"></span><span id="SOFTWARE_BUNDLE"></span>

**Software Bundle** (13)


</dt> <dd></dd> <dt>

<span id="Management_Firmware"></span><span id="management_firmware"></span><span id="MANAGEMENT_FIRMWARE"></span>

**Management Firmware** (14)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>15 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*URI* \[in\]
</dt> <dd>

See CIM\_SoftwareInstallationService.InstallFromURI.URI for details.

</dd> <dt>

*InstallOptions* \[in\]
</dt> <dd>

See CIM\_SoftwareInstallationService.InstallFromURI.InstallOptions for details.

<dt>

<span id="Defer_target_system_reset"></span><span id="defer_target_system_reset"></span><span id="DEFER_TARGET_SYSTEM_RESET"></span>

**Defer target/system reset** (2)


</dt> <dd></dd> <dt>

<span id="Force_installation"></span><span id="force_installation"></span><span id="FORCE_INSTALLATION"></span>

**Force installation** (3)


</dt> <dd></dd> <dt>

<span id="Install"></span><span id="install"></span><span id="INSTALL"></span>

**Install** (4)


</dt> <dd></dd> <dt>

<span id="Update"></span><span id="update"></span><span id="UPDATE"></span>

**Update** (5)


</dt> <dd></dd> <dt>

<span id="Repair"></span><span id="repair"></span><span id="REPAIR"></span>

**Repair** (6)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (7)


</dt> <dd></dd> <dt>

<span id="Password"></span><span id="password"></span><span id="PASSWORD"></span>

**Password** (8)


</dt> <dd></dd> <dt>

<span id="Uninstall"></span><span id="uninstall"></span><span id="UNINSTALL"></span>

**Uninstall** (9)


</dt> <dd></dd> <dt>

<span id="Log"></span><span id="log"></span><span id="LOG"></span>

**Log** (10)


</dt> <dd></dd> <dt>

<span id="SilentMode"></span><span id="silentmode"></span><span id="SILENTMODE"></span>

**SilentMode** (11)


</dt> <dd></dd> <dt>

<span id="AdministrativeMode"></span><span id="administrativemode"></span><span id="ADMINISTRATIVEMODE"></span>

**AdministrativeMode** (12)


</dt> <dd></dd> <dt>

<span id="ScheduleInstallAt"></span><span id="scheduleinstallat"></span><span id="SCHEDULEINSTALLAT"></span>

**ScheduleInstallAt** (13)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>14 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*InstallOptionsValues* \[in\]
</dt> <dd>

See CIM\_SoftwareInstallationService.InstallFromURI.InstallOptionsValues for details.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Job Started** (4096)
</dt> <dt>

**DMTF Reserved** (4097 32767)
</dt> <dt>

**Vendor Reserved** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PhysicalComputerSystemView**](cim-physicalcomputersystemview.md)
</dt> </dl>

 

 




