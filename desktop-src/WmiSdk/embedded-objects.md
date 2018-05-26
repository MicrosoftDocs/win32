---
Description: An embedded object is an object of a class that exists within a class or instance declaration of another class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 11a4556b-f682-4850-aedc-793602c5745b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Embedding Objects in a Class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Embedding Objects in a Class

An embedded object is an object of a class that exists within a class or instance declaration of another class. For example, the [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) class contains [**Win32\_Trustee**](https://msdn.microsoft.com/library/aa394501) embedded objects. Each of the **Win32\_Trustee** objects contains a [**Win32\_ACE**](https://msdn.microsoft.com/library/aa394063) object. WMI does not limit the depth to which a class can have embedded objects. However, using another design, such as creating an association class, may make a more manageable schema.

For more information about embedded objects, see the following topics:

-   [Creating Embedded Objects](creating-embedded-objects.md)
-   [Querying Embedded Objects](querying-embedded-objects.md)

## Related topics

<dl> <dt>

[Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)
</dt> </dl>

 

 



