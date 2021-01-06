---
description: Client-Side Requirements for Impersonation
ms.assetid: c2d20233-93c6-4d2d-946d-8abccbeb3c5e
title: Client-Side Requirements for Impersonation
ms.topic: article
ms.date: 05/31/2018
---

# Client-Side Requirements for Impersonation

The following two settings can be specified relative to impersonation on the client side:

-   Impersonation level, which indicates the client's willingness to have the server use its identity.
-   A setting in the Active Directory Service through which the client account can be marked "Account is sensitive and cannot be delegated," which will disable delegation.

The impersonation level can be set in a variety of ways. If the client does not indicate an impersonation level, the machine-wide default will be used by COM. The machine-wide default can be set using either the Component Services administrative tool or Dcomcnfg.exe. The client can also indicate a preferred impersonation level administratively with Dcomcnfg.exe.

The client can indicate the impersonation level programmatically, using either [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket)—equivalent to [**IClientSecurity::SetBlanket**](/windows/desktop/api/objidl/nf-objidl-iclientsecurity-setblanket), which can be called as often as necessary—or [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity), which can be called once per process.

If the client indicates delegate-level impersonation—the broadest authority it can grant to the server—the client should be running under an identity that is properly configured in the Active Directory Service to enable its identity to be delegated.

For more detail regarding impersonation levels and the requirements for delegation to work, see [Delegation and Impersonation](/windows/desktop/com/delegation-and-impersonation).

COM+ applications can always act as clients, of course. When the COM+ application makes a call to another application or resource, it expresses an impersonation level. For COM+ server applications, you can set an impersonation level administratively. COM+ library applications cannot set their own impersonation level; they use that of the host process instead. To learn how to set impersonation for a COM+ application, see [Setting an Impersonation Level](setting-an-impersonation-level.md).

## Related topics

<dl> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Cloaking](cloaking.md)
</dt> <dt>

[Server-Side Requirements for Impersonation](server-side-requirements-for-impersonation.md)
</dt> </dl>

 

 
