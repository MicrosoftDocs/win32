---
title: User Modal Functions
description: The network management user modal functions get and set system-wide parameters related to security system behavior.
ms.assetid: e655b9f6-2808-4bd4-998c-c8a2e980920b
ms.topic: article
ms.date: 05/31/2018
---

# User Modal Functions

The network management user modal functions get and set system-wide parameters related to security system behavior.

The user modal functions are listed following.



| Function                                     | Description                                                                                                                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetUserModalsGet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsget) | Returns global information for all users and global groups in the security database, which is the security accounts manager (SAM) database or, in the case of domain controllers, the Active Directory. |
| [**NetUserModalsSet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsset) | Sets global information for all users and global groups in the security database.                                                                                                                       |



 

The **NetUserModalsGet** and **NetUserModalsSet** functions examine and modify the modal settings, which are global parameters that affect every account in the security database (for example, the minimum allowable password length). All modal settings can be altered by calling **NetUserModalsSet**. Most of the modals can also be altered by using the **net accounts** command. The network management user modal functions do not require the server to have user-level security.

User modal information is available at the following levels:

-   [**USER\_MODALS\_INFO\_0**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_0)
-   [**USER\_MODALS\_INFO\_1**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1)
-   [**USER\_MODALS\_INFO\_2**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_2)
-   [**USER\_MODALS\_INFO\_3**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_3)

The following information levels are valid only for [**NetUserModalsSet**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusermodalsset) and replace the older way of passing in a *Parmnum* to set a specific field:

-   [**USER\_MODALS\_INFO\_1001**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1001)
-   [**USER\_MODALS\_INFO\_1002**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1002)
-   [**USER\_MODALS\_INFO\_1003**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1003)
-   [**USER\_MODALS\_INFO\_1004**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1004)
-   [**USER\_MODALS\_INFO\_1005**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1005)
-   [**USER\_MODALS\_INFO\_1006**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1006)
-   [**USER\_MODALS\_INFO\_1007**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_modals_info_1007)

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management user modal functions. For more information, see [**IADsDomain**](/windows/desktop/api/iads/nn-iads-iadsdomain).

 

 