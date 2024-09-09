---
title: Key and Key ID
description: Key and Key ID
ms.assetid: 40618771-d601-4c31-8da9-5c649651f2f2
keywords:
- Windows Media Format SDK,digital rights management (DRM)
- digital rights management (DRM),keys
- DRM (digital rights management),keys
- digital rights management (DRM),KID
- DRM (digital rights management),KID
- key ID (KID)
- KID (key ID)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Key and Key ID

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you package a file, you use a key. A key is a piece of data used in the encryption algorithms that protect the content. There are two parts to each key: a license key seed and a key ID (often abbreviated as KID). The key ID is public, and is stored in the file header as a way to identify the key required to decrypt the file. The license key seed is a secret value that must be shared by the content packager and the license issuer.

A key ID identifies protected content from the perspective of the license. Although you can use the same key ID for multiple files, it is recommended that you always use a unique key ID for each piece of protected content.

Many of the methods described in this documentation use key ID strings to select licenses. These strings contain the key ID encoded in base64.

## Related topics

<dl> <dt>

[**Concepts**](drmconcepts.md)
</dt> </dl>

 

 




