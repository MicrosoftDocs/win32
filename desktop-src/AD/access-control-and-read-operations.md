---
title: Access Control and Read Operations
description: Security is an implicit filter for searching, enumerating containers, or reading properties.
ms.assetid: ee46cbc4-5539-48ce-991f-3ad0429f65ca
ms.tgt_platform: multiple
keywords:
- Access Control and Read Operations AD
ms.topic: reference
ms.date: 02/13/2024
---

# Access Control and Read Operations

Security is an implicit filter for searching, enumerating containers, or reading properties. If you don't have the necessary access rights, attempts to list objects or read properties can fail with the following error codes even though the object or property exists:

- **E_ADS_INVALID_DOMAIN_OBJECT**
- **E_ADS_PROPERTY_NOT_SUPPORTED**
- **E_ADS_PROPERTY_NOT_FOUND**

Be aware that a caller with **ADS_RIGHT_ACTRL_DS_LIST** access to a container can enumerate the child objects in the container. However, an attempt to access a child object can still fail with an error such as **E_ADS_UNKNOWN_OBJECT** if the caller does not have **ADS_RIGHT_ACTRL_DS_LIST_OBJECT** access to the child object.

The impact of security on read operations is not necessarily manifested as an error. For example, a search operation can succeed, but the search results don't include objects or properties to which the caller doesn't have access.
