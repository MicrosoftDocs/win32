---
title: NAP Utility Functions
description: The following utility functions support the NAP API.
ms.assetid: 0819067c-cca5-4140-8b4d-f3b996826152
ms.topic: article
ms.date: 05/31/2018
---

# NAP Utility Functions

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The following utility functions support the NAP API.

All the COM interfaces supported by the NAP system use standard COM memory management rules and the COM memory allocator (CoTaskMemAlloc and CoTaskMemFree).

-   IN parameters — allocated and freed by caller.
-   OUT parameters — allocated by callee, freed by caller using CoTaskMem\*()
-   IN/OUT parameters — allocated by caller, freed and reallocated by callee, ultimately freed by caller, using CoTaskMem\*()

In the FreeXxx() functions, all embedded pointers will also be freed.

-   [**AllocConnections**](allocconnections-func.md)
-   [**AllocCountedString**](alloccountedstring-func.md)
-   [**AllocFixupInfo**](allocfixupinfo-func.md)
-   [**FreeConnections**](freeconnections-func.md)
-   [**FreeCountedString**](freecountedstring-func.md)
-   [**FreeFixupInfo**](freefixupinfo-func.md)
-   [**FreeIsolationInfo**](freeisolationinfo-func.md)
-   [**FreeIsolationInfoEx**](freeisolationinfoex.md)
-   [**FreeNapComponentRegistrationInfoArray**](freenapcomponentregistrationinfoarray-func.md)
-   [**FreeNetworkSoH**](freenetworksoh-func.md)
-   [**FreePrivateData**](freeprivatedata-func.md)
-   [**FreeSoH**](freesoh-func.md)
-   [**FreeSoHAttributeValue**](freesohattributevalue-func.md)
-   [**FreeSystemHealthAgentState**](freesystemhealthagentstate-func.md)
-   [**InitializeNapAgentNotifier**](initializenapagentnotifier.md)
-   [**UninitializeNapAgentNotifier**](uninitializenapagentnotifier.md)

 

 




