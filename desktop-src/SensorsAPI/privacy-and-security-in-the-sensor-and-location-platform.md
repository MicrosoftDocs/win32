---
description: The Windows Sensor and Location platform includes privacy settings to help protect users' personal information.
ms.assetid: 24425ed2-7b94-4b05-b117-9118d2074f49
title: Privacy and Security in the Windows Sensor and Location Platform
ms.topic: article
ms.date: 05/31/2018
---

# Privacy and Security in the Windows Sensor and Location Platform

The Windows Sensor and Location platform includes privacy settings to help protect users' personal information.

The platform helps to ensure that sensor data remains private, when privacy is required, in the following ways:

-   By default, sensors are off. Because the platform design presumes that any sensor can provide personal data, each sensor is disabled until the user provides explicit consent to access the sensor data.
-   Windows provides disclosure messages and Help content for the user. This content helps users understand how sensors can affect the privacy of their personal data and helps users make informed decisions.
-   Providing permission for a sensor requires administrator rights.
-   When it is enabled, a sensor device works for all programs running under a particular user account (or for all user accounts). This includes noninteractive users and services, such as ASPNET or SYSTEM. For example, if you enable a GPS sensor for your user account, only programs running under your user account have access to the GPS. If you enable the GPS for all users, any program running under any user account has access to the GPS.
-   Programs that use sensors can call a method to open a system dialog box that prompts users to enable needed sensor devices. This feature makes it easy for developers and users to make sure that sensors work when programs need them, while maintaining user control of disclosure of sensor data.
-   Sensor drivers use a special object that processes all I/O requests. This object makes sure that only programs that have user permission can access sensor data.

 

 



