---
description: You may occasionally need to determine whether your application is running on a Tablet PC because you may want your applications to take advantage of inherent ink, recognition, and pen capabilities.
ms.assetid: 86a3eddb-6541-4b73-b2ca-6adedad1a1e5
title: Determining Whether a PC is a Tablet PC
ms.topic: article
ms.date: 05/31/2018
---

# Determining Whether a PC is a Tablet PC

You may occasionally need to determine whether your application is running on a Tablet PC because you may want your applications to take advantage of inherent ink, recognition, and pen capabilities. To help you determine whether your application has access to the Tablet PC features, you can use the GetSystemMetrics() Windows API call as described in this topic.

## Client-Side Applications

You can use the following techniques to determine whether your code is running on a Tablet PC.

-   [Using GetSystemMetrics (SM\_TABLETPC)](/windows)
-   [Using the Presence of Tablet Platform Binaries](#using-the-presence-of-tablet-platform-binaries)
-   [Web-Based Applications](#web-based-applications)

### Using GetSystemMetrics (SM\_TABLETPC)

### Windows XP Tablet PC Edition

In Microsoft Windows XP Tablet PC Edition, use the GetSystemMetrics(SM\_TABLETPC) function to determine whether a computer is a Tablet PC. GetSystemMetrics(SM\_TABLETPC) is designed to return TRUE on a computer running Windows XP Tablet PC Edition.

### Windows Vista

In Windows Vista, there is no longer a distinct Tablet PC SDK. The Windows SDK now contains a section called "Tablet PC and Touch Technology" and the logic of GetSystemMetrics(SM\_TABLETPC) has been changed to reflect this. GetSystemMetrics(SM\_TABLETPC) now returns true if all of the following are true:

-   There is an integrated digitizer, either pen or touch, on the system.
-   The Tablet PC optional component is installed. This component contains features such as Tablet PC Input Panel and Windows Journal.
-   The computer is licensed to use the optional component. Premium versions of Windows Vista—such as Windows Vista Home Premium, Windows Vista Small Business, Windows Vista Professional, Windows Vista Enterprise, and Windows Vista Ultimate—are licensed to use the optional component.
-   Tablet PC Input Service is running. Tablet PC Input Service is a new service for Windows Vista that controls Tablet PC input.

With this increased accuracy, GetSystemMetrics(SM\_TABLETPC) continues to be the recommended way to determine whether a computer running Windows Vista is a Tablet PC.

### Using the Presence of Tablet Platform Binaries

In both Windows XP Tablet PC Edition and Windows Vista, you can search for the presence of the ink binaries—such as inkobj.dll and Microsoft.Ink.dll—and use their supported functionality if they are present.

In Windows Vista, the Tablet PC Platform binaries are installed on all client versions by default. Input and inking functionality are available on those versions. Recognition is available only in premium versions of Windows Vista.

### Web-Based Applications

In Windows Vista, the user-agent string reported by Internet Explorer includes "Tablet PC 2.0" if, according to GetSystemMetrics(SM\_TABLETPC), the device is a Tablet PC.

In Windows XP Tablet PC Edition 2005, the user-agent string includes Tablet PC 1.7. The user-agent string looks something like the following:

`Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705; Tablet PC 2.0)`

Use this value to determine whether the client computer is a Tablet PC and supports Web-based inking controls.

## Related topics

<dl> <dt>

[**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics)
</dt> </dl>

 

 
