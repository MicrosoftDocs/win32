---
description: After you have created your network provider or credential manager, you must register it with the system.
ms.assetid: 4c58671d-d11d-4f32-866b-e278fc8e6114
title: Registering Network Providers and Credential Managers
ms.topic: article
ms.date: 05/31/2018
---

# Registering Network Providers and Credential Managers

After you have created your network provider or credential manager, you must register it with the system. This is necessary so the MPR will know what network providers are installed. When the MPR starts, it checks the registry and loads any network providers or credential managers it finds.

Because network providers and credential managers are related, they are registered in the same subkeys of the registry. In fact, network provider DLLs can also be credential managers.

For detailed information about the registry keys you should create for your network provider or credential manager, see [Authentication Registry Keys](authentication-registry-keys.md).

 

 



