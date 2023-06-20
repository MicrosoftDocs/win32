---
description: Certificate Revocation Lists
ms.assetid: 146e7e4a-4281-4f5c-8346-d6c0d5f5442f
title: Certificate Revocation Lists
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Certificate Revocation Lists

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes how to examine the certificate revocation list (CRL) for revoked drivers when using Certified Output Protection Protocol (COPP).

The CRL contains digests of revoked certificates and can be provided and signed only by Microsoft. The CRL is distributed through digital rights management (DRM) licenses. The CRL can revoke any certificate in the driver's certificates chain. If any certificate in the chain is revoked, then that certificate and all of the certificates below it in the chain are also revoked.

To get the CRL, the application must use the Windows Media Format SDK, version 9 or later, and perform the following steps:

1.  Call **WMCreateReader** to create the Windows Media Format SDK reader object.
2.  Query the reader object for the **IWMDRMReader** interface.
3.  Call **IWMDRMReader::GetDRMProperty** with a value of g\_wszWMDRMNet\_Revocation to get the CRL. You must call this method twice: Once to get the size of the buffer to allocate, and once to fill the buffer. The second call returns a string that contains the CRL. The entire string is base-64 encoded.
4.  Decode the base-64 encoded string. You can use the **CryptStringToBinary** function to do this. This function is part of CryptoAPI.

> [!Note]  
> To use the **IWMDRMReader** interface, you must obtain a static DRM library from Microsoft and link your application to this library file. For more information, see the topic "Obtaining the Required DRM Library" in the Windows Media Format SDK documentation.

 

If the CRL is not present on the user's computer, the **GetDRMProperty** method returns NS\_E\_DRM\_UNSUPPORTED\_PROPERTY. Currently, the only way to obtain the CRL is to acquire a DRM license.

The following code shows a function that returns the CRL:


```C++
////////////////////////////////////////////////////////////////////////
//  Name: GetCRL
//  Description: Gets the certificate revocation list (CRL).
//
//  ppBuffer: Receives a pointer to the buffer that contains the CRL.
//  pcbBuffer: Receives the size of the buffer returned in ppBuffer.
//
//  The caller must free the returned buffer by calling CoTaskMemFree.
////////////////////////////////////////////////////////////////////////
HRESULT GetCRL(BYTE **ppBuffer, DWORD *pcbBuffer)
{
    IWMReader *pReader = NULL;
    IWMDRMReader *pDrmReader = NULL;
    HRESULT hr = S_OK;

    // DRM attribute data.
    WORD cbAttributeLength = 0;
    BYTE *pDataBase64 = NULL;
    WMT_ATTR_DATATYPE type;

    // Buffer for base-64 decoded CRL.
    BYTE *pCRL = NULL;
    DWORD cbCRL = 0;

    // Create the WMReader object.
    hr = WMCreateReader(NULL, 0, &pReader);

    // Query for the IWMDRMReader interface.
    if (SUCCEEDED(hr))
    {
        hr = pReader->QueryInterface(
            IID_IWMDRMReader, (void**)&pDrmReader);
    }

    // Call GetDRMProperty once to find the size of the buffer.
    if (SUCCEEDED(hr))
    {
        hr = pDrmReader->GetDRMProperty(
            g_wszWMDRMNET_Revocation,
            &type,
            NULL,
            &cbAttributeLength
            );
    }

    // Allocate a buffer.
    if (SUCCEEDED(hr))
    {
        pDataBase64 = (BYTE*)CoTaskMemAlloc(cbAttributeLength);
        if (pDataBase64 == NULL)
        {
            hr = E_OUTOFMEMORY;
        }
    }

    // Call GetDRMProperty again to get the property.
    if (SUCCEEDED(hr))
    {
        hr = pDrmReader->GetDRMProperty(
            g_wszWMDRMNET_Revocation,
            &type,
            pDataBase64,
            &cbAttributeLength
            );
    }

    // Find the size of the buffer for the base-64 decoding.
    if (SUCCEEDED(hr))
    {
        BOOL bResult = CryptStringToBinary(
            (WCHAR*)pDataBase64,    // Base-64 encoded string.
            0,                      // Null-terminated.
            CRYPT_STRING_BASE64,    
            NULL,                   // Buffer (NULL).
            &cbCRL,                 // Receives the size of the buffer. 
            NULL, NULL              // Optional.
            );
        if (!bResult)
        {
            hr = __HRESULT_FROM_WIN32(GetLastError());
        }
    }

    // Allocate a buffer for the CRL.
    if (SUCCEEDED(hr))
    {
        pCRL = (BYTE*)CoTaskMemAlloc(cbCRL);
        if (pCRL == NULL)
        {
            hr = E_OUTOFMEMORY;
        }
    }

    // Base-64 decode to get the CRL.
    if (SUCCEEDED(hr))
    {
        BOOL bResult = CryptStringToBinary(
            (WCHAR*)pDataBase64,    // Base-64 encoded string.
            0,                      // Null-terminated.
            CRYPT_STRING_BASE64,    
            pCRL,                   // Buffer.
            &cbCRL,                 // Receives the size of the buffer. 
            NULL, NULL              // Optional.
            );
        if (!bResult)
        {
            hr = __HRESULT_FROM_WIN32(GetLastError());
        }
    }

    // Return the buffer to the caller. Caller must free the buffer.
    if (SUCCEEDED(hr))
    {
        *ppBuffer = pCRL;
        *pcbBuffer = cbCRL;
    }
    else
    {
        CoTaskMemFree(pCRL);
    }

    CoTaskMemFree(pDataBase64);
    SAFE_RELEASE(pReader);
    SAFE_RELEASE(pDrmReader);
    return hr;
}
```



