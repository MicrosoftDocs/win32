---
description: Obtaining the Drivers Certificate Chain
ms.assetid: bc7b346c-3382-4f2b-90b6-03f6a1a5a9ce
title: Obtaining the Drivers Certificate Chain
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining the Drivers Certificate Chain

To use Certified Output Protection Protocol (COPP), the application first must build a DirectShow graph that includes the Video Mixing Render filter (VMR-7 or VMR-9). The older Video Renderer filter does not support COPP. Before calling any COPP methods, the application must build a video playback graph and connect the decoder to the VMR filter's input pin. It is not necessary to play the video file.

After building the graph, query the VMR for the [**IAMCertifiedOutputProtection**](/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection) interface, and then call [**IAMCertifiedOutputProtection::KeyExchange**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-keyexchange). This method returns a 128-bit random number typed as a GUID, along with a pointer to a byte array that contains the driver's XML certificate chain in UTF-8 format. The following code shows how to get the certificate chain.


```C++
GUID guidRandom;
BYTE *pbCertificateChain = NULL;
DWORD cbCertificateChainLen;   // Size of the certificate chain, in bytes.
hr = pCOPP->KeyExchange(&guidRandom, &pbCertificateChain,
         &cbCertificateChainLen);
if (SUCCEEDED(hr))
{
    // TODO: Validate the certificate chain and get the driver's
    // public key. 

    // When you are done, free the buffer that contains the 
    // certificate chain.
    CoTaskMemFree(pbCertificateChain);
}
```



## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



