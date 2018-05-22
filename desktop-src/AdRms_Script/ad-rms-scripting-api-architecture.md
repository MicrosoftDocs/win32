---
Description: 'One top-level object, ConfigurationManager, that is your entry point into the scripting API.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '79a2e806-af6e-43a8-bf22-f04a9d8e2ecd'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: AD RMS Scripting API Architecture
---

# AD RMS Scripting API Architecture

The AD RMS Scripting API contains one top-level object, [**ConfigurationManager**](configurationmanager-object.md), that is your entry point into the scripting API. You can use it to retrieve cluster information, manage rights templates, enable and monitor logging, manage the RMS service account, and retrieve an [**Enterprise**](enterprise-object.md) object to manage the enterprise infrastructure. The following two topics contain the architectural illustrations for these objects.

> [!Note]  
> Although the [**Enterprise**](enterprise-object.md) object resides beneath the [**ConfigurationManager**](configurationmanager-object.md) object in the scripting API hierarchy, it is sufficiently complex that a separate illustration is warranted.

 

-   [ConfigurationManager Architectural Illustration](configurationmanager-architectural-illustration.md)
-   [Enterprise Architectural Illustration](enterprise-architectural-illustration.md)

## Related topics

<dl> <dt>

[About the Active Directory Rights Management Services Scripting API](about-the-active-directory-rights-management-services-scripting-api.md)
</dt> </dl>

 

 



