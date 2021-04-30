---
description: Provides status information about a hardware test of a fully decrypted operating system volume.
ms.assetid: d76bc266-3718-443e-94f9-dcaa0ec53151
title: GetHardwareTestStatus method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetHardwareTestStatus
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetHardwareTestStatus method of the Win32\_EncryptableVolume class

The **GetHardwareTestStatus** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class provides status information about a hardware test of a fully decrypted operating system volume.

Use this method to show whether a hardware test is pending, as well as the success or failure of a hardware test that completed on the last computer restart. To request a hardware test, use the [**EncryptAfterHardwareTest**](encryptafterhardwaretest-win32-encryptablevolume.md) method.

## Syntax


```mof
uint32 GetHardwareTestStatus(
  [out] uint32 TestStatus,
  [out] uint32 TestError
);
```



## Parameters

<dl> <dt>

*TestStatus* \[out\]
</dt> <dd>

Type: **uint32**

Specifies whether a hardware test is pending, as well as the success of failure of a hardware test that completed on the last computer restart.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="NotFailed_and_NonePending"></span><span id="notfailed_and_nonepending"></span><span id="NOTFAILED_AND_NONEPENDING"></span><dl> <dt><strong>NotFailed_and_NonePending</strong></dt> <dt>0</dt> </dl></td>
<td>If a test was requested, the test has succeeded on the last computer restart and volume encryption is now in progress. For the encryption status, see the <a href="getconversionstatus-win32-encryptablevolume.md"><strong>GetConversionStatus</strong></a> method. Otherwise, no test ran on the last computer restart and none is pending. <br/></td>
</tr>
<tr class="even">
<td><span id="Failed"></span><span id="failed"></span><span id="FAILED"></span><dl> <dt><strong>Failed</strong></dt> <dt>1</dt> </dl></td>
<td>Volume encryption did not start. All key protectors were removed.<br/> To resolve a failed test:<br/>
<ul>
<li>Consult the information in the <em>TestError</em> parameter.</li>
<li>Add key protectors and use the <a href="encryptafterhardwaretest-win32-encryptablevolume.md"><strong>EncryptAfterHardwareTest</strong></a> method again.</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="Pending"></span><span id="pending"></span><span id="PENDING"></span><dl> <dt><strong>Pending</strong></dt> <dt>2</dt> </dl></td>
<td>A test has been requested and will run on the next computer restart.<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*TestError* \[out\]
</dt> <dd>

Type: **uint32**

Specifies the error from the last completed hardware test.



| Value                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>                        | No errors occurred or no hardware test ran on the last computer restart.<br/>                                                                                                                                                                                                                                                                      |
| <dl> <dt> 2150694972 (0x8031003C)</dt> </dl> | FVE\_E\_KEYFILE\_NOT\_FOUND<br/> A USB flash drive with an external key file was not found. If this failure persists, the computer cannot read USB drives during restart. You may not be able to use external keys to unlock the operating system volume during restart.<br/>                                                                |
| <dl> <dt> 2150694973 (0x8031003D)</dt> </dl> | FVE\_E\_KEYFILE\_INVALID<br/> The external key file on the USB flash drive was corrupt. Try a different USB flash drive to store the external key file.<br/>                                                                                                                                                                                 |
| <dl> <dt> 2150694975 (0x8031003F)</dt> </dl> | FVE\_E\_TPM\_DISABLED<br/> The TPM is either disabled or deactivated or both disabled and deactivated. To turn on the TPM, use the [**Win32\_Tpm**](win32-tpm.md) WMI provider or run the TPM management snap-in (Tpm.msc).<br/>                                                                                                            |
| <dl> <dt> 2150694977 (0x80310041)</dt> </dl> | FVE\_E\_TPM\_INVALID\_PCR<br/> The TPM detected a change in operating system restart services within the current platform validation profile. Remove any startup CD or DVD from the computer. If this failure persists, check that the latest firmware and BIOS upgrades are installed, and that the TPM is otherwise working properly.<br/> |
| <dl> <dt>2150694979 (0x80310043)</dt> </dl>  | FVE\_E\_PIN\_INVALID<br/> The provided PIN was incorrect.<br/>                                                                                                                                                                                                                                                                               |



 

</dd> </dl>

## Return value

Type: **uint32**

The following table lists some of the common return codes.



| Return code/value                                                                                                                                                                  | Description                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method succeeded.<br/> |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl> | The volume is locked.<br/> |



 

## Remarks

To request a hardware test, use the [**EncryptAfterHardwareTest**](encryptafterhardwaretest-win32-encryptablevolume.md) method.

To run a hardware test when its status is pending, follow these steps:

1.  Insert into the computer a USB flash drive that contains an external key file. This step applies only if the volume has a key protector of type "External Key" or "TPM And Startup Key".
2.  Restart the computer. On computer restart, the hardware test runs automatically.

To cancel the hardware test, use the [**Encrypt**](encrypt-win32-encryptablevolume.md) method.

A successful test determines that:

-   The TPM can unlock the volume if a TPM-related key protector exists.
-   The computer can read a USB flash drive that contains an external key file during startup if the volume can be unlocked by an external key (including a startup key).

Hardware test results will not be available after any changes in conversion or after the next computer restart. Check the System event log for the information about any hardware tests that previously ran on the computer.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 
