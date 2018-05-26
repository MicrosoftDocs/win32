---
Description: You can access most fax service Component Object Model (COM) objects through a single root object, the FaxServer object.
ms.assetid: 521534dc-7cd5-48fb-b1c1-61dbc1e4eb1f
title: Creating the Root Object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating the Root Object

You can access most fax service Component Object Model (COM) objects through a single root object, the [**FaxServer**](-mfax-faxserver.md) object. You must first create this root object and then use its properties to access subordinate objects in the object model. You must also connect to the fax server, as described later.

A small number of objects is accessed through the [**FaxDocument**](-mfax-faxdocument.md) object, which can be used as a root object to access those specific objects. For more information, see the [Fax Service Extended COM Object Model](-mfax-fax-service-extended-com-object-model.md).

This section contains the following topics.

-   [Creating the Root Object in Scripting Languages and Visual Basic](-mfax-creating-the-root-object-in-scripting-languages-and-visual-basic.md)
-   [Creating the Root Object in C++](-mfax-creating-the-root-object-in-c-.md)

 

 



