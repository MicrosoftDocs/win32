---
title: Custom Scheme Registry Settings
description: Custom Scheme Registry Settings
ms.assetid: ded2b492-7755-4ba5-87cf-720a79ec79de
keywords:
- Windows Media Player,custom scheme registry settings
- Windows Media Player,schemes
- Windows Media Player,registry
- registry,custom scheme settings
- registry,schemes
- registry,settings for Windows Media Player
- schemes
- custom scheme registry settings
ms.topic: article
ms.date: 05/31/2018
---

# Custom Scheme Registry Settings

Schemes are custom protocols. Windows Media Player maintains a list of schemes in the registry on the user's computer. When the user attempts to play a digital media file, the Player first checks whether the Windows Media Format SDK supports the scheme. If it doesn't, the Player checks the scheme against the list in the registry. If a match is found, the Player then checks a value that indicates which underlying technology, or *runtime* (such as Microsoft DirectShow or the Windows Media Format SDK), can be used to play the file. If no match is found, the Player presents the user with a warning dialog box that prompts the user for permission to attempt to play the file. If you stream digital media files using a custom protocol scheme, you can prevent this warning from appearing on the user's computer by registering the scheme and providing a value for the runtime.

The list of schemes is maintained as a set of registry keys that match the registered schemes, without the colon and the two slashes (://). For example, the key for the wmhtml:// scheme, which is used to stream rich media, is named "wmhtml". A separate list is maintained for the local machine and for each user. For the local machine, the scheme keys are subkeys of the following registry key:

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Multimedia\\WMPlayer\\Schemes\\**

For example, the key for the wmhtml:// scheme for the local machine is:

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Multimedia\\WMPlayer\\Schemes\\wmhtml**

To change values in this key or to create a new subkey, the current user must be an administrator for the computer.

For individual users, the scheme keys are subkeys of the following registry key:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\Player\\Schemes\\**

For example, the key for the wmhtml:// scheme for the current user is:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\Player\\Schemes\\wmhtml**

When checking for registered schemes, the Player first checks the values located in **HKEY\_LOCAL\_MACHINE**. If none are found for the current scheme, the Player next checks the values in **HKEY\_CURRENT\_USER**. If none are found for the current scheme, the Player displays the warning to the user.

Each scheme subkey may contain one of the following possible values for *Runtime*.



| Value | Description                                |
|-------|--------------------------------------------|
| 6     | Render using the Windows Media Format SDK. |
| 7     | Render using Microsoft DirectShow.         |



 

Changing the *Runtime* value for a scheme that the Windows Media Format SDK supports will have no effect. The Player will always use the Windows Media Format SDK as the runtime for schemes that the Windows Media Format SDK supports. This registry value is designed to allow runtime configuration for custom schemes.

## Related topics

<dl> <dt>

[**Registry Settings**](registry-settings.md)
</dt> </dl>

 

 




