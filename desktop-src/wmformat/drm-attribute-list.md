---
title: DRM Attribute List
description: DRM Attribute List
ms.assetid: 222ef91c-b776-4de8-b1ad-88c2beca05aa
keywords:
- Windows Media Format SDK,attributes
- Advanced Systems Format (ASF),attributes
- ASF (Advanced Systems Format),attributes
- attributes,digital rights management (DRM)
- digital rights management (DRM),attributes
- DRM (digital rights management),attributes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM Attribute List

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

For convenience, the following table lists all the DRM-related file attributes. (These attributes are also listed in the table of all attributes under [Attribute List](attribute-list.md).)

Applications can set these values when writing DRM files and can retrieve them when reading.



| DRM file attribute                                                                   | Global identifier                             | Data type             |
|--------------------------------------------------------------------------------------|-----------------------------------------------|-----------------------|
| [**DRM\_ContentID**](drm-contentid.md)                                              | g\_wszWMDRM\_ContentID                        | **WMT\_TYPE\_STRING** |
| [**DRM\_DRMHeader\_ContentDistributor**](drm-drmheader-contentdistributor.md)       | g\_wszWMDRM\_DRMHeader\_ContentDistributor    | **WMT\_TYPE\_STRING** |
| [**DRM\_DRMHeader\_ContentID**](drm-drmheader-contentid.md)                         | g\_wszWMDRM\_DRMHeader\_ContentID             | **WMT\_TYPE\_STRING** |
| [**DRM\_DRMHeader\_IndividualizedVersion**](drm-drmheader-individualizedversion.md) | g\_wszWMDRM\_DRMHeader\_IndividualizedVersion | **WMT\_TYPE\_STRING** |
| [**DRM\_DRMHeader\_KeyID**](drm-drmheader-keyid.md)                                 | g\_wszWMDRM\_DRMHeader\_KeyID                 | **WMT\_TYPE\_STRING** |
| [**DRM\_DRMHeader\_LicenseAcqURL**](drm-drmheader-licenseacqurl.md)                 | g\_wszWMDRM\_DRMHeader\_LicenseAcqURL         | **WMT\_TYPE\_STRING** |
| [**DRM\_DRMHeader\_SubscriptionContentID**](drm-drmheader-subscriptioncontentid.md) | g\_wszWMDRM\_DRMHeader\_SubscriptionContentID | **WMT\_TYPE\_STRING** |
| [**DRM\_DRMHeader**](drm-drmheader.md)                                              | g\_wszWMDRM\_DRMHeader                        | **WMT\_TYPE\_STRING** |
| [**DRM\_IndividualizedVersion**](drm-individualizedversion.md)                      | g\_wszWMDRM\_IndividualizedVersion            | **WMT\_TYPE\_STRING** |
| [**DRM\_KeyID**](drm-keyid.md)                                                      | g\_wszWMDRM\_KeyID                            | **WMT\_TYPE\_STRING** |
| [**DRM\_LASignatureCert**](drm-lasignaturecert.md)                                  | g\_wszWMDRM\_LASignatureCert                  | **WMT\_TYPE\_STRING** |
| [**DRM\_LASignatureLicSrvCert**](drm-lasignaturelicsrvcert.md)                      | g\_wszWMDRM\_LASignatureLicSrvCert            | **WMT\_TYPE\_STRING** |
| [**DRM\_LASignaturePrivKey**](drm-lasignatureprivkey.md)                            | g\_wszWMDRM\_LASignaturePrivKey               | **WMT\_TYPE\_STRING** |
| [**DRM\_LASignatureRootCert**](drm-lasignaturerootcert.md)                          | g\_wszWMDRM\_LASignatureRootCert              | **WMT\_TYPE\_STRING** |
| [**DRM\_LicenseAcqURL**](drm-licenseacqurl.md)                                      | g\_wszWMDRM\_LicenseAcqURL                    | **WMT\_TYPE\_STRING** |
| [**DRM\_V1LicenseAcqURL**](drm-v1licenseacqurl.md)                                  | g\_wszWMDRM\_V1LicenseAcqURL                  | **WMT\_TYPE\_STRING** |



 

## Related topics

<dl> <dt>

[**Attributes By Type**](attributes-by-type.md)
</dt> <dt>

[**DRM Properties**](drm-properties.md)
</dt> </dl>

 

 




