---
title: Moving Objects
description: Moving Objects
ms.assetid: 3afdf480-a7ee-4b7b-99f6-4a8e8cb2096c
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , moving objects
ms.topic: article
ms.date: 05/31/2018
---

# Moving Objects

To move an object within a domain, use the [**IADsContainer.MoveHere**](/windows/desktop/api/iads/nf-iads-iadscontainer-movehere) method.

**To move an object within a domain**

1.  Bind to the [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interface of the object to move.
2.  Get the ADsPath of the object to move from the [**IADs.ADsPath**](/windows/desktop/ADSI/iads-property-methods) property.
3.  Bind to the [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) interface of the container where the object will be moved to.
4.  Move the object with the [**IADsContainer.MoveHere**](/windows/desktop/api/iads/nf-iads-iadscontainer-movehere) method.

If an interface exists to the object that was moved, the interface is not valid after the object is moved because the directory object the interface represents no longer exists.

For more information and a code example that shows how to move an object, see [Example Code for Moving an Object](example-code-for-moving-an-object.md).

 

 