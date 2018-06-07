---
Description: When you open a handle to an object, the returned handle has some combination of access rights to the object.
ms.assetid: 581de4ba-0f90-42d7-b7db-1324d42595e2
title: Requesting Access Rights to an Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Requesting Access Rights to an Object

When you open a handle to an object, the returned handle has some combination of access rights to the object. Some functions, such as [**CreateSemaphore**](https://msdn.microsoft.com/library/windows/desktop/ms682438), do not require a specific set of requested access rights. These functions always try to open the handle for full access. Other functions, such as [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) and [**OpenProcess**](https://msdn.microsoft.com/library/windows/desktop/ms684320), allow you to specify the set of access rights that you want. You should request only the access rights that you need, rather than opening a handle for full access. This prevents using the handle in an unintended way, and increases the chances that the access request will succeed if the object's DACL only allows limited access.

Use [generic access rights](generic-access-rights.md) to specify the type of access needed when opening a handle to an object. This is typically simpler than specifying all the corresponding standard and specific rights. Alternatively, use the MAXIMUM\_ALLOWED constant to request that the object be opened with all the access rights that are valid for the caller.

> [!Note]  
> The MAXIMUM\_ALLOWED constant cannot be used in an ACE.

 

To get or set the SACL in an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly), request the [ACCESS\_SYSTEM\_SECURITY access right](sacl-access-right.md) when opening a handle to the object.

 

 



