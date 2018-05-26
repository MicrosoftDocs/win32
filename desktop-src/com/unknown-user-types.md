---
title: Unknown User Types
description: Unknown User Types
ms.assetid: c2a4bd83-6eaf-4130-8f86-e99f1e18b63d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Unknown User Types

You can ease product localization by adding the following registry key:

**HKEY\_LOCAL\_MACHINES\\SOFTWARE\\Microsoft\\OLE2**\\**UnknownUserType** = *usertype*

This key allows functions to return a specified string rather than a default value of "Unknown", enabling localizers to specify a user type of a different language.

The COM default handler's implementation of [**IOleObject::GetUserType**](/windows/win32/OleIdl/nf-oleidl-ioleobject-getusertype?branch=master) examines the registry by calling [**OleRegGetUserType**](/windows/win32/Ole2/nf-ole2-olereggetusertype?branch=master). If the object's class is not found in the registry, the user type from the object's [**IStorage**](https://msdn.microsoft.com/library/windows/desktop/aa380015) instance is returned. If the class is not found in the object's **IStorage** instance, the string "Unknown" is returned.

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 




