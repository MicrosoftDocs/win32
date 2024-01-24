---
description: Windows Installer implements a number of standard controls that package authors can place onto dialog boxes. However, not all standard Microsoft Windows controls are available, and custom controls cannot be created for use with the installer UI.
ms.assetid: 28416905-ce9a-4bb7-97b7-646c01f370ab
title: Controls Overview
ms.topic: article
ms.date: 05/31/2018
---

# Controls Overview

Windows Installer implements a number of standard controls that package authors can place onto dialog boxes. However, not all standard Microsoft Windows controls are available, and custom controls cannot be created for use with the installer UI.

Controls are created on dialog boxes in the installer in a manner similar to how dialog boxes are created programmatically using the Microsoft Windows user interface API. A control is created from a template recorded in the Control table. This template is slightly different in that it contains the unique name of the dialog box on which the control appears.

In the Microsoft Windows user interface API, user interaction is accomplished by creating a callback function to handle messages posted by the control. Also, most Microsoft Windows controls receive messages, such as those sent by the [SendMessage](/windows/win32/api/winuser/nf-winuser-sendmessage) function.

Communication between the user and controls is accomplished in the installer through the use of [ControlEvents](controlevent-overview.md). However, there is a limited set of ControlEvents that are specific to each control in the limited set of controls in Windows Installer. Controls may post more than one ControlEvent and may receive more than one ControlEvent.

Controls can publish specific ControlEvents through the use of the ControlEvent table. Controls can receive ControlEvents through the use of the [EventMapping table](eventmapping-table.md).

Windows Installer publishes ControlEvents during the execution of some actions as well, and controls subscribed to these ControlEvents in the EventMapping table receive them.

 

 
