---
title: Type Libraries
description: A type library is a file or part of a file that describes the type of one or more ActiveX objects.
ms.assetid: 7a66764e-6f5a-4f27-a64f-aa3c5e058eef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Type Libraries

A *type library* is a file or part of a file that describes the type of one or more ActiveX objects. Type libraries do not store objects; they store type information. By accessing a type library, applications and browsers can determine the characteristics of an object, such as the interfaces supported by the object and the names and addresses of the members of each interface. A member can also be invoked through a type library. For details about the interfaces, refer to [Type Description Interfaces](type-description-interfaces.md).

When ActiveX objects are exposed, you should create a type library to make objects easily accessible to other developers. The simplest way to do this is to describe objects in an Object Description Language file (.odl), and then compile the file using the MIDL compiler, as described in [Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md).

For information about the MIDL compiler, refer to the [Microsoft Interface Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa367091).

 

 




