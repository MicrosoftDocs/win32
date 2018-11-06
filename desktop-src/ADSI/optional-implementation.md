---
title: Optional Implementation
description: The following features are optional, but recommended
ms.assetid: 6123bdda-06cf-4b8b-b2a8-89882b6341b4
ms.tgt_platform: multiple
keywords:
- Optional Implementation ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Optional Implementation

The following features are optional, but recommended:

-   The [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface for non-Automation clients. Because the ADSI OLE DB provider uses **IDirectorySearch** to present queries and collect results from the underlying directory service, providers that implement this interface automatically provide access to OLE DB style databases without having to implement any additional interfaces.
-   The [**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor), [**IADsAccessControlList**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist), and [**IADsAccessControlEntry**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry) interfaces. Providers for directory services that support ACL-based object security are encouraged to implement these additional features.

 

 




