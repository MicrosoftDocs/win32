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
| [**NetFileEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525378), [**NetFileGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525379) | [**IADsResource**](https://msdn.microsoft.com/library/aa706124), [**IADsFileServiceOperations**](https://msdn.microsoft.com/library/aa706015) |
| [NetGroup](group-functions.md)\*                                          | [**IADsGroup**](https://msdn.microsoft.com/library/aa706021)                                                                        |
| [NetLocalGroup](local-group-functions.md)\*                               | [**IADsGroup**](https://msdn.microsoft.com/library/aa706021)                                                                        |
| [NetServer](server-functions.md)\*                                        | [**IADsComputer**](https://msdn.microsoft.com/library/aa705980)                                                                  |
| [NetSession](session-functions.md)\*                                      | [**IADsSession**](https://msdn.microsoft.com/library/aa746331), [**IADsFileServiceOperations**](https://msdn.microsoft.com/library/aa706015)   |
| [NetShare](share-functions.md)\*                                          | [**IADsFileShare**](https://msdn.microsoft.com/library/aa706019)                                                                |
| [NetUser](user-functions.md)\*                                            | [**IADsUser**](https://msdn.microsoft.com/library/aa746340), [**IADsComputer**](https://msdn.microsoft.com/library/aa705980)                                   |
| [NetUserModals](user-modal-functions.md)\*                                | [**IADsDomain**](https://msdn.microsoft.com/library/aa706002)                                                                      |



 

For more information about directory services and programming with ADSI, see [Active Directory Service Interfaces](https://msdn.microsoft.com/library/aa772170). For information about the custom properties the WinNT provider makes available for the User class, and the property methods of the [**IADsUSer**](https://msdn.microsoft.com/library/aa746340) interface the WinNT provider does not support, see [ADSI WinNT Provider](https://msdn.microsoft.com/library/aa772237).

 

 




