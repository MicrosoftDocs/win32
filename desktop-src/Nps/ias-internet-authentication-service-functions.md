---
title: NPS Extensions Functions
description: NPS Extensions Functions
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ca217314-00f9-4f9d-a9fe-ed928b3c3b3d
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NPS Extensions Functions

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

## Application Defined

The architecture for NPS Extension DLLs supports the following exported functions:

-   [**RadiusExtensionFreeAttributes**](https://msdn.microsoft.com/library/bb892001)
-   [**RadiusExtensionInit**](https://msdn.microsoft.com/library/bb892002)
-   [**RadiusExtensionProcess**](https://msdn.microsoft.com/library/bb892003)
-   [**RadiusExtensionProcessEx**](https://msdn.microsoft.com/library/bb892005)
-   [**RadiusExtensionProcess2**](https://msdn.microsoft.com/library/bb892004)
-   [**RadiusExtensionTerm**](https://msdn.microsoft.com/library/bb892006)

The [**RadiusExtensionInit**](https://msdn.microsoft.com/library/bb892002) and [**RadiusExtensionTerm**](https://msdn.microsoft.com/library/bb892006) functions are optional.

The Extension DLL may export [**RadiusExtensionProcess2**](https://msdn.microsoft.com/library/bb892004) instead of [**RadiusExtensionProcess**](https://msdn.microsoft.com/library/bb892003) or [**RadiusExtensionProcessEx**](https://msdn.microsoft.com/library/bb892005).

If the Extension DLL exports [**RadiusExtensionProcessEx**](https://msdn.microsoft.com/library/bb892005), then it must also export [**RadiusExtensionFreeAttributes**](https://msdn.microsoft.com/library/bb892001).

## System Defined

When NPS calls an implementation of [**RadiusExtensionProcess2**](https://msdn.microsoft.com/library/bb892004), NPS passes the function a pointer to a [**RADIUS\_EXTENSION\_CONTROL\_BLOCK**](https://msdn.microsoft.com/library/bb892016) structure.

The [**RADIUS\_EXTENSION\_CONTROL\_BLOCK**](https://msdn.microsoft.com/library/bb892016) structure contains function pointers to the following functions provided by NPS:

-   [**GetRequest**](https://msdn.microsoft.com/library/bb891990)
-   [**GetResponse**](https://msdn.microsoft.com/library/bb891991)
-   [**SetResponseType**](https://msdn.microsoft.com/library/bb892022)

The functions [**GetRequest**](https://msdn.microsoft.com/library/bb891990) and [**GetResponse**](https://msdn.microsoft.com/library/bb891991) return pointers to a structure of type [**RADIUS\_ATTRIBUTE\_ARRAY**](https://msdn.microsoft.com/library/bb892010).

The [**RADIUS\_ATTRIBUTE\_ARRAY**](https://msdn.microsoft.com/library/bb892010) structure contains function pointers to the following functions provided by NPS:

-   [**Add**](https://msdn.microsoft.com/library/bb891986)
-   [**AttributeAt**](https://msdn.microsoft.com/library/bb891987)
-   [**GetSize**](https://msdn.microsoft.com/library/bb891992)
-   [**InsertAt**](https://msdn.microsoft.com/library/bb891994)
-   [**RemoveAt**](https://msdn.microsoft.com/library/bb892020)
-   [**SetAt**](https://msdn.microsoft.com/library/bb892021)

 

 




