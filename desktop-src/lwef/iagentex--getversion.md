---
title: IAgentEx GetVersion
description: IAgentEx GetVersion
ms.assetid: e5d55fcd-c1b4-4c9e-b3c7-4471af2f86af
ms.topic: article
ms.date: 05/31/2018
---

# IAgentEx::GetVersion

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVersion(
   short * psMajor,  // address of major version
   short * psMinor   // address of minor version
);
```

Retrieves the version number of Microsoft Agent server.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="psMajor"></span><span id="psmajor"></span><span id="PSMAJOR"></span>*psMajor*
</dt> <dd>

Address of a variable that receives the major version.

</dd> <dt>

<span id="psMinor"></span><span id="psminor"></span><span id="PSMINOR"></span>*psMinor*
</dt> <dd>

Address of a variable that receives the minor version.

</dd> </dl>

 

 




