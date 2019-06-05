---
Description: A null DACL grants full access to any user that requests it. An empty DACL is a properly allocated and initialized DACL that contains no access control entries. An empty DACL grants no access to the object it is assigned to.
ms.assetid: 26e5c98d-bbdc-4f9f-96e0-18d1c429f1e6
title: Null DACLs and Empty DACLs
ms.topic: article
ms.date: 05/31/2018
---

# Null DACLs and Empty DACLs

If the [*discretionary access control list*](https://docs.microsoft.com/windows/desktop/SecGloss/d-gly) (DACL) that belongs to an object's [*security descriptor*](https://docs.microsoft.com/windows/desktop/SecGloss/s-gly) is set to **NULL**, a null DACL is created. A null DACL grants full access to any user that requests it; normal security checking is not performed with respect to the object. A null DACL should not be confused with an empty DACL. An empty DACL is a properly allocated and initialized DACL that contains no [*access control entries*](https://docs.microsoft.com/windows/desktop/SecGloss/a-gly) (ACEs). An empty DACL grants no access to the object it is assigned to.

For an example of how to create a DACL, see [Creating a DACL](https://docs.microsoft.com/windows/desktop/SecBP/creating-a-dacl).

 

 



