---
title: Rules for Each Line
description: Rules for Each Line
ms.assetid: 9bc7ed16-6e94-4cda-81da-f71dcb81580d
keywords:
- Windows Media Player Mobile skins,rules for text lines
- skins,rules for text lines
- skin definition files,rules for text lines
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Rules for Each Line

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Each definition in the skin definition file must be on a separate line. You must enter text in lines using the following rules:

-   Each line must end with a paragraph return. Some lines may be longer than the visible line length of your text editor, but do not break the lines. You may want to turn line wrap off to be sure your lines do not break.
-   Use only visible characters as defined in the Skin Reference.
-   A line consists of one or more items, separated by spaces.
-   You can enter as many spaces between items as you want for readability.
-   Do not use any tab characters anywhere in the file.
-   Lines that begin with two consecutive forward slashes (//) are ignored. Use these for comments. Blank lines are also ignored.
-   Include spaces between the brackets and the name of the section.

## Related topics

<dl> <dt>

[**Skin Definition File**](skin-definition-file-mobile.md)
</dt> </dl>

 

 




