---
title: Access Control and Read Operations
description: Security is an implicit filter for searching, enumerating containers, or reading properties.
ms.assetid: ee46cbc4-5539-48ce-991f-3ad0429f65ca
ms.tgt_platform: multiple
keywords:
- Access Control and Read Operations AD
ms.topic: article
ms.date: 05/31/2018
---

# Access Control and Read Operations

Security is an implicit filter for searching, enumerating containers, or reading properties. If you do not have the necessary access rights, attempts to list objects or read properties can fail with the following error codes even thought the object or property exists:

-   **E\_ADS\_INVALID\_DOMAIN\_OBJECT**
-   **E\_ADS\_PROPERTY\_NOT\_SUPPORTED**
-   **E\_ADS\_PROPERTY\_NOT\_FOUND**

Be aware that a caller with **ADS\_RIGHT\_ACTRL\_DS\_LIST** access to a container can enumerate the child objects in the container. But an attempt to access a child object can still fail with an error such as **E\_ADS\_UNKNOWN\_OBJECT** if the caller does not have **ADS\_RIGHT\_ACTRL\_DS\_LIST\_OBJECT** access to the child object.

The impact of security on read operations is not necessarily manifested as an error. For example, a search operation can succeed, but the search results do not include objects or properties to which the caller does not have access.

 

 




