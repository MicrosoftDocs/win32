---
title: Viewing or Modifying the Music Signal (deprecated)
description: Viewing or Modifying the Music Signal (deprecated)
ms.assetid: 47150951-2ab5-4cbe-ae57-4ebd23943f1d
keywords:
- Windows Media Format SDK,Microsoft Secure Audio Path (SAP)
- digital rights management (DRM),Microsoft Secure Audio Path (SAP)
- DRM (digital rights management),Microsoft Secure Audio Path (SAP)
- Windows Media Format SDK,Secure Audio Path (SAP)
- digital rights management (DRM),Secure Audio Path (SAP)
- DRM (digital rights management),Secure Audio Path (SAP)
- Windows Media Format SDK,music signal viewing or modifying
- digital rights management (DRM),music signal viewing or modifying
- DRM (digital rights management),music signal viewing or modifying
- Microsoft Secure Audio Path (SAP),music signal viewing or modifying
- Secure Audio Path (SAP),music signal viewing or modifying
- SAP (Secure Audio Path),music signal viewing or modifying
ms.topic: article
ms.date: 05/31/2018
---

# Viewing or Modifying the Music Signal (deprecated)

This page documents a feature that will be supported with a different technical solution in future versions of Windows.

In the Microsoft Secure Audio Path (SAP) model, applications cannot modify protected music in any way. For example, when an application attempts to intercept a music signal, the signal sounds like random noise. As a result, applications that normally modify signals (such as an equalizer) cannot change the sound of the music.

Some applications merely view a music signal. For example, some applications display flashing lights in time with the music signal, but do not modify it. To accommodate applications that view signals, a small part of the music is decrypted and passed in clear form with the encrypted content. The resulting signal is very poor (worse than telephone quality) but can suffice for applications that view signals.

## Related topics

<dl> <dt>

[**Microsoft Secure Audio Path**](microsoft-secure-audio-path--deprecated.md)
</dt> </dl>

 

 




