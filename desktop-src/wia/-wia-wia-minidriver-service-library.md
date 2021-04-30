---
description: To simplify driver implementation as much as possible, Windows Image Acquisition (WIA) provides a Minidriver Service Library that performs many of the administrative tasks required by the WIA architecture.
ms.assetid: 074a53a3-20b0-4b25-991d-5d48f75c5d75
title: WIA Minidriver Service Library
ms.topic: article
ms.date: 05/31/2018
---

# WIA Minidriver Service Library

To simplify driver implementation as much as possible, Windows Image Acquisition (WIA) provides a Minidriver Service Library that performs many of the administrative tasks required by the WIA architecture. The service library provides helper functions to maintain the device's tree of [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) objects.

The basic service library functions perform helper functions that most device drivers would otherwise need to implement. These functions read and write properties. They also create driver item objects and copy device information properties.

 

 



