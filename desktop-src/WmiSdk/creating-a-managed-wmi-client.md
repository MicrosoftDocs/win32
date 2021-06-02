---
description: WMI does not currently support managed code on WMI, but is supported on MI.
ms.assetid: ED6EF216-7FF7-45F2-9FDD-3A73D5F65F9B
ms.tgt_platform: multiple
title: Creating a Managed WMI Client
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating a Managed WMI Client

The current release of WMI does contain the System.Management namespace, which exposes a number of API's that interact with WMI. However, it is not recommended that you use this namespace.

If you wish to create a managed WMI client, it is recommended that you use the Windows Management Infrastructure (MI). MI is the next-generation version of WMI, and contains full support for managed code. For more information, see [How to Implement a Managed MI Client](/previous-versions/windows/desktop/wmi_v2/how-to-implement-a-managed-mi-client).

 

 
