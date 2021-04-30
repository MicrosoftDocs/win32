---
description: An objects owner implicitly has WRITE\_DAC access to the object. This means that the owner can modify the objects discretionary access control list (DACL), and thus, can control access to the object.
ms.assetid: 16144f38-3416-4594-b5e4-ca84fcbdddc9
title: Owner of a New Object
ms.topic: article
ms.date: 05/31/2018
---

# Owner of a New Object

An object's owner implicitly has WRITE\_DAC access to the object. This means that the owner can modify the object's [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL), and thus, can control access to the object.

The owner of a new object is the default owner [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) from the [*primary*](/windows/desktop/SecGloss/p-gly) or [*impersonation token*](/windows/desktop/SecGloss/i-gly) of the creating [*process*](/windows/desktop/SecGloss/p-gly). To get or set the default owner in an [*access token*](/windows/desktop/SecGloss/a-gly), call the [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) or [**SetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-settokeninformation) function with the [**TOKEN\_OWNER**](/windows/desktop/api/Winnt/ns-winnt-token_owner) structure. The system does not allow you to set a token's default owner to a SID that is not valid, such as the SID of another user's account.

A process with the SE\_TAKE\_OWNERSHIP privilege enabled can set itself as the owner of an object. A process with the SE\_RESTORE\_NAME privilege enabled or with WRITE\_OWNER access to the object can set any valid user or group SID as the owner of an object.

 

 
