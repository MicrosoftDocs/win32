---
title: Security Considerations
description: This overview provides information about security considerations related to still images. This document does not provide all you need to know about security issues instead, use it as a starting point and reference for this technology area.
ms.assetid: 5dc0f20e-3f89-4623-8b37-76ea55636845
keywords:
- Still Image (STI),security
- STI (Still Image),security
- Still Image API,security
- still images,security
- security for Still Image (STI)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations

This overview provides information about security considerations related to still images. This document does not provide all you need to know about security issues?instead, use it as a starting point and reference for this technology area.

## Use quotation marks around path names

When using [**IStillImage::RegisterLaunchApplication**](istillimage-registerlaunchapplication.md) to register an application to receive device events, be sure to surround the path and filename of the application with quotation marks. This avoids the possibility that the path is misinterpreted and an unauthorized application is run.

## Place registered applications in secure locations

When an application is registered to receive a device event, that application can be run by any user that has access to that device. For example, if an application is registered for a scan event, pressing the "scan" button on a scanner will cause that application to run. If the application runs with a higher privilege than the user has, this causes a potential security issue.

## Related Topics

-   [Security Developer Center](http://msdn2.microsoft.com/security/default.aspx)
-   [Windows Security](http://msdn2.microsoft.com/security/aa570416.aspx)
-   [Security How Tos Index](http://msdn2.microsoft.com/library/ms978512.aspx)
-   [TechNet Security Center](http://www.microsoft.com/technet/security/default.mspx)

 

 




