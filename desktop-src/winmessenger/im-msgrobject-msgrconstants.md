---
title: MSGRConstants enumeration
description: Do not use.
ms.assetid: c7cf3d42-85ba-47ed-a28c-39abff8e6a70
keywords:
- MSGRConstants enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Mdisp.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSGRConstants enumeration

\[**MSGRConstants** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The following are constants used for error or success returns of methods and properties of the Windows Messenger APIs.

> [!Note]  
> The **MSGRConstants** enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**MSGRConstants**](im-msgrconstants.md) instead.

 

## Syntax


```C++
typedef enum  { 
  MSGR_E_CONNECT                             = MSGR_E(0x0001),
  MSGR_E_INVALID_SERVER_NAME                 = MSGR_E(0x0002),
  MSGR_E_INVALID_PASSWORD                    = MSGR_E(0x0003),
  MSGR_E_ALREADY_LOGGED_ON                   = MSGR_E(0x0004),
  MSGR_E_SERVER_VERSION                      = MSGR_E(0x0005),
  MSGR_E_LOGON_TIMEOUT                       = MSGR_E(0x0006),
  MSGR_E_LIST_FULL                           = MSGR_E(0x0007),
  MSGR_E_AI_REJECT                           = MSGR_E(0x0008),
  MSGR_E_AI_REJECT_NOT_INST                  = MSGR_E(0x0009),
  MSGR_E_USER_NOT_FOUND                      = MSGR_E(0x000A),
  MSGR_E_ALREADY_IN_LIST                     = MSGR_E(0x000B),
  MSGR_E_DISCONNECTED                        = MSGR_E(0x000C),
  MSGR_E_UNEXPECTED                          = MSGR_E(0x000D),
  MSGR_E_SERVER_TOO_BUSY                     = MSGR_E(0x000E),
  MSGR_E_INVALID_AUTH_PACKAGES               = MSGR_E(0x000F),
  MSGR_E_NEWER_CLIENT_AVAILABLE              = MSGR_E(0x0010),
  MSGR_E_AI_TIMEOUT                          = MSGR_E(0x0011),
  MSGR_E_CANCEL                              = MSGR_E(0x0012),
  MSGR_E_TOO_MANY_MATCHES                    = MSGR_E(0x0013),
  MSGR_E_SERVER_UNAVAILABLE                  = MSGR_E(0x0014),
  MSGR_E_LOGON_UI_ACTIVE                     = MSGR_E(0x0015),
  MSGR_E_OPTION_UI_ACTIVE                    = MSGR_E(0x0016),
  MSGR_E_CONTACT_UI_ACTIVE                   = MSGR_E(0x0017),
  MSGR_E_PRIMARY_SERVICE_NOT_LOGGED_ON       = MSGR_E(0x0018),
  MSGR_E_LOGGED_ON                           = MSGR_E(0x0019),
  MSGR_E_CONNECT_PROXY                       = MSGR_E(0x001A),
  MSGR_E_PROXY_AUTH                          = MSGR_E(0x001B),
  MSGR_E_PROXY_AUTH_TYPE                     = MSGR_E(0x001C),
  MSGR_E_INVALID_PROXY_NAME                  = MSGR_E(0x001D),
  MSGR_E_NOT_LOGGED_ON                       = MSGR_E(0x001E),
  MSGR_E_NOT_PRIMARY_SERVICE                 = MSGR_E(0x0020),
  MSGR_E_TOO_MANY_SESSIONS                   = MSGR_E(0x0021),
  MSGR_E_TOO_MANY_MESSAGES                   = MSGR_E(0x0022),
  MSGR_E_REMOTE_LOGIN                        = MSGR_E(0x0023),
  MSGR_E_INVALID_FRIENDLY_NAME               = MSGR_E(0x0024),
  MSGR_E_SESSION_FULL                        = MSGR_E(0x0025),
  MSGR_E_NOT_ALLOWING_NEW_USERS              = MSGR_E(0x0026),
  MSGR_E_INVALID_DOMAIN                      = MSGR_E(0x0027),
  MSGR_E_TCP_ERROR                           = MSGR_E(0x0028),
  MSGR_E_SESSION_TIMEOUT                     = MSGR_E(0x0029),
  MSGR_E_MULTIPOINT_SESSION_BEGIN_TIMEOUT    = MSGR_E(0x002a),
  MSGR_E_MULTIPOINT_SESSION_END_TIMEOUT      = MSGR_E(0x002b),
  MSGR_E_REVERSE_LIST_FULL                   = MSGR_E(0x002c),
  MSGR_E_SERVER_ERROR                        = MSGR_E(0x002d),
  MSGR_E_SYSTEM_CONFIG                       = MSGR_E(0x002e),
  MSGR_E_NO_DIRECTORY                        = MSGR_E(0x002f),
  MSGR_E_RETRY_SET                           = MSGR_E(0x0030),
  MSGR_E_CHILD_WITHOUT_CONSENT               = MSGR_E(0x0031),
  MSGR_E_USER_CANCELLED                      = MSGR_E(0x0032),
  MSGR_E_CANCEL_BEFORE_CONNECT               = MSGR_E(0x0033),
  MSGR_E_VOICE_IM_TIMEOUT                    = MSGR_E(0x0034),
  MSGR_E_NOT_ACCEPTING_PAGES                 = MSGR_E(0x0035),
  MSGR_E_EMAIL_PASSPORT_NOT_VALIDATED        = MSGR_E(0x0036),
  MSGR_E_AUDIO_UI_ACTIVE                     = MSGR_E(0x0037),
  MSGR_E_NO_HARDWARE                         = MSGR_E(0x0038),
  MSGR_E_PAGING_UNAVAILABLE                  = MSGR_E(0x0039),
  MSGR_E_PHONE_INVALID_NUMBER                = MSGR_E(0x003a),
  MSGR_E_PHONE_NO_FUNDS                      = MSGR_E(0x003b),
  MSGR_E_VOICE_NO_ANSWER                     = MSGR_E(0x003c),
  MSGR_E_VOICE_WAVEIN_DEVICE                 = MSGR_E(0x003d),
  MSGR_E_FT_TIMEOUT                          = MSGR_E(0x003e),
  MSGR_E_MESSAGE_TOO_LONG                    = MSGR_E(0x003f),
  MSGR_E_VOICE_FIREWALL                      = MSGR_E(0x0040),
  MSGR_E_VOICE_NETCONN                       = MSGR_E(0x0041),
  MSGR_E_PHONE_CIRCUITS_BUSY                 = MSGR_E(0x0042),
  MSGR_E_SERVER_PROTOCOL                     = MSGR_E(0x0043),
  MSGR_E_UNAVAILABLE_VIA_HTTP                = MSGR_E(0x0044),
  MSGR_E_PHONE_INVALID_PIN                   = MSGR_E(0x0045),
  MSGR_E_PHONE_PINPROCEED_TIMEOUT            = MSGR_E(0x0046),
  MSGR_E_SERVER_SHUTDOWN                     = MSGR_E(0x0047),
  MSGR_E_CLIENT_DISALLOWED                   = MSGR_E(0x0048),
  MSGR_E_PHONE_CALL_NOT_COMPLETE             = MSGR_E(0x0049),
  MSGR_E_GROUPS_NOT_ENABLED                  = MSGR_E(0x004a),
  MSGR_E_GROUP_ALREADY_EXISTS                = MSGR_E(0x004b),
  MSGR_E_TOO_MANY_GROUPS                     = MSGR_E(0x004c),
  MSGR_E_GROUP_DOES_NOT_EXIST                = MSGR_E(0x004d),
  MSGR_E_USER_NOT_GROUP_MEMBER               = MSGR_E(0x004e),
  MSGR_E_GROUP_NAME_TOO_LONG                 = MSGR_E(0x004f),
  MSGR_E_GROUP_NOT_EMPTY                     = MSGR_E(0x0050),
  MSGR_E_BAD_GROUP_NAME                      = MSGR_E(0x0051),
  MSGR_E_PHONESERVICE_UNAVAILABLE            = MSGR_E(0x0052),
  MSGR_E_CANNOT_RENAME                       = MSGR_E(0x0053),
  MSGR_E_CANNOT_DELETE                       = MSGR_E(0x0054),
  MSGR_E_INVALID_SERVICE                     = MSGR_E(0x0055),
  MSGR_E_POLICY_RESTRICTED                   = MSGR_E(0x0056),
  MSGR_E_BUSY                                = MSGR_E(0x0057),
  MSGR_E_DNS_SRV_FAIL                        = MSGR_E(0x0058),
  MSGR_E_DNS_A_RES_FAIL                      = MSGR_E(0x0059),
  MSGR_E_NO_SERVER_ADDRESS_SPECIFIED         = MSGR_E(0x0060),
  MSGR_E_TLS_FAIL                            = MSGR_E(0x0061),
  MSGR_E_INCOMPATIBLE_ENCRYPTION             = MSGR_E(0x0062),
  MSGR_E_SSL_TUNNEL_FAILED                   = MSGR_E(0x0063),
  MSGR_E_SIP_TIMEOUT                         = MSGR_E(0x0064),
  MSGR_E_INCOMPATIBLE_IM                     = MSGR_E(0x0065),
  MSGR_E_MIM_ADD_TO_CONTACTS_FAIL            = MSGR_E(0x0066),
  MSGR_E_INVALID_ADDRESS_FORMAT              = MSGR_E(0x0067),
  MSGR_E_INVALID_CERTIFICATE                 = MSGR_E(0x0068),
  MSGR_E_AUTH_TIME_SKEW                      = MSGR_E(0x0069),
  MSGR_E_CHANGED_CREDENTIALS                 = MSGR_E(0x0070),
  MSGR_E_SIP_LOGIN_FORBIDDEN                 = MSGR_E(0x0071),
  MSGR_E_SIP_HIGH_SECURITY_SET_TLS           = MSGR_E(0x0072),
  MSGR_E_CALLEE_INSUFFICIENT_SECURITY_LEVEL  = MSGR_E(0x0073),
  MSGR_E_CALLER_PEER2PEER_CALLS_NOT_ALLOWED  = MSGR_E(0x0074),
  MSGR_E_SIP_UDP_UNSUPPORTED                 = MSGR_E(0x0075),
  MSGR_E_SIP_SEARCH_FORBIDDEN                = MSGR_E(0x0076),
  MSGR_E_SESSION_RESTRICTED                  = MSGR_E(0x0080),
  MSGR_E_MANAGED_USER_INVALID_CVR            = MSGR_E(0x0081),
  MSGR_E_RESTRICTED_USER                     = MSGR_E(0x0082),
  MSGR_E_PROXY_AUTH_REQUIRED                 = MSGR_E(0x0083),
  MSGR_E_PROXY_REALM_MISMATCH                = MSGR_E(0x0084),
  MSGR_E_PROXY_PASSWORD_INCORRECT            = MSGR_E(0x0085),
  MSGR_E_RESTRICTED_USER_LOGON_RESTRICED     = MSGR_E(0x0086),
  MSGR_E_IE_OFFLINE                          = MSGR_E(0x0086),
  MSGR_E_IE_CANT_CONNECT                     = MSGR_E(0x0088),
  MSGR_S_ALREADY_IN_THE_MODE                 = MSGR_S(0x0001),
  MSGR_S_TRANSFER_SEND_BEGUN                 = MSGR_S(0x0002),
  MSGR_S_TRANSFER_SEND_FINISHED              = MSGR_S(0x0003),
  MSGR_S_TRANSFER_RECEIVE_BEGUN              = MSGR_S(0x0004),
  MSGR_S_TRANSFER_RECEIVE_FINISHED           = MSGR_S(0x0005),
  MSGR_S_GROUP_ALREADY_EXISTS                = MSGR_S(0x0006),
  MSGR_E_FAIL                                = E_FAIL,
  MSGR_S_OK                                  = S_OK
} LockError;
```



