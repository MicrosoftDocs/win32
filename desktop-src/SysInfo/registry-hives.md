---
description: A hive is a logical group of keys, subkeys, and values in the registry that has a set of supporting files containing backups of its data.
ms.assetid: fe517d88-7b03-4dc3-b3db-6a92665bca8e
title: Registry Hives
ms.topic: article
ms.date: 05/31/2018
---

# Registry Hives

A *hive* is a logical group of keys, subkeys, and values in the registry that has a set of supporting files loaded into memory when the operating system is started or a user logs in.

Each time a new user logs on to a computer, a new hive is created for that user with a separate file for the user profile. This is called the *user profile hive*. A user's hive contains specific registry information pertaining to the user's application settings, desktop, environment, network connections, and printers. User profile hives are located under the **HKEY\_USERS** key.

Registry files have the following two formats: standard and latest. The standard format is the only format supported by Windows 2000. It is also supported by later versions of Windows for backward compatibility. The latest format is supported starting with Windows XP. On versions of Windows that support the latest format, the following hives still use the standard format: **HKEY\_CURRENT\_USER**, **HKEY\_LOCAL\_MACHINE\\SAM**, **HKEY\_LOCAL\_MACHINE\\Security**, and **HKEY\_USERS\\.DEFAULT**; all other hives use the latest format.

Most of the supporting files for the hives are in the %SystemRoot%\\System32\\Config directory. These files are updated each time a user logs on. The file name extensions of the files in these directories, or in some cases a lack of an extension, indicate the type of data they contain. The following table lists these extensions along with a description of the data in the file.



| Extension       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| none<br/> | A complete copy of the hive data.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .alt<br/> | A backup copy of the critical **HKEY\_LOCAL\_MACHINE\\System** hive. Only the System key has an .alt file.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .log<br/> | A transaction log of changes to the keys and value entries in the hive.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| .sav<br/> | A backup copy of a hive.<br/> **Windows Server 2003 and Windows XP/2000:** Copies of the hive files as they looked at the end of the text-mode stage in Setup. Setup has two stages: text mode and graphics mode. The hive is copied to a .sav file after the text-mode stage of setup to protect it from errors that might occur if the graphics-mode stage of setup fails. If setup fails during the graphics-mode stage, only the graphics-mode stage is repeated when the computer is restarted; the .sav file is used to restore the hive data.<br/> |



 

The following table lists the standard hives and their supporting files.



| Registry hive                      | Supporting files                           |
|------------------------------------|--------------------------------------------|
| **HKEY\_CURRENT\_CONFIG**          | System, System.alt, System.log, System.sav |
| **HKEY\_CURRENT\_USER**            | Ntuser.dat, Ntuser.dat.log                 |
| **HKEY\_LOCAL\_MACHINE\\SAM**      | Sam, Sam.log, Sam.sav                      |
| **HKEY\_LOCAL\_MACHINE\\Security** | Security, Security.log, Security.sav       |
| **HKEY\_LOCAL\_MACHINE\\Software** | Software, Software.log, Software.sav       |
| **HKEY\_LOCAL\_MACHINE\\System**   | System, System.alt, System.log, System.sav |
| **HKEY\_USERS\\.DEFAULT**          | Default, Default.log, Default.sav          |



 

 

 




