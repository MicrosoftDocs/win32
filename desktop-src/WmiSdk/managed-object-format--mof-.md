---
description: Managed Object Format (MOF) is the language used to describe Common Information Model (CIM) classes.
ms.assetid: 26494142-2078-4d46-a794-e43973255c2d
ms.tgt_platform: multiple
title: Managed Object Format (MOF)
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Managed Object Format (MOF)

Managed Object Format (MOF) is the language used to describe [*Common Information Model (CIM)*](gloss-c.md) classes.

The recommended way for WMI providers to implement new WMI classes is in MOF files which are compiled using [**Mofcomp.exe**](mofcomp.md) into the [*WMI repository*](gloss-w.md). It is also possible to create and manipulate CIM classes and instances using the [COM API for WMI](com-api-for-wmi.md).

A WMI provider normally consists of a MOF file, which defines the data and event classes for which the provider returns data, and a DLL file which contains the code that supplies data. For more information, see [Providing Data to WMI](providing-data-to-wmi.md).

WMI client scripts and applications can query for instances of provider MOF classes or subscribe to receive event notifications.

You can perform the following tasks with MOF:

-   [Compiling MOF Files](compiling-mof-files.md)
-   [Creating a Class](creating-a-class.md)
-   [Creating an Instance](creating-an-instance.md)
-   [Creating a Method](creating-a-method.md)
-   [Adding a Qualifier](adding-a-qualifier.md)
-   [Creating a Comment](creating-a-comment.md)

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> </dl>

 

 



