---
Description: The COMMCONFIG structure defines the configuration of a communications resource, serial or otherwise.
ms.assetid: 05094b98-4694-42dd-883c-b3c90735b3bc
title: Communications Resource Configuration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Communications Resource Configuration

The [**COMMCONFIG**](/windows/win32/Winbase/ns-winbase-_commconfig?branch=master) structure defines the configuration of a communications resource, serial or otherwise. The format of the structure varies depending on the type of communications resource (the provider subtype). The first few structure members are common to all communications resources; additional members are defined for specific provider subtypes. Specific service providers may extend the **COMMCONFIG** structure as well.

An application can get and set the configuration of a communications resource by using the [**GetCommConfig**](/windows/win32/Winbase/nf-winbase-getcommconfig?branch=master) and [**SetCommConfig**](/windows/win32/Winbase/nf-winbase-setcommconfig?branch=master) functions. When opened, a communications resource is initialized using the default configuration for its provider subtype. To get and set the default configuration for a provider subtype, use the [**GetDefaultCommConfig**](/windows/win32/Winbase/nf-winbase-getdefaultcommconfiga?branch=master) and [**SetDefaultCommConfig**](/windows/win32/Winbase/nf-winbase-setdefaultcommconfiga?branch=master) functions.

To prompt the user for configuration information, use the [**CommConfigDialog**](/windows/win32/Winbase/nf-winbase-commconfigdialoga?branch=master) function. This function displays a dialog box defined by the service provider and fills in a [**COMMCONFIG**](/windows/win32/Winbase/ns-winbase-_commconfig?branch=master) structure based on user input.

 

 