## Constants

<dl> <dt>

<span id="MSGR_E_CONNECT"></span><span id="msgr_e_connect"></span>**MSGR\_E\_CONNECT**
</dt> <dd>

Error connecting to the server.

</dd> <dt>

<span id="MSGR_E_INVALID_SERVER_NAME"></span><span id="msgr_e_invalid_server_name"></span>**MSGR\_E\_INVALID\_SERVER\_NAME**
</dt> <dd>

Name of the server that the client is trying to connect to is invalid.

</dd> <dt>

<span id="MSGR_E_INVALID_PASSWORD"></span><span id="msgr_e_invalid_password"></span>**MSGR\_E\_INVALID\_PASSWORD**
</dt> <dd>

Password specified for the user is invalid.

</dd> <dt>

<span id="MSGR_E_ALREADY_LOGGED_ON"></span><span id="msgr_e_already_logged_on"></span>**MSGR\_E\_ALREADY\_LOGGED\_ON**
</dt> <dd>

Attempt to log on when the user is already signed in.

</dd> <dt>

<span id="MSGR_E_SERVER_VERSION"></span><span id="msgr_e_server_version"></span>**MSGR\_E\_SERVER\_VERSION**
</dt> <dd>

Version of the server that the client is trying to connect to is incompatible.

</dd> <dt>

