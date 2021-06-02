---
description: In addition to information discussed in previous sections, uisample.msi also contains data for a sample user interface.
ms.assetid: 7e4ae4b8-e7b2-49b3-97b7-374b69006a2f
title: Importing the User Interface
ms.topic: article
ms.date: 05/31/2018
---

# Importing the User Interface

In addition to information discussed in previous sections, uisample.msi also contains data for a sample user interface. If you merged uisample.msi into MNP2000.msi in the section [Importing a Blank Database](importing-a-blank-database.md), then this information is present in MNP2000.msi as well. The information for the sample user interface is in the following tables.

-   [ActionText table](actiontext-table.md)
-   [Binary table](binary-table.md)
-   [Control table](control-table.md)
-   [ControlEvent table](controlevent-table.md)
-   [Dialog table](dialog-table.md)
-   [Error table](error-table.md)
-   [EventMapping table](eventmapping-table.md)
-   [RadioButton table](radiobutton-table.md)
-   [TextStyle table](textstyle-table.md)
-   [UIText table](uitext-table.md)

The database editor Orca provided with the installer includes a dialog preview option that you can use to preview the dialogs of the user interface that is specified by the data in the above tables.

The sample installation package MNP2000.msi is now ready for package validation. Always run validation on a new package before attempting to install the package for the first time. This is discussed in Validating the Installation Sample.

If you do not want to include the user interface in the sample package, omit or remove the all information in the tables shown above except for the [TextStyle table](textstyle-table.md) (which is needed to define the [**DefaultUIFont**](defaultuifont.md) property). You should also remove user interface properties from the [Property Table](property-table.md). An example Property table for the Notepad sample, without a UI, is shown below. Do not reuse the GUIDs shown in the table if you copy this example.

[Property Table](property-table.md)



| Property                                   | Value                                  |
|--------------------------------------------|----------------------------------------|
| [**DefaultUIFont**](defaultuifont.md)     | DlgFont8                               |
| [**INSTALLLEVEL**](installlevel.md)       | 3                                      |
| [**LIMITUI**](limitui.md)                 | 1                                      |
| [**Manufacturer**](manufacturer.md)       | Microsoft                              |
| [**ProductCode**](productcode.md)         | {18A9233C-0B34-4127-A966-C257386270BC} |
| [**ProductLanguage**](productlanguage.md) | 1033                                   |
| [**ProductName**](productname.md)         | MNP2000                                |
| [**ProductVersion**](productversion.md)   | 01.40.0000                             |
| [**UpgradeCode**](upgradecode.md)         | {908E378A-9551-4772-BF1D-5CFAF6FD9CB4} |



 

A package without a user interface can be installed from the command line or from a program. To install a package from the command line use the methods described in [Command Line Options](command-line-options.md). To install a package from a program use the methods described in [Using Installer Functions](using-installer-functions.md). Always run validation on a new package before attempting to install a new package for the first time.

[Continue](validating-an-installation-database.md)

 

 



