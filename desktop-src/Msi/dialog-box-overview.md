---
description: The process of creating a dialog box in Windows Installer is similar to the process of creating a dialog box programmatically using a Microsoft Windows API dialog box template.
ms.assetid: c46f6b7b-e78c-4dd8-a4ff-7da5465391f9
title: Dialog Box Overview
ms.topic: article
ms.date: 05/31/2018
---

# Dialog Box Overview

The process of creating a dialog box in Windows Installer is similar to the process of creating a dialog box programmatically using a Microsoft Windows API dialog box template. While a Windows dialog box template is stored in a null terminated–character string, Windows Installer stores the dialog box parameters in the Dialog table. The Dialog table contains an attributes column that is analogous to Window styles in the Microsoft Windows user interface API. However, the number of dialog style bits in Windows Installer is a reduced and specialized set.

To physically create the dialog box using the Windows user interface API, [**DialogBox**](/windows/win32/api/winuser/nf-winuser-dialogboxa) is called and passes a pointer to the template. In Windows Installer, the dialog box is created during execution of one of the three UI sequence tables.

Windows Installer does not contain a default UI that package authors can utilize for their packages. It does contain a limited set of default dialog boxes that display error and information messages, but these are displayed only if Windows Installer queries the Dialog and UI Sequence tables and finds there are no custom dialog boxes available.

The installer SDK includes a minimal database named Uisample.msi that contains populated UI and execution sequence tables and a complete UI. This database is easily customized and merged on to any package.

Some standard actions and internal Windows Installer error conditions return a specific set of UI data and therefore require a dialog box with a specific set of controls to accommodate that data. Windows Installer checks two separate locations for the identifiers for these dialog boxes.

-   Windows Installer contains a set of embedded dialog box names. The custom action queries the Dialog table for these reserved names.
-   In each of the three UI sequence tables, dialog names with a sequence number of -1,-2, or -3 are displayed in response to exit, user requested exit, and fatal error messages from Windows Installer.

A complete list of reserved primary key dialog box names is available in [dialog boxes](dialog-boxes.md). Note that the primary key dialog box name is only reserved by the installer and there is no specific implementation of the dialog box within Windows Installer. Package authors must still populate all the fields in the database that specify the attributes and controls of these reserved dialog boxes.

 

 
