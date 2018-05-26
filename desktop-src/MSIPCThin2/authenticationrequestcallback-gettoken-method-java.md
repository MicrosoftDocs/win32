---
title: AuthenticationRequestCallback.getToken method
description: Gets the token.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7CCFA55A-E9E0-43EF-86A2-ED5B9933C3A3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- AuthenticationRequestCallback.getToken method
topic_type:
- apiref
api_name:
- AuthenticationRequestCallback.getToken method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AuthenticationRequestCallback.getToken method

Gets the token. This method is invoked by the SDK whenever an authentication is required to complete an operation. The app developer will be given the authentication parameters that can be used to acquire the access token via a separate authentication library.

We recommend that you use the [Azure AD Authentication Library (ADAL)](https://msdn.microsoft.com/library/jj573266.aspx). However, other authentication libraries that support OAuth 2.0 can be used as well. For more information, see the *Prerequisites* section in the [Android Apps](android-sdk.md) topic under [Get started](get-started.md).

## Signature

``` syntax
public void getToken(Map<String, String> authenticationParameters,
                         AuthenticationCompletionCallback authenticationCompletionCallback);
```

## Parameters



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Datatype</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>authenticationParameters</em><br/></td>
<td><strong>Map</strong>&lt;<strong>String</strong>, <strong>String</strong>&gt;<br/></td>
<td>the authentication parameters as key value pairs.<br/>
<pre class="syntax" data-space="preserve"><code>{
  (&quot;oauth2.authority&quot;, &quot;https://login.windows.net/common/oauth2/token&quot;), 
  (&quot;oauth2.resource&quot;, &quot;api.aadrm.com&quot;),
  (&quot;oauth2.scope&quot; : &quot;the scope&quot;), 
  (&quot;userId&quot; : &quot;the user Id&quot;)
}</code></pre></td>
</tr>
<tr class="even">
<td><em>authenticationCompletionCallback</em><br/></td>
<td>[<strong>AuthenticationCompletionCallback</strong>](authenticationcompletioncallback-interface-java.md)<br/></td>
<td>the completion block to put the async result<br/></td>
</tr>
</tbody>
</table>



 

## Defined in

AuthenticaionRequestCallback.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





