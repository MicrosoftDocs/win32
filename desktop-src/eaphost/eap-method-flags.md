---
title: EAP Method Flags (Eaptypes.h)
description: The EAP method flags are used within the supplicant, authenticator, and peer functions to specify behaviors of an EAP authentication session.
ms.assetid: b6305349-3418-475e-8a37-2c06b399556e
topic_type:
- apiref
api_name:
- EAP_FLAG_Reserved1
- EAP_FLAG_NON_INTERACTIVE
- EAP_FLAG_LOGON
- EAP_FLAG_PREVIEW
- EAP_FLAG_Reserved2
- EAP_FLAG_MACHINE_AUTH
- EAP_FLAG_GUEST_ACCESS
- EAP_FLAG_Reserved3
- EAP_FLAG_Reserved4
- EAP_FLAG_RESUME_FROM_HIBERNATE
- EAP_FLAG_Reserved5
- EAP_FLAG_Reserved6
- EAP_FLAG_FULL_AUTH
- EAP_FLAG_PREFER_ALT_CREDENTIALS
- EAP_FLAG_Reserved7
- EAP_PEER_FLAG_HEALTH_STATE_CHANGE
- EAP_FLAG_SUPRESS_UI
- EAP_FLAG_PRE_LOGON
- EAP_FLAG_USER_AUTH
- EAP_FLAG_CONFG_READONLY
- EAP_FLAG_Reserved8
api_location:
- eaptypes.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EAP Method Flags

The EAP method flags are used within the supplicant, authenticator, and peer functions to specify behaviors of an EAP authentication session.

<dl> <dt>

<span id="EAP_FLAG_Reserved1"></span><span id="eap_flag_reserved1"></span><span id="EAP_FLAG_RESERVED1"></span>**EAP\_FLAG\_Reserved1**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_NON_INTERACTIVE"></span><span id="eap_flag_non_interactive"></span>**EAP\_FLAG\_NON\_INTERACTIVE**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



Do not display a user interface (UI).


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_LOGON"></span><span id="eap_flag_logon"></span>**EAP\_FLAG\_LOGON**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



User data was obtained from Windows logon.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_PREVIEW"></span><span id="eap_flag_preview"></span>**EAP\_FLAG\_PREVIEW**
</dt> <dd> <dl> <dt>

0x00000008
</dt> <dt>



Show credentials UI before authenticating, even if cached credentials are present.


</dt> </dl> </dd> <dt>

<span id="_EAP_FLAG_Reserved2"></span><span id="_eap_flag_reserved2"></span><span id="_EAP_FLAG_RESERVED2"></span> **EAP\_FLAG\_Reserved2**
</dt> <dd> <dl> <dt>

0x00000010
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_MACHINE_AUTH"></span><span id="eap_flag_machine_auth"></span>**EAP\_FLAG\_MACHINE\_AUTH**
</dt> <dd> <dl> <dt>

0x00000020
</dt> <dt>



Use machine level authentication; not setting this flag indicates user level authentication is being used.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_GUEST_ACCESS"></span><span id="eap_flag_guest_access"></span>**EAP\_FLAG\_GUEST\_ACCESS**
</dt> <dd> <dl> <dt>

 0x00000040
</dt> <dt>



Indicates a request to provide guest access.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_Reserved3"></span><span id="eap_flag_reserved3"></span><span id="EAP_FLAG_RESERVED3"></span>**EAP\_FLAG\_Reserved3**
</dt> <dd> <dl> <dt>

0x00000080 
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="_EAP_FLAG_Reserved4__"></span><span id="_eap_flag_reserved4__"></span><span id="_EAP_FLAG_RESERVED4__"></span> **EAP\_FLAG\_Reserved4** 
</dt> <dd> <dl> <dt>

0x00000100 
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_RESUME_FROM_HIBERNATE"></span><span id="eap_flag_resume_from_hibernate"></span>**EAP\_FLAG\_RESUME\_FROM\_HIBERNATE**
</dt> <dd> <dl> <dt>

0x00000200
</dt> <dt>



Indicates this is the first call after machine activity has resumed from a period of hibernation.


</dt> </dl> </dd> <dt>

