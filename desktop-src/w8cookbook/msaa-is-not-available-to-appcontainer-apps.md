---
title: MSAA is not available to Windows Store apps
description: MSAA is not available to Windows Store apps
ms.assetid: C3C12BC7-7A0B-4859-93D0-AA78BC06E90B
ms.topic: article
ms.date: 05/31/2018
---

# MSAA is not available to Windows Store apps

## Platform

**Clients** – Windows 8 


## Description

Windows 8 does not support MSAA (Microsoft Active Accessibility) for reading or automating accessible data from Windows Store apps. The UI Automation (UIA) API, available since Windows 7, should be used instead. Since there are no existing Windows Store app features, there are no existing implementations that are affected by this change. This affects only new apps and features written for Windows 8. Developers can still use MSAA to expose their accessibility data. If MSAA data is provided by Windows Store app provider, UIA clients will still be able to read and automate the data.

To simplify the API for Windows 8Windows Store apps, we decided to support only UI Automation as a client for these apps. UIA clients can read UIA providers natively, with no translation. UIA clients can read MSAA providers as translated through the UIA-to-MSAA Proxy. This will reduce the testing burden for Windows Store app developers.

Eliminating support for MSAA providers would further reduce the testing matrix, but there are major apps that are still MSAA-based and we do not want to render them inaccessible.

## Manifestation

Windows Store app developers will not be able to access the details of MSAA within the app model.

## Solution

No new automated cases should be authored in MSAA for features of Windows Store apps.

Switch any existing in-box tools that use MSAA to UIA if they need to interact with Windows Store apps. Windows Store app developers should use the UI Automation API.

## Resources

-   [UI Automation Fundamentals](../winauto/entry-uiauto-win32.md)

 

 