---
title: IWMDRMLicense CreateSecureDecryptor method (Wmdrmsdk.h)
description: The CreateSecureDecryptor method creates a secure decryptor object. The secure decryptor differs from the normal decryptor in that it decrypts the content and then re-encrypts it according to the settings specified in the parameters of this method.
ms.assetid: f3fe8d47-ec7b-4ba5-b5ae-6262cb455ffc
keywords:
- CreateSecureDecryptor method windows Media Format
- CreateSecureDecryptor method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , CreateSecureDecryptor method
topic_type:
- apiref
api_name:
- IWMDRMLicense.CreateSecureDecryptor
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicense::CreateSecureDecryptor method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CreateSecureDecryptor** method creates a secure decryptor object. The secure decryptor differs from the normal decryptor in that it decrypts the content and then re-encrypts it according to the settings specified in the parameters of this method.

## Syntax


```C++
HRESULT CreateSecureDecryptor(
  [in]      BYTE          *pbCertificate,
  [in]      DWORD         cbCertificate,
  [in]      DWORD         dwCertificateType,
  [in]      DWORD         dwFlags,
  [out]     BYTE          *pbInitializationVector,
  [in, out] DWORD         *pcbInitializationVector,
  [out]     IWMDRMDecrypt **ppDecryptor
);
```



## Parameters

<dl> <dt>

*pbCertificate* \[in\]
</dt> <dd>

Certificate of the calling application.

</dd> <dt>

*cbCertificate* \[in\]
</dt> <dd>

Size of the certificate in bytes.

</dd> <dt>

*dwCertificateType* \[in\]
</dt> <dd>

The type of the certificate. Set to WMDRM\_CERTIFICATE\_TYPE\_XML.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

The type of session protection to use for re-encoding. Must be set to one of the constants in the following table:



| Constant                     | Description                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------|
| WMDRM\_PROTECTION\_TYPE\_RC4 | Uses RC4 encryption for session encryption. This is the only supported session protection for this version. |



 

</dd> <dt>

*pbInitializationVector* \[out\]
</dt> <dd>

Receives the initialization vector. The initialization vector is RSA encrypted using the OAEP padding scheme with the RSA public key found in the certificate. Set to **NULL** to receive the required buffer size in *pcbInitializationVector*.

</dd> <dt>

*pcbInitializationVector* \[in, out\]
</dt> <dd>

On input, the size of the buffer passed as *pbInitializationVector*. On output, the size of the used portion of the buffer. If you pass **NULL** for *pbInitializationVector*, this value is set to the required buffer size on output.

</dd> <dt>

*ppDecryptor* \[out\]
</dt> <dd>

Receives a pointer to the [**IWMDRMDecrypt**](iwmdrmdecrypt.md) interface of the newly created object.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 





