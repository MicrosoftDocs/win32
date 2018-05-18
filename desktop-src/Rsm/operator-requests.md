---
Description: 'An RSM operator request is a request for a person (often an administrator, but can be a user) to perform a task.'
ms.assetid: '68f25f92-bf59-4e3c-8caa-6e87ce95ac15'
title: Operator Requests
---

# Operator Requests

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

An RSM operator request is a request for a person (often an administrator, but can be a user) to perform a task. Operator requests can be issued by RSM or by RSM applications. RSM generates operator requests in the following situations:

-   Media must be moved online because an application has initiated a mount request for media that is offline.
-   There are no Available media online in the specified application media pool or in the appropriate free media pool when an application requests media allocation. The operator can supply new media or Available media that is offline to satisfy the request.
-   A device failed and requires service.
-   A drive needs to be cleaned and there is no usable cleaner cartridge available in the library unit.

Operator requests are displayed in the RSM MMC snap-in. The person acting on the request must ether complete or refuse it in the snap-in. When the individual performs the request successfully then the request must be completed. If the request cannot be completed then it must be refused.. When an operator cancels an operator request, RSM notifies the application that generated the request.

Sometimes, even with robotic libraries, manual assistance is needed to complete a request or perform maintenance or support. If an application requests that a cartridge in the offline library be mounted, the cartridge must be manually entered into a library, generating a request to the operator to enter the cartridge.

Operator requests can be presented to an administrator through the Messenger Service or the status area of the taskbar. An administrator can refuse or complete these requests.

> [!Note]  
> "Operator" as used here, is synonymous with "administrator."

 

 

 



