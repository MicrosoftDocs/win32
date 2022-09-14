---
description: The following list contains the TAPI MSP supported features.
ms.assetid: e36bba94-1fa7-4514-9f8a-bcd690b04d73
title: Features Supported
ms.topic: article
ms.date: 05/31/2018
---

# Features Supported

The following list contains the TAPI MSP supported features.

-   Implements an MSP that handles a single address per instance of the MSP. Multiple like addresses are handled by instantiating the MSP multiple times. This greatly simplifies the implementation of the MSP and the base classes.
-   Implements all the MSPI interfaces, including [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress), [**ITTerminalSupport**](/windows/win32/api/tapi3if/nn-tapi3if-itterminalsupport), [**ITStreamControl**](/windows/win32/api/tapi3if/nn-tapi3if-itstreamcontrol), and [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream).
-   Implements ready-to-use static terminals for both audio and video.
-   Implements generic terminal base classes. These terminal base classes are used by both the above-mentioned static terminal implementations and the implementations of dynamic terminals that are found in Termmgr.dll. The MSP can also use them to implement additional terminals.
-   Uses the Terminal Manager to handle dynamic terminals. Creates dynamic terminals on a worker thread with a message pump (to free console applications from having to process window messages for video render terminals and to simplify synchronization issues).
-   Supports calls that use a filter graph per stream.
-   Implements handling of graph events.
-   Uses the thread pooling APIs, in conjunction with a worker thread of its own, to handle events.
-   Uses the tracing APIs of Windows 2000 (originally developed for the Routing project) along with additional logic to provide a flexible, generic logging mechanism that can simultaneously log to any combination of the following: a user or kernel-mode debugger; a separate console window with log messages separated by component; a log file.
-   Runs free-threaded.

 

 
