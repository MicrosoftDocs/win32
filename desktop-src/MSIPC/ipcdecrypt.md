---
title: IpcDecrypt function
description: Decrypts encrypted data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7ce8ec85-6285-42c3-91a2-ef146dc5a45b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcDecrypt function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcDecrypt
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcDecrypt function

Decrypts encrypted data. For information about using this function with MSDRM encryption, see **Remarks**.

## Syntax


```C++
HRESULT WINAPI IpcDecrypt(
  _In_  IPC_KEY_HANDLE hKey,
        DWORD          dwBlockNumber,
        BOOL           fFinal,
  _In_  PBYTE          pbInput,
        DWORD          cbInput,
  _Out_ PBYTE          pbOutput,
        DWORD          cbOutput,
  _Out_ DWORD          *pcbResult
);
```



## Parameters

<dl> <dt>

*hKey* \[in\]
</dt> <dd>

The handle to a key object from [**IpcGetKey**](ipcgetkey.md) or [**IpcSerializeLicense**](ipcserializelicense.md).

</dd> <dt>

*dwBlockNumber* 
</dt> <dd>

The block number (calculated as block number == offset/block size). For more information on usage, see Remarks.

</dd> <dt>

*fFinal* 
</dt> <dd>

Specifies whether this is the last section in a series being decrypted. **TRUE** for the last or only block; **FALSE** if there are more blocks to be decrypted.

</dd> <dt>

*pbInput* \[in\]
</dt> <dd>

A pointer to the cipher text to decrypt.

</dd> <dt>

*cbInput* 
</dt> <dd>

The byte count of the cipher text to decrypt. The length of the cipher text must be a multiple of the block size unless *fFinal* is **TRUE**.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

A pointer to the output buffer. On output, this buffer receives the plaintext.

Set to **NULL** to query for the size required for the output buffer.

</dd> <dt>

*cbOutput* 
</dt> <dd>

The size of the output buffer, in bytes.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

A pointer to a **ULONG** that receives the number of bytes copied to *pbOutput*. If *pbOutput* is **NULL**, *pcbResult* receives the size, in bytes, required for the plaintext.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

### Data decryption approach

When decrypting data, memory must be allocated by the caller to store the decrypted data. To reduce runtime memory usage, you may choose to decrypt a large amount of contiguous data by breaking it up into smaller blocks first, rather than decrypting all the data in a single call.

> [!Note]  
> Breaking your content into multiple segments and performing multiple calls may also be required if the content of your document is not stored contiguously.

 

To decrypt a block of data in a single call, pass in 0 (zero) for *dwBlockNumber*, **TRUE** for *fFinal*, and set *pbInput* to the beginning of your data.

To decrypt a large block of contiguous data over the course of several calls, use the **IPC\_KI\_BLOCK\_SIZE** property from [**IpcGetKeyProperty**](ipcgetkeyproperty.md) to determine the block size used by the platform. Break up your data into segments that are multiples of this size. For each successive call to **IpcDecrypt**, set *dwBlockNumber* to the value of (bytes of data encrypted so far / block size as determined by **IpcGetKeyProperty**). Be sure to set *pbInput* to the location of next block of data to decrypt, and *pbOutput* to the proper location to receive the next block of data to receive the result of that decryption. Set *fFinal* to **TRUE** only if you are passing in the last block of data to be decrypted.

### Padding

In the default case, when *fFinal* is set to **TRUE**, the size of the decrypted data may not be a multiple of the platform's block size. **IpcDecrypt** will determine the size of the original plaintext data and return this value in *pcbResult*.

If your application decrypts data that was protected by using either the MSDRM library or the RMS SDK 2.1 library in the case when the **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** property was set during license creation, then automatic padding is not supported. The final decrypted block will be a multiple of the platform's block size, as determined by [**IpcGetKeyProperty**](ipcgetkeyproperty.md).

If your application decrypts data that could be encrypted in either mode, you must query which type of encryption was used to decrypt the final block correctly. Use the **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** property to do this.

### Compatibility with MSDRM

In most cases, it is possible to use RMS SDK 2.1 to decrypt content encrypted by using MSDRM.

It is also possible to create MSDRM applications that will produce information that RMS SDK 2.1 cannot decrypt.

The following prerequisites will help to ensure decryption is possible:

-   The license generated by MSDRM's [**DRMGetSignedIssuanceLicense**](https://msdn.microsoft.com/library/aa362561) specified L"AES" as the *wszSymKeyType* parameter.
-   Content was encrypted by MSDRM in multiples of the blocksize, queried using [**DRMGetInfo**](https://msdn.microsoft.com/library/aa362533).
-   Content is decrypted by RMS SDK 2.1 in multiples of the blocksize, queried using [**IpcGetKeyProperty**](ipcgetkeyproperty.md) .

Testing is the only way to know for sure if your MSDRM-encrypted data can be decrypted by using RMS SDK 2.1.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**DRMGetInfo**](https://msdn.microsoft.com/library/aa362533)
</dt> <dt>

[**DRMGetSignedIssuanceLicense**](https://msdn.microsoft.com/library/aa362561)
</dt> <dt>

[**IpcDecrypt**](ipcdecrypt.md)
</dt> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**IpcGetKeyProperty**](ipcgetkeyproperty.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





