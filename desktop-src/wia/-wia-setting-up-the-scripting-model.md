---
description: To use the Windows Image Acquisition (WIA) scripting model, you must have the file Wiascr.dll installed and registered on the computer.
ms.assetid: 94b08833-9fbd-46cf-b6a3-71713cc6ac30
title: Setting up the Scripting Model Development Environment
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Setting up the Scripting Model Development Environment

To use the Windows Image Acquisition (WIA) scripting model, you must have the file Wiascr.dll installed and registered on the computer.

> [!Note]  
> This scripting system has been replaced with Windows Image Acquisition (WIA) Automation Layer. See [Windows Image Acquisition Automation Layer](/previous-versions/windows/desktop/wiaaut/-wiaaut-startpage).

 

Copy this file from the WIA SDK into the *%windir%*/System32 (for example, c:\\windows\\System32) directory. At the command line, navigate to this directory, and type **regsvr32 Wiascr.dll**.

This enters the necessary information in the system registry.

You are now ready to use the WIA scripting model.

 

 
