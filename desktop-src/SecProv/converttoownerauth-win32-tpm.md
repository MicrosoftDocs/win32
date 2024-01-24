---
description: Translates a user-provided passphrase input into a 20-byte owner authorization that can be used to interact with the TPM. Methods such as TakeOwnership and ResetAuthLockOut require the resulting owner authorization value.
ms.assetid: 69eed934-1668-495a-b5b7-cd4a87df1ab3
title: ConvertToOwnerAuth method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.ConvertToOwnerAuth
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# ConvertToOwnerAuth method of the Win32\_Tpm class

The **ConvertToOwnerAuth** method of the [**Win32\_Tpm**](win32-tpm.md) class translates a user-provided passphrase input into a 20-byte owner authorization that can be used to interact with the TPM. Methods such as [**TakeOwnership**](takeownership-win32-tpm.md) and [**ResetAuthLockOut**](resetauthlockout-win32-tpm.md) require the resulting owner authorization value.

The conversion process follows the specifications from the [Trusted Computing Group](https://www.trustedcomputinggroup.org/).

## Syntax


```mof
uint32 ConvertToOwnerAuth(
  [in]  string OwnerPassPhrase,
  [out] string OwnerAuth
);
```



## Parameters

<dl> <dt>

*OwnerPassPhrase* \[in\]
</dt> <dd>

Type: **string**

A string to convert to an owner authorization value. The string can contain any number of alphanumeric characters.

</dd> <dt>

*OwnerAuth* \[out\]
</dt> <dd>

Type: **string**

A string derived from the *OwnerPassPhrase* parameter. This value is a 20-byte binary value encoded to a 28-byte base64 **null**-terminated string.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

The following tables lists some of the common return codes.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

A Unicode UTF-16LE encoded string is converted to the 20-byte TPM owner authorization value by taking the SHA-1 hash of the string's binary representation. The **null** termination of the Unicode string is not included in the hash. No salt is used in the SHA-1 hash.

For example, to convert the TPM owner passphrase "1Sample" to a TPM owner authorization value, the SHA-1 hash is taken from the following byte stream:

`0x31 0x00 0x53 0x00 0x61 0x00 0x6D 0x00 0x70 0x00 0x6C 0x00 0x65 0x00`

To convert a zero-length passphrase to an owner authorization value, the SHA-1 hash is taken of the **NULL** byte stream.

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
</dt> <dt>

[**TakeOwnership**](takeownership-win32-tpm.md)
</dt> </dl>

 

 
