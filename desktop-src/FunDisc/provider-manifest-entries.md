---
Description: Provider Manifest Entries
ms.assetid: e8d5f53f-09a1-4285-8688-791b6b76afe8
title: Provider Manifest Entries
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Provider Manifest Entries

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

For queries (operations) made directly to Provider categories a manifest entry will be found in the following registry key:

**HKLM\\SOFTWARE\\Microsoft\\Function Discovery\\Categories\\Provider**\\**categoryX**

Manifest entries should be REG\_SZ string values containing valid XML data of the following form:

``` syntax
<provider type="{2a0f2c55-332b-4e5c-9563-5007863df405}" ></provider>
```

The value of the **type** attribute is the CLSID of the provider.

Any additional information within the XML string will be ignored.

 

 



