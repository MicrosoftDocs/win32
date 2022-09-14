---
title: Unknown User Types
description: Unknown User Types
ms.assetid: c2a4bd83-6eaf-4130-8f86-e99f1e18b63d
ms.topic: article
ms.date: 05/31/2018
---

# Unknown User Types

You can ease product localization by adding the following registry key:

**HKEY\_LOCAL\_MACHINES\\SOFTWARE\\Microsoft\\OLE2**\\**UnknownUserType** = *usertype*

This key allows functions to return a specified string rather than a default value of "Unknown", enabling localizers to specify a user type of a different language.

The COM default handler's implementation of [**IOleObject::GetUserType**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getusertype) examines the registry by calling [**OleRegGetUserType**](/windows/desktop/api/Ole2/nf-ole2-olereggetusertype). If the object's class is not found in the registry, the user type from the object's [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) instance is returned. If the class is not found in the object's **IStorage** instance, the string "Unknown" is returned.

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 