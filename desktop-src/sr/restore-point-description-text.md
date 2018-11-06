---
title: Restore Point Description Text
description: When an application calls the SRSetRestorePoint function, it can provide any text as a description for the restore point; however, the following table shows the recommended description text.
ms.assetid: e6e1974b-c162-4019-9349-936f3786cb9b
ms.topic: article
ms.date: 05/31/2018
---

# Restore Point Description Text

When an application calls the [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) function, it can provide any text as a description for the restore point; however, the following table shows the recommended description text.



| System modification                            | Restore point type      | Description            |
|------------------------------------------------|-------------------------|------------------------|
| Application installation                       | APPLICATION\_INSTALL    | Installed *AppName*    |
| Application modification (add/remove features) | MODIFY\_SETTINGS        | Configured *AppName*   |
| Application removal                            | APPLICATION\_UNINSTALL  | Removed *AppName*      |
| Device driver installation                     | DEVICE\_DRIVER\_INSTALL | Installed *DriverName* |



 

Installers, such as Windows Installer and InstallShield, use these conventions for the description text:

-   The product name follows the verb; for example, Installed *AppName*.
-   The product name can be used alone (*AppName*) or the product name and the company name may both be used (*MyCompany AppName*).

 

 




