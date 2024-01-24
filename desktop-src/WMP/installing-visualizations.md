---
title: Installing Visualizations
description: Installing Visualizations
ms.assetid: ca391e38-def5-47da-81f7-94aa96530387
keywords:
- Windows Media Player plug-ins,visualizations
- plug-ins,visualizations
- visualizations,installing
- custom visualizations,installing
- installing visualizations
- visualizations,registering
- custom visualizations,registering
- registry,visualizations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Installing Visualizations

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must provide an installation process for the user of your visualization. You must also provide an uninstall process for the user. The current version of Windows Media Player does not install visualizations from the user interface.

## Installing to the Visualization Folder

It is recommended that you install all visualizations in the Visualizations subfolder of the folder where Windows Media Player is installed.

## Registering Your Visualization

Visualizations are COM DLLs and follow all the normal rules of installation and removal. You can use regsvr32.exe or other installation tools to register your visualization.

## Related topics

<dl> <dt>

[**About Custom Visualizations**](about-custom-visualizations.md)
</dt> </dl>

 

 




