---
Description: In Windows Vista and later, metadata became central as a method of organizing items such as files, e-mail, or contacts.
ms.assetid: 9dacd399-2cf3-40dd-9501-f26f0281500d
title: Implementing Property Handlers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing Property Handlers

In Windows Vista and later, metadata became central as a method of organizing items such as files, e-mail, or contacts. To enable a system where items can be searched based on their metadata and where users can read or write that metadata, Windows Vista introduced a new property system. Metadata in this system is represented by an extensible set of properties. In this set of topics we describe how you can create a handler that reads and writes properties to and from a file stream. These handlers are called property handlers and each is associated with a given file types, identified by the file name extension.

The following topics discuss the requirements and strategies involved in defining your properties and property handlers.

-   [Understanding Property Handlers](shell.Building_Property_Handlers_Properties)
-   [Using Kind Names](shell.Building_Property_Handlers_User_Friendly_Kind_Names)
-   [Using Property Lists](shell.Building_Property_Handlers_Property_Lists)
-   [Initializing Property Handlers](shell.Building_Property_Handlers_Property_Handlers)
-   [Registering and Distributing Property Handlers](shell.prophand_reg_dist)
-   [Property Handler Best Practices and FAQ](shell.prophand_bestprac_faq)

## Related topics

<dl> <dt>

[Creating Custom Properties](shell.Building_Property_Handlers_Property_Schemas)
</dt> <dt>

[Property Description Schema](shell.propdesc_schema_entry)
</dt> </dl>

 

 



