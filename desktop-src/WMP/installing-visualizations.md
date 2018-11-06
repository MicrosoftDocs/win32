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
ms.date: 05/31/2018
---

# Installing Visualizations

You must provide an installation process for the user of your visualization. You must also provide an uninstall process for the user. The current version of Windows Media Player does not install visualizations from the user interface.

## Installing to the Visualization Folder

It is recommended that you install all visualizations in the Visualizations subfolder of the folder where Windows Media Player is installed.

## Registering Your Visualization

Visualizations are COM DLLs and follow all the normal rules of installation and removal. You can use regsvr32.exe or other installation tools to register your visualization.

## Related topics

<dl> <dt>

[**About Custom Visualizations**](about-custom-visualizations.md)
</dt> </dl>

 

 




