---
title: Mapping ADSI Interfaces to the Network Management Functions
description: The Active Directory Service Interfaces (ADSI) are a set of COM interfaces used to access the capabilities of directory services from different network providers.
ms.assetid: dfa81c58-3ce4-40ee-8bfc-a19a13781992
ms.topic: article
ms.date: 05/31/2018
---

# Mapping ADSI Interfaces to the Network Management Functions

The Active Directory Service Interfaces (ADSI) are a set of COM interfaces used to access the capabilities of directory services from different network providers. ADSI presents a single set of directory service interfaces for managing network resources in a distributed computing environment.

If you are programming for Active Directory, you may be able to call certain ADSI interface methods to achieve the same functionality you can achieve by calling certain network management functions.

The following table lists network management functions and function groups, and the ADSI interfaces to which the functions map.



| Functions                                                                  | Interfaces                                                                                             |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**NetFileEnum**](/windows/desktop/api/lmshare/nf-lmshare-netfileenum), [**NetFileGetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netfilegetinfo) | [**IADsResource**](/windows/desktop/api/iads/nn-iads-iadsresource), [**IADsFileServiceOperations**](/windows/desktop/api/iads/nn-iads-iadsfileserviceoperations) |
| [NetGroup](group-functions.md)\*                                          | [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup)                                                                        |
| [NetLocalGroup](local-group-functions.md)\*                               | [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup)                                                                        |
| [NetServer](server-functions.md)\*                                        | [**IADsComputer**](/windows/desktop/api/iads/nn-iads-iadscomputer)                                                                  |
| [NetSession](session-functions.md)\*                                      | [**IADsSession**](/windows/desktop/api/iads/nn-iads-iadssession), [**IADsFileServiceOperations**](/windows/desktop/api/iads/nn-iads-iadsfileserviceoperations)   |
| [NetShare](share-functions.md)\*                                          | [**IADsFileShare**](/windows/desktop/api/iads/nn-iads-iadsfileshare)                                                                |
| [NetUser](user-functions.md)\*                                            | [**IADsUser**](/windows/desktop/api/iads/nn-iads-iadsuser), [**IADsComputer**](/windows/desktop/api/iads/nn-iads-iadscomputer)                                   |
| [NetUserModals](user-modal-functions.md)\*                                | [**IADsDomain**](/windows/desktop/api/iads/nn-iads-iadsdomain)                                                                      |



 

For more information about directory services and programming with ADSI, see [Active Directory Service Interfaces](/windows/desktop/ADSI/active-directory-service-interfaces-adsi). For information about the custom properties the WinNT provider makes available for the User class, and the property methods of the [**IADsUser**](/windows/desktop/api/iads/nn-iads-iadsuser) interface the WinNT provider does not support, see [ADSI WinNT Provider](/windows/desktop/ADSI/adsi-winnt-provider).

 

 