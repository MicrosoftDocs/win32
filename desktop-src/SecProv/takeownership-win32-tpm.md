---
description: Installs an owner for the TPM.
ms.assetid: 7b4c8785-0925-41a8-a878-7c1f38d31853
title: TakeOwnership method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.TakeOwnership
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# TakeOwnership method of the Win32\_Tpm class

The **TakeOwnership** method of the [**Win32\_Tpm**](win32-tpm.md) class installs an owner for the TPM. The owner of the TPM can make full use of TPM capabilities. After an owner is set, no other user or software can claim ownership of the TPM.

The [**IsEnabled**](isenabled-win32-tpm.md), [**IsActivated**](isactivated-win32-tpm.md), and [**IsOwnershipAllowed**](isownershipallowed-win32-tpm.md) methods must all be true before the **TakeOwnership** method can succeed.

## Syntax


```mof
uint32 TakeOwnership(
  [in, optional] string OwnerAuth
);
```



## Parameters

<dl> <dt>

*OwnerAuth* \[in, optional\]
</dt> <dd>

Type: **string**

A string that identifies the TPM owner. This string must be a base64-encoded null-terminated string that contains exactly 20 bytes of binary data. Use the [**ConvertToOwnerAuth**](converttoownerauth-win32-tpm.md) method to translate a passphrase to this expected format. The *OwnerAuth* parameter is read from the registry if none is provided.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

The following table lists some of the common return codes.



| Return code/value                                                                                                                                                                         | Description                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                         | The method was successful.<br/>                                                                                                                                                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>                 | The *OwnerAuth* parameter is not valid.<br/>                                                                                                                                                                 |
| <dl> <dt>**TPM\_E\_OWNER\_SET**</dt> <dt>2150105108 (0x80280014)</dt> </dl>            | An owner already exists on the TPM.<br/>                                                                                                                                                                     |
| <dl> <dt>**TPM\_E\_NO\_ENDORSEMENT**</dt> <dt>2150105123 (0x80280023)</dt> </dl>       | No endorsement key can be found on the TPM.<br/> To create an endorsement key pair on the TPM, see the [**CreateEndorsementKeyPair**](createendorsementkeypair-win32-tpm.md) method.<br/>             |
| <dl> <dt>**TPM\_E\_INSTALL\_DISABLED**</dt> <dt>2150105099 (0x8028000B)</dt> </dl>     | An owner cannot be installed on this TPM.<br/> For information about how to allow installation of a device owner, see [**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md).<br/> |
| <dl> <dt>**TPM\_E\_DEFEND\_LOCK\_RUNNING**</dt> <dt>2150107139 (0x80280803)</dt> </dl> | The TPM is defending against dictionary attacks and is in a time-out period. For more information, see the [**ResetAuthLockOut**](resetauthlockout-win32-tpm.md) method.<br/>                               |



 

## Remarks

The methods [**IsEnabled**](isenabled-win32-tpm.md), [**IsActivated**](isactivated-win32-tpm.md), and [**IsOwnershipAllowed**](isownershipallowed-win32-tpm.md) must all be true before **TakeOwnership** can succeed.

You should use the [**ConvertToOwnerAuth**](converttoownerauth-win32-tpm.md) method to change a passphrase into the input value used for the *OwnerAuth* parameter.

The **TakeOwnership** method backs up the owner authorization value to Active Directory if the appropriate Group Policy settings have been configured.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftTpm<br/>                                            |
| MOF<br/>                      | <dl> <dt>Win32\_tpm.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Win32\_tpm.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Tpm**](win32-tpm.md)
</dt> </dl>

 

 