<span id="MSGR_E_LOGON_TIMEOUT"></span><span id="msgr_e_logon_timeout"></span>**MSGR\_E\_LOGON\_TIMEOUT**
</dt> <dd>

Attempt to sign in timed out.

</dd> <dt>

<span id="MSGR_E_LIST_FULL"></span><span id="msgr_e_list_full"></span>**MSGR\_E\_LIST\_FULL**
</dt> <dd>

Contact list is full or has reached the maximum limit.

</dd> <dt>

<span id="MSGR_E_AI_REJECT"></span><span id="msgr_e_ai_reject"></span>**MSGR\_E\_AI\_REJECT**
</dt> <dd>

Internal use only. This error code is never returned to a user.

</dd> <dt>

<span id="MSGR_E_AI_REJECT_NOT_INST"></span><span id="msgr_e_ai_reject_not_inst"></span>**MSGR\_E\_AI\_REJECT\_NOT\_INST**
</dt> <dd>

Internal use only. This error code is never returned to a user.

</dd> <dt>

<span id="MSGR_E_USER_NOT_FOUND"></span><span id="msgr_e_user_not_found"></span>**MSGR\_E\_USER\_NOT\_FOUND**
</dt> <dd>

Specified user is not found on the specified service.

</dd> <dt>

<span id="MSGR_E_ALREADY_IN_LIST"></span><span id="msgr_e_already_in_list"></span>**MSGR\_E\_ALREADY\_IN\_LIST**
</dt> <dd>

Attempt to add a contact that is already in the contact list.

</dd> <dt>

<span id="MSGR_E_DISCONNECTED"></span><span id="msgr_e_disconnected"></span>**MSGR\_E\_DISCONNECTED**
</dt> <dd>

