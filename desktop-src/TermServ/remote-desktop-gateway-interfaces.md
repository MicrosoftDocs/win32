---
title: Remote Desktop Gateway Interfaces
description: The Remote Desktop Gateway (RD Gateway) API supports the following interfaces. You can use these interfaces to implement plug-ins that provide customized authentication and authorization.
ms.assetid: a457574a-d856-4490-b20d-48343a82acff
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Gateway Interfaces

The Remote Desktop Gateway (RD Gateway) API supports the following interfaces. You can use these interfaces to implement plug-ins that provide customized authentication and authorization. There is no dependency between the authentication plug-in and the authorization plug-in, and you can implement only a single plug-in if you choose.

The authentication plug-ins are [**ITSGAuthenticateUserSink**](/windows/desktop/api/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticateusersink) and [**ITSGAuthenticationEngine**](/windows/desktop/api/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticationengine).

The authorization plug-ins are [**ITSGAccountingEngine**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgaccountingengine), [**ITSGAuthorizeConnectionSink**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeconnectionsink), [**ITSGAuthorizeResourceSink**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeresourcesink), and [**ITSGPolicyEngine**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgpolicyengine).

## In this section

<dl> <dt>

[**ITSGAccountingEngine**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgaccountingengine)
</dt> <dd>

Exposes methods that provide information about the creation or closing of sessions for a connection.

</dd> <dt>

[**ITSGAuthenticateUserSink**](/windows/desktop/api/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticateusersink)
</dt> <dd>

Exposes methods that notify RD Gateway about authentication events.

</dd> <dt>

[**ITSGAuthenticationEngine**](/windows/desktop/api/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticationengine)
</dt> <dd>

Exposes methods that authenticate users for RD Gateway.

</dd> <dt>

[**ITSGAuthorizeConnectionSink**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeconnectionsink)
</dt> <dd>

Exposes methods that notify RD Gateway about the result of an attempt to authorize a connection.

</dd> <dt>

[**ITSGAuthorizeResourceSink**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeresourcesink)
</dt> <dd>

Exposes methods that notify RD Gateway about the result of an attempt to authorize a resource.

</dd> <dt>

[**ITSGPolicyEngine**](/windows/desktop/api/TSGPolicyEngine/nn-tsgpolicyengine-itsgpolicyengine)
</dt> <dd>

Exposes methods that authorize connections and resources.

</dd> </dl>

 

 




