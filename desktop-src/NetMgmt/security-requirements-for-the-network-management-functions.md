---
title: Security Requirements for the Network Management Functions
description: Calling some of the network management functions does not require special group membership.
ms.assetid: 846a5b81-d5bf-4275-a898-38e6ba308b8f
ms.topic: article
ms.date: 05/31/2018
---

# Security Requirements for the Network Management Functions

Calling some of the network management functions does not require special group membership. Other functions require that users have a specific privilege level to execute successfully. When applicable, the Remarks section on a function's reference page indicates the privilege level a user must have to execute the particular function.

Security requirements that apply to Active Directory domain controllers can differ from those that apply to servers and workstations.

For more information, and a list of affected functions, see the following topics:

-   [Requirements for Network Management functions on Active Directory domain controllers](requirements-for-network-management-functions-on-active-directory-domain-controllers.md)
-   [Requirements for Network Management functions on servers and workstations](requirements-for-network-management-functions-on-servers-and-workstations.md)

For more information about controlling access to securable objects, see [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860), [Privileges](https://msdn.microsoft.com/library/windows/desktop/aa379306), and [Securable Objects](https://msdn.microsoft.com/library/windows/desktop/aa379557).

For more information about specific security descriptors that are used during access checks, see the individual function reference page. For more information about calling functions that require administrator privileges, see [Running with Special Privileges](https://msdn.microsoft.com/library/windows/desktop/ms717802).

 

 




