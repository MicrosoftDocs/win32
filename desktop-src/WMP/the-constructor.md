---
title: The Constructor
description: The Constructor
ms.assetid: 227aac8a-8bd1-4f94-9c2a-5371f87afbb7
keywords:
- Windows Media Player plug-ins,constructor
- plug-ins,constructor
- user interface plug-ins,constructor
- UI plug-ins,constructor
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The Constructor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The constructor that the wizard provides stores a pointer to the main plug-in class in a member variable. The wizard uses this reference to gain access to member variables declared in the CSearch class. No implementation change is needed.

## Related topics

<dl> <dt>

[**Implementing CPluginWindow**](implementing-cpluginwindow.md)
</dt> </dl>

 

 




