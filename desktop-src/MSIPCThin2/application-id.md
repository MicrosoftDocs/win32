---
title: How to Get an Azure Application ID
description: Creating an RMS-enabled app with the Rights Management SDK 4.2 requires you to create an agreement with the RMS Team.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: CF0FE9DC-BC91-4018-B28D-2DB293A3EAA2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to: Get an Azure Application ID

Creating an RMS-enabled app with the Rights Management SDK 4.2 requires you to create an agreement with the RMS Team.

## Overview

Creating and releasing an RMS-enabled app with the RMS SDK 4.2 requires you to also create a services usage agreement with the RMS Team. This agreement, also known as a Rights Management License Agreement (RMLA), guides you in honoring the contract for content protection that you will be upholding on behalf of the user and/or content owner by the behaviors (adherence to business rules) of your app. As a creator of an RMS-enable app, your contract with the RMS Team will be enforced by the existence of an "Azure Application ID" that represents this agreement and enables your app to connect to the Azure AD Authentication Service.

## Process

Use the following steps to create your app Id and sign your usage agreement with the RMS Team.

-   Follow the guidance in the topic, [How to create an App ID on Azure](https://msdn.microsoft.com/library/azure/dn132599.aspx) to create your app Id.
-   Write to the RMS Team to initiate your RMLA process, sending your "App ID" to <askipteam@microsoft.com>.
-   Sign the RMLA and return it to the RMS Team.
-   Now that you have a signed RMLA you should pass the Application ID when calling the authentication library through the *clientID* parameter.

    This is what the authentication call looks like in our [iOS/OS X code examples](ios-os-x-code-examples.md) topic.

    ```
    // Retrieve token using ADAL
        [context acquireTokenWithResource:authenticationParameters.resource
                                 clientId:appClientId
                              redirectUri:redirectURI
                                   userId:authenticationParameters.userId
                          completionBlock:^(ADAuthenticationResult *result)
    ```

    

> [!Note]  
> If the RMS Team does not receive your signed RMLA within 60 days, your app will be blocked from authenticating with the Azure Authentication System.

 

 

 