Next, the application must verify that the CRL is valid. To do so, verify that the CRL certificate, which is part of the CRL, is directly signed by the Microsoft Root Certificate and has the SignCRL element value set to 1. Also, verify the signature of the CRL.

After the CRL is verified, the application can store it. The CRL version number should also be checked before storing so that the application always stores the newest version.

The CRL has the following format.



| Section            | Contents                                                             |
|--------------------|----------------------------------------------------------------------|
| Header             | 32-bit CRL version32-bit number of entries                           |
| Revocation Entries | Multiple 160-bit revocation entries                                  |
| Certificate        | 32-bit certificate lengthVariable-length certificate                 |
| Signature          | 8-bit signature type16-bit signature lengthVariable-length signature |



 

> [!Note]  
> All integer values are unsigned and are represented in big-endian (network byte order) notation.

 

CRL Section Descriptions

<dl> <dt>

<span id="Header"></span><span id="header"></span><span id="HEADER"></span>Header
</dt> <dd>

The header contains the version number of the CRL and the number of revocation entries in the CRL. A CRL can contain zero or more entries.

</dd> <dt>

<span id="Revocation_entries"></span><span id="revocation_entries"></span><span id="REVOCATION_ENTRIES"></span>Revocation entries
</dt> <dd>

Each revocation entry is the 160-bit digest of a revoked certificate. Compare this digest with the DigestValue element within the certificate.

</dd> <dt>

<span id="Certificate"></span><span id="certificate"></span><span id="CERTIFICATE"></span>Certificate
</dt> <dd>

The certificate section contains a 32-bit value indicating the length (in bytes) of the XML certificate and its certificate chain, along with a byte array that contains both the XML certificate of the Certificate Authority (CA) and the certificate chain that has Microsoft as the Root. The certificate must be signed by a CA that has the authority to issue CRLs.

> [!Note]  
> The certificate must not be null-terminated.

 

</dd> <dt>

<span id="Signature"></span><span id="signature"></span><span id="SIGNATURE"></span>Signature
</dt> <dd>

The signature section contains the signature type and length, and the digital signature itself. The 8-bit type is set to 2 to indicate that it uses SHA-1 with 1024-bit RSA encryption. The length is a 16-bit value containing the length of the digital signature in bytes. The digital signature is calculated over all prior sections of the CRL.

The signature is calculated using the RSASSA-PSS digital signature scheme that is defined in PKCS \#1 (version 2.1). The hash function is SHA-1, which is defined in Federal Information Processing Standard (FIPS) 180-2, and the mask generation function is MGF1, which is defined in section B.2.1 in PKCS \#1 (version 2.1). The RSASP1 and RSAVP1 operations use RSA with a 1024-bit modulus with a verification exponent of 65537.

</dd> </dl>

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



