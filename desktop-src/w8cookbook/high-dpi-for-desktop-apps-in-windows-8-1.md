---
title: High DPI for desktop apps in Windows 8.1
description: High DPI for desktop apps in Windows 8.1
ms.assetid: 1E92D3C8-C117-463A-AF31-12D3CAA31E2A
ms.topic: article
ms.date: 05/31/2018
---

# High DPI for desktop apps in Windows 8.1

## Platforms

<dl> Clients - Windows 8.1  
Servers - Windows Server 2012 R2  
</dl>

## Description

In Windows 8.1 desktop applications are expected to run on displays with 200% scaling in addition to the 100%, 125%, and 150% scaling that is supported in Windows 8. In addition, desktop applications are scaled on a per-monitor basis rather than to a single scale factor applied to all displays. Developers can also call new APIs in Windows 8.1 to get per-monitor scale factors.

## Manifestations

Users can use new high density displays with Windows 8.1 for a terrific visual experience that takes advantage of the higher pixel data. If applications don’t handle high DPI, Windows will scale them for the user. In addition, users can use a mix of high and low density displays on the same computer, and Windows will scale content appropriately for each display. This is an improvement over Windows 8, where content can be too large on some displays.

## Mitigation

Since Windows will scale apps that don’t scale themselves, developers generally do not have to do additional work, but developers who do invest in writing applications that support high DPI will have a competitive advantage, as those applications will look better on new high DPI laptops and desktop monitors.

## Solution

Making an application that can take advantage of high DPI is a complex design and implementation task. See the links below for tutorial information, BUILD presentation content, and similar support.

## Tests

Even if developers do not choose to make their applications take advantage of high DPI, they should test their application at 100%, 125%, 150%, and 200% scaling to be sure the end-user experience is satisfactory and competitive.

## Resources

-   [White paper and tutorial on high DPI in Windows 8.1](../hidpi/high-dpi-desktop-application-development-on-windows.md)
-   [Windows desktop sample programs](https://www.microsoft.com/?ref=go)
-   [BUILD 2013 break-out session on high DPI in Windows 8.1](https://channel9.msdn.com/Events/Build/2013/4-184)

 

 