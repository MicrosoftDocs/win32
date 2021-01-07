---
description: If after running an installation, you need to verify that a particular feature, component, or file has been installed, turn on the verbose logging option during the installation. See Windows Installer Logging and Command Line Options.
ms.assetid: c4547e5d-ea71-494f-9d92-c7fef23bcc0f
title: Checking the Installation of Features, Components, Files
ms.topic: article
ms.date: 05/31/2018
---

# Checking the Installation of Features, Components, Files

If after running an installation, you need to verify that a particular feature, component, or file has been installed, turn on the verbose logging option during the installation. See [Windows Installer Logging](windows-installer-logging.md) and [Command Line Options](command-line-options.md).

The verbose log includes an entry for each feature and component the installation package may install. The log tells what the state of that feature or component was prior to the installation, what state was requested by the installation, and in what state the installer left the feature or component. Feature and component entries in the log appear as the following examples.

``` syntax
MSI (s) (40:A4): Feature: QuickTest; Installed: Absent;   Request:
 Local;   Action: Local
MSI (s) (40:A4): Component: QuickTest; Installed: Absent;   Request:
 Local;   Action: Local
```

This verbose log indicates that:

-   the installation state of the QuickTest feature and component was absent before running the package
-   the package requested a local installation of these
-   the feature and component were both left in the locally installed state after running the package.

The label "Installed" in the log refers to the current install state of the feature or component, "Request" refers to the requested install state of the feature or component. "Action" refers to the actual action state of the feature or component.

The following table lists the possible component or feature states that can appear in the log.



| Log Entry              | Description                                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------------------|
| Request: Null          | No request.                                                                                                     |
| Action: Null           | No action taken.                                                                                                |
| Installed: Absent      | Component or feature is not currently installed.                                                                |
| Request: Absent        | Installation requests component or feature be uninstalled.                                                      |
| Action: Absent         | Installer actually uninstalls component or feature.                                                             |
| Installed: Local       | Component or feature is currently installed to run local.                                                       |
| Request: Local         | Installation requests component or feature be installed to run local.                                           |
| Action: Local          | Installer actually installs component or feature to run local.                                                  |
| Installed: Source      | Component or feature is currently installed to run from source.                                                 |
| Requested: Source      | Installation requests that component or feature be installed to run from source.                                |
| Action: Source         | Installer actually installs the component or feature to run from source.                                        |
| Installed: Advertise   | Feature is currently advertised. Components are never advertised.                                               |
| Request: Advertise     | Installation requests feature be installed as an advertised feature.                                            |
| Action: Advertise      | Installer actually installs the feature as an advertised feature.                                               |
| Request: Reinstall     | Installation requests feature be reinstalled. Components do not use reinstall state.                            |
| Action: Reinstall      | Installer actually reinstalls feature.                                                                          |
| Installed: Current     | Feature is currently installed in the default authored install state.                                           |
| Request: Current       | Installation requests feature be installed in the default authored install state.                               |
| Action: Current        | Installer actually installs the feature in the default authored install state.                                  |
| Action: FileAbsent     | Installer actually uninstalls component's files and leaves all other resources of the component installed.      |
| Action: HKCRAbsent     | Installer actually removes component's HKCR information. File and non-HKCR information remain.                  |
| Action: HKCRFileAbsent | Installer actually removes component's HKCR information and files. All other resources of the component remain. |



 

The verbose log has an entry for each file that may be installed by the package. The log tells what was done to the file and provides some explanation. File entries in the log appear as in the following example.

``` syntax
MSI (s) (40:A4): File: C:\Test\TESTDB.EXE;  Won't Overwrite;  Existing
 file is of an equal version
```

This log indicates that the installer will not overwrite the existing Testdb.exe file because the existing file is the same as the version being installed.

> [!Note]  
> If you need to author an installation package that searches for an existing file or directory on the user's computer during an installation, use the method described in [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md).

 

 

 



