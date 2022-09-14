---
description: The COMMCONFIG structure defines the configuration of a communications resource, serial or otherwise.
ms.assetid: 05094b98-4694-42dd-883c-b3c90735b3bc
title: Communications Resource Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Communications Resource Configuration

The [**COMMCONFIG**](/windows/desktop/api/Winbase/ns-winbase-commconfig) structure defines the configuration of a communications resource, serial or otherwise. The format of the structure varies depending on the type of communications resource (the provider subtype). The first few structure members are common to all communications resources; additional members are defined for specific provider subtypes. Specific service providers may extend the **COMMCONFIG** structure as well.

An application can get and set the configuration of a communications resource by using the [**GetCommConfig**](/windows/desktop/api/Winbase/nf-winbase-getcommconfig) and [**SetCommConfig**](/windows/desktop/api/Winbase/nf-winbase-setcommconfig) functions. When opened, a communications resource is initialized using the default configuration for its provider subtype. To get and set the default configuration for a provider subtype, use the [**GetDefaultCommConfig**](/windows/desktop/api/Winbase/nf-winbase-getdefaultcommconfiga) and [**SetDefaultCommConfig**](/windows/desktop/api/Winbase/nf-winbase-setdefaultcommconfiga) functions.

To prompt the user for configuration information, use the [**CommConfigDialog**](/windows/desktop/api/Winbase/nf-winbase-commconfigdialoga) function. This function displays a dialog box defined by the service provider and fills in a [**COMMCONFIG**](/windows/desktop/api/Winbase/ns-winbase-commconfig) structure based on user input.

 

 



