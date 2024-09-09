---
title: The DRM Kernel Component (deprecated)
description: The DRM Kernel Component (deprecated)
ms.assetid: 016899fb-6d0a-4529-8649-5e8f29c89253
keywords:
- Windows Media Format SDK,Microsoft Secure Audio Path (SAP)
- digital rights management (DRM),Microsoft Secure Audio Path (SAP)
- DRM (digital rights management),Microsoft Secure Audio Path (SAP)
- Windows Media Format SDK,Secure Audio Path (SAP)
- digital rights management (DRM),Secure Audio Path (SAP)
- DRM (digital rights management),Secure Audio Path (SAP)
- Windows Media Format SDK,DRM kernel component
- digital rights management (DRM),kernel component
- DRM (digital rights management),kernel component
- Microsoft Secure Audio Path (SAP),DRM kernel component
- Secure Audio Path (SAP),DRM kernel component
- SAP (Secure Audio Path),DRM kernel component
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The DRM Kernel Component (deprecated)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature that will be supported with a different technical solution in future versions of Windows.

In the Microsoft Secure Audio Path (SAP) model, the DRM kernel component provides two basic features that protect the integrity of encrypted music.

First, the DRM client component and the DRM kernel component are in communication when a music file is played. This communication between components prevents anyone from tampering with the encrypted signal or from inserting false information.

Second, the DRM kernel component does not decrypt the music signal until all remaining components are authenticated. That is, before decrypting content and passing it to the next system component, the DRM kernel component checks each component that remains in the path to the sound card (each component that can access the content) and verifies that these components are signed with a certificate from Microsoft. An unsigned component might indicate a suspicious component or a malicious driver. So, when the DRM kernel component validates remaining components, if any component fails this test, the signal is halted and cannot be played. Otherwise, if all components pass validation, the DRM kernel component decrypts the music and passes it to the next component.

Microsoft digitally signs drivers that pass the Windows® Hardware Quality Lab (WHQL) tests to assure users that they are using the highest-quality drivers. This practice is standard and guarantees the authenticity of components because the signature cannot be forged, nor can the code be modified without destroying the signature. Drivers that are certified for Secure Audio Path must protect the audio data they process from access by untrusted components. 

Drivers included with Windows Millennium Edition and Windows XP are updated for Secure Audio Path and signed. Drivers that are not signed for use with Windows Me or Windows XP cannot play protected music. Driver manufacturers can reissue updated versions of their drivers that are signed by WHQL, and publish them on the Internet for consumers to download.

## Related topics

<dl> <dt>

[**Microsoft Secure Audio Path**](microsoft-secure-audio-path--deprecated.md)
</dt> </dl>

 

 




