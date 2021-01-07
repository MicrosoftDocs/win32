---
description: This document provides information about security considerations related to Windows Image Acquisition (WIA).
ms.assetid: 35455320-7d08-49de-938d-40dc0873917b
title: 'Security Considerations: Windows Image Acquisition'
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations: Windows Image Acquisition

This document provides information about security considerations related to Windows Image Acquisition (WIA). This document doesn't provide all you need to know about security issues - instead, use it as a starting point and reference for this technology area.

-   [Use quotation marks around path names](#use-quotation-marks-around-path-names)
-   [Place registered applications in secure locations](#place-registered-applications-in-secure-locations)
-   [Do not use underlying directories or registry keys](#do-not-use-underlying-directories-or-registry-keys)
-   [Related Topics](#related-topics)

## Use quotation marks around path names

When using [**IWiaDevMgr::RegisterEventCallbackProgram**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-registereventcallbackprogram) to register an application to receive device events, be sure to surround the path and filename of the application with quotation marks. This avoids the possibility that the path is misinterpreted and an unauthorized application is run.

## Place registered applications in secure locations

When an application is registered to receive a device event, that application can be run by any user that has access to that device. For example, if an application is registered for a scan event, pressing the "scan" button on a scanner will cause that application to run. If the application runs with a higher privilege than the user has, this causes a potential security issue.

## Do not use underlying directories or registry keys

WIA uses several directories and registry keys internally to store data or information. Do not access these directories or registry keys directly. Instead, use the exposed interface methods to specify directories for acquired images.

## Related Topics

-   [Microsoft Security](https://www.microsoft.com/security/)
-   [MSDN Library Security Home Page](https://msdn.microsoft.com/security/default.aspx)
-   [Security How-to Resources](https://www.microsoft.com/technet/solutionaccelerators/howto/sechow.mspx)
-   [TechNet Security Resources](https://technet.microsoft.com/security/default.aspx)
-   [Security Considerations for Windows XP Embedded Developers](/previous-versions/ms838345(v=msdn.10))
-   [Security Best Practices](../secbp/best-practices-for-the-security-apis.md)

 

 
