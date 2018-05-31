---
title: Tuning with the Video Control
description: Tuning with the Video Control
ms.assetid: e0f8845c-d651-4e33-9a60-b96a3c55a243
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Tuning with the Video Control

This topic applies to Windows XP or later.

The Video Control is designed to shield applications from the complexities of TV tuning and filter-graph building on the PC. To perform tuning, the application obtains a *tune request*, which is an object that contains information about the network type, the channel, and so forth. The application passes the tune request to the Video Control's **View** command.

An application can retrieve a tune request from a database or other storage mechanism or it can create a tune request programmatically. The details of creating the request will depend on the network type, such as analog, ATSC, or DVB. This approach sacrifices *network* independence, but retains *device* independence. In other words, if the application creates an ATSC tune request, it will not function with a DVB network, but it work with different BDA-compliant tuner cards. For more information, see [The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md).

Once the Video Control receives the tune request, it searches the local system for an appropriate input device. When the application calls **Build** or **Run**, the Video Control builds and configures the filter graph based on the selected input device. When the application calls **Run**, the Video Control renders the television.

## Related topics

<dl> <dt>

[Using the Video Control](using-the-video-control.md)
</dt> </dl>

 

 




