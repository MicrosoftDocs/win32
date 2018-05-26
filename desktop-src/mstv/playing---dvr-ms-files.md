---
title: Playing \ .dvr-ms Files
description: Playing \ .dvr-ms Files
ms.assetid: b7edd6ee-33fb-49ac-8935-9d779ae4a386
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Playing \*.dvr-ms Files

The Media Center user interface allows the playback of any recorded TV show. However, it is also possible for DirectShow-based applications to add playback support for unencrypted \*.dvr-ms files.

The ability to access \*.dvr-ms files by using DirectShow depends on the copy protection policy that is set by the content owner and/or broadcaster. Microsoft Windows XP Media Center determines the copy protection policy by reading the broadcaster's copy protection flag. If the content owner and/or broadcaster has set the policy to protect the content, playback will be restricted to the Media Center computer that was used to record the content.

**Playback on a Media Center PC**

To enable playback of \*.dvr-ms files outside of the Media Center user interface using a DirectShow capable player, the [QFE Q329979](http://go.microsoft.com/fwlink/p/?linkid=14431) must be present and can be installed from Windows Update.

The following registry key can be used to determine if the QFE is already installed on the users system:

<dl> HKLM,SOFTWARE\\Microsoft\\WindowsNT\\CurrentVersion\\Hotfix\\Q329979  
Installed=1  
</dl>

**Playback on Microsoft Windows XP Home or Microsoft Windows XP Professional**

To enable playback of unprotected \*.dvr-ms files on Microsoft Windows XP Home or Microsoft Windows XP Professional, the following is required:

-   Microsoft Windows XP Service Pack 1
-   QFE Q810243
-   Microsoft Windows XP compatible DVD decoder

The following registry entry indicates whether Service Pack 1 is installed:

<dl> HKLM,SOFTWARE\\Microsoft\\WindowsNT\\CurrentVersion\\Hotfix\\Q329979  
Installed=1  
</dl>

The following registry entry indicates whether QFE Q810243 is installed:

<dl> HKLM,SOFTWARE\\Microsoft\\WindowsNT\\CurrentVersion\\Hotfix\\Q810243  
Installed=1  
</dl>

## Related topics

<dl> <dt>

[About the dvr-ms File Format](about-the-dvr-ms-file-format.md)
</dt> </dl>

 

 




