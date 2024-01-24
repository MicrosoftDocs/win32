---
description: This example illustrates how to create a simple Windows Installer package that installs an application.
ms.assetid: eee1e3e6-74e9-41d0-b732-1f792a4df423
title: An Installation Example
ms.topic: article
ms.date: 05/31/2018
---

# An Installation Example

This example illustrates how to create a simple Windows Installer package that installs an application. The sample installs Notepad, a text editor included with Windows, and several text files describing events and admissions at the imaginary Red Park Arena.

The sample has the following specifications:

-   The application is provided to users as a self-installing Windows Installer package that installs all the required files, shortcuts, and registry information.
-   The installation package may present a UI wizard to the user during setup to collect user information.
-   During setup, users have the option of selecting individual features to be installed to run-locally, to run-from-source, or to not be installed.
-   One of the features can be presented to users as an install-on-demand feature.
-   The same package uninstalls the application and removes all the application files and registry information from the user's computer.
-   The package is prepared to receive a major upgrade that includes changing its product code.

To reproduce the example, you need a software tool capable of creating and editing a blank Windows Installer database. Several package creation tools are available from independent software vendors. A Windows Installer database editor called Orca is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

To complete the example, follow these steps:

[Planning the Installation](planning-the-installation.md)

[Importing a Blank Database](importing-a-blank-database.md)

[Specifying Directory Structure](specifying-directory-structure.md)

[Specifying Components](specifying-components.md)

[Specifying Files and File Attributes](specifying-files-and-file-attributes.md)

[Specifying Source Media](specifying-source-media.md)

[Specifying Features](specifying-features.md)

[Specifying Feature-Component Relationships](specifying-feature-component-relationships.md)

[Adding Registry Information](adding-registry-information.md)

[Specifying Shortcuts](specifying-shortcuts.md)

[Specifying Properties](specifying-properties.md)

[Importing the InstallExecuteSequence](importing-the-installexecutesequence.md)

[Importing the InstallUISequence](importing-the-installuisequence.md)

[Importing the AdminExecuteSequence](importing-the-adminexecutesequence.md)

[Importing the AdminUISequence](importing-the-adminuisequence.md)

[Importing the AdvtExecuteSequence](importing-the-advtexecutesequence.md)

[Adding Summary Information](adding-summary-information.md)

[Importing the User Interface](importing-the-user-interface.md)

[Validating an Installation Database](validating-an-installation-database.md)

 

 



