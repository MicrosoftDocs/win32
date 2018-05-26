---
title: Remote Desktop Gateway Interfaces
description: The Remote Desktop Gateway (RD Gateway) API supports the following interfaces. You can use these interfaces to implement plug-ins that provide customized authentication and authorization.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a457574a-d856-4490-b20d-48343a82acff
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Gateway Interfaces

The Remote Desktop Gateway (RD Gateway) API supports the following interfaces. You can use these interfaces to implement plug-ins that provide customized authentication and authorization. There is no dependency between the authentication plug-in and the authorization plug-in, and you can implement only a single plug-in if you choose.

The authentication plug-ins are [**ITSGAuthenticateUserSink**](/windows/win32/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticateusersink?branch=master) and [**ITSGAuthenticationEngine**](/windows/win32/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticationengine?branch=master).

The authorization plug-ins are [**ITSGAccountingEngine**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgaccountingengine?branch=master), [**ITSGAuthorizeConnectionSink**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeconnectionsink?branch=master), [**ITSGAuthorizeResourceSink**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeresourcesink?branch=master), and [**ITSGPolicyEngine**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgpolicyengine?branch=master).

## In this section

<dl> <dt>

[**ITSGAccountingEngine**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgaccountingengine?branch=master)
</dt> <dd>

Exposes methods that provide information about the creation or closing of sessions for a connection.

</dd> <dt>

[**ITSGAuthenticateUserSink**](/windows/win32/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticateusersink?branch=master)
</dt> <dd>

Exposes methods that notify RD Gateway about authentication events.

</dd> <dt>

[**ITSGAuthenticationEngine**](/windows/win32/TSGAuthenticationEngine/nn-tsgauthenticationengine-itsgauthenticationengine?branch=master)
</dt> <dd>

Exposes methods that authenticate users for RD Gateway.

</dd> <dt>

[**ITSGAuthorizeConnectionSink**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeconnectionsink?branch=master)
</dt> <dd>

Exposes methods that notify RD Gateway about the result of an attempt to authorize a connection.

</dd> <dt>

[**ITSGAuthorizeResourceSink**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgauthorizeresourcesink?branch=master)
</dt> <dd>

Exposes methods that notify RD Gateway about the result of an attempt to authorize a resource.

</dd> <dt>

[**ITSGPolicyEngine**](/windows/win32/TSGPolicyEngine/nn-tsgpolicyengine-itsgpolicyengine?branch=master)
</dt> <dd>

Exposes methods that authorize connections and resources.

</dd> </dl>

 

 




