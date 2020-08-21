---
title: Locating a Remote Object
description: Locating a Remote Object
ms.assetid: b329de53-646b-42a2-afa3-06473c3483d6
ms.topic: article
ms.date: 05/31/2018
---

# Locating a Remote Object

With the advent of COM for distributed systems, COM uses the basic model for object creation described in [COM Class Objects and CLSIDs](com-class-objects-and-clsids.md) and adds more than one way to locate an object that might reside on another system in a network, without overburdening the client application.

COM has added registry keys that permit a server to register the name of the machine on which it resides or the machine where an existing storage is located. Therefore, client applications need know only the CLSID of the server.

However, for cases where it is desired, COM has replaced a previously reserved parameter of [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) with a [**COSERVERINFO**](/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure, which allows a client to specify the location of a server. Another important value in the **CoGetClassObject** function is the [**CLSCTX**](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx) enumeration, which specifies whether the expected object is to be run in-process, out-of-process local, or out-of-process remote. Taken together, these two values and the values in the registry determine how and where the object is to be run.

> [!Note]  
> Instance creation calls, when they specify a server location, can override a registry setting. The algorithm COM uses for doing this is described in the reference for the [**CLSCTX**](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx) enumeration.

 

Remote activation depends on the security relationship between client and server. For more information, see [Security in COM](security-in-com.md).

## Related topics

<dl> <dt>

[COM Class Objects and CLSIDs](com-class-objects-and-clsids.md)
</dt> <dt>

[Creating an Object Through a Class Object](creating-an-object-through-a-class-object.md)
</dt> </dl>

 

 