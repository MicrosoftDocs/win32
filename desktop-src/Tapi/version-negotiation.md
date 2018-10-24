---
Description: Over time, different versions may exist for TAPI applications, TAPI, and the service providers.
ms.assetid: '39b16328-931e-4d75-a6ec-1edc97f1a287'
title: Version Negotiation
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Version Negotiation

Over time, different versions may exist for TAPI applications, TAPI, and the service providers. Optimal interoperability of a TAPI application requires knowledge of not just the application's TAPI version, but also of the TAPI DLL, TAPISVR, and service provider versions.

Failure to do proper version negotiation can result in serious problems. For example, some heavily used structures have data members added from one version to the next. If the structure size does not match what the application or TAPI expects, the consequences range from memory leaks to intermittent AVs.

For additional information, see [TAPI Versioning](https://msdn.microsoft.com/en-us/library/ms737251(v=VS.85).aspx).

**TAPI 2.x:** Applications negotiate with TAPI and TAPISVR during [**lineInitializeEx**](https://msdn.microsoft.com/en-us/library/ms735983(v=VS.85).aspx). Applications perform device negotiation with service providers by calling [**lineNegotiateAPIVersion**](https://msdn.microsoft.com/en-us/library/ms736002(v=VS.85).aspx) for each line that the application might use.

**TAPI 3.x:** There is no need to perform version negotiation; however, you can use [**QueryInterface**](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx) to determine if an interface is available on their version.

 

 



