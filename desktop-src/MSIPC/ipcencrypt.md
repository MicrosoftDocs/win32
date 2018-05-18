---
title: IpcEncrypt function
description: Encrypts plaintext data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '07db6ce0-060b-497f-b9f1-8081bbdb99a1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcEncrypt function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcEncrypt
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcEncrypt function

Encrypts plaintext data. For important information about using this function, see **Remarks**.

## Syntax


```C++
HRESULT WINAPI IpcEncrypt(
  _In_  IPC_KEY_HANDLE hKey,
        DWORD          dwBlockNumber,
        BOOL           fFinal,
  _In_  PBYTE          pbInput,
        DWORD          cbInput,
  _Out_ PBYTE          pbOutput,
        DWORD          cbOutput,
  _Out_ DWORD          *pcbResult
);
```



## Parameters

<dl> <dt>

*hKey* \[in\]
</dt> <dd>

A handle to a key object from [**IpcGetKey**](ipcgetkey.md) or [**IpcSerializeLicense**](ipcserializelicense.md).

</dd> <dt>

*dwBlockNumber* 
</dt> <dd>

The block number (calculated as block number == offset/block size). For information about usage, see Remarks.

</dd> <dt>

*fFinal* 
</dt> <dd>

Specifies whether this is the last section in a series being encrypted. **TRUE** for the last or only block; **FALSE** if there are more blocks to be encrypted.

</dd> <dt>

*pbInput* \[in\]
</dt> <dd>

A pointer to the plaintext to encrypt.

</dd> <dt>

*cbInput* 
</dt> <dd>

The byte count of the plaintext to encrypt. The length of the plaintext must be a multiple of the block size unless *fFinal* is **FALSE**.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

A pointer to the output buffer. On output, this buffer receives the ciphertext.

Set to **NULL** to query for the size required for the output buffer.

</dd> <dt>

*cbOutput* 
</dt> <dd>

The size of the output buffer, in bytes.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

A pointer to a **ULONG** that receives the number of bytes copied to *pbOutput*. If *pbOutput* is **NULL**, *pcbResult* receives the size, in bytes, required for the ciphertext.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

### Data encryption approach

When encrypting data, memory must be allocated by the caller to store the encrypted data. To reduce runtime memory usage, you may choose to encrypt a large amount of contiguous data by breaking it up into smaller blocks first, rather than encrypting all the data in a single call.

> [!Note]  
> Breaking your content into multiple segments and performing multiple calls may also be required if the content of your document is not stored contiguously.

 

To encrypt a block of data in a single call, pass in 0 (zero) for *dwBlockNumber*, **TRUE** for *fFinal*, and set *pbInput* to the beginning of your data.

To encrypt a large block of contiguous data over the course of several calls, use the **IPC\_KI\_BLOCK\_SIZE** property from [**IpcGetKeyProperty**](ipcgetkeyproperty.md) to determine the block size used by the platform. Break up your data into segments that are multiples of this size. For each successive call to **IpcEncrypt**, set *dwBlockNumber* to the value of (bytes of data encrypted so far / block size as determined by **IpcGetKeyProperty**). Be sure to set *pbInput* to the location of the next block of data to encrypt, and *pbOutput* to the proper location to receive the next block of data resulting from that encryption. Set *fFinal* to **TRUE** only if you are passing in the last block of data to be encrypted.

> [!Note]  
> Automatic padding is not supported. All segments of data must be a multiple of the platform's block size, as determined by [**IpcGetKeyProperty**](ipcgetkeyproperty.md).

 

### Padding

In the default case, when *fFinal* is set to **TRUE**, the input data does not need to be a multiple of the platform's block size. **IpcEncrypt** may generate encrypted data that is larger in size than the original data. To ensure correct behavior, you must first query the required size of the encrypted data by calling **IpcEncrypt** with *pbOutput* set to **NULL**. It is not recommended to pad the input data to a multiple of the platform's block size in your application because the platform's block size may be significantly larger than the padding data actually required.

If your application encrypts data that can be consumed by using the MSDRM library, you may choose to set the **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** property when creating a license. In this case, automatic padding is not supported. All segments of data must be a multiple of the platform's block size, as determined by [**IpcGetKeyProperty**](ipcgetkeyproperty.md).

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**IpcEncrypt**](ipcencrypt.md)
</dt> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**IpcGetKeyProperty**](ipcgetkeyproperty.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





