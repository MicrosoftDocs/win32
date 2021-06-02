---
description: Parental Controls API Overview
ms.assetid: 647e5df8-7c6d-466a-a3d4-eac13efa797d
title: Parental Controls API Overview
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls API Overview

APIs used for Parental Controls expose the policy and in-box restrictions settings, and logging functionality.

## Settings

Two public APIs are provided:

-   A lightweight COM-based minimum compliance API (called the Compliance API) primarily for applications to determine whether logging should be turned on. In addition, simple methods are provided for:
    -   Retrieving the restrictions state for web restrictions, time limits, games restrictions, and application restrictions.
    -   Retrieving the ID of the active Web content filter.
    -   Determining whether vendor user interface elements should be shown, in a manner consistent with the in-box hiding when joined to a domain.
    -   Retrieving the last time a setting has been changed for a user.
    -   Retrieving whether browser-based or browser-like file downloads need to be blocked for a user, and the ability to request a URL to be specifically allowed by the Web Content Filter for that user.
    -   Determining whether a given game is blocked for a user.
-   Windows Management Instrumentation (WMI) API access to a Parental Controls namespace for full write and read access to all exposed settings. Parental Controls deploys a WMI Provider to manage read/write permissions to the underlying settings store with proper enforcement of privileges for administrators and controlled users.

ISVs are requested to use the Compliance API, and the WMI API as necessary, to control restrictions as appropriate for child safety based on the functionality of the application or solution.

## Logging

-   Windows standard event publishing and consuming APIs are used for Parental Controls activity monitoring. The Windows Vista Event Reporting and Tracing system has improved performance over previous Event Tracing for Windows (ETW) functionality. Parental Controls defines a unique channel for its data in ETW.
-   ISVs are requested to use the event publishing API to log user activity as specified in the Using Parental Controls APIs section.

 

 