Client is disconnected from the network.

</dd> <dt>

<span id="MSGR_E_UNEXPECTED"></span><span id="msgr_e_unexpected"></span>**MSGR\_E\_UNEXPECTED**
</dt> <dd>

Unexpected error occurred.

</dd> <dt>

<span id="MSGR_E_SERVER_TOO_BUSY"></span><span id="msgr_e_server_too_busy"></span>**MSGR\_E\_SERVER\_TOO\_BUSY**
</dt> <dd>

Server is too busy to handle the specified request.

</dd> <dt>

<span id="MSGR_E_INVALID_AUTH_PACKAGES"></span><span id="msgr_e_invalid_auth_packages"></span>**MSGR\_E\_INVALID\_AUTH\_PACKAGES**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_NEWER_CLIENT_AVAILABLE"></span><span id="msgr_e_newer_client_available"></span>**MSGR\_E\_NEWER\_CLIENT\_AVAILABLE**
</dt> <dd>

Newer version of the client is available to download.

</dd> <dt>

<span id="MSGR_E_AI_TIMEOUT"></span><span id="msgr_e_ai_timeout"></span>**MSGR\_E\_AI\_TIMEOUT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_CANCEL"></span><span id="msgr_e_cancel"></span>**MSGR\_E\_CANCEL**
</dt> <dd>

User cancelled the operation in progress.

</dd> <dt>

<span id="MSGR_E_TOO_MANY_MATCHES"></span><span id="msgr_e_too_many_matches"></span>**MSGR\_E\_TOO\_MANY\_MATCHES**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_SERVER_UNAVAILABLE"></span><span id="msgr_e_server_unavailable"></span>**MSGR\_E\_SERVER\_UNAVAILABLE**
</dt> <dd>

Server is unavailable to handle the specified request.

</dd> <dt>

<span id="MSGR_E_LOGON_UI_ACTIVE"></span><span id="msgr_e_logon_ui_active"></span>**MSGR\_E\_LOGON\_UI\_ACTIVE**
</dt> <dd>

Sign in UI is active and expecting user input.

</dd> <dt>

<span id="MSGR_E_OPTION_UI_ACTIVE"></span><span id="msgr_e_option_ui_active"></span>**MSGR\_E\_OPTION\_UI\_ACTIVE**
</dt> <dd>

**Options** dialog is active and waiting for user input.

</dd> <dt>

<span id="MSGR_E_CONTACT_UI_ACTIVE"></span><span id="msgr_e_contact_ui_active"></span>**MSGR\_E\_CONTACT\_UI\_ACTIVE**
</dt> <dd>

**Add a contact** wizard is active and waiting for user input.

</dd> <dt>

<span id="MSGR_E_PRIMARY_SERVICE_NOT_LOGGED_ON"></span><span id="msgr_e_primary_service_not_logged_on"></span>**MSGR\_E\_PRIMARY\_SERVICE\_NOT\_LOGGED\_ON**
</dt> <dd>

Client is not signed in to primary service.

</dd> <dt>

<span id="MSGR_E_LOGGED_ON"></span><span id="msgr_e_logged_on"></span>**MSGR\_E\_LOGGED\_ON**
</dt> <dd>

User is already signed in.

</dd> <dt>

<span id="MSGR_E_CONNECT_PROXY"></span><span id="msgr_e_connect_proxy"></span>**MSGR\_E\_CONNECT\_PROXY**
</dt> <dd>

Error connecting the proxy.

</dd> <dt>

<span id="MSGR_E_PROXY_AUTH"></span><span id="msgr_e_proxy_auth"></span>**MSGR\_E\_PROXY\_AUTH**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PROXY_AUTH_TYPE"></span><span id="msgr_e_proxy_auth_type"></span>**MSGR\_E\_PROXY\_AUTH\_TYPE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_INVALID_PROXY_NAME"></span><span id="msgr_e_invalid_proxy_name"></span>**MSGR\_E\_INVALID\_PROXY\_NAME**
</dt> <dd>

Specified proxy name is invalid.

</dd> <dt>

<span id="MSGR_E_NOT_LOGGED_ON"></span><span id="msgr_e_not_logged_on"></span>**MSGR\_E\_NOT\_LOGGED\_ON**
</dt> <dd>

User is not logged on to the client.

</dd> <dt>

<span id="MSGR_E_NOT_PRIMARY_SERVICE"></span><span id="msgr_e_not_primary_service"></span>**MSGR\_E\_NOT\_PRIMARY\_SERVICE**
</dt> <dd>

Specified service is not the primary service.

</dd> <dt>

<span id="MSGR_E_TOO_MANY_SESSIONS"></span><span id="msgr_e_too_many_sessions"></span>**MSGR\_E\_TOO\_MANY\_SESSIONS**
</dt> <dd>

Maximum number of sessions that can be opened has been reached.

</dd> <dt>

