---
Description: The installer sets the UILevel property to the level of the user interface.
ms.assetid: c89545b5-aeb7-4b05-94b0-d6e2a237152e
title: UILevel property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UILevel property

The installer sets the **UILevel** property to the level of the user interface. The internal UI is enabled and set by [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui). This property is set to one of the following INSTALLUILEVEL data types.



| INSTALLUILEVEL          | Numeric value | User interface level                        |
|-------------------------|---------------|---------------------------------------------|
| INSTALLUILEVEL\_NONE    | 2             | Completely silent installation.             |
| INSTALLUILEVEL\_BASIC   | 3             | Simple progress and error handling.         |
| INSTALLUILEVEL\_REDUCED | 4             | Authored UI, wizard dialogs suppressed.     |
| INSTALLUILEVEL\_FULL    | 5             | Authored UI with wizards, progress, errors. |



 

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[User Interface](user-interface.md)
</dt> <dt>

[Determining UI Level from a Custom Action](determining-ui-level-from-a-custom-action.md)
</dt> </dl>

 

 




