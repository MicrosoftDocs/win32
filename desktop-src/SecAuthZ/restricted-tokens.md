---
description: A restricted token is a primary or impersonation access token that has been modified by the CreateRestrictedToken function.
ms.assetid: 06580ab9-ff58-4aa9-bf88-9536a2e1981d
title: Restricted Tokens
ms.topic: article
ms.date: 05/31/2018
---

# Restricted Tokens

A restricted token is a [*primary*](/windows/desktop/SecGloss/p-gly) or impersonation [*access token*](/windows/desktop/SecGloss/a-gly) that has been modified by the [**CreateRestrictedToken**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken) function. A [*process*](/windows/desktop/SecGloss/p-gly) or impersonating thread running in the [*security context*](/windows/desktop/SecGloss/s-gly) of a restricted token is restricted in its ability to access securable objects or perform privileged operations. The **CreateRestrictedToken** function can restrict a token in the following ways:

-   Remove [privileges](privileges.md) from the token.
-   Apply the deny-only attribute to SIDs in the token so that they cannot be used to access secured objects. For more information about the deny-only attribute, see [SID Attributes in an Access Token](sid-attributes-in-an-access-token.md).
-   Specify a list of restricting SIDs, which can limit access to securable objects.

The system uses the list of restricting SIDs when it checks the token's access to a securable object. When a restricted process or thread tries to access a securable object, the system performs two access checks: one using the token's enabled SIDs, and another using the list of restricting SIDs. Access is granted only if both access checks allow the requested access rights. For more information about access checks, see [How DACLs Control Access to an Object](how-dacls-control-access-to-an-object.md).

You can use a restricted [*primary token*](/windows/desktop/SecGloss/p-gly) in a call to the [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function. Typically, the process that calls **CreateProcessAsUser** must have the SE\_ASSIGNPRIMARYTOKEN\_NAME privilege, which is usually held only by system code or by services running in the LocalSystem account. However, if the **CreateProcessAsUser** call specifies a restricted version of the caller's primary token, this privilege is not required. This enables ordinary applications to create restricted processes.

You can also use a restricted primary or [*impersonation token*](/windows/desktop/SecGloss/i-gly) in the [**ImpersonateLoggedOnUser**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateloggedonuser) function.

To determine whether a token has a list of restricting SIDs, call the [**IsTokenRestricted**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-istokenrestricted) function.

> [!Note]  
> Applications that use restricted tokens should run the restricted application on desktops other than the default desktop. This is necessary to prevent an attack by a restricted application, using **SendMessage** or **PostMessage**, to unrestricted applications on the default desktop. If necessary, switch between desktops for your application purposes.

 

 

 