<span id="MSGR_E_TOO_MANY_MESSAGES"></span><span id="msgr_e_too_many_messages"></span>**MSGR\_E\_TOO\_MANY\_MESSAGES**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_REMOTE_LOGIN"></span><span id="msgr_e_remote_login"></span>**MSGR\_E\_REMOTE\_LOGIN**
</dt> <dd>

User signed in on a computer and also signed in from another (remote) computer.

</dd> <dt>

<span id="MSGR_E_INVALID_FRIENDLY_NAME"></span><span id="msgr_e_invalid_friendly_name"></span>**MSGR\_E\_INVALID\_FRIENDLY\_NAME**
</dt> <dd>

Friendly name specified is not valid, for example user@microsoft.com (@microsoft.com is not part of a friendly name).

</dd> <dt>

<span id="MSGR_E_SESSION_FULL"></span><span id="msgr_e_session_full"></span>**MSGR\_E\_SESSION\_FULL**
</dt> <dd>

Number of participants allowed for the session has been reached.

</dd> <dt>

<span id="MSGR_E_NOT_ALLOWING_NEW_USERS"></span><span id="msgr_e_not_allowing_new_users"></span>**MSGR\_E\_NOT\_ALLOWING\_NEW\_USERS**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_INVALID_DOMAIN"></span><span id="msgr_e_invalid_domain"></span>**MSGR\_E\_INVALID\_DOMAIN**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_TCP_ERROR"></span><span id="msgr_e_tcp_error"></span>**MSGR\_E\_TCP\_ERROR**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_SESSION_TIMEOUT"></span><span id="msgr_e_session_timeout"></span>**MSGR\_E\_SESSION\_TIMEOUT**
</dt> <dd>

Session timed out.

</dd> <dt>

<span id="MSGR_E_MULTIPOINT_SESSION_BEGIN_TIMEOUT"></span><span id="msgr_e_multipoint_session_begin_timeout"></span>**MSGR\_E\_MULTIPOINT\_SESSION\_BEGIN\_TIMEOUT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_MULTIPOINT_SESSION_END_TIMEOUT"></span><span id="msgr_e_multipoint_session_end_timeout"></span>**MSGR\_E\_MULTIPOINT\_SESSION\_END\_TIMEOUT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_REVERSE_LIST_FULL"></span><span id="msgr_e_reverse_list_full"></span>**MSGR\_E\_REVERSE\_LIST\_FULL**
</dt> <dd>

Reverse contact list is full.

</dd> <dt>

<span id="MSGR_E_SERVER_ERROR"></span><span id="msgr_e_server_error"></span>**MSGR\_E\_SERVER\_ERROR**
</dt> <dd>

Unspecified server error.

</dd> <dt>

<span id="MSGR_E_SYSTEM_CONFIG"></span><span id="msgr_e_system_config"></span>**MSGR\_E\_SYSTEM\_CONFIG**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_NO_DIRECTORY"></span><span id="msgr_e_no_directory"></span>**MSGR\_E\_NO\_DIRECTORY**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_RETRY_SET"></span><span id="msgr_e_retry_set"></span>**MSGR\_E\_RETRY\_SET**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_CHILD_WITHOUT_CONSENT"></span><span id="msgr_e_child_without_consent"></span>**MSGR\_E\_CHILD\_WITHOUT\_CONSENT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_USER_CANCELLED"></span><span id="msgr_e_user_cancelled"></span>**MSGR\_E\_USER\_CANCELLED**
</dt> <dd>

User cancelled a specified operation such as a sign in.

</dd> <dt>

<span id="MSGR_E_CANCEL_BEFORE_CONNECT"></span><span id="msgr_e_cancel_before_connect"></span>**MSGR\_E\_CANCEL\_BEFORE\_CONNECT**
</dt> <dd>

User cancelled a specified operation before the connection was established.

</dd> <dt>

<span id="MSGR_E_VOICE_IM_TIMEOUT"></span><span id="msgr_e_voice_im_timeout"></span>**MSGR\_E\_VOICE\_IM\_TIMEOUT**
</dt> <dd>

Voice IM session timed out.

</dd> <dt>

<span id="MSGR_E_NOT_ACCEPTING_PAGES"></span><span id="msgr_e_not_accepting_pages"></span>**MSGR\_E\_NOT\_ACCEPTING\_PAGES**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_EMAIL_PASSPORT_NOT_VALIDATED"></span><span id="msgr_e_email_passport_not_validated"></span>**MSGR\_E\_EMAIL\_PASSPORT\_NOT\_VALIDATED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_AUDIO_UI_ACTIVE"></span><span id="msgr_e_audio_ui_active"></span>**MSGR\_E\_AUDIO\_UI\_ACTIVE**
</dt> <dd>

Audio UI (voice configuration wizard) is active and waiting for user input.

</dd> <dt>

<span id="MSGR_E_NO_HARDWARE"></span><span id="msgr_e_no_hardware"></span>**MSGR\_E\_NO\_HARDWARE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PAGING_UNAVAILABLE"></span><span id="msgr_e_paging_unavailable"></span>**MSGR\_E\_PAGING\_UNAVAILABLE**
</dt> <dd>

