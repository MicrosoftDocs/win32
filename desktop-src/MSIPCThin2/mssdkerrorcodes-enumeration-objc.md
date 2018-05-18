---
title: MSSdkErrorCodes enum
description: Defines the error codes that can be returned.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '670bbd6a-6191-40bd-8885-19328c86d4a6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSSdkErrorCodes enum"]
topic_type:
- apiref
api_name:
- MSSdkErrorCodes enum
api_type:
- NA
---

# MSSdkErrorCodes enum

Defines the error codes that can be returned.

## Signature

``` syntax
typedef uint32_t MSSdkErrorCodes;
```

## Members



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SDK_ERROR_GENERAL</strong><br/></td>
<td>-1<br/></td>
<td>The Security Token Service (STS) fails to accept a token or to issue a token for the REST service. An internal consumption related error; for example, formatting errors in JSON responses, publish license parsing, encryption initialization and template retrieval.<br/> When this error is encountered you will be prompted, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.<br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_COMMUNICATION</strong><br/></td>
<td>-2<br/></td>
<td>The device has no connection to the network.<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_DEVICE_REJECTED</strong> <br/></td>
<td>-3<br/></td>
<td>The device is blocked from using RMS services.<br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_NO_CONSUMPTION_RIGHTS</strong><br/></td>
<td>-4<br/></td>
<td>The user doesn't have consumption rights over the content.<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_UNSUPPORTED_SDK_VERSION</strong><br/></td>
<td>-5<br/></td>
<td>The SDK that is being used by the app is not supported.<br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_SERVICE_NOT_AVAILABLE</strong><br/></td>
<td>-6<br/></td>
<td>The Rights Management Service is temporarily unable to answer.<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_INVALID_PL</strong><br/></td>
<td>-7<br/></td>
<td>The publish license provided is not valid.<br/> When this error is encountered you will be prompted, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.<br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_ONPREM_SERVERS_NOT_SUPPORTED</strong><br/></td>
<td>-8<br/></td>
<td>Your local AD RMS server does not support your device so, this content can not be decrypted.<br/> Contact your administrator for more information.<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_REST_SERVICE_NOT_ENABLED</strong><br/></td>
<td>-9<br/></td>
<td>Azure AD Rights Management is not enabled for your organization.<br/> Contact your administrator for further details.<br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_NO_PUBLISHING_RIGHTS</strong><br/></td>
<td>-10<br/></td>
<td>You do not have permission to create new protected content for this organization.<br/> Try signing in as a different user, or contacting your administrator for additional permissions.&quot;;<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_PUBLISHING_LICENSE_EXPIRED</strong><br/></td>
<td>-11<br/></td>
<td>You can not view this content because the time limit has ended.<br/> Contact the content owner or your administrator to renew this content.<br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_INVALID_SSL_CERTIFICATE</strong> <br/></td>
<td>-12<br/></td>
<td>User message: &quot;There is a problem with the service's security certificate, which may indicate an attempt to fool you or intercept any data you send to the server. If the problem continues, contact your administrator.&quot;<br/> This error occurs when the AD RMS server’s SSL certificate is incorrect or cannot be trusted by the device (e.g. no equivalent root CA on the device)<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_NOT_AVAILABLE_IN_OFFLINE_MODE</strong><br/></td>
<td>-13<br/></td>
<td>User messgage: &quot;You can't view this content without internet connection. Please check your connection before trying again and that your app is not working in offline mode.&quot;<br/> This error occurs when the application asked the SDK to consume content with offline access only but no cached policy (i.e. EUL) was found, thus application must request online access from the SDK.
<blockquote>
[!Note]<br />
In case the 3rd party application does not handle this scenario, the error message will be confusing to the user, which might have internet connection but can’t access the content.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_USER_CANCELLED</strong><br/></td>
<td>-14<br/></td>
<td>The user has canceled the consent process.<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_INVALID_PARAMETER</strong><br/></td>
<td>-1000<br/></td>
<td>Invalid input. This error is mainly for developer convenience and is not meant for the user.<br/> When this error is encountered you will be prompted, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.<br/></td>
</tr>
<tr class="even">
<td><strong>SDK_ERROR_AUTH_FAILED_BAD_TOKEN</strong><br/></td>
<td>-2000<br/></td>
<td>Authentication failed, bad access token.<br/></td>
</tr>
<tr class="odd">
<td><strong>SDK_ERROR_AUTHENTICATION_BUSY</strong><br/></td>
<td>-3000<br/></td>
<td>The system detects that you are already attempting to sign in.<br/> Complete your previous attempt before trying again.<br/></td>
</tr>
</tbody>
</table>



 

## Defined in

MSSDKErrorCodes.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





