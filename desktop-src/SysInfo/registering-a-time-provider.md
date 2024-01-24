---
description: The system loads a time provider based on its configuration information stored in the registry.
ms.assetid: 67f79c31-9dd7-4e3f-bfe1-701b10611f91
title: Registering a Time Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Time Provider

The system loads a time provider based on its configuration information stored in the registry. Each time provider should create the following registry key:

**HKEY\_LOCAL\_MACHINE\\System**\\**CurrentControlSet**\\**Services**\\**W32Time**\\**TimeProviders**\\*ProviderName*

The following table describes the values that must exist in each provider's key.



| Value             | Description                                                                                                                                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DllName**       | The name of the DLL that contains the provider. This value has the type **REG\_SZ**.                                                                                                                                     |
| **Enabled**       | Indicates whether the provider should be started. If this value is 1, the provider is started. Otherwise, the provider is not started. This value has the type **REG\_DWORD**.                                           |
| **InputProvider** | Indicates whether the provider is an input provider or an output provider. If this value is 1, the provider is an input provider. Otherwise, the provider is an output provider. This value has the type **REG\_DWORD**. |



 

The time provider manager enumerates the keys under the **TimeProviders** key and starts each enabled provider. Providers are started at system startup and whenever there are parameter changes.

Each time provider can also store application-specific configuration information in the registry.

 

 



