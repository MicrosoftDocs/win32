---
title: Security Methods
description: Microsoft RPC supports two different methods for adding security to your distributed application.
ms.assetid: 10dd8e71-668a-46bf-ab5d-e4b1e0e56a46
ms.topic: reference
ms.date: 05/31/2018
---

# Security Methods

Microsoft RPC supports two different methods for adding security to your distributed application. The first method is to use the Security Support Provider Interface (SSPI), which can be accessed using the RPC functions. In general, it is best to use this method. The SSPI provides the most flexible and network-independent authentication features.

The second method is to use the security features built into the system transport protocols. The transport-level security method is not the preferred method. Using the SSPI is recommended because it works on all transports, across platforms, and provides high levels of security, including privacy.

This section provides overviews of both SSPI and transport-level security in the following topics:

-   [Security Support Provider Interface (SSPI)](security-support-provider-interface-sspi-.md)
-   [Transport Security](transport-security.md)

 

 




