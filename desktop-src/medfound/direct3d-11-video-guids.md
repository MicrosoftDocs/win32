---
description: The following GUIDs support Direct3D 11 Video APIs.
ms.assetid: CF2F3058-328A-4128-B5C6-29723B49AB1E
title: Direct3D 11 Video GUIDs (D3d11.h)
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 11 Video GUIDs

The following GUIDs support Direct3D 11 Video APIs.

<dl> <dt>

<span id="D3D11_KEY_EXCHANGE_HW_PROTECTION"></span><span id="d3d11_key_exchange_hw_protection"></span>**D3D11\_KEY\_EXCHANGE\_HW\_PROTECTION**
</dt> <dd> <dl> <dt>



Indicates that the decoder will receive data from a hardware-based DRM component

**D3D11\_KEY\_EXCHANGE\_HW\_PROTECTION** can be specified in the *pKeyExchangeType* parameter of the [**ID3D11VideoDevice::CreateCryptoSession**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-createcryptosession) function to indicate that the [**ID3D11CryptoSession**](/windows/desktop/api/d3d11/nn-d3d11-id3d11cryptosession) interface will be used purely for communication between a user mode DRM component and the secure execution environment.

When this GUID is specified, the following methods should not be called:

-   [**ID3D11CryptoSession::GetCertificateSize**](/windows/desktop/api/d3d11/nf-d3d11-id3d11cryptosession-getcertificatesize)
-   [**ID3D11CryptoSession::GetCertificate**](/windows/desktop/api/d3d11/nf-d3d11-id3d11cryptosession-getcertificate)
-   [**ID3D11VideoContext::EncryptionBlt**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-encryptionblt)
-   [**ID3D11VideoContext::DecryptionBlt**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-decryptionblt)
-   [**ID3D11VideoContext::StartSessionKeyRefresh**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-startsessionkeyrefresh)
-   [**ID3D11VideoContext::FinishSessionKeyRefresh**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-finishsessionkeyrefresh)
-   [**ID3D11VideoContext::GetEncryptionBltKey**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-getencryptionbltkey)


</dt> </dl> </dd> <dt>

<span id="D3D11_DECODER_ENCRYPTION_HW_CENC"></span><span id="d3d11_decoder_encryption_hw_cenc"></span>**D3D11\_DECODER\_ENCRYPTION\_HW\_CENC**
</dt> <dd> <dl> <dt>



Indicates that the decoder will receive data from a hardware-based DRM component

Setting this GUID in the **guidConfigBitstreamEncryption** member of the [**D3D11\_VIDEO\_DECODER\_CONFIG**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_video_decoder_config) structure passed to the [**ID3D11VideoDevice::CreateVideoDecoder**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-createvideodecoder) API indicates that the following parameters will be passed in the [**ID3D11VideoDevice::DecoderBeginFrame**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-decoderbeginframe) call:



| Value                 | Description                                                                                                                                                                                                                                                    |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *ContentKeySize* | Contains the size of the [**D3D11\_VIDEO\_DECODER\_BEGIN\_FRAME\_CRYPTO\_SESSION**](/windows/desktop/api/d3d11_1/ns-d3d11_1-d3d11_video_decoder_begin_frame_crypto_session) structure.                                                                                                  |
| *pContentKey*    | A pointer to a [**D3D11\_VIDEO\_DECODER\_BEGIN\_FRAME\_CRYPTO\_SESSION**](/windows/desktop/api/d3d11_1/ns-d3d11_1-d3d11_video_decoder_begin_frame_crypto_session) providing the [**ID3D11CryptoSession**](/windows/desktop/api/d3d11/nn-d3d11-id3d11cryptosession) and the key information needed to decrypt the frame. |



 


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>D3d11.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D 11 Video APIs](direct3d-11-video-apis.md)
</dt> </dl>

 

 




