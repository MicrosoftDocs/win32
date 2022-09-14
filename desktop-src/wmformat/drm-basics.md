---
title: DRM Basics
description: DRM Basics
ms.assetid: f36da29d-5f9d-441d-8061-eb50331a8e7a
keywords:
- Windows Media Format SDK,DRM basics
- digital rights management (DRM),about
- DRM (digital rights management),about
- digital rights management (DRM),protecting content
- DRM (digital rights management),protecting content
- digital rights management (DRM),packaging content
- DRM (digital rights management),packaging content
- digital rights management (DRM),reading protected content
- DRM (digital rights management),reading protected content
- protecting content
- packaging content
ms.topic: article
ms.date: 05/31/2018
---

# DRM Basics

The Windows Media DRM technologies are fairly simple from the perspective of the Windows Media Format SDK. Components of the SDK can be used to protect content and to play protected content.

## Protecting Content

Protecting content (also called packaging content) involves encrypting the data section of the file and including some information in the file header that enables players to decrypt the content.

To encrypt the content, you need a key, which is a value used to seed the encryption algorithms. A key is made up of two pieces: a key seed (or private key), and a key identifier (or public key). The key seed is the secret value with which you encode content. The key identifier is a public value that is included in the header of a protected file.

When a file is protected, it cannot be decrypted without a license. A license includes information that specifies the terms of use for the protected content. The terms of a license are decided by the content owner and can be customized to meet a variety of needs. Part of the process of packaging a file is to include the URL of a Web page where users can acquire a license to access the content.

## Reading Protected Content

To read protected content, a license for the content must reside on the client computer. Some license restrictions are checked internally by the DRM components of the Windows Media Format SDK, while others must be enforced by your application.

You can use the objects of the Windows Media Format SDK to assist the user in acquiring licenses for content and to perform other administrative tasks, such as updating DRM components and backing up licenses.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