Paging is not supported for this client.

</dd> <dt>

<span id="MSGR_E_PHONE_INVALID_NUMBER"></span><span id="msgr_e_phone_invalid_number"></span>**MSGR\_E\_PHONE\_INVALID\_NUMBER**
</dt> <dd>

Specified phone number is invalid.

</dd> <dt>

<span id="MSGR_E_PHONE_NO_FUNDS"></span><span id="msgr_e_phone_no_funds"></span>**MSGR\_E\_PHONE\_NO\_FUNDS**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_VOICE_NO_ANSWER"></span><span id="msgr_e_voice_no_answer"></span>**MSGR\_E\_VOICE\_NO\_ANSWER**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_VOICE_WAVEIN_DEVICE"></span><span id="msgr_e_voice_wavein_device"></span>**MSGR\_E\_VOICE\_WAVEIN\_DEVICE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_FT_TIMEOUT"></span><span id="msgr_e_ft_timeout"></span>**MSGR\_E\_FT\_TIMEOUT**
</dt> <dd>

Not supported.&gt;

</dd> <dt>

<span id="MSGR_E_MESSAGE_TOO_LONG"></span><span id="msgr_e_message_too_long"></span>**MSGR\_E\_MESSAGE\_TOO\_LONG**
</dt> <dd>

Message being sent is too long.

</dd> <dt>

<span id="MSGR_E_VOICE_FIREWALL"></span><span id="msgr_e_voice_firewall"></span>**MSGR\_E\_VOICE\_FIREWALL**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_VOICE_NETCONN"></span><span id="msgr_e_voice_netconn"></span>**MSGR\_E\_VOICE\_NETCONN**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PHONE_CIRCUITS_BUSY"></span><span id="msgr_e_phone_circuits_busy"></span>**MSGR\_E\_PHONE\_CIRCUITS\_BUSY**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_SERVER_PROTOCOL"></span><span id="msgr_e_server_protocol"></span>**MSGR\_E\_SERVER\_PROTOCOL**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_UNAVAILABLE_VIA_HTTP"></span><span id="msgr_e_unavailable_via_http"></span>**MSGR\_E\_UNAVAILABLE\_VIA\_HTTP**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PHONE_INVALID_PIN"></span><span id="msgr_e_phone_invalid_pin"></span>**MSGR\_E\_PHONE\_INVALID\_PIN**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PHONE_PINPROCEED_TIMEOUT"></span><span id="msgr_e_phone_pinproceed_timeout"></span>**MSGR\_E\_PHONE\_PINPROCEED\_TIMEOUT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_SERVER_SHUTDOWN"></span><span id="msgr_e_server_shutdown"></span>**MSGR\_E\_SERVER\_SHUTDOWN**
</dt> <dd>

Windows Messenger signed out due to server shutdown.

</dd> <dt>

<span id="MSGR_E_CLIENT_DISALLOWED"></span><span id="msgr_e_client_disallowed"></span>**MSGR\_E\_CLIENT\_DISALLOWED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PHONE_CALL_NOT_COMPLETE"></span><span id="msgr_e_phone_call_not_complete"></span>**MSGR\_E\_PHONE\_CALL\_NOT\_COMPLETE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_GROUPS_NOT_ENABLED"></span><span id="msgr_e_groups_not_enabled"></span>**MSGR\_E\_GROUPS\_NOT\_ENABLED**
</dt> <dd>

Groups are not enabled on this service.

</dd> <dt>

<span id="MSGR_E_GROUP_ALREADY_EXISTS"></span><span id="msgr_e_group_already_exists"></span>**MSGR\_E\_GROUP\_ALREADY\_EXISTS**
</dt> <dd>

New group specified already exists on the specified provider.

</dd> <dt>

<span id="MSGR_E_TOO_MANY_GROUPS"></span><span id="msgr_e_too_many_groups"></span>**MSGR\_E\_TOO\_MANY\_GROUPS**
</dt> <dd>

More groups cannot be created because the provider has reached the maximum limit.

</dd> <dt>

<span id="MSGR_E_GROUP_DOES_NOT_EXIST"></span><span id="msgr_e_group_does_not_exist"></span>**MSGR\_E\_GROUP\_DOES\_NOT\_EXIST**
</dt> <dd>

Specified group name does not exist.

</dd> <dt>

<span id="MSGR_E_USER_NOT_GROUP_MEMBER"></span><span id="msgr_e_user_not_group_member"></span>**MSGR\_E\_USER\_NOT\_GROUP\_MEMBER**
</dt> <dd>

Specified user is not a member of the specified group.

</dd> <dt>

<span id="MSGR_E_GROUP_NAME_TOO_LONG"></span><span id="msgr_e_group_name_too_long"></span>**MSGR\_E\_GROUP\_NAME\_TOO\_LONG**
</dt> <dd>

Specified group name is longer than the allowed limit.

</dd> <dt>

<span id="MSGR_E_GROUP_NOT_EMPTY"></span><span id="msgr_e_group_not_empty"></span>**MSGR\_E\_GROUP\_NOT\_EMPTY**
</dt> <dd>

