---
title: Library Access
description: Library Access
ms.assetid: 9f722531-a551-4ca9-be5f-01a291a180b0
keywords:
- Windows Media Player,library
- Windows Media Player object model,library
- object model,library
- Windows Media Player Mobile,library for object model
- Windows Media Player ActiveX control,library for object model
- Windows Media Player Mobile ActiveX control,library for object model
- ActiveX control,library for object model
- Windows Media Player library,access
- library,accessing
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Library Access

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Properties and methods of the Windows Media Player object model that access the library require either read-only or read/write access to the database. The library contains information that some users want to keep private and that should be accessed or altered only with their consent.

For Windows Media Player 9 Series or later, you can programmatically determine access level. To determine the current level of access granted to your code, retrieve the *Settings*.**mediaAccessRights** property. That property returns "none", "read", or "full" (read/write). To request specific access rights, call the *Settings*.**requestMediaAccessRights** method, passing a parameter that specifies the level you are requesting. The method displays a message to the user explaining the requested level of access, and returns a **Boolean** value indicating whether the access was granted.

Certain access rights are granted automatically depending on where your code is running relative to the user's computer.

-   If your webpage or program is located on the user's computer, full access rights are granted by default.
-   Web pages have read access to *Player*.**currentMedia**, *Player*.**currentPlaylist**, and *Media*.**sourceURL** when the webpage is located in an Internet Explorer security zone that is the same as or less restricted than the security zone of the media item or playlist.

    Ranging from least restricted to most restricted, the security zones are the **Trusted** zone (including the user's local computer), the **Local intranet** zone, the **Internet** zone, and the **Restricted** zone.

    For example, a webpage in the **Local intranet** zone has full access rights to *Player*.**currentMedia** when the corresponding media item is on the local intranet or the Internet, but access rights must be requested for media items located on a user's local computer or on a website in the **Trusted** zone.

You should test your Web-based or Windows-based application in all of the security zones it may encounter. The application should be designed to handle denial of an access request correctly.

Windows Media Player object model versions prior to Windows Media Player 9 Series do not include **mediaAccessRights** or **requestMediaAccessRights**. These earlier versions of Windows Media Player enable the user to set access levels using the **Options** dialog box.

## Related topics

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> <dt>

[**Working with the Library**](working-with-the-library.md)
</dt> </dl>

 

 




