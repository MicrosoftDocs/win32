---
title: Creating and Initializing a DRM Writer
description: Creating and Initializing a DRM Writer
ms.assetid: ce0508e1-f69f-4e09-8c32-8c9dac48b5ec
keywords:
- Windows Media Format SDK,DRM writers
- digital rights management (DRM),creating DRM writers
- DRM (digital rights management),creating DRM writers
- digital rights management (DRM),initializing DRM writers
- DRM (digital rights management),initializing DRM writers
- DRM Client Extended APIs,DRM writers
- Client Extended APIs,DRM writers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating and Initializing a DRM Writer

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following steps are required to initialize an ASF writer object for importing encrypted media samples in Windows Media DRM.

1.  Follow steps 1 to 4 of [Importing License and Key Material](importing-license-and-key-material.md).
2.  Create and initialize an ASF writer object using the appropriate Windows Media DRM key material. For more information, see [Enabling DRM Support](enabling-drm-support.md).
3.  Set each of the following attributes by calling [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute):
    -   DRM\_HeaderSignPrivKey
    -   DRM\_V1LicenseAcqURL
    -   DRM\_KeyID
    -   DRM\_LicenseAcqURL
4.  If a licensed version of Windows Media Rights Manager is not installed on the computer running your software, then the following four attributes must also be set:
    -   DRM\_LASignatureRootCert
    -   DRM\_LASignatureCert
    -   DRM\_LASignatureLicSrvCert
    -   DRM\_LASignaturePrivKey
    -   Application for the necessary encryption certificates can be completed by filling out the [Windows Media Licensing Agreement (WMLA)](https://www.microsoft.com/licensing/default) online.
5.  Create a session key and fill out a [**WMDRM\_IMPORT\_SESSION\_KEY**](wmdrm-import-session-key.md) structure. The session key will be used for encrypting a content key. For an example, see [Create Session Key Example](create-session-key-example.md).
6.  Create a content key from a random RC4 initialization vector, and fill out a [**WMDRM\_IMPORT\_CONTENT\_KEY**](wmdrm-import-content-key.md) structure. The content key is used for encrypting the media samples. For an example, see [Create Content Key Example](create-content-key-example.md).
7.  Encrypt the content key with the session key, using RC4 encryption.
8.  Extract the machine certificate collection key. For an example, see [Get Machine Certificate Example](get-machine-certificate-example.md).
9.  Encrypt the session key with the public key extracted from the certificate.
10. Fill out a [**WMDRM\_IMPORT\_INIT\_STRUCT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmdrm_import_init_struct) structure.
11. Call the [**IWMDRMWriter3::SetProtectStreamSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter3-setprotectstreamsamples) method to notify the SDK that samples coming into the writer are already protected and should be sent directly to the Windows Media DRM client for import.
12. Call [**IWMWriter::BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).

The remaining steps for creating a DRM-protected file are documented in the Windows Media Format SDK Programming Guide. For more information, see [Creating Protected Files](creating-protected-files.md).

The next step is to iterate through each media sample, encrypt it, and pass it to the writer object. For more information, see the [Encrypting and Importing Media Samples](encrypting-and-importing-media-samples.md).

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> <dt>

[**DRM Import**](drm-import.md)
</dt> </dl>

 

 




