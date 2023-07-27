---
description: Initiating a COPP Session
ms.assetid: c84a83b4-51b2-4b46-860f-d740b42323fa
title: Initiating a COPP Session
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Initiating a COPP Session

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To initiate a Certified Output Protection Protocol (COPP) session, you must prepare a *signature*, which is an array that contains the concatenation of the following numbers:

-   The 128-bit random number returned by the driver. (This value is shown as *guidRandom* in [Obtaining the Driver's Certificate Chain](obtaining-the-drivers-certificate-chain.md).)
-   A 128-bit symmetric AES key.
-   A 32-bit starting sequence number for status requests.
-   A 32-bit starting sequence number for COPP commands.

Generate a symmetric AES key as follows:


```C++
DWORD dwFlag = 0x80;         // Bit length: 128-bit AES.
dwFlag <<= 16;               // Move this value to the upper 16 bits.
dwFlag |= CRYPT_EXPORTABLE;  // We want to export the key.
CryptGenKey(
    hCSP,           // Handle to the CSP.
    CALG_AES_128,   // Use 128-bit AES block encryption algorithm.
    dwFlag,
    &m_hAESKey      // Receives a handle to the AES key.
);
```



The **CryptGenKey** function creates the symmetric key, but the key is still held in the CSP. To export the key into a byte array, use the **CryptExportKey** function. This is the reason for using the CRYPT\_EXPORTABLE flag when calling **CryptGenKey**. The following code exports the key and copies it into the


```
pData
```



array.


```C++
DWORD cbData = 0; 
BYTE *pData = NULL;
// Get the size of the blob.
CryptExportKey(hAESKey, 0, PLAINTEXTKEYBLOB, 0, NULL, &cbData);  

// Allocate the array and call again.
pData = new BYTE[cbData];
CryptExportKey(hAESKey, 0, PLAINTEXTKEYBLOB, 0, pData, &cbData);  
```



The data returned in


```
pData
```



has the following layout:


```C++
BLOBHEADER header
DWORD      cbSize
BYTE       key[]
```



However, no structure that matches this layout is defined in the CryptoAPI headers. You can either define one or do some pointer arithmetic. For example, to verify the size of the key:


```C++
DWORD *pcbKey = (DWORD*)(pData + sizeof(BLOBHEADER));
if (*pcbKey != 16)
{
    // Wrong size! Should be 16 bytes (128 bits).
}
```



To get the pointer to the key itself:


```C++
BYTE *pKey = pData + sizeof(BLOBHEADER) + sizeof(DWORD);
```



Next, generate a 32-bit random number to use as the starting sequence for COPP status requests. The recommended way to create a random number is to call the **CryptGenRandom** function. Do not use the **rand** function in the C run-time library, because it is not truly random. Generate a second 32-bit random number to use as the starting sequence for COPP commands.


```C++
UINT uStatusSeq;     // Status sequence number.
UINT uCommandSeq;    // Command sequence number.
CryptGenRandom(hCSP, sizeof(UINT), &uStatusSeq);
CryptGenRandom(hCSP, sizeof(UINT), &uCommandSeq);
```



Now you can prepare the COPP signature. This is a 256-byte array, defined as the [**AMCOPPSignature**](/windows/win32/api/strmif/ns-strmif-amcoppsignature) structure. Initialize the contents of the array to zero. Then copy the four numbers into the array—the driver's random number, the AES key, the status sequence number, and the command sequence number, in that order. Finally, swap the byte order of the entire array.

According to the documentation for **CryptEncrypt**:

<dl> "The length of plaintext data that can be encrypted with a call to **CryptEncrypt** with an RSA key is the length of the key modulus minus eleven bytes. The eleven bytes is the chosen minimum for PKCS \#1 padding."  
</dl>

In this case, the modulus is 256 bytes, so the maximum message length is 245 bytes (256 – 11). The **AMCOPPSignature** structure is 256 bytes, but the meaningful data in the signature is only 40 bytes. The following code encrypts the signature and provides the result in


```
CoppSig
```



.


```C++
AMCOPPSignature CoppSig;
ZeroMemory(&CoppSig, sizeof(CoppSig));
// Copy the signature data into CoppSig. (Not shown.)

// Encrypt the signature:
const DWORD RSA_PADDING = 11;    // 11-byte padding.
DWORD cbDataOut = sizeof(AMCOPPSignature);
DWORD cbDataIn = cbDataOut - RSA_PADDING;
CryptEncrypt(
    hRSAKey, 
    NULL,     // No hash object.
    TRUE,     // Final block to encrypt.
    0,        // Reserved.
    &CoppSig, // COPP signature.
    &cbDataOut, 
    cbDataIn
);
```



Now pass the encrypted array to [**IAMCertifiedOutputProtection::SessionSequenceStart**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-sessionsequencestart):


```C++
hr = pCOPP->SessionSequenceStart(&CoppSig);
if (SUCCEEDED(hr))
{
    // Ready to send COPP commands and status requests.
}
```



If this method succeeds, you are ready to send COPP commands and status requests to the driver.

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



