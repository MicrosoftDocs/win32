---
title: Direct2D Debug Layer
description: A runtime extension for Direct2D which offers descriptive error messages, object leak detection, performance notices, and other cues to help you create Direct2D apps.
ms.assetid: 23b522d4-0733-4892-b93d-28f899fa0f17
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D Debug Layer

## Purpose

The Direct2D debug layer, implemented separately from Direct2D in its own DLL named d2d1debug.dll, provides design-time debug messages for you to minimize runtime application failure. The debug messages often result from violations of API contracts such as invalid parameters (could be Direct3D-related), invalid resources, threading violations, and other performance issues such as using a layer when a clip would suffice.

To help you decide how much information is traced by the debug layer, the debug layer offers three debug levels: information, warning, and error. These three levels are interpreted as follows:

-   **Error:** Direct2D sends severe error messages to the debug layer. For example, breaking a threading constraint will generate a severe error.

    Further, a message of level error triggers the breakpoint to help you debug.

-   **Warning:** Direct2D sends error messages and warnings to the debug layer so that you can address any of these messages.

-   **Information:** Direct2D sends error messages, warnings, and additional diagnostic information to the debug layer. For example, performance improvement messages will be sent at this debug level.

## In this section



| Topic                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [Installing the Direct2D Debug Layer](installing-the-direct2d-debug-layer.md)<br/> | Describes how to install the Direct2D debug layer.<br/>      |
| [Direct2D Debug Layer Overview](direct2ddebuglayer-overview.md)<br/>               |                                                                    |
| [Debug Messages](direct2ddebuglayer-debugmessages.md)<br/>                         | Lists the debug messages from the Direct2D Debug Layer.<br/> |



 

 

 





