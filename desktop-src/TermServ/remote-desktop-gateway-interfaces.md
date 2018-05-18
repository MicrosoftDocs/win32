---
title: Remote Desktop Gateway Interfaces
description: The Remote Desktop Gateway (RD Gateway) API supports the following interfaces. You can use these interfaces to implement plug-ins that provide customized authentication and authorization.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a457574a-d856-4490-b20d-48343a82acff'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Remote Desktop Gateway Interfaces

The Remote Desktop Gateway (RD Gateway) API supports the following interfaces. You can use these interfaces to implement plug-ins that provide customized authentication and authorization. There is no dependency between the authentication plug-in and the authorization plug-in, and you can implement only a single plug-in if you choose.

The authentication plug-ins are [**ITSGAuthenticateUserSink**](itsgauthenticateusersink.md) and [**ITSGAuthenticationEngine**](itsgauthenticationengine.md).

The authorization plug-ins are [**ITSGAccountingEngine**](itsgaccountingengine.md), [**ITSGAuthorizeConnectionSink**](itsgauthorizeconnectionsink.md), [**ITSGAuthorizeResourceSink**](itsgauthorizeresourcesink.md), and [**ITSGPolicyEngine**](itsgpolicyengine.md).

## In this section

<dl> <dt>

[**ITSGAccountingEngine**](itsgaccountingengine.md)
</dt> <dd>

Exposes methods that provide information about the creation or closing of sessions for a connection.

</dd> <dt>

[**ITSGAuthenticateUserSink**](itsgauthenticateusersink.md)
</dt> <dd>

Exposes methods that notify RD Gateway about authentication events.

</dd> <dt>

[**ITSGAuthenticationEngine**](itsgauthenticationengine.md)
</dt> <dd>

Exposes methods that authenticate users for RD Gateway.

</dd> <dt>

[**ITSGAuthorizeConnectionSink**](itsgauthorizeconnectionsink.md)
</dt> <dd>

Exposes methods that notify RD Gateway about the result of an attempt to authorize a connection.

</dd> <dt>

[**ITSGAuthorizeResourceSink**](itsgauthorizeresourcesink.md)
</dt> <dd>

Exposes methods that notify RD Gateway about the result of an attempt to authorize a resource.

</dd> <dt>

[**ITSGPolicyEngine**](itsgpolicyengine.md)
</dt> <dd>

Exposes methods that authorize connections and resources.

</dd> </dl>

 

 