<span id="_EAP_FLAG_Reserved5"></span><span id="_eap_flag_reserved5"></span><span id="_EAP_FLAG_RESERVED5"></span> **EAP\_FLAG\_Reserved5**
</dt> <dd> <dl> <dt>

0x00000400 
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_Reserved6________________"></span><span id="eap_flag_reserved6________________"></span><span id="EAP_FLAG_RESERVED6________________"></span>**EAP\_FLAG\_Reserved6** 
</dt> <dd> <dl> <dt>

0x00000800
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_FULL_AUTH"></span><span id="eap_flag_full_auth"></span>**EAP\_FLAG\_FULL\_AUTH**
</dt> <dd> <dl> <dt>

0x00001000
</dt> <dt>



Indicates that tunnel methods should perform a full authentication instead of an abbreviated version, such as [Protected EAP (PEAP) Fast Reconnect](/previous-versions/windows/it-pro/windows-server-2003/cc757996(v=ws.10)).


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_PREFER_ALT_CREDENTIALS"></span><span id="eap_flag_prefer_alt_credentials"></span>**EAP\_FLAG\_PREFER\_ALT\_CREDENTIALS**
</dt> <dd> <dl> <dt>

0x00002000
</dt> <dt>



Indicates credentials passed into [**EapPeerBeginSession**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerbeginsession) are preferred to all other forms of credential retrieval, even if configuration data passed into the current function requests a different mode of credential retrieval.

> [!Note]  
> This flag is only used by [**EapPeerBeginSession**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerbeginsession).

 


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_Reserved7"></span><span id="eap_flag_reserved7"></span><span id="EAP_FLAG_RESERVED7"></span>**EAP\_FLAG\_Reserved7**
</dt> <dd> <dl> <dt>

0x00004000
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="EAP_PEER_FLAG_HEALTH_STATE_CHANGE"></span><span id="eap_peer_flag_health_state_change"></span>**EAP\_PEER\_FLAG\_HEALTH\_STATE\_CHANGE**
</dt> <dd> <dl> <dt>

0x00008000
</dt> <dt>



Indicates the cause of re-authentication is a [Network Access Protection](/windows/desktop/NAP/network-access-protection-start-page) (NAP) callback; NAP initiated the authentication session because the health state changed. This flag must be sent only when this function is called by a NAP-specific [*NotificationHandler*](/previous-versions/windows/desktop/api) callback provided by a previous call to this function.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_SUPRESS_UI"></span><span id="eap_flag_supress_ui"></span>**EAP\_FLAG\_SUPRESS\_UI**
</dt> <dd> <dl> <dt>

0x00010000
</dt> <dt>



Continue authentication with available information. If the authentication cannot proceed then fail.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_PRE_LOGON"></span><span id="eap_flag_pre_logon"></span>**EAP\_FLAG\_PRE\_LOGON**
</dt> <dd> <dl> <dt>

0x00020000
</dt> <dt>



Indicates that EAPHost should provide Single-Sign-On (SSO). For more information, see [SSO and PLAP](understanding-sso-and-plap.md).


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_USER_AUTH"></span><span id="eap_flag_user_auth"></span>**EAP\_FLAG\_USER\_AUTH**
</dt> <dd> <dl> <dt>

0x00040000
</dt> <dt>



Indicates user level authentication for legacy methods that cannot set **EAP\_FLAG\_MACHINE\_AUTH**.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_CONFG_READONLY"></span><span id="eap_flag_confg_readonly"></span>**EAP\_FLAG\_CONFG\_READONLY**
</dt> <dd> <dl> <dt>

 0x00080000
</dt> <dt>



Indicates the configuration can be viewed but not updated.


</dt> </dl> </dd> <dt>

<span id="EAP_FLAG_Reserved8"></span><span id="eap_flag_reserved8"></span><span id="EAP_FLAG_RESERVED8"></span>**EAP\_FLAG\_Reserved8**
</dt> <dd> <dl> <dt>

0x00100000
</dt> <dt>



Do not use. Reserved for future use.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Eaptypes.h</dt> </dl> |



## See also

<dl> <dt>

[Common EAPHost Constants](common-eap-host-error-constants.md)
</dt> </dl>