Group cannot be deleted because it has contacts in it.

</dd> <dt>

<span id="MSGR_E_BAD_GROUP_NAME"></span><span id="msgr_e_bad_group_name"></span>**MSGR\_E\_BAD\_GROUP\_NAME**
</dt> <dd>

Specified group name is not valid.

</dd> <dt>

<span id="MSGR_E_PHONESERVICE_UNAVAILABLE"></span><span id="msgr_e_phoneservice_unavailable"></span>**MSGR\_E\_PHONESERVICE\_UNAVAILABLE**
</dt> <dd>

Phone service is not enabled.

</dd> <dt>

<span id="MSGR_E_CANNOT_RENAME"></span><span id="msgr_e_cannot_rename"></span>**MSGR\_E\_CANNOT\_RENAME**
</dt> <dd>

Specified group cannot be renamed.

</dd> <dt>

<span id="MSGR_E_CANNOT_DELETE"></span><span id="msgr_e_cannot_delete"></span>**MSGR\_E\_CANNOT\_DELETE**
</dt> <dd>

Specified contact or group cannot be deleted.

</dd> <dt>

<span id="MSGR_E_INVALID_SERVICE"></span><span id="msgr_e_invalid_service"></span>**MSGR\_E\_INVALID\_SERVICE**
</dt> <dd>

Specified contact or group does not belong to the specified service.

</dd> <dt>

<span id="MSGR_E_POLICY_RESTRICTED"></span><span id="msgr_e_policy_restricted"></span>**MSGR\_E\_POLICY\_RESTRICTED**
</dt> <dd>

Operation cannot be performed because of policy restrictions.

</dd> <dt>

<span id="MSGR_E_BUSY"></span><span id="msgr_e_busy"></span>**MSGR\_E\_BUSY**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_DNS_SRV_FAIL"></span><span id="msgr_e_dns_srv_fail"></span>**MSGR\_E\_DNS\_SRV\_FAIL**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_DNS_A_RES_FAIL"></span><span id="msgr_e_dns_a_res_fail"></span>**MSGR\_E\_DNS\_A\_RES\_FAIL**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_NO_SERVER_ADDRESS_SPECIFIED"></span><span id="msgr_e_no_server_address_specified"></span>**MSGR\_E\_NO\_SERVER\_ADDRESS\_SPECIFIED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_TLS_FAIL"></span><span id="msgr_e_tls_fail"></span>**MSGR\_E\_TLS\_FAIL**
</dt> <dd>

TLS connection failed.

</dd> <dt>

<span id="MSGR_E_INCOMPATIBLE_ENCRYPTION"></span><span id="msgr_e_incompatible_encryption"></span>**MSGR\_E\_INCOMPATIBLE\_ENCRYPTION**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_SSL_TUNNEL_FAILED"></span><span id="msgr_e_ssl_tunnel_failed"></span>**MSGR\_E\_SSL\_TUNNEL\_FAILED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_SIP_TIMEOUT"></span><span id="msgr_e_sip_timeout"></span>**MSGR\_E\_SIP\_TIMEOUT**
</dt> <dd>

SIP connection attempt timed out.

</dd> <dt>

<span id="MSGR_E_INCOMPATIBLE_IM"></span><span id="msgr_e_incompatible_im"></span>**MSGR\_E\_INCOMPATIBLE\_IM**
</dt> <dd>

Client versions are incompatible.

</dd> <dt>

<span id="MSGR_E_MIM_ADD_TO_CONTACTS_FAIL"></span><span id="msgr_e_mim_add_to_contacts_fail"></span>**MSGR\_E\_MIM\_ADD\_TO\_CONTACTS\_FAIL**
</dt> <dd>

Cannot add more contacts to MIM conversation.

</dd> <dt>

<span id="MSGR_E_INVALID_ADDRESS_FORMAT"></span><span id="msgr_e_invalid_address_format"></span>**MSGR\_E\_INVALID\_ADDRESS\_FORMAT**
</dt> <dd>

Specified user address is in an invalid format.

</dd> <dt>

<span id="MSGR_E_INVALID_CERTIFICATE"></span><span id="msgr_e_invalid_certificate"></span>**MSGR\_E\_INVALID\_CERTIFICATE**
</dt> <dd>

Client does not have a valid certificate to connect over TLS.

</dd> <dt>

<span id="MSGR_E_AUTH_TIME_SKEW"></span><span id="msgr_e_auth_time_skew"></span>**MSGR\_E\_AUTH\_TIME\_SKEW**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_CHANGED_CREDENTIALS"></span><span id="msgr_e_changed_credentials"></span>**MSGR\_E\_CHANGED\_CREDENTIALS**
</dt> <dd>

User logon credentials are different from the stored ones.

</dd> <dt>

<span id="MSGR_E_SIP_LOGIN_FORBIDDEN"></span><span id="msgr_e_sip_login_forbidden"></span>**MSGR\_E\_SIP\_LOGIN\_FORBIDDEN**
</dt> <dd>

