---
title: Structure of the ProviderSpecific Buffer
description: The ProviderSpecific buffer includes a length field and a pointer to a buffer.
ms.assetid: 98907187-ad29-4b2c-804c-594fa5ef7401
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Structure of the ProviderSpecific Buffer

The ProviderSpecific buffer includes a length field and a pointer to a buffer. The buffer may include multiple objects, and each object must contain the following, in the order shown:

-   A type field that identifies the object
-   A length field that contains the length of the object, including the header
-   The object data itself

Note that all objects referenced in the ProviderSpecific buffer must be contained within the same piece of contiguous buffer memory (the entire [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure is contained within a contiguous block of memory).

 

 




