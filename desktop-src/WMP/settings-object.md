---
title: Settings Object (Windows Media Player SDK)
description: The Settings object provides a way to modify various Windows Media Player settings by using the following properties and methods.
ms.assetid: 'f22e8c37-f0c6-4268-a6ed-ce03cff5f3e5'
keywords:
- Settings Object Windows Media Player
topic_type:
- apiref
api_name:
- Settings Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Settings Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Settings** object provides a way to modify various Windows Media Player settings by using the following properties and methods.

The **Settings** object supports the following properties.



| Property                                                  | Description                                                                                                                      |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [autoStart](settings-autostart.md)                       | Specifies or retrieves a value indicating whether the current media item begins playing automatically.                           |
| [balance](settings-balance.md)                           | Specifies or retrieves the current stereo balance.                                                                               |
| [baseURL](settings-baseurl.md)                           | Specifies or retrieves the base URL used for relative path resolution with URL script commands that are embedded in media files. |
| [defaultAudioLanguage](settings-defaultaudiolanguage.md) | Retrieves the locale identifier (LCID) of the default audio language specified in Windows Media Player.                          |
| [defaultFrame](settings-defaultframe.md)                 | Specifies or retrieves the name of the frame used to display a URL that is received in a **ScriptCommand** event.                |
| [enableErrorDialogs](settings-enableerrordialogs.md)     | Specifies or retrieves a value indicating whether error dialog boxes are shown automatically.                                    |
| [invokeURLs](settings-invokeurls.md)                     | Specifies or retrieves a value indicating whether URL events should launch a Web browser.                                        |
| [isAvailable](settings-isavailable.md)                   | Retrieves whether a specified type of information is available or a specified action can be performed.                           |
| [mediaAccessRights](settings-mediaaccessrights.md)       | Retrieves a value indicating the rights currently granted for library access.                                                    |
| [mute](settings-mute.md)                                 | Specifies or retrieves a value indicating whether audio is muted.                                                                |
| [playCount](settings-playcount.md)                       | Specifies or retrieves the number of times a media item will play.                                                               |
| [rate](settings-rate.md)                                 | Specifies or retrieves the current playback rate.                                                                                |
| [volume](settings-volume.md)                             | Specifies or retrieves the current volume.                                                                                       |



 

The **Settings** object supports the following methods.



| Method                                                            | Description                                                 |
|-------------------------------------------------------------------|-------------------------------------------------------------|
| [getMode](settings-getmode.md)                                   | Determines whether the loop mode or shuffle mode is active. |
| [requestMediaAccessRights](settings-requestmediaaccessrights.md) | Requests a specified level of access to the library.        |
| [setMode](settings-setmode.md)                                   | Sets the loop mode or shuffle mode to active or inactive.   |



 

The **Settings** object is accessed through the following property.



| Object                      | Property                        |
|-----------------------------|---------------------------------|
| [Player](player-object.md) | [settings](player-settings.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




