---
description: The following functions are implemented by a network provider DLL to communicate with the Multiple Provider Router (MPR).
ms.assetid: ebdaec3d-6335-4bdf-b150-91e538068f2b
title: Functions Implemented by Network Providers
ms.topic: article
ms.date: 05/31/2018
---

# Functions Implemented by Network Providers

The following functions are implemented by a network provider DLL to communicate with the [*Multiple Provider Router*](/windows/desktop/SecGloss/m-gly) (MPR). Note that only the [Capabilities Functions](capabilities-functions.md) must be implemented by a network provider. Implementation of the other types of functions is optional and depends on the requirements of the network provider.



| Function set                                                                                    | Description                                                                                                                                        |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [Capabilities Functions](capabilities-functions.md)<br/>                                 | Allows the caller to determine the capabilities of the network provider.<br/>                                                                |
| [User Name Functions](user-name-functions.md)<br/>                                       | Prompts the network provider for the user name associated with a connection.<br/>                                                            |
| [Device-Redirecting Functions](device-redirecting-functions.md)<br/>                     | Allows a network provider to redirect devices, drive letters, and LPT ports that are standard on the Microsoft MS-DOS operating system.<br/> |
| [Provider-Specific Dialog Box Functions](provider-specific-dialog-box-functions.md)<br/> | Allows a network provider to display or act on network-specific information.<br/>                                                            |
| [Administrative Functions](administrative-functions.md)<br/>                             | Allows a network provider to display or act on special network directories.<br/>                                                             |
| [Enumeration Functions](enumeration-functions.md)<br/>                                   | Allows the user to browse network resources.<br/>                                                                                            |



 

For more information about how to create and register a network provider, see [Implementing a Network Provider](implementing-a-network-provider.md) and [Registering Network Providers and Credential Managers](registering-network-providers-and-credential-managers.md).

 