SIP logon for the user is forbidden.

</dd> <dt>

<span id="MSGR_E_SIP_HIGH_SECURITY_SET_TLS"></span><span id="msgr_e_sip_high_security_set_tls"></span>**MSGR\_E\_SIP\_HIGH\_SECURITY\_SET\_TLS**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_CALLEE_INSUFFICIENT_SECURITY_LEVEL"></span><span id="msgr_e_callee_insufficient_security_level"></span>**MSGR\_E\_CALLEE\_INSUFFICIENT\_SECURITY\_LEVEL**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_CALLER_PEER2PEER_CALLS_NOT_ALLOWED"></span><span id="msgr_e_caller_peer2peer_calls_not_allowed"></span>**MSGR\_E\_CALLER\_PEER2PEER\_CALLS\_NOT\_ALLOWED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_SIP_UDP_UNSUPPORTED"></span><span id="msgr_e_sip_udp_unsupported"></span>**MSGR\_E\_SIP\_UDP\_UNSUPPORTED**
</dt> <dd>

UDP is not supported on the specified server.

</dd> <dt>

<span id="MSGR_E_SIP_SEARCH_FORBIDDEN"></span><span id="msgr_e_sip_search_forbidden"></span>**MSGR\_E\_SIP\_SEARCH\_FORBIDDEN**
</dt> <dd>

User search is forbidden on SIP.

</dd> <dt>

<span id="MSGR_E_SESSION_RESTRICTED"></span><span id="msgr_e_session_restricted"></span>**MSGR\_E\_SESSION\_RESTRICTED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_MANAGED_USER_INVALID_CVR"></span><span id="msgr_e_managed_user_invalid_cvr"></span>**MSGR\_E\_MANAGED\_USER\_INVALID\_CVR**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_RESTRICTED_USER"></span><span id="msgr_e_restricted_user"></span>**MSGR\_E\_RESTRICTED\_USER**
</dt> <dd>

Attempt to invite a user who is not on the contact list.

</dd> <dt>

<span id="MSGR_E_PROXY_AUTH_REQUIRED"></span><span id="msgr_e_proxy_auth_required"></span>**MSGR\_E\_PROXY\_AUTH\_REQUIRED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PROXY_REALM_MISMATCH"></span><span id="msgr_e_proxy_realm_mismatch"></span>**MSGR\_E\_PROXY\_REALM\_MISMATCH**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_PROXY_PASSWORD_INCORRECT"></span><span id="msgr_e_proxy_password_incorrect"></span>**MSGR\_E\_PROXY\_PASSWORD\_INCORRECT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_RESTRICTED_USER_LOGON_RESTRICED"></span><span id="msgr_e_restricted_user_logon_restriced"></span>**MSGR\_E\_RESTRICTED\_USER\_LOGON\_RESTRICED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_E_IE_OFFLINE"></span><span id="msgr_e_ie_offline"></span>**MSGR\_E\_IE\_OFFLINE**
</dt> <dd>

Internet Explorer is working in offline mode.

</dd> <dt>

<span id="MSGR_E_IE_CANT_CONNECT"></span><span id="msgr_e_ie_cant_connect"></span>**MSGR\_E\_IE\_CANT\_CONNECT**
</dt> <dd>

Internet Explorer cannot connect to the network.

</dd> <dt>

<span id="MSGR_S_ALREADY_IN_THE_MODE"></span><span id="msgr_s_already_in_the_mode"></span>**MSGR\_S\_ALREADY\_IN\_THE\_MODE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_S_TRANSFER_SEND_BEGUN"></span><span id="msgr_s_transfer_send_begun"></span>**MSGR\_S\_TRANSFER\_SEND\_BEGUN**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_S_TRANSFER_SEND_FINISHED"></span><span id="msgr_s_transfer_send_finished"></span>**MSGR\_S\_TRANSFER\_SEND\_FINISHED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_S_TRANSFER_RECEIVE_BEGUN"></span><span id="msgr_s_transfer_receive_begun"></span>**MSGR\_S\_TRANSFER\_RECEIVE\_BEGUN**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_S_TRANSFER_RECEIVE_FINISHED"></span><span id="msgr_s_transfer_receive_finished"></span>**MSGR\_S\_TRANSFER\_RECEIVE\_FINISHED**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="MSGR_S_GROUP_ALREADY_EXISTS"></span><span id="msgr_s_group_already_exists"></span>**MSGR\_S\_GROUP\_ALREADY\_EXISTS**
</dt> <dd>

Group specified to be created already exists on the specified provider.

</dd> <dt>

<span id="MSGR_E_FAIL"></span><span id="msgr_e_fail"></span>**MSGR\_E\_FAIL**
</dt> <dd>

General failure.

</dd> <dt>

<span id="MSGR_S_OK"></span><span id="msgr_s_ok"></span>**MSGR\_S\_OK**
</dt> <dd>

Success.

</dd> </dl>

## Requirements



|                                  |                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                |
| End of server support<br/> | Windows Server 2003<br/>                                                       |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl> |



 

 





