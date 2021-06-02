---
description: This section is concerned primarily with how developers of installation packages author an installation user interface (UI) using the installer's database and internal UI.
ms.assetid: c04e32ba-08a9-49fe-9a4a-db258767f0b3
title: Using the User Interface
ms.topic: article
ms.date: 05/31/2018
---

# Using the User Interface

This section is concerned primarily with how developers of installation packages author an installation user interface (UI) using the installer's database and internal UI. For more information about the difference between an internal and external UI see [About the User Interface](about-the-user-interface.md).

To display a dialog box sequence or billboard during the installation, the name of the dialog box must be entered into the Action column of the appropriate action sequence table. The name of the dialog box must appear in the [InstallUISequence](installuisequence-table.md) or [AdminUISequence table](adminuisequence-table.md) depending on whether the UI is scheduled to run under the [INSTALL](install-action.md), [ADVERTISE](advertise-action.md), or [ADMIN action](admin-action.md).

Although the installer supports the authoring of custom dialog boxes and billboards, there are also a number of reserved names for certain dialog box sequences. Because the installer uses these names when executing certain actions, these names must only be used with the types of dialog boxes for which they are reserved. A list of these reserved names, and a description of each of the special dialog box sequences, is given in [Dialog Boxes](dialog-boxes.md).

The properties of each dialog box or billboard in the UI must be specified in the [Dialog](dialog-table.md) and [BillBoard](billboard-table.md) tables, respectively. The style of each dialog box must also be specified in the Dialog table by setting the [dialog's style bit](dialog-style-bits.md) flag.

Controls and text must be added to the dialog box, and these must be tied to [ControlEvents](controlevent-overview.md), to enable the user to interact with the installation process. See [Adding Controls and Text](adding-controls-and-text.md) for more information on how to add controls to a dialog box.

Windows Installer internal UI handler can selectively show or hide dialog boxes to control the level of end-user interactivity during the installation. These levels of end-user interactivity are referred to as full, reduced, basic, and none. See [User Interface Levels](user-interface-levels.md). for a full description of these UIlevels.

There are two methods to set the UI level. The UI level can be set programmatically with a call to [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui), and the first parameter of **MsiSetInternalUI** specifies the UI level. Package developers can also set the UI level using the [command line option](command-line-options.md) "/q".

The behavior of each of the UI levels is determined by the authoring of the .msi file by the package developer. The author of an internal UI has flexibility in how these levels behave for a package. The availability of these levels depends on the authoring of the installation package. The author must specify every dialog box and control in the user interface in the Dialog and Control tables.

-   A full UI typically exhibits [user interface wizard behavior](user-interface-wizard-behavior.md), such as each dialog box in a sequence containing a **Next>>** button. This form of UI is familiar to many users and is the most common type of UI for an author to create. The installer presents a logical sequence of dialog boxes and prompts the user to interact with controls located in each dialog box.
-   A reduced UI typically suppresses the display of wizard behavior.
-   A basic UI typically only displays progress messages to the user.
-   A UI level of None means a silent installation.

Windows Installer provides a unique progress bar indicator in the [ProgressBar control](progressbar-control.md) that displays to the user an estimate of the total time remaining until the installation is complete. For more information about the progress bar, see [Authoring a ProgressBar Control](authoring-a-progressbar-control.md).

UI authors should facilitate the accessibility of their application or product for all users. To learn more about Active Accessibility and Windows Installer, see [Accessibility](accessibility.md).

For more information about authoring a user interface, see [Adding Controls and Text](adding-controls-and-text.md), [Authoring a ProgressBar Control](authoring-a-progressbar-control.md), [Authoring Disk Prompt Messages](authoring-disk-prompt-messages.md), [Authoring a Conditional "Please Wait . . ." Message Box](authoring-a-conditional-please-wait-------message-box.md), and [Previewing the User Interface](previewing-the-user-interface.md). For more information about author billboards see [Displaying Billboards on a Modeless Dialog](displaying-billboards-on-a-modeless-dialog.md)

Beginning with Windows Installer 4.5 a custom user interface can be embedded within the Windows Installer package. For an example of an embedded custom UI see [Using an Embedded UI](using-an-embedded-ui.md).

 

 



