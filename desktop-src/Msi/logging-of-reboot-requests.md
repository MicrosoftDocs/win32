---
description: If the InstallValidate action detects the installation of a file in use it displays the FilesInUse Dialog and logs the following information.
ms.assetid: 59237d2c-6dda-4edc-bbaf-39c6b4c221b9
title: Logging of Reboot Requests
ms.topic: article
ms.date: 05/31/2018
---

# Logging of Reboot Requests

If the [InstallValidate action](installvalidate-action.md) detects the installation of a file in use it displays the [FilesInUse Dialog](filesinuse-dialog.md) and logs the following information.

``` syntax
Info 1603. The file E:\testdb\Test\CustAct1.dll is being held in use
by the following process: Name: test, Id: 137, Window Title: 'Test'.
```

If the installer detects that it is about to overwrite a file that is in use, it logs the following information.

``` syntax
Info 1603. The file E:\testdb\Test\CustAct2.dll is being held in use.

Info 1903.Scheduling reboot operation: Deleting file [filename]. Must 
reboot to complete operation.
```

The \[filename\] token may actually contain a path to a file with an .rbf extension. In this case the .rbf file is actually the original file logged by the 1603 message which has been renamed to the .rbf file. The file that's in use is first renamed with an .rbf extension and then deleted.

To obtain more information about why the installer is attempting to overwrite this particular file, you can use the verbose logging option. Use the INSTALLLOGMODE\_VERBOSE value in a call to [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga) or use the verbose output option of the [Command Line Options](command-line-options.md). This logs the following information.

``` syntax
MSI (s) (D0:F0): File: E:\testdb\Test\CustAct2.dll;  Overwrite;  
REINSTALLMODE specifies all files to be overwritten
```

The log will include a message such as "Existing file is a lower version" or "Existing file is corrupt (invalid checksum)"

 

 



