---
description: Verifies the signature of a signed file and obtains the hash value and algorithm identifier for the file.
ms.assetid: 130b3c3e-cc67-44ec-acc7-daa87b714299
title: WTHelperGetFileHash function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WTHelperGetFileHash
api_type: 
- DllExport
api_location: 
- Wintrust.dll
---

# WTHelperGetFileHash function

\[The **WTHelperGetFileHash** function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The **WTHelperGetFileHash** function verifies the signature of a signed file and obtains the hash value and algorithm identifier for the file.

> [!Note]  
> This function is not declared in a published header file. To use this function, declare it in the exact format shown. This function also has no associated import library. You must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Wintrust.dll.

 

## Syntax


```C++
LONG WINAPI WTHelperGetFileHash(
  _In_        LPCWSTR pwszFilename,
  _In_        DWORD   dwFlags,
  _Inout_opt_ PVOID   pvReserved,
  _Out_opt_   BYTE    *pbFileHash,
  _Inout_opt_ DWORD   *pcbFileHash,
  _Out_opt_   ALG_ID  *pHashAlgid
);
```



## Parameters

<dl> <dt>

*pwszFilename* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that contains the path and file name of the file to get the hash for.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is not used and should be zero.

</dd> <dt>

*pvReserved* \[in, out, optional\]
</dt> <dd>

This parameter is not used and should be **NULL**.

</dd> <dt>

*pbFileHash* \[out, optional\]
</dt> <dd>

A pointer to a buffer to receive the hash value for the file. The *pcbFileHash* parameter contains the size of this buffer.

</dd> <dt>

*pcbFileHash* \[in, out, optional\]
</dt> <dd>

A pointer to a **DWORD** variable that, on input, contains the size, in bytes, of the *pbFileHash* buffer and, on output, receives the size, in bytes, of the hash value.

To obtain the required size of the hash value, pass **NULL** for the *pbFileHash* parameter. This function will place the required size, in bytes, of the hash value in this location.

If the *pbFileHash* parameter is not **NULL**, and the size is not large enough to receive the hash value, this function will place the required size, in bytes, in this location and return **ERROR\_MORE\_DATA**.

</dd> <dt>

*pHashAlgid* \[out, optional\]
</dt> <dd>

A pointer to an [**ALG\_ID**](alg-id.md) variable to receive the identifier of the algorithm used to create the hash value. This parameter can be **NULL** if this information is not needed.

</dd> </dl>

## Return value

Returns a status code that indicates the success or failure of the function.

Possible return codes include, but are not limited to, the following.



| Return code                                                                                               | Description                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_SUCCESS**</dt> </dl>             | The file is signed, and the signature was verified.<br/>                                                                                        |
| <dl> <dt>**ERROR\_MORE\_DATA**</dt> </dl>          | The *pbFileHash* parameter is not **NULL**, and the size specified by the *pcbFileHash* parameter is not large enough to receive the hash.<br/> |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl> | A memory allocation failure occurred.<br/>                                                                                                      |
| <dl> <dt>**TRUST\_E\_BAD\_DIGEST**</dt> </dl>      | The signature of the file was not verified.<br/>                                                                                                |
| <dl> <dt>**TRUST\_E\_NOSIGNATURE**</dt> </dl>      | The file was not signed or had a signature that is not valid.<br/>                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Wintrust.dll</dt> </dl> |



 

 
