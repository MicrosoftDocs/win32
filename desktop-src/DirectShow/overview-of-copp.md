---
description: Overview of COPP
ms.assetid: 4421ab65-e44a-4d1f-8d9b-b187227429c6
title: Overview of COPP
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Overview of COPP

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Here are the basic steps that an application must perform to use Certified Output Protection Protocol (COPP).

**Get the driver's certificate chain**

1.  Build a DirectShow playback graph that renders video using the Video Mixing Renderer (VMR-7 or VMR-9) or the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) filter (EVR).
2.  Query the VMR for the [**IAMCertifiedOutputProtection**](/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection) interface.
3.  Call [**IAMCertifiedOutputProtection::KeyExchange**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-keyexchange). This method returns a 128-bit random number from the driver, along with a certificate chain that contains the driver's 2048-bit RSA public key.

**Validate the certificate chain**

1.  Validate the certificate chain. If the certificate chain is not valid, stop.
2.  Check the certificate revocation list (CRL). If any of the certificates in the certificate chain appears in the revocation list, stop.
3.  Get the RSA public key from the certificate chain.

**Initialize the COPP Session**

1.  Generate a 128-bit AES session key. This key is used to sign data and to verify that signed data has not been tampered with.
2.  Generate two cryptographically secure 32-bit random numbers. The first is a status sequence number, and the second is a command sequence number. Each time the application sends a command or status request, it increments the corresponding sequence number, and includes this number in the COPP command or request data.
3.  Concatenate the 128-bit random number from the graphics driver, the AES session key, the status sequence number, and the command sequence number. Encrypt this byte array using the driver's public key and pass the result to [**IAMCertifiedOutputProtection::SessionSequenceStart**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-sessionsequencestart).

**Send COPP Commands and Status Requests**

1.  Query for the available protection types and other information by calling [**IAMCertifiedOutputProtection::ProtectionStatus**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-protectionstatus).
2.  Set the desired protection levels by calling [**IAMCertifiedOutputProtection::ProtectionCommand**](/windows/desktop/api/Strmif/nf-strmif-iamcertifiedoutputprotection-protectioncommand).
3.  Periodically query for the current local protection level. Stop playback if the local protection level changes unexpectedly or if a problem is detected.

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



