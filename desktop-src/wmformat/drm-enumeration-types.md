---
title: Microsoft Windows Media DRM Client Enumeration Types
description: Learn about the enumerations that are supported by the Microsoft Windows Media DRM Client Extended APIs.
ms.assetid: 940f66e1-1dc1-414f-bba9-b91f4f0dfc45
keywords:
- Windows Media Format SDK,enumeration types
- digital rights management (DRM),enumeration types
- DRM (digital rights management),enumeration types
- DRM Client Extended APIs,enumeration types
- Client Extended APIs,enumeration types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Microsoft Windows Media DRM Client Enumeration Types

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table describes the enumerations that are supported by the Microsoft Windows Media DRM Client Extended APIs.



| Enumeration                                                                      | Description                                                                                                                                                   |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_ACTION\_ALLOWED\_QUERY\_RESULTS**](drm-action-allowed-query-results.md) | Used by the [**IWMDRMLicenseQuery::QueryActionAllowed**](iwmdrmlicensequery-queryactionallowed.md) interface to specify the reason an action is not allowed. |
| [**DRM\_ATTR\_DATATYPE**](drm-attr-datatype.md)                                 | Defines the data types used for DRM attributes and properties.                                                                                                |
| [**DRM\_CRYPTO\_TYPE**](drm-crypto-type.md)                                     | Defines the cryptographic algorithm types that can be used to encrypt content.                                                                                |
| [**DRM\_HTTP\_STATUS**](drmdrm-http-status.md)                                  | Defines a range of HTTP states for a DRM request.                                                                                                             |
| [**DRM\_INDIVIDUALIZATION\_STATUS**](drmdrm-individualization-status.md)        | Defines the valid states for DRM individualization.                                                                                                           |
| [**DRM\_LICENSE\_STATE\_CATEGORY**](drmdrm-license-state-category.md)           | Specifies the type of license restriction that is described by a [**DRM\_LICENSE\_STATE\_DATA**](drmdrm-license-state-data.md) structure.                    |
| [**MSDRM\_STATUS**](msdrm-status.md)                                            | Defines status conditions for the DRM subsystem.                                                                                                              |
| [**WMDRMNET\_POLICY\_TYPE**](wmdrmnet-policy-type.md)                           | Lists the types of policies that are available for Windows Media DRM for Network Devices operations.                                                          |
| [**WMT\_RIGHTS**](drm-wmt-rights.md)                                            | Defines the rights that may be specified in a DRM license.                                                                                                    |



 

## Related topics

<dl> <dt>

[**Programming Reference**](drm-programming-reference.md)
</dt> </dl>

 

 




