---
title: Redistributing Windows Media Player 11
description: Redistributing Windows Media Player 11
ms.assetid: 3348821f-6d72-40c2-954b-0046ce502401
ms.topic: article
ms.date: 05/31/2018
---

# Redistributing Windows Media Player 11

You can install Windows Media Player 11 on Windows XP by using one of the following setup programs, where *localeId* is a locale identifier.

-   wmp11-windowsxp-x86-*localeId*.exe
-   wmp11-windowsxp-x64-*localeId*.exe

Here is an example of a command line for installation with no UI and no restart or restart prompt.


```
wmp11-windowsxp-x86-enu.exe /q:A /c:"setup_wm.exe /Q /R:N"
```



The following table shows additional parameters that you can use with the Windows Media Player 11 setup program.



| Parameter              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /NoMigrate             | Prevent library migration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| /NestedRestore         | Create a nested system restore point. Use this if your application creates a system restore point to nest the Windows Media Player restore point within your application restore point.                                                                                                                                                                                                                                                                                                                             |
| /DisallowSystemRestore | Disallow the creation of a system restore point. This flag will disable the creation of a system restore point. Under most circumstances this flag should not be used for general software redistribution. This should be used only when you can make an explicit choice on behalf of the end user not to support the rollback of the Windows Media Player files to an earlier version of the Player. This flag should be used only for corporate deployment or original equipment manufacturer (OEM) installation. |
| /DefaultService        | Set the initial online store. For more information, see [Setup Command-line Parameters for Online Stores](setup-command-line-parameters-for-online-stores.md).                                                                                                                                                                                                                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[**Redistributing Windows Media Player Software**](redistributing-windows-media-player-software.md)
</dt> </dl>

 

 




