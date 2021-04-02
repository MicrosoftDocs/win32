---
description: Retrieves the security identifier and flags used to protect a key.
ms.assetid: 5EF97F44-78FF-4FBF-9142-F2DD0A849057
title: GetKeyProtectorAdSidInformation method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetKeyProtectorCertificate
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetKeyProtectorAdSidInformation method of the Win32\_EncryptableVolume class

The **GetKeyProtectorAdSidInformation** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class retrieves the security identifier and flags used to protect a key.

## Syntax


```mof
uint32 GetKeyProtectorCertificate(
  [in]  string VolumeKeyProtectorID,
  [out] string SidString,
  [out] uint32 Flags
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A string identifier that can be used to manage an encrypted volume key protector.

</dd> <dt>

*SidString* \[out\]
</dt> <dd>

Type: **string**

A string that contains the security identifier (SID).

</dd> <dt>

*Flags* \[out\]
</dt> <dd>

Type: **uint32**

Flags that change the function behavior. This can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FVE_DPAPI_NG_FLAG_NONE"></span><span id="fve_dpapi_ng_flag_none"></span><dl> <dt>**FVE\_DPAPI\_NG\_FLAG\_NONE**</dt> <dt>0x0000</dt> </dl>                                                                   | No effect.<br/>                                                                                                                                                                                                                                                                                                                   |
| <span id="FVE_DPAPI_NG_FLAG_UNLOCK_AS_SERVICE_ACCOUNT"></span><span id="fve_dpapi_ng_flag_unlock_as_service_account"></span><dl> <dt>**FVE\_DPAPI\_NG\_FLAG\_UNLOCK\_AS\_SERVICE\_ACCOUNT**</dt> <dt>0x0001</dt> </dl> | Specifies that the SID-based protector was protected to a service account. If this flag is specified, the caller should ensure that it is running as the appropriate service account before calling [**UnlockWithAdSid**](unlockwithadsid-win32-encryptablevolume.md) (by temporarily dropping impersonation, for example).<br/> |



 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 Enterprise, Windows 8 Pro \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 
