---
description: Windows Installer contains functionality that enables installation package developers to author a graphical user interface (GUI) that is displayed to the end-user during installation.
ms.assetid: 58ef0043-fb30-4f64-9291-e703d7a28bb5
title: About the User Interface
ms.topic: article
ms.date: 05/31/2018
---

# About the User Interface

Windows Installer contains functionality that enables installation package developers to author a graphical user interface (GUI) that is displayed to the end-user during installation. This user interface can exhibit [user interface wizard behavior](user-interface-wizard-behavior.md), display dialog boxes and billboards, and present interactive controls to users during the installation.

The installer internal UI is managed and controlled through a set of database tables within Windows Installer itself. The installer provides only a small set of default dialog boxes that are intended to handle error and information messages. All custom dialog boxes must be created by the package author.

There is no specific Windows Installer API to allow a package author to create a UI programmatically. It is possible to use the Microsoft Windows API to create a UI programmatically; however, it is recommended that package authors use the internal UI provided.

Installer package authors create custom dialog boxes by entering the name of their custom dialog into the "\_Dialog" column of the dialog table and specifying the size, position, and other attributes using the remaining columns.

Windows Installer also implements a number of standard controls that a package author can place onto dialog boxes. Not all standard Microsoft Windows controls are available, and custom controls cannot be created for use with the installer UI.

Controls are created on a specific dialog box by entering the name of the dialog box, the primary key to the dialog box's entry in the dialog table, into the second field of the control table and specifying the control's size, position, and other attributes using the remaining columns.

Active controls must be linked to a ControlEvent in the [ControlEvent table](controlevent-table.md) to allow user interaction with the installation. Passive controls that receive and display information must be subscribed to an appropriate ControlEvent in the [EventMapping table](eventmapping-table.md).

For more information about ControlEvents, see [ControlEvent Overview](controlevent-overview.md). Note that a control publishes a ControlEvent if listed in the ControlEvent table and subscribes to an event if listed in the EventMapping table.

The installer UI display during installation is managed through the UI sequence tables: [InstallUISequence Table](installuisequence-table.md), and [AdminUISequence Table](adminuisequence-table.md). One of these sequence tables is executed depending on the top-level action that initiated the installation: [INSTALL](install-action.md), [ADMIN](admin-action.md), or [ADVERTISE](advertise-action.md).

For more information about implementing a UI in Windows Installer, please see [Using the User Interface](using-the-user-interface.md), [User Interface Schema](user-interface-schema.md), as well as the individual topics for dialog boxes and controls.

 

 



