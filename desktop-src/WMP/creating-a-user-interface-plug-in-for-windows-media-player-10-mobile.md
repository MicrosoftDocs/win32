---
title: Creating a User Interface Plug-in for Windows Media Player 10 Mobile
description: Creating a User Interface Plug-in for Windows Media Player 10 Mobile
ms.assetid: 050418b7-d99c-49ab-8ce6-6511b194ffe6
keywords:
- Windows Media Player Mobile,plug-ins
- Windows Media Player Mobile,user interface plug-ins
- Windows Media Player Mobile plug-ins
- plug-ins,user interface
- plug-ins,Windows Media Player Mobile
- user interface plug-ins,Windows Media Player Mobile
- UI plug-ins,Windows Media Player Mobile
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating a User Interface Plug-in for Windows Media Player 10 Mobile

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 10 Mobile uses the same UI plug-in model as the desktop Windows Media Player. However, Windows Media Player 10 Mobile can only interact with background UI plug-ins. Because of the similar plug-in models, the same API calls that apply to background UI plug-ins on the desktop also apply to background UI plug-ins on a Windows Mobile device.

The following sections describe how to create a background UI plug-in by using wizard-generated code from the Windows Media Player Plug-in Wizard.



| Section                                                                | Description                                                                                                                                            |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Getting Started](getting-started.md)                                 | Describes what you need to install and how to use the Windows Media Player Plug-in Wizard to help automate the creation of a background UI plug-in.    |
| [Modifying Wizard-generated Code](modifying-wizard-generated-code.md) | Describes what you need to modify from the wizard-generated code created in the previous section so that it works with Windows Media Player 10 Mobile. |



 

## Related topics

<dl> <dt>

[**User Interface Plug-ins Programming Guide**](user-interface-plug-ins-programming-guide.md)
</dt> </dl>

 

 




