---
description: Notification Sounds for Legacy Audio Applications
ms.assetid: c5ad67d9-56fb-4bf0-aea4-5b49b0e5bf95
title: Notification Sounds for Legacy Audio Applications
ms.topic: article
ms.date: 05/31/2018
---

# Notification Sounds for Legacy Audio Applications

In Windows Vista, the operating system assigns all of its system notification sounds to a cross-process audio session that plays through the rendering endpoint device that is currently assigned to the eConsole [device role](device-roles.md). The system volume-control program, Sndvol, displays a volume slider that is dedicated to system notification sounds.

Some applications play notification sounds. Instead of requiring the user to manage an application's notification sounds through a separate volume slider in Sndvol, the application can assign its notification sounds to the same session as the system notification sounds. The Sndvol volume slider that controls the system notification sounds then controls the notification sounds from the application.

To enable this behavior, Windows Vista defines a SND\_SYSTEM flag for the legacy [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function. (This flag is not supported in earlier versions of Windows, including Windows Server 2003, Windows XP, and Windows 2000.) If the caller sets this flag, then the **PlaySound** function assigns the sound that it plays to the cross-process session that the operating system uses for its notification sounds. If the caller does not set the flag, then **PlaySound** assigns the sound that it plays to the default session—the process-specific session that is identified by the session GUID value GUID\_NULL. SND\_SYSTEM is defined in the header file Mmsystem.h. For more information about **PlaySound**, see the Windows SDK documentation.

## Related topics

<dl> <dt>

[Interoperability with Legacy Audio APIs](interoperability-with-legacy-audio-apis.md)
</dt> </dl>

 

 
