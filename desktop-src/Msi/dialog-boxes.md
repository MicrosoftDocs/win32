---
description: Dialog boxes are specified in the Dialog column of the Dialog table. For more information on adding a dialog box or billboard to a user interface, see Using the User Interface.
ms.assetid: 7cecb1c6-3dc3-48a1-94b9-1976c72b7764
title: Dialog Boxes (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Dialog Boxes (Windows Installer)

Dialog boxes are specified in the Dialog column of the [Dialog table](dialog-table.md). For more information on adding a dialog box or billboard to a user interface, see [Using the User Interface](using-the-user-interface.md).

## Reserved Dialog Box Names

The following dialog box names are reserved by Windows Installer and should not be used for any user-authored custom dialog boxes. The installer requires that these dialog boxes be listed in the [Dialog table](dialog-table.md) using the following reserved names. Each dialog box and name can only be listed once. Developers must author these dialog boxes into the user interface. For information about how to preview dialog boxes, see [Importing the User Interface](importing-the-user-interface.md).



| Dialog box name                                      | Brief description of dialog box                                                                                                                                         |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FilesInUse Dialog](filesinuse-dialog.md)           | Alerts user to processes overwriting or deleting files.                                                                                                                 |
| [FirstRun Dialog](firstrun-dialog.md)               | Collects user name, company name, and product ID.                                                                                                                       |
| [MsiRMFilesInUse Dialog](msirmfilesinuse-dialog.md) | Alerts the user to processes overwriting or deleting files and gives the user the option to use the [Restart Manager](/windows/desktop/RstMgr/restart-manager-portal) to close and restart applications. |



 

## Required Dialog Boxes

During the installation, certain events cause Windows Installer to check the [user interface sequence tables](using-a-sequence-table.md) in the package and display the specified dialog box. For example, in the case of a fatal error, Windows Installer displays the dialog box that is listed with a sequence number of -3 in the user interface sequence table regardless of what that dialog box is named in the [Dialog table](dialog-table.md). The following table lists the specific events and their corresponding sequence number in the user interface sequence table:



| Type of Event                        | User interface sequence table sequence number | Description of dialog box                              |
|--------------------------------------|-----------------------------------------------|--------------------------------------------------------|
| [Fatal error](fatalerror-dialog.md) | -3                                            | The installation was terminated by a fatal error.      |
| [User exit](userexit-dialog.md)     | -2                                            | The installation was terminated at the user's request. |
| [Exit](exit-dialog.md)              | -1                                            | The installation completed successfully.               |



 

In addition, the package author must create a generic dialog box to display Windows Installer [error](error-dialog.md) messages. This dialog box can be named anything, but this name must be specified in the **ErrorDialog** property.

## Typical Dialog Boxes

The following dialog boxes are optional and are commonly included in the authored user interface of an installation package. These dialogs are typical of most [user interface wizards](user-interface-wizard-behavior.md) for installing files. These dialog boxes can have any name in the Dialog table. The names shown are only recommended for clarity and can be modified as necessary. For example, two different custom **LicenseAgreement** dialog boxes can be used in the package and distinguished in the Dialog table by the names ProfessionalLicenseAgreement and LimitedLicenseAgreement.



| Dialog box type                                             | Brief description of dialog box                         |
|-------------------------------------------------------------|---------------------------------------------------------|
| [DiskCost dialog box](diskcost-dialog.md)                  | Indicates insufficient disk space for the installation. |
| [Browse dialog box](browse-dialog.md)                      | Enables user to select a directory.                     |
| [Cancel dialog box](cancel-dialog.md)                      | Confirms a request to terminate the installation.       |
| [License agreement dialog box](licenseagreement-dialog.md) | Modal box displaying the license agreement.             |
| [Selection dialog box](selection-dialog.md)                | Modal box enabling the user to select items.            |



 

 

 
