---
description: Attempts to provision the TPM to a completely ready state and will take the ownership of TPM if it is not already owned.
ms.assetid: D0C09A48-00D0-4BF2-8F0A-451A61EA7810
title: Win32_Tpm::Provision method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.Provision
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# Win32\_Tpm::Provision method

Attempts to provision the TPM to a completely ready state and will take the ownership of TPM if it is not already owned. This method is expensive to execute because it performs many checks. It is recommended applications use this method only when necessary.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 Provision(
  [in]  BOOL   ForceClear_Allowed,
  [in]  BOOL   PhysicalPresencePrompts_Allowed,
  [out] uint32 Information
);
```



## Parameters

<dl> <dt>

*ForceClear\_Allowed* \[in\]
</dt> <dd>

When set to **TRUE** the method may request physical presence operations to clear the TPM. If set to **FALSE**, the method will not request a physical presence operation to clear the TPM.

</dd> <dt>

*PhysicalPresencePrompts\_Allowed* \[in\]
</dt> <dd>

When set to **TRUE** the method may request physical presence operations that require user involvement during the boot process to confirm the TPM state change.

</dd> <dt>

*Information* \[out\]
</dt> <dd>

Returns a bitmask of as much information as is available of what is needed to fully provision the TPM. Mask values like INFORMATION\_REBOOT indicate the method call should initiate a reboot to move the provisioning process forwards.

The *Information* parameter may consist of the following values.



| Value                                                                                                                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INFORMATION_SHUTDOWN"></span><span id="information_shutdown"></span><dl> <dt>**INFORMATION\_SHUTDOWN**</dt> <dt>0x00000002</dt> </dl>                                                 | Platform restart is required (shutdown).<br/>                                                                                                                                                                                    |
| <span id="INFORMATION_REBOOT"></span><span id="information_reboot"></span><dl> <dt>**INFORMATION\_REBOOT**</dt> <dt>0x00000004</dt> </dl>                                                       | Platform restart is required (reboot).<br/>                                                                                                                                                                                      |
| <span id="INFORMATION_TPM_FORCE_CLEAR"></span><span id="information_tpm_force_clear"></span><dl> <dt>**INFORMATION\_TPM\_FORCE\_CLEAR**</dt> <dt>0x00000008</dt> </dl>                          | The TPM is already owned. Either the TPM needs to be cleared or the TPM owner authorization value needs to be imported.<br/>                                                                                                     |
| <span id="INFORMATION_PHYSICAL_PRESENCE"></span><span id="information_physical_presence"></span><dl> <dt>**INFORMATION\_PHYSICAL\_PRESENCE**</dt> <dt>0x00000010</dt> </dl>                     | Physical Presence is required to provision the TPM.<br/>                                                                                                                                                                         |
| <span id="INFORMATION_TPM_ACTIVATE"></span><span id="information_tpm_activate"></span><dl> <dt>**INFORMATION\_TPM\_ACTIVATE**</dt> <dt>0x00000020</dt> </dl>                                    | The TPM is disabled or deactivated.<br/>                                                                                                                                                                                         |
| <span id="INFORMATION_TPM_TAKE_OWNERSHIP"></span><span id="information_tpm_take_ownership"></span><dl> <dt>**INFORMATION\_TPM\_TAKE\_OWNERSHIP**</dt> <dt>0x00000040</dt> </dl>                 | The TPM ownership was taken.<br/>                                                                                                                                                                                                |
| <span id="INFORMATION_TPM_CREATE_EK"></span><span id="information_tpm_create_ek"></span><dl> <dt>**INFORMATION\_TPM\_CREATE\_EK**</dt> <dt>0x00000080</dt> </dl>                                | An Endorsement Key (EK) exists in the TPM. <br/>                                                                                                                                                                                 |
| <span id="INFORMATION_TPM_OWNERAUTH"></span><span id="information_tpm_ownerauth"></span><dl> <dt>**INFORMATION\_TPM\_OWNERAUTH**</dt> <dt>0x00000100</dt> </dl>                                 | The TPM owner authorization is not properly stored in the registry.<br/>                                                                                                                                                         |
| <span id="INFORMATION_TPM_SRK_AUTH"></span><span id="information_tpm_srk_auth"></span><dl> <dt>**INFORMATION\_TPM\_SRK\_AUTH**</dt> <dt>0x000000200</dt> </dl>                                  | The Storage Root Key (SRK) authorization value is not all zeros.<br/>                                                                                                                                                            |
| <span id="INFORMATION_TPM_DISABLE_OWNER_CLEAR"></span><span id="information_tpm_disable_owner_clear"></span><dl> <dt>**INFORMATION\_TPM\_DISABLE\_OWNER\_CLEAR**</dt> <dt>0x00000400</dt> </dl> | If the operating system is configured to disable clearing of the TPM with the TPM owner authorization value and the TPM has not yet been configured to prevent clearing of the TPM with the TPM owner authorization value .<br/> |
| <span id="INFORMATION_TPM_SRKPUB"></span><span id="information_tpm_srkpub"></span><dl> <dt>**INFORMATION\_TPM\_SRKPUB**</dt> <dt>0x00000800</dt> </dl>                                          | The operating system's registry information about the TPM’s Storage Root Key does not match the TPM Storage Root Key.<br/>                                                                                                       |
| <span id="INFORMATION_TPM_READ_SRKPUB"></span><span id="information_tpm_read_srkpub"></span><dl> <dt>**INFORMATION\_TPM\_READ\_SRKPUB**</dt> <dt>0x00001000</dt> </dl>                          | The TPM permanent flag to allow reading of the Storage Root Key public value is not set.<br/>                                                                                                                                    |
| <span id="INFORMATION_TPM_BOOT_COUNTER"></span><span id="information_tpm_boot_counter"></span><dl> <dt>**INFORMATION\_TPM\_BOOT\_COUNTER**</dt> <dt>0x00002000</dt> </dl>                       | The monotonic counter incremented during boot has not been created.<br/>                                                                                                                                                         |
| <span id="INFORMATION_TPM_AD_BACKUP"></span><span id="information_tpm_ad_backup"></span><dl> <dt>**INFORMATION\_TPM\_AD\_BACKUP**</dt> <dt>0x00004000</dt> </dl>                                | The TPM’s owner authorization has not been backed up to Active Directory.<br/>                                                                                                                                                   |
| <span id="INFORMATION_TPM_AD_BACKUP_PHASE_I"></span><span id="information_tpm_ad_backup_phase_i"></span><dl> <dt>**INFORMATION\_TPM\_AD\_BACKUP\_PHASE\_I**</dt> <dt>0x00008000</dt> </dl>      | The first portion of the TPM owner authorization information storage in Active Directory is in progress.<br/>                                                                                                                    |
| <span id="INFORMATION_TPM_AD_BACKUP_PHASE_II"></span><span id="information_tpm_ad_backup_phase_ii"></span><dl> <dt>**INFORMATION\_TPM\_AD\_BACKUP\_PHASE\_II**</dt> <dt>0x00010000</dt> </dl>   | The second portion of the TPM owner authorization information storage in Active Directory is in progress.<br/>                                                                                                                   |
| <span id="INFORMATION_LEGACY_CONFIGURATION"></span><span id="information_legacy_configuration"></span><dl> <dt>**INFORMATION\_LEGACY\_CONFIGURATION**</dt> <dt>0x00020000</dt> </dl>            | Windows Group Policy is configured to not store any TPM owner authorization so the TPM cannot be fully ready.<br/>                                                                                                               |
| <span id="INFORMATION_EK_CERTIFICATE"></span><span id="information_ek_certificate"></span><dl> <dt>**INFORMATION\_EK\_CERTIFICATE**</dt> <dt>0x00040000</dt> </dl>                              | The EK Certificate was not read from the TPM NV Ram and stored in the registry. <br/>                                                                                                                                            |
| <span id="INFORMATION_TCG_EVENT_LOG"></span><span id="information_tcg_event_log"></span><dl> <dt>**INFORMATION\_TCG\_EVENT\_LOG**</dt> <dt>0x00080000</dt> </dl>                                | The TCG event log is empty or cannot be read. <br/>                                                                                                                                                                              |
| <span id="INFORMATION_NOT_REDUCED"></span><span id="information_not_reduced"></span><dl> <dt>**INFORMATION\_NOT\_REDUCED**</dt> <dt>0x00100000</dt> </dl>                                       | The TPM is not owned.<br/>                                                                                                                                                                                                       |
| <span id="INFORMATION_GENERIC_ERROR"></span><span id="information_generic_error"></span><dl> <dt>**INFORMATION\_GENERIC\_ERROR**</dt> <dt>0x00200000</dt> </dl>                                 | An error occurred, but not specific to a particular task.<br/>                                                                                                                                                                   |
| <span id="INFORMATION_DEVICE_LOCK_COUNTER"></span><span id="information_device_lock_counter"></span><dl> <dt>**INFORMATION\_DEVICE\_LOCK\_COUNTER**</dt> <dt>0x00400000</dt> </dl>              | The device lock counter has not been created.<br/>                                                                                                                                                                               |



 

</dd> </dl>

## Return value

All TPM errors as well as errors specific to [TPM Base Services](../tbs/tbs-return-codes.md) can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | \\\\.\\root\\CIMV2\\Security\\MicrosoftTpm<br/>                                     |
| MOF<br/>                      | <dl> <dt>Win32\_tpm.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Win32\_tpm.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Tpm**](win32-tpm.md)
</dt> </dl>

 

 
