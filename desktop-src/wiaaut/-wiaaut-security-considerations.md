---
title: Security Considerations Windows Image Acquisition Automation Layer
description: This document provides information about security considerations related to the Windows Image Acquisition (WIA) Automation Layer.
ms.assetid: '2d327c79-df8d-4ceb-bbd0-e75dc72d04e1'
keywords: ["Windows Image Acquisition (WIA),security", "WIA (Windows Image Acquisition),security", "Windows Image Acquisition Automation Layer,security", "WIA Automation Layer,security", "Image Acquisition Automation Layer,security"]
---

# Security Considerations: Windows Image Acquisition Automation Layer

This document provides information about security considerations related to the Windows Image Acquisition (WIA) Automation Layer. This document does not provide all you need to know about security issues; instead, use it as a starting point and reference for this technology area.

-   [Controls Are Not Safe for Scripting](#controls-are-not-safe-for-scripting)
-   [Configure Security Settings for ASP Access](#configure-security-settings-for-asp-access)
-   [Administrator Permission](#administrator-permission)
-   [Place Registered Applications in Secure Locations](#place-registered-applications-in-secure-locations)
-   [Do Not Use Underlying Directories or Registry Keys](#do-not-use-underlying-directories-or-registry-keys)
-   [Related Topics](#related-topics)

## Controls Are Not Safe for Scripting

The WIA Automation Layer is not marked safe for scripting. Therefore, proper functionality depends on your security settings.

## Configure Security Settings for ASP Access

Before you can create a [**DeviceManager**](-wiaaut-devicemanager.md) object on an .asp page, you must configure the security settings for the WIA Automation Layer. For more information, see [How to Configure Security Settings](-wiaaut-configure-security.md).

## Administrator Permission

To function successfully, the [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md) and [**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md) methods require Administrator permission. For an example that uses these methods, see [Implement a Windows Script Host Script that Runs Automatically](-wiaaut-shared-samples.md#implement-a-windows-script-host-script-that-runs-automatically) in Shared Samples.

## Place Registered Applications in Secure Locations

When an application is registered to receive a device event, that application can be run by any user with access to that device. For example, if an application is registered for a scan event, pressing the scan button on a scanner causes that application to run. If the application runs with a higher privilege than the user has, there is a potential security issue.

## Do Not Use Underlying Directories or Registry Keys

Windows Image Acquisition (WIA) uses several directories and registry keys internally to store data or information. Do not access these directories or registry keys directly. Instead, use the exposed methods to specify directories for acquired images.

## Related Topics

-   [Getting Started with Samples](-wiaaut-getting-started-samples.md)
-   [Microsoft Security](http://www.microsoft.com/security/)
-   [MSDN Library Security Home Page](http://msdn.microsoft.com/security/)
-   [Security How-To Resources](http://www.microsoft.com/technet/solutionaccelerators/howto/sechow.mspx)
-   [TechNet Security Resources](http://technet.microsoft.com/security/default.aspx)
-   [Security Considerations for Windows XP Embedded Developers](http://msdn.microsoft.com/library/ms838345.aspx)
-   [Best Practices for the Security APIs](http://msdn.microsoft.com/library/ms717796(VS.85).aspx)

 

 




