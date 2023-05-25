---
title: Disabling Digital Output (deprecated)
description: Disabling Digital Output (deprecated)
ms.assetid: 208ceb23-e0a0-4dee-aeba-e9d640248f75
keywords:
- Windows Media Format SDK,Microsoft Secure Audio Path (SAP)
- digital rights management (DRM),Microsoft Secure Audio Path (SAP)
- DRM (digital rights management),Microsoft Secure Audio Path (SAP)
- Windows Media Format SDK,Secure Audio Path (SAP)
- digital rights management (DRM),Secure Audio Path (SAP)
- DRM (digital rights management),Secure Audio Path (SAP)
- Microsoft Secure Audio Path (SAP),disabling digital output
- Secure Audio Path (SAP),disabling digital output
- SAP (Secure Audio Path),disabling digital output
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Disabling Digital Output (deprecated)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature that will be supported with a different technical solution in future versions of Windows.

Another feature of Microsoft Secure Audio Path is the ability to disable digital output. Certain sound cards provide a way to send digital output from a hardware device; these devices might be certified and will pass authorization from the DRM kernel component. So, if a legitimate sound card has digital output enabled, people can still capture a perfect digital recording of protected music.

This feature lets content owners or license issuers disable digital output by setting a parameter in licenses for their music. If this parameter is set, the sound card disables its digital output capability when playing protected music. Users can listen to decrypted music, but they cannot make copies.

## Related topics

<dl> <dt>

[**Microsoft Secure Audio Path**](microsoft-secure-audio-path--deprecated.md)
</dt> </dl>

 

 




