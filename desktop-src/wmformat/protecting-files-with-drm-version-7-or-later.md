---
title: Protecting Files with DRM Version 7 or Later
description: Protecting Files with DRM Version 7 or Later
ms.assetid: 906f16c1-6573-47e9-8228-58dc126f6357
keywords:
- Windows Media Format SDK,creating protected files
- Windows Media Format SDK,protected files
- Advanced Systems Format (ASF),creating protected files
- ASF (Advanced Systems Format),creating protected files
- Advanced Systems Format (ASF),protected files
- ASF (Advanced Systems Format),protected files
- Advanced Systems Format (ASF),WMStubDRM.lib
- ASF (Advanced Systems Format),WMStubDRM.lib
- WMStubDRM.lib,creating protected files
- WMStubDRM.lib,protected files
- digital rights management (DRM),WMStubDRM.lib
- DRM (digital rights management),WMStubDRM.lib
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Protecting Files with DRM Version 7 or Later

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To protect files with Windows Media DRM version 7 or later, use the writer object's [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) method to set DRM attributes. Because DRM version 7 and later versions enable unique licenses for each protected file or set of files, the **IWMDRMWriter** interface also has methods for creating keys. These methods are provided for convenience only.

To protect ASF files using DRM version 7 or later, perform the following steps:

1.  Link to WMStubDRM.lib and, if necessary, unlink wmvcore.lib.
2.  Call the [**WMCreateWriter**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter) function to create the DRM writer. The first argument is reserved and must be set to **NULL**.
3.  Set a profile for the writer to use by calling [**IWMWriter::SetProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setprofile) or [**IWMWriter::SetProfileByID**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmwriter-setprofilebyid). You must set a profile in the writer before setting any DRM attributes. DRM is supported only for profiles that use the Windows Media Audio or Windows Media Video codecs
4.  Obtain the writer object's [**IWMDRMWriter**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmwriter) interface.
5.  Call [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) and set [**Use\_Advanced\_DRM**](use-advanced-drm.md) to **TRUE**.
6.  If you need to generate a new key seed, call [**IWMDRMWriter::GenerateKeySeed**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-generatekeyseed). In most cases, you will be reusing a key seed that was generated previously. This value must remain secret; it is not written into the file.
7.  Call [**IWMDRMWriter::GenerateKeyID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-generatekeyid) to create a key ID, which is the second value used to create the actual key. Unlike the key seed, the key ID is public and is written to the file in the DRM header in the clear. Create a new key ID for each new file you create.
8.  Call **IWMDRMWriter::GenerateSigningKeyPair** if necessary to generate a public and private key that will be used to sign the advanced DRM ASF Header object. For more information about these keys, see [**IWMDRMWriter::GenerateSigningKeyPair**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-generatesigningkeypair).
9.  If necessary, obtain the values to populate the DRM header's digital signature object. If you do not have a working version of Windows Media Rights Manager installed on your system, you must configure the ASF file header's digital signature object by specifying the following four attributes, which all must be obtained from Microsoft:

    -   [**DRM\_LASignatureRootCert**](drm-lasignaturerootcert.md)
    -   [**DRM\_LASignatureCert**](drm-lasignaturecert.md)
    -   [**DRM\_LASignatureLicSrvCert**](drm-lasignaturelicsrvcert.md)
    -   [**DRM\_LASignaturePrivKey**](drm-lasignatureprivkey.md)

    If you do have Windows Media Rights Manager installed, there is no need to set these attributes in your application. The DRM component will retrieve these attributes and use them to sign the header automatically. If you have an activated version of Windows Media Rights Manager on another machine, and wish to reuse those digital signature object values, you can find them in the registry. The license server certificate is stored under HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\WM Rights Manager\\License Server\\Certs:cert1, and the root certificate is stored under HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\WM Rights Manager\\License Server\\Certs:cert2. When protecting files with DRM version 7, you must use the values from these registry keys. For the **DRM\_LASignaturePrivKey property**, use either **GenerateSigningKeysEx** (through the Windows Media Rights Manager SDK) or else reuse the value installed by Windows Media Rights Manager under HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\WM Rights Manager\\License Server:Info\_Cert0. For the **DRM\_LASignatureCert** property, use either **GenerateSigningKeysEx** (through the Windows Media Rights Manager SDK) or else the value installed by Windows Media Rights Manager under HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\WM Rights Manager\\License Server\\Certs:cert0.

10. Call [**IWMDRMWriter::SetDRMAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmwriter-setdrmattribute) as many times as necessary to configure the writer object, which will set the required DRM header attributes as necessary. These properties persist for the lifetime of the writer object or until they are reset with a new value. They do not need to be reset for each new file you create.

    The following properties are required by the writer object:

    -   [**DRM\_HeaderSignPrivKey**](drm-headersignprivkey.md)
    -   [**DRM\_KeySeed**](drm-keyseed.md)
    -   [**DRM\_V1LicenseAcqURL**](drm-v1licenseacqurl.md)
    -   [**DRM\_KeyID**](drm-keyid.md)
    -   [**DRM\_LicenseAcqURL**](drm-licenseacqurl.md)

    The following properties are optional:

    -   [**DRM\_ContentID**](drm-contentid.md)
    -   [**DRM\_IndividualizedVersion**](drm-individualizedversion.md)

    In addition, you may specify user-defined DRM file attributes directly using the [**DRM\_DRMHeader**](drm-drmheader.md) base attribute. You can add any additional attribute you wish, such as "DRMHeader.RequireSAP" for example, as a way of communicating additional information that will be used by the license server in creating the license. The license server must be aware in advance of any additional properties you add. There is no way to discover unknown properties programmatically.

11. Write the file using the [**IWMWriter**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter) interface methods as described elsewhere in this documentation. To create a live-DRM stream, simply write to a network sink. You can also write to a push sink.
12. If necessary, create a license for the file using Windows Media Rights Manager. This task can also be performed by a third-party license server. For live-DRM scenarios, end users will need to obtain a license either before the stream begins, or else at the time they first attempt to connect to it.

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> <dt>

[**DRM Attribute List**](drm-attribute-list.md)
</dt> <dt>

[**DRM Properties**](drm-properties.md)
</dt> <dt>

[**IWMDRMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmwriter)
</dt> <dt>

[**IWMHeaderInfo::SetAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-setattribute)
</dt> <dt>

[**IWMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter)
</dt> <dt>

[**Reading Protected Files**](reading-protected-files.md)
</dt> <dt>

[**WMCreateWriter**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter)
</dt> </dl>

 

 




