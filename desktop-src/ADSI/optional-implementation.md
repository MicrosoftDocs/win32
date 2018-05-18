---
title: Optional Implementation
description: The following features are optional, but recommended
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '6123bdda-06cf-4b8b-b2a8-89882b6341b4'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Optional Implementation ADSI"]
---

# Optional Implementation

The following features are optional, but recommended:

-   The [**IDirectorySearch**](idirectorysearch.md) interface for non-Automation clients. Because the ADSI OLE DB provider uses **IDirectorySearch** to present queries and collect results from the underlying directory service, providers that implement this interface automatically provide access to OLE DB style databases without having to implement any additional interfaces.
-   The [**IADsSecurityDescriptor**](iadssecuritydescriptor.md), [**IADsAccessControlList**](iadsaccesscontrollist.md), and [**IADsAccessControlEntry**](iadsaccesscontrolentry.md) interfaces. Providers for directory services that support ACL-based object security are encouraged to implement these additional features.

 

 




