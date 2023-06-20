---
title: Revocation Type Identifiers
description: Revocation Type Identifiers
ms.assetid: a52d51bf-bbde-4ad5-8cd2-b86a232ac07e
keywords:
- Windows Media Format SDK,revocation type identifiers
- digital rights management (DRM),revocation type identifiers
- DRM (digital rights management),revocation type identifiers
- DRM Client Extended APIs,revocation type identifiers
- Client Extended APIs,revocation type identifiers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Revocation Type Identifiers

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The constants listed in the following table define GUID values that identify different types of revocation.



| Constant                         | Description                                                                                         |
|----------------------------------|-----------------------------------------------------------------------------------------------------|
| WMDRM\_REVOCATION\_TYPE\_APP     | Identifies revocation information pertaining to application certificates.                           |
| WMDRM\_REVOCATION\_TYPE\_DEVICE  | Identifies revocation information pertaining to device certificates.                                |
| WMDRM\_REVOCATION\_TYPE\_CARDEA  | Identifies revocation information pertaining to Windows Media DRM for Network Devices certificates. |
| WMDRM\_REVOCATION\_TYPE\_REVINFO | Not documented in this release.                                                                     |
| WMDRM\_REVOCATION\_TYPE\_GRL     | Not documented in this release.                                                                     |
| WMDRM\_REVOCATION\_TYPE\_HDCP    | Not documented in this release.                                                                     |



 

## Related topics

<dl> <dt>

[**Constants**](constants.md)
</dt> </dl>

 

 




