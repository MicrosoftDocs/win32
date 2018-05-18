---
title: User Modal Functions
description: The network management user modal functions get and set system-wide parameters related to security system behavior.
ms.assetid: 'e655b9f6-2808-4bd4-998c-c8a2e980920b'
---

# User Modal Functions

The network management user modal functions get and set system-wide parameters related to security system behavior.

The user modal functions are listed following.



| Function                                     | Description                                                                                                                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetUserModalsGet**](netusermodalsget.md) | Returns global information for all users and global groups in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. |
| [**NetUserModalsSet**](netusermodalsset.md) | Sets global information for all users and global groups in the security database.                                                                                                                       |



 

The **NetUserModalsGet** and **NetUserModalsSet** functions examine and modify the modal settings, which are global parameters that affect every account in the security database (for example, the minimum allowable password length). All modal settings can be altered by calling **NetUserModalsSet**. Most of the modals can also be altered by using the **net accounts** command. The network management user modal functions do not require the server to have user-level security.

User modal information is available at the following levels:

-   [**USER\_MODALS\_INFO\_0**](user-modals-info-0-str.md)
-   [**USER\_MODALS\_INFO\_1**](user-modals-info-1-str.md)
-   [**USER\_MODALS\_INFO\_2**](user-modals-info-2-str.md)
-   [**USER\_MODALS\_INFO\_3**](user-modals-info-3-str.md)

The following information levels are valid only for [**NetUserModalsSet**](netusermodalsset.md) and replace the older way of passing in a *Parmnum* to set a specific field:

-   [**USER\_MODALS\_INFO\_1001**](user-modals-info-1001-str.md)
-   [**USER\_MODALS\_INFO\_1002**](user-modals-info-1002-str.md)
-   [**USER\_MODALS\_INFO\_1003**](user-modals-info-1003-str.md)
-   [**USER\_MODALS\_INFO\_1004**](user-modals-info-1004-str.md)
-   [**USER\_MODALS\_INFO\_1005**](user-modals-info-1005-str.md)
-   [**USER\_MODALS\_INFO\_1006**](user-modals-info-1006-str.md)
-   [**USER\_MODALS\_INFO\_1007**](user-modals-info-1007-str.md)

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management user modal functions. For more information, see [**IADsDomain**](https://msdn.microsoft.com/library/aa706002).

 

 




