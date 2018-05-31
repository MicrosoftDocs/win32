---
Description: This guide describes how you can extend the fax service administration Microsoft Management Console (MMC) snap-in component.
ms.assetid: de36ca81-1b1f-49b7-b855-a27f29532ba1
title: MMC Snap-in Extensibility Guide
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC Snap-in Extensibility Guide

This guide describes how you can extend the fax service administration Microsoft Management Console (MMC) snap-in component.

You should be familiar with MMC programming concepts and with writing MMC snap-in extensions before you read this document. You should also understand the concepts of the [IDataObject](http://msdn.microsoft.com/en-us/library/ms688421.aspx) mechanism that MMC uses to pass context information between extensions. The IDataObject interface contains methods that enable data transfer.

For more information, see [Extending the Fax Service MMC Snap-in](-mfax-extending-the-fax-service-mmc-snap-in.md) and the [node types](-mfax-mmc-snap-in-node-types.md) reference. Constants that apply to extension of MMC components are declared in the FaxMmc.h header file in versions of Windows later than Windows 2000.

 

 



