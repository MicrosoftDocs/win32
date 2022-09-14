---
description: Interoperability with Legacy Audio APIs
ms.assetid: 34939f6d-a6e4-4f7a-afa3-b1fed52b471f
title: Interoperability with Legacy Audio APIs
ms.topic: article
ms.date: 05/31/2018
---

# Interoperability with Legacy Audio APIs

Many existing applications use legacy audio APIs such as DirectSound, DirectShow, and the Windows multimedia functions. With only minor modifications, these applications can be augmented to make use of [device roles](device-roles.md), [session volume controls](session-volume-controls.md), and other features of the core audio APIs in Windows Vista.

As discussed in [User-Mode Audio Components](user-mode-audio-components.md), the core audio APIs serve as the foundation on which higher-level audio APIs are built. In Windows Vista, the audio devices that applications access through legacy audio APIs such as DirectSound and the Windows media **waveOutXxx** and **waveInXxx** functions are, in fact, [audio endpoint devices](audio-endpoint-devices.md) that are implemented by the core audio APIs. Because of inherent limitations in the interfaces of legacy audio APIs, an application can access some but not all of the capabilities of audio endpoint devices through these interfaces. The following sections describe techniques for enhancing existing applications by accessing additional capabilities of audio endpoint devices directly through the core audio APIs. These enhancements typically require only minor changes to the existing application code.

The following sections describe how to incorporate features of the core audio APIs into existing applications that use legacy audio APIs:

-   [Device Roles for DirectSound Applications](device-roles-for-directsound-applications.md)
-   [Device Roles for DirectShow Applications](device-roles-for-directshow-applications.md)
-   [Device Roles for Legacy Windows Multimedia Applications](device-roles-for-legacy-windows-multimedia-applications.md)
-   [Audio Events for Legacy Audio Applications](audio-events-for-legacy-audio-applications.md)
-   [Notification Sounds for Legacy Audio Applications](notification-sounds-for-legacy-audio-applications.md)

## Related topics

<dl> <dt>

[Device Roles](device-roles.md)
</dt> </dl>

 

 



