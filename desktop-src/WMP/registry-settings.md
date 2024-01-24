---
title: Registry Settings
description: Registry Settings
ms.assetid: 'aeb1f731-9d1f-4962-9101-fadf2dd23b4b'
keywords:
- Windows Media Player,registry
- registry,settings for Windows Media Player
- SDK (software development kit),registry
- software development kit (SDK),registry
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Registry Settings

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 9 Series or later uses the registry to store certain settings. You can make changes to these settings to change the behavior of Windows Media Player and the Windows Media Player control.

The following sections detail the supported registry settings.



| Section                                                                                                        | Description                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [File Name Extension Registry Settings](file-name-extension-registry-settings.md)                             | Describes how to register a custom file name extension.                                                                                                               |
| [Custom Scheme Registry Settings](custom-scheme-registry-settings.md)                                         | Describes how to register a custom scheme.                                                                                                                            |
| [Folder Monitoring Registry Settings](folder-monitoring-registry-settings.md)                                 | Describes how to register file folders to be monitored by Windows Media Player.                                                                                       |
| [Firewall Port Registry Settings](firewall-port-registry-settings.md)                                         | Describes a registry entry that Windows Media Player sets to specify whether firewalls should leave ports open for library sharing.                                   |
| [Silent Acquisition Registry Setting](silent-acquisition-registry-setting.md)                                 | Describes a registry entry that Windows Media Player uses to determine whether to download usage rights automatically when the user plays or syncs protected content. |
| [Registering Application Dependency](registering-application-dependency.md)                                   | Provides information about how to register your application to ensure the correct runtime files exist on the user's computer.                                         |
| [Registry Entries for Tracking Installation Progress](registry-entries-for-tracking-installation-progress.md) | Describes registry entries that installation programs can use to track the progress of Windows Media Player setup.                                                    |



 

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 




