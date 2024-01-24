---
description: Computes the key block used by the Extensible Authentication Protocol (EAP).
ms.assetid: 0f382668-6fc6-440f-ba61-70b1db0f3987
title: SslComputeEapKeyBlock function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslComputeEapKeyBlock
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslComputeEapKeyBlock function

The **SslComputeEapKeyBlock** function computes the key block used by the Extensible Authentication Protocol (EAP).

## Syntax


```C++
SECURITY_STATUS WINAPI SslComputeEapKeyBlock(
  _In_      NCRYPT_PROV_HANDLE hSslProvider,
  _In_      NCRYPT_KEY_HANDLE  hMasterKey,
  _In_      PBYTE              pbRandoms,
  _In_      DWORD              cbRandoms,
  _Out_opt_ PBYTE              pbOutput,
  _In_      DWORD              cbOutput,
  _Out_     DWORD              *pcbResult,
  _In_      DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol provider instance.

</dd> <dt>

*hMasterKey* \[in\]
</dt> <dd>

The handle of the [*master key*](/windows/desktop/SecGloss/m-gly) object.

</dd> <dt>

*pbRandoms* \[in\]
</dt> <dd>

A pointer to a buffer that contains a concatenation of the client\_random and server\_random values of the SSL session.

</dd> <dt>

*cbRandoms* \[in\]
</dt> <dd>

The length, in bytes, of the *pbRandoms* buffer.

</dd> <dt>

*pbOutput* \[out, optional\]
</dt> <dd>

The address of a buffer that receives the key BLOB. The *cbOutput* parameter contains the size of this buffer. If this parameter is **NULL**, this function will place the required size, in bytes, in the **DWORD** pointed to by the *pcbResult* parameter.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The length, in bytes, of the *pbOutput* buffer.

</dd> <dt>

*pcbResult* \[out\]
</dt> <dd>

A pointer to a **DWORD** value that specifies the length, in bytes, of the hash written to the *pbOutput* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Set to **NCRYPT\_SSL\_SERVER\_FLAG** to indicate that this is a server call.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.



| Return code/value                                                                                                                                                    | Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl> | One of the supplied handles is not valid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

