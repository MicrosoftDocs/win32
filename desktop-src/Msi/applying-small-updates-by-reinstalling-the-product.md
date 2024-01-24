---
description: A small update can be applied to an application by completely or partially reinstalling the application from the command line or from a program.
ms.assetid: 6f8b68da-7748-436d-bc95-96e39cf42143
title: Applying Small Updates by Reinstalling the Product
ms.topic: article
ms.date: 05/31/2018
---

# Applying Small Updates by Reinstalling the Product

A small update can be applied to an application by completely or partially reinstalling the application from the command line or from a program.

**To propagate the small update to current users (this is a complete reinstall) from the command line**

1.  From the command line use either: **msiexec /fvomus \[***path to updated .msi file***\]** or **msiexec /I \[***path to updated .msi file***\] REINSTALL=ALL REINSTALLMODE=vomus**.
2.  The updated .msi file is cached on the user's computer. Note that it is not possible for the user to reinstall the product using Add/Remove Programs because the updated .msi file is not yet on the user's computer.

**To propagate a small update to current users (this is a complete reinstall) from a program**

1.  From a program, call [**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta) and specify REINSTALLMODE\_PACKAGE, REINSTALLMODE\_FILEOLDERVERSION, REINSTALLMODE\_MACHINEDATA, REINSTALLMODE\_USERDATA, and REINSTALLMODE\_SHORTCUT
2.  The updated .msi file is cached on the user's computer.

The following method launches a reinstallation of only those features or components that are affected by the small update.

**To propagate a small update to current users (this is a partial reinstall)**

1.  Obtain a list of the names of features and components that are affected by the small update.
2.  From the command prompt use: **msiexec /I \[***path to updated .msi file***\] REINSTALL=\[***Feature list\]* **REINSTALLMODE=vomus**.
3.  The updated .msi file is cached on the user's computer.

 

 



