---
description: Server-Side Requirements for Impersonation
ms.assetid: f6128688-dfd8-40ff-83ec-99d740b9152c
title: Server-Side Requirements for Impersonation
ms.topic: article
ms.date: 05/31/2018
---

# Server-Side Requirements for Impersonation

The server performs impersonation programmatically. It explicitly assumes the client's security credentials by using [**CoImpersonateClient**](/windows/desktop/api/combaseapi/nf-combaseapi-coimpersonateclient). When the client has granted the server sufficient authority, this has the effect of substituting the client's security credentials with the server thread token, in place of the process token.

When this has been done, the server can, for example, use the client token to access resources guarded with a security descriptor. Or it can make calls under the client identity, if cloaking is enabled.

The server can explicitly set cloaking programmatically, or it can rely on an administrative setting. By default, COM+ applications are configured to use dynamic cloaking. For more detail, see [Cloaking](cloaking.md).

If the server is implementing delegation on behalf of the client—using the client identity over network—the server process identity must be marked as "Trusted for delegation" in the Active Directory Service; otherwise, delegation will fail.

When it has finished using the client's identity, the server can revert to its own process token using [**CoRevertToSelf**](/windows/desktop/api/combaseapi/nf-combaseapi-coreverttoself).

For details on implementing impersonation and delegation, see [Delegation and Impersonation](/windows/desktop/com/delegation-and-impersonation).

## Related topics

<dl> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Client-Side Requirements for Impersonation](client-side-requirements-for-impersonation.md)
</dt> <dt>

[Cloaking](cloaking.md)
</dt> </dl>

 

 
