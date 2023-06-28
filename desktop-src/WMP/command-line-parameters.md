---
title: Command Line Parameters
description: Command Line Parameters
ms.assetid: c4af8a03-2cab-4ecd-bbd8-c83869822901
keywords:
- Windows Media Player,parameters
- Windows Media Player,command-line parameters
- Windows Media Player,Wmplayer
- Windows Media Player,Wmpconfig
- Windows Media Player,Wmpnscfg
- command-line parameters
- Wmplayer
- Wmpconfig
- Wmpnscfg
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Command Line Parameters

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Command Line Parameters for Wmplayer

Windows Media Player supports a set of command line parameters that specify how the Player behaves when it starts. The following table details the parameters and their behaviors.



| Syntax                                                                                                              | Behavior                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "*path\\filename*"(For example: `wmplayer "c:\filename.wma"`)<br/>                                            | Start the Player and play the file.                                                                                                                                                                                                                                                                                                        |
| "*path\\filename*" /fullscreen(For example: `wmplayer "c:\filename.wmv" /fullscreen`)<br/>                    | Play the specified file in full-screen mode.You must specify the path and file name of the content to play.<br/>                                                                                                                                                                                                                     |
| /Device:{DVD\|AudioCD}(For example: `wmplayer /device:audio CD`)<br/>                                         | Play a DVD or audio CD.                                                                                                                                                                                                                                                                                                                    |
| "*path\\filename*?WMPSkin=*skin name*"For example: `wmplayer "c:\filename.wma?wmpskin=headspace"`<br/>        | Open the Player, applying the specified skin.                                                                                                                                                                                                                                                                                              |
| /Service:*keyname*                                                                                                  | Open the Player showing the online store specified by *keyname*.Requires Windows Media Player 10 or later.<br/>                                                                                                                                                                                                                      |
| /Task NowPlaying                                                                                                    | Open the Player in the **Now Playing** feature.                                                                                                                                                                                                                                                                                            |
| /Task MediaGuide                                                                                                    | Open the Player in the **Media Guide** feature (current active online store in Windows Media Player 10 or later).                                                                                                                                                                                                                          |
| /Task CDAudio                                                                                                       | Open the Player in the **Copy from CD** feature (**Rip** feature in Windows Media Player 10 or Windows Media Player 11). This parameter is not supported in Windows Media Player 12.                                                                                                                                                       |
| /Task CDWrite                                                                                                       | Open the Player in the **Burn** feature.Requires Windows Media Player 10.<br/>                                                                                                                                                                                                                                                       |
| /Task MediaLibrary                                                                                                  | Open the Player in the **Library** feature.                                                                                                                                                                                                                                                                                                |
| /Task RadioTuner                                                                                                    | Open the Player in the **Radio Tuner** feature (current active online store in Windows Media Player 10 or later).                                                                                                                                                                                                                          |
| /Task PortableDevice                                                                                                | Open the Player in the **Copy to CD or Device** feature (**Sync** feature in Windows Media Player 10 or later).                                                                                                                                                                                                                            |
| /Task Services /Service *servicename*                                                                               | Open the Player in the **Premium Services** feature, showing the service specified by the *servicename* parameter. This value is the unique name for the service. If the specified service has not been previously viewed, the *servicename* parameter is ignored. (Opens the specified online store in Windows Media Player 10 or later.) |
| /Task ServiceTask*X*                                                                                                | Open the Player in the online store service task pane specified by *X*. For example, /Task ServiceTask1 opens the Player in the first online store service task pane.                                                                                                                                                                      |
| /Task SkinViewer                                                                                                    | Open the Player in the **Skin Chooser** feature.                                                                                                                                                                                                                                                                                           |
| /Playlist *PlaylistName*                                                                                            | Open the Player and play the specified playlist.                                                                                                                                                                                                                                                                                           |
| /Schema:{Music\|Pictures\|Video\|TV\|Other}For example: `wmplayer /Schema:Pictures /Task:PortableDevice`<br/> | Open the Player, showing the specified media category. Requires Windows Media Player 11.                                                                                                                                                                                                                                                   |



 

## Command Line Parameters for Wmpconfig

Wmpconfig.exe is used to execute certain commands in Windows Media Player that require administrator permission. Examples include the starting and stopping of browsing and sharing services and the enabling of exceptions in the Windows Firewall. The following table describes the possible values for the command line parameters.



| Syntax                                                                                    | Behavior                                                                   |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| DisableHMEDevice *MAC*                                                                    | Disables the device specified by a Media Access Control (MAC) identifier.  |
| HMEOff Example:<br/> wmpconfig HMEOff<br/>                                    | Disables the Windows Media Player Network Sharing Service.                 |
| HMEOn Example:<br/> wmpconfig HMEOn<br/>                                      | Enables sharing, browsing, and the firewall exception.                     |
| RemoveHMEDevice *MAC*                                                                     | Removes the device specified by a MAC identifier.                          |
| RestoreHMEDevice *MAC*                                                                    | Restores the device specified by a MAC identifier.                         |
| SetDVDParentalLevel *level*Example:<br/> wmpconfig SetDVDParentalLevel 3<br/> | Sets the DVD parental control level. The level is specified as an integer. |



 

## Command Line Parameters for Wmpnscfg

Microsoft Windows uses wmpnscfg.exe to alert users when media rendering devices are found on the network. Wmpnscfg starts the Windows Media Player Network Sharing Service (NSS) and then waits for notifications from the service. When wmpnscfg is notified that a new media device is available on the network, it displays a popup in the system tray that informs the user about the availability of the new device. If the user clicks the popup, wmpnscfg launches Windows Media Player, which displays a dialog box that asks the user to either allow or deny sharing with the new device.

Typically, Windows calls wmpnscfg with no command line parameters. However, there is one parameter available, described in the following table.



| Parameter | Behavior                         |
|-----------|----------------------------------|
| /Close    | Close all instances of wmpnscfg. |



 

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 





