---
title: Moving Objects
description: Moving Objects
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3afdf480-a7ee-4b7b-99f6-4a8e8cb2096c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , moving objects
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Moving Objects

To move an object within a domain, use the [**IADsContainer.MoveHere**](https://msdn.microsoft.com/library/aa705991) method.

**To move an object within a domain**

1.  Bind to the [**IADs**](https://msdn.microsoft.com/library/aa705950) interface of the object to move.
2.  Get the ADsPath of the object to move from the [**IADs.ADsPath**](https://msdn.microsoft.com/library/aa746351) property.
3.  Bind to the [**IADsContainer**](https://msdn.microsoft.com/library/aa705985) interface of the container where the object will be moved to.
4.  Move the object with the [**IADsContainer.MoveHere**](https://msdn.microsoft.com/library/aa705991) method.

If an interface exists to the object that was moved, the interface is not valid after the object is moved because the directory object the interface represents no longer exists.

For more information and a code example that shows how to move an object, see [Example Code for Moving an Object](example-code-for-moving-an-object.md).

 

 




