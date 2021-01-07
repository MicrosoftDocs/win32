---
description: ICE91 posts a warning if a file, .ini file, or shortcut file is installed into a per-user only directory.
ms.assetid: 1834d841-b1d9-4646-8057-a41dd88310b6
title: ICE91
ms.topic: article
ms.date: 05/31/2018
---

# ICE91

ICE91 posts a warning if a file, .ini file, or shortcut file is installed into a per-user only directory. These warnings are harmless if the package is only used for installation in the per-user [installation context](installation-context.md) and never used for per-machine installations.

Files, .ini files, or shortcuts in per-user only directories are installed into a particular user's profile. Even if the user sets the [**ALLUSERS**](allusers.md) property for a per-machine installations, files, .ini files, or shortcuts in per-user only directories are not copied in to the "All Users" profile and are not available to other users. The per-user only directories do not vary with the **ALLUSERS** property. The following is a list of the per-user only directories:

-   AppDataFolder
-   FavoritesFolder
-   NetHoodFolder
-   PersonalFolder
-   PrintHoodFolder
-   RecentFolder
-   SendToFolder
-   MyPicturesFolder
-   LocalAppDataFolder

## Result

ICE91 posts the following warnings.



| ICE91 warning                                                                                                                                                                                                                            | Description                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| The file '\[1\]' will be installed to the per user directory '\[2\]' that does not vary based on [**ALLUSERS**](allusers.md) value. This file won't be copied to each user's profile even if a per machine installation is desired.     | The file is installed into a per-user only directory. It is not installed into each user's profile during a per-machine installation.      |
| The IniFile '\[1\]' will be installed to the per user directory '\[2\]' that does not vary based on [**ALLUSERS**](allusers.md) value. This file won't be copied to each user's profile even if a per machine installation is desired.  | The .ini file is installed into a per-user only directory. It is not installed into each user's profile during a per-machine installation. |
| The shortcut '\[1\]' will be installed to the per user directory '\[2\]' that does not vary based on [**ALLUSERS**](allusers.md) value. This file won't be copied to each user's profile even if a per machine installation is desired. | The shortcut is installed into a per-user only directory. It is not installed into each user's profile during a per-machine installation.  |



 

## Example

ICE91 reports the following warnings for the example:

``` syntax
The file 'File1' will be installed to the per user directory 'MyPicturesFolder' that does not vary based on ALLUSERS value. This file won't be copied to each user's profile even if a per machine installation is desired.

The IniFile 'IniFile1' will be installed to the per user directory 'MyIniDir' that does not vary based on ALLUSERS value. This file won't be copied to each user's profile even if a per machine installation is desired.

The shortcut 'Shortcut1' will be installed to the per user directory 'MyShortcutDir' that does not vary based on ALLUSERS value. This file won't be copied to each user's profile even if a per machine installation is desired.
```

[File Table](file-table.md) (partial)



| File  | Component\_ |
|-------|-------------|
| File1 | C1          |



 

[Component Table](component-table.md) (partial) (partial) (partial) (partial)



| Component | Directory\_ |
|-----------|-------------|
| C1        | MyDir       |



 

[IniFile Table](inifile-table.md)



| IniFile  | DirProperty |
|----------|-------------|
| IniFile1 | MyIniDir    |



 

[Shortcut Table](shortcut-table.md)



| Shortcut  | Directory\_   |
|-----------|---------------|
| Shortcut1 | MyShortcutDir |



 

[Directory Table](directory-table.md)



| Directory     | Directory\_Parent  |
|---------------|--------------------|
| MyDir         | FavoritesFolder    |
| MyIniDir      | LocalAppDataFolder |
| MyShortcutDir | PersonalFolder     |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



