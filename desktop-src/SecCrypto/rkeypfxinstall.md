---
Description: The RKeyPFXInstall function is not supported.
ms.assetid: 061e3d9d-fc92-4204-92f3-f3425afdbe27
title: RKeyPFXInstall function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RKeyPFXInstall
api_type: 
- HeaderDef
api_location: 
- Rkeysvcc.h
---

# RKeyPFXInstall function

The **RKeyPFXInstall** function is not supported.

**Windows Server 2003:** The **RKeyPFXInstall** function installs a certificate on a remote computer. Note that this behavior has changed with Windows Server 2003 with Service Pack 1 (SP1).

## Syntax


```C++
ULONG RKeyPFXInstall(
  _In_ KEYSVCC_HANDLE         hKeySvcCli,
  _In_ PKEYSVC_BLOB           pPFX,
  _In_ PKEYSVC_UNICODE_STRING pPassword,
  _In_ ULONG                  ulFlags
);
```



## Parameters

<dl> <dt>

*hKeySvcCli* \[in\]
</dt> <dd>

A [**KEYSVCC\_HANDLE**](keysvcc-handle.md) handle previously opened by [**RKeyOpenKeyService**](rkeyopenkeyservice.md). The handle represents the remote computer that will receive the certificate. This value cannot be **NULL**.

</dd> <dt>

*pPFX* \[in\]
</dt> <dd>

A pointer to a [**KEYSVC\_BLOB**](keysvc-blob.md) structure that represents the certificate to install. The BLOB is in [*PKCS \#12*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) format.

</dd> <dt>

*pPassword* \[in\]
</dt> <dd>

A pointer to a [**KEYSVC\_UNICODE\_STRING**](keysvc-unicode-string.md) structure that represents the password for the BLOB. When you have finished using the password, clear the password from memory by calling the [**SecureZeroMemory**](https://msdn.microsoft.com/en-us/library/Aa366877(v=VS.85).aspx) function. For more information about protecting passwords, see [Handling Passwords](https://msdn.microsoft.com/en-us/library/ms717799(v=VS.85).aspx).

</dd> <dt>

*ulFlags* \[in\]
</dt> <dd>

Flags that specify the certificate installation options. This parameter can be a zero or a combination of the following values.



| Value                                                                                                                                                                                                                                     | Meaning                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="CRYPT_EXPORTABLE"></span><span id="crypt_exportable"></span><dl> <dt>**CRYPT\_EXPORTABLE**</dt> <dt></dt> </dl>              | Imported keys are marked as exportable.<br/>                                           |
| <span id="CRYPT_MACHINE_KEYSET"></span><span id="crypt_machine_keyset"></span><dl> <dt>**CRYPT\_MACHINE\_KEYSET**</dt> <dt></dt> </dl> | Private keys are stored under the remote computer and not under the current user.<br/> |



 

</dd> </dl>

## Return value

If the function is successful, the return value is S\_OK.

If the function fails, the return value is a **ULONG** that indicates the error.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Rkeysvcc.h</dt> </dl> |



## See also

<dl> <dt>

[**RKeyCloseKeyService**](rkeyclosekeyservice.md)
</dt> <dt>

[**RKeyOpenKeyService**](rkeyopenkeyservice.md)
</dt> </dl>

 

 




