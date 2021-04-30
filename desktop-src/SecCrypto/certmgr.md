---
description: CertMgr
ms.assetid: c9b68a81-c4f7-4754-9b47-c83f3679f0e3
title: CertMgr
ms.topic: article
ms.date: 05/31/2018
---

# CertMgr

The CertMgr tools replaces DumpCert. It includes new capabilities for the management of [*certificates*](../secgloss/c-gly.md), [*certificate trust lists*](../secgloss/c-gly.md) (CTLs), and [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs). The tool is installed in the \\Bin folder of the Microsoft Windows Software Development Kit (SDK) installation path.

CertMgr is available as part of the Windows SDK, which you can download from <https://go.microsoft.com/fwlink/p/?linkid=84091>.

CertMgr performs one of four functions depending on the action indicated in the command.

**CertMgr** \[**-add**\|**-del**\|**-put**\] \[*Options*\] \[ **-s** \[ **-r** *RegistryLocation* \] \] *SourceName* \[ **-s** \[ **-r** *RegistryLocation* \] \] \[*DestinationName*\]

The following table indicates the basic actions of the CertMgr tool.



| Action flag | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| none        | Displays certificates, CRLs, or CTLs.With no action flag (to display only), *SourceName* is the name of the certificate store or file containing the items to display. The store can be a [*serialized*](../secgloss/s-gly.md) store (StoreFile) or a system store. By default, CertMgr displays all the certificates, CTLs, or CRLs in the certificate store or file. *DestinationName* is not used for display.<br/>                                                                                                                                                                                                                                                                                                                                  |
| -add        | Copies certificates, CTLs, and CRLs to a certificate store.When using **-add**, *SourceName* is the source certificate store that contains the existing certificates, CTLs, and CRLs. *DestinationName* is the destination certificate store to which the certificates, CTLs, and CRLs will be added. The destination store will be saved as a [*serialized*](../secgloss/s-gly.md) store, unless the **-7** option is used, which saves the store as a [*PKCS*](../secgloss/p-gly.md) \#7 file. Note that the **-7** option cannot be used when the destination store is a system store.<br/>                                                                                                                          |
| -del        | Deletes certificates, CTLs, and CRLs from a certificate store.When using **-del**, *SourceName* is the source certificate store that contains the existing certificates, CTLs, and CRLs. *DestinationName* is the destination certificate store which will contain copies of the remaining certificates, CTLs, and CRLs after the specified items have been deleted. If *DestinationName* is not specified, *SourceName* will also serve as the destination store (it will be modified). The destination store will be saved as a [*serialized*](../secgloss/s-gly.md) store, unless the **-7** option is used, which saves the store as a PKCS \#7 file. Note that the **-7** option cannot be used when the destination store is a system store.<br/> |
| -put        | Saves an [*X.509*](../secgloss/x-gly.md) encoded certificate, CTL, or CRL to a file.When using **-put**, *SourceName* is the source certificate store that contains the existing certificates, CTLs, and CRLs. *DestinationName* is the name of a file to which an [*X.509*](../secgloss/x-gly.md) encoded certificate, CTL, and CRL will be saved. If the **-7** option is used, the file will be saved as a PKCS \#7 file.<br/>                                                                                                                                                                                                                                                                                             |



 

## Options

The following options apply to all CertMgr functions except where noted.



| Option                     | Action flag                                 | Description                                                                                                                                                                                                                                        |
|----------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-v**                     | none (display only)                         | Verbose mode. Displays detailed information about certificates, CTLs, and CRLs. The default is to display brief information.                                                                                                                       |
| **-c**                     | all                                         | Use certificates only.                                                                                                                                                                                                                             |
| **-CTL**                   | all                                         | Use CTLs only.                                                                                                                                                                                                                                     |
| **-CRL**                   | all                                         | Use CRLs only.                                                                                                                                                                                                                                     |
| **-all**                   | **-add-del**<br/> **-put**<br/> | Adds all entries of the chosen type.                                                                                                                                                                                                               |
| **-e** *encodingType*      | all                                         | Certificate [*encoding type*](../secgloss/e-gly.md).                                                                                                                                             |
| **-y** *storeProviderType* | all                                         | Store provider type.                                                                                                                                                                                                                               |
| **-7**                     | **-add-del**<br/> **-put**<br/> | Saves the destination store as a PKCS \#7 file.                                                                                                                                                                                                    |
| **-f** *dwFlags*           | all                                         | Store open flag. This is the *dwFlags* parameter passed to [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore). The default value is CERT\_SYSTEM\_STORE\_CURRENT\_USER. Meaningful only if **-y** is set. For more information, see **CertOpenStore**.         |
| **-n** *commonNameString*  | **-add-del**<br/> **-put**<br/> | Common name of the certificate. Can be used only with certificates.                                                                                                                                                                                |
| **-sha1** *sha1Hash*       | **-add-del**<br/> **-put**<br/> | SHA1 hash of the certificate, CTL, or CRL to be copied, deleted, or saved.                                                                                                                                                                         |
| **-s**                     | all                                         | Indicates that the store is a system store.                                                                                                                                                                                                        |
| **-r** *registryLocation*  | all                                         | Registry location of the system certificate store. Meaningful only when **-s** is set. Must be set to either *currentUser* (registry key HKEY\_CURRENT\_USER) or *localMachine* (registry key HKEY\_LOCAL\_MACHINE). *currentUser* is the default. |
| **-?**                     | all                                         | Displays all the options.                                                                                                                                                                                                                          |



 

## Remarks

CertMgr is only supported in Internet Explorer 4.0 or later.

CertMgr can copy, delete, or save one or more certificates, CTLs, or CRLs. If there is more than one item in one of these categories, the user has three options:

-   Use the **-all** option to copy, delete, or save all the items in the category indicated.
-   Use the **-n** and **-sha1** options to uniquely identify the item to be copied, deleted, or saved.
-   If **-all**, or **-n** and **-sha1** are not indicated, CertMgr prompts the user with a list of items to copy, delete, or save. The user responds by entering the index of the item to be copied, deleted, or saved.

The actions of CertMgr use slight variations of the syntax and options. The syntax and options specific to an action must be used.

CertMgr works with two kinds of certificate stores: StoreFile and system store. A StoreFile can be one of the following kinds of files:

-   An encoded CTL/CRL/certificate file (could be base 64 encoded)
-   A PKCS \#7 file
-   A signed document
-   A serialized StoreFile

It is not necessary to specify the type of the StoreFile. CertMgr can determine the StoreFile type and take the appropriate actions.

A system store is a certificate store normally located in the registry under **currentUser**. The user can refer to a system store by providing just its name. It is not necessary to specify the certificate store provider type. Depending on the type of StoreFile or system store, CertMgr chooses the corresponding store provider type.

## Related topics

<dl> <dt>

[Using CertMgr](using-certmgr.md)
</dt> </dl>

 

 
