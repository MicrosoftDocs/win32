---
title: Windows components installed on demand
description: Windows components installed on demand
ms.assetid: 14865DD7-167C-462C-B85A-BD07C929D7B8
ms.topic: article
ms.date: 05/31/2018
---

# Windows components installed on demand

## Platform

**Clients -** Windows 8.1  







## Description

Two Windows components will be installed on demand in Windows 8.1: DirectPlay and NTVDM. These components are listed within Optional Components under the “Legacy Components” node. These components are installed locally as part of the operating system, and compressed as optional components. When an app references or calls one of these components (usually at first launch of the app), installation is triggered automatically. Users will be notified that the component will be installed, and they must confirm the action in order to proceed. Elevation is required for this to succeed if the user is not an administrator. After the initial installation, the user does not need to perform any other actions to use the component again.

## Manifestation

When an app references or calls a legacy component in optional components (at first launch), the app will be suspended and the Feature on Demand dialog will open, requesting user permission to install the component. If users click OK, they may also see an elevation prompt where they must enter their credentials. The component will then be installed and the app will resume.

## Mitigation

To keep the Features on Demand UI from opening, you can pre-install DirectPlay and NTVDM using DISM or the Optional Components UI.

## Solution

You are strongly encouraged to avoid referencing or calling components that have been listed as Legacy Optional Components in Windows in future versions of your app. Legacy Optional Components will only include older, lesser-used components that could potentially cause performance and security issues for users.

## Tests

No additional test accommodations are necessary for compatibility. It is important to be aware that this dialog will appear when the optional component is called or referenced, and this installation requires elevation.

 

 




