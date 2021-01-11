---
description: Secures the volume's encryption key by using a Active Directory security identifier (SID).
ms.assetid: 881EEAF2-49C5-4BBD-B2AA-5E30B61E7D3A
title: ProtectKeyWithAdSid method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ProtectKeyWithAdSid
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ProtectKeyWithAdSid method of the Win32\_EncryptableVolume class

The **ProtectKeyWithAdSid** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class secures the volume's encryption key by using a Active Directory security identifier (SID).

## Syntax


```mof
uint32 ProtectKeyWithAdSid(
  [in, optional] string FriendlyName,
  [in]           string SidString,
  [in]           uint32 Flags,
  [out]          string VolumeKeyProtectorID
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in, optional\]
</dt> <dd>

A string that specifies a user-assigned identifier for this key protector. If this parameter is not specified, a blank value is used.

</dd> <dt>

*SidString* \[in\]
</dt> <dd>

String that contains the Active Directory SID used to protect the encryption key.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags that change the function behavior. This can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FVE_DPAPI_NG_FLAG_NONE"></span><span id="fve_dpapi_ng_flag_none"></span><dl> <dt>**FVE\_DPAPI\_NG\_FLAG\_NONE**</dt> <dt>0x0000</dt> </dl>                                                                   | No effect.<br/>                                                                                                                                                                                                                                                                                                                   |
| <span id="FVE_DPAPI_NG_FLAG_UNLOCK_AS_SERVICE_ACCOUNT"></span><span id="fve_dpapi_ng_flag_unlock_as_service_account"></span><dl> <dt>**FVE\_DPAPI\_NG\_FLAG\_UNLOCK\_AS\_SERVICE\_ACCOUNT**</dt> <dt>0x0001</dt> </dl> | Specifies that the SID-based protector was protected to a service account. If this flag is specified, the caller should ensure that it is running as the appropriate service account before calling [**UnlockWithAdSid**](unlockwithadsid-win32-encryptablevolume.md) (by temporarily dropping impersonation, for example).<br/> |



 

</dd> <dt>

*VolumeKeyProtectorID* \[out\]
</dt> <dd>

A unique identifier associated with the created protector. You can use this string to manage the key protector.

If the drive supports hardware encryption and BitLocker has not taken band ownership, the ID string is set to "BitLocker" and the key protector is written to per band metadata.

</dd> </dl>

## Return value

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md)

By default, you cannot add an Active Directory account or group protector remotely. You must enable constrained delegation on the domain controller and source computer. On the domain controller, perform the following steps:

1.  Open Server Manager
2.  Select Computers in Active Directory roles
3.  Select the target client computer and right click
4.  Select the Delegation tab
5.  Select the "Trust this computer for delegation to specified services only" radio button
6.  Select the "Use Kerberos only" radio button
7.  Click Add
8.  Select "Users or Computers"
9.  Select host/ as the Service Principal Name

Perform steps 3 through 9 on the source computer.

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

 

 
