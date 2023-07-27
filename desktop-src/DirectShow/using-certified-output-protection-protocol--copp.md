---
description: Using Certified Output Protection Protocol (COPP)
ms.assetid: 23eebe93-416b-48c8-a05f-019e38b9a660
title: Using Certified Output Protection Protocol (COPP)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Certified Output Protection Protocol (COPP)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Certified Output Protection Protocol (COPP) enables an application to protect a video stream as it travels from the graphics adapter to the display device. An application can use COPP to discover what kind of physical connector is attached to the display device, and what types of output protection are available. Protection mechanisms include the following:

-   High-Bandwidth Digital Content Protection (HDCP)
-   Copy Generation Management System — Analog (CGMS-A)
-   Analog Copy Protection (ACP)

If the graphics adapter supports one of these mechanisms, the application can use COPP to set the protection level.

COPP defines a protocol that is used to establish a secure communications channel with the graphics driver. It uses Message Authentication Codes (MACs) to verify the integrity of the COPP commands that are passed between the application and the display driver. The application uses COPP by calling methods on the [**IAMCertifiedOutputProtection**](/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection) interface of the DirectShow Video Mixing Renderer filter (VMR-7 or VMR-9).

COPP does not define anything about the digital rights policies that might apply to digital media content. Also, COPP itself does not implement any output protection systems. The COPP protocol simply provides a way to set and query protection levels on the graphics adapter, using the protection systems provided by the adapter.

This section assumes that you are familiar with the following technologies:

-   DirectShow
-   Windows Media Format SDK
-   XML
-   Public-key cryptography and symmetric cryptography

The code examples in this section use Microsoft's CryptoAPI to perform cryptographic operations. This section contains the following topics:

-   [Overview of COPP](overview-of-copp.md)
-   [Obtaining the Driver's Certificate Chain](obtaining-the-drivers-certificate-chain.md)
-   [Validating the Certificate Chain](validating-the-certificate-chain.md)
-   [Certificate Revocation Lists](certificate-revocation-lists.md)
-   [Importing the Driver's Public Key](importing-the-drivers-public-key.md)
-   [Initiating a COPP Session](initiating-a-copp-session.md)
-   [Sending COPP Status Requests](sending-copp-status-requests.md)
-   [Sending COPP Commands](sending-copp-commands.md)
-   [Testing Whether a Graphics Driver Supports COPP](testing-whether-a-graphics-driver-supports-copp.md)
-   [COPP Query Reference](copp-query-reference.md)
-   [COPP Command Reference](copp-command-reference.md)

## Related topics

<dl> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 



