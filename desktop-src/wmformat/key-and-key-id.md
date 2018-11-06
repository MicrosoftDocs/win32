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
ms.date: 05/31/2018
---

# Key and Key ID

When you package a file, you use a key. A key is a piece of data used in the encryption algorithms that protect the content. There are two parts to each key: a license key seed and a key ID (often abbreviated as KID). The key ID is public, and is stored in the file header as a way to identify the key required to decrypt the file. The license key seed is a secret value that must be shared by the content packager and the license issuer.

A key ID identifies protected content from the perspective of the license. Although you can use the same key ID for multiple files, it is recommended that you always use a unique key ID for each piece of protected content.

Many of the methods described in this documentation use key ID strings to select licenses. These strings contain the key ID encoded in base64.

## Related topics

<dl> <dt>

[**Concepts**](drmconcepts.md)
</dt> </dl>

 

 




