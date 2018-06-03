---
title: SESSION\_RESULT enumeration
description: Do not use. Provides the list of possible result codes of the session invitation.
ms.assetid: 99e41f1c-f4ce-494f-a264-83157392e243
keywords:
- SESSION_RESULT enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrpriv.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# SESSION\_RESULT enumeration

\[[**LockStatus**](im-lockstatus-enum.md) is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Provides the list of possible result codes of the session invitation.

## Syntax


```C++
typedef enum  { 
  SR_APPLICATION_LAUNCH_FAILED  = 0x81000601,
  SR_INVITATION_DECLINED        = 0x81000602,
  SR_CONNECTION_FAILURE         = 0x81000603,
  SR_AUTHENTICATION_FAILED      = 0x81000604,
  SR_SESSION_NOT_READY          = 0x81000605,
  SR_SESSION_CANCELLED_LOCAL    = 0x81000606,
  SR_SESSION_CANCELLED_REMOTE   = 0x81000607,
  SR_SESSION_PROTOCOL_ERROR     = 0x81000608,
  SR_SESSION_TIMEOUT            = 0x81000609,
  SR_CANCEL_BEFORE_CONNECT      = 0x8100060a,
  SR_NOT_INVITEE                = 0x8100060b,
  SR_NOT_INVITER                = 0x8100060c,
  SR_APP_ALREADY_REGISTERED     = 0x8100060d,
  SR_APP_NOT_REGISTERED         = 0x8100060e,
  SR_NOT_VALID_FOR_APP_INVITE   = 0x8100060f,
  SR_APP_NOT_SPECIFIED          = 0x81000610,
  SR_CONTEXT_DATA_OVER_LIMIT    = 0x81000611,
  SR_NO_USER_INVITED            = 0x81000612,
  SR_INVITED_SELF               = 0x81000613,
  SR_SESSION_STATE_INVALID      = 0x81000614,
  SR_INVITATION_SEND_FAILURE    = 0x81000615,
  SR_CANCEL_SEND_FAILURE        = 0x81000616,
  SR_DECLINE_SEND_FAILURE       = 0x81000617,
  SR_ACCEPT_SEND_FAILURE        = 0x81000618,
  SR_CONTEXT_DATA_SEND_FAILURE  = 0x81000619,
  SR_NETWORK_CONFIG_FAILURE     = 0x81000620,
  SR_NET_NOT_SUPPORTED          = 0x81000621,
  SR_REMOTE_NET_NOT_SUPPORTED   = 0x81000622,
  SR_FIREWALL_NOT_SUPPORTED     = 0x81000623,
  SR_OLD_SIP_STACK              = 0x81000624
} LockError;
```



## Constants

<dl> <dt>

<span id="SR_APPLICATION_LAUNCH_FAILED"></span><span id="sr_application_launch_failed"></span>**SR\_APPLICATION\_LAUNCH\_FAILED**
</dt> <dd>

The application failed to start.

</dd> <dt>

<span id="SR_INVITATION_DECLINED"></span><span id="sr_invitation_declined"></span>**SR\_INVITATION\_DECLINED**
</dt> <dd>

The invitation was declined by the recipient.

</dd> <dt>

<span id="SR_CONNECTION_FAILURE"></span><span id="sr_connection_failure"></span>**SR\_CONNECTION\_FAILURE**
</dt> <dd>

Connection failure.

</dd> <dt>

<span id="SR_AUTHENTICATION_FAILED"></span><span id="sr_authentication_failed"></span>**SR\_AUTHENTICATION\_FAILED**
</dt> <dd>

The authentication failed.

</dd> <dt>

<span id="SR_SESSION_NOT_READY"></span><span id="sr_session_not_ready"></span>**SR\_SESSION\_NOT\_READY**
</dt> <dd>

The session is not ready.

</dd> <dt>

<span id="SR_SESSION_CANCELLED_LOCAL"></span><span id="sr_session_cancelled_local"></span>**SR\_SESSION\_CANCELLED\_LOCAL**
</dt> <dd>

The local session canceled.

</dd> <dt>

<span id="SR_SESSION_CANCELLED_REMOTE"></span><span id="sr_session_cancelled_remote"></span>**SR\_SESSION\_CANCELLED\_REMOTE**
</dt> <dd>

The session is remotely canceled.

</dd> <dt>

<span id="SR_SESSION_PROTOCOL_ERROR"></span><span id="sr_session_protocol_error"></span>**SR\_SESSION\_PROTOCOL\_ERROR**
</dt> <dd>

Protocol error.

</dd> <dt>

<span id="SR_SESSION_TIMEOUT"></span><span id="sr_session_timeout"></span>**SR\_SESSION\_TIMEOUT**
</dt> <dd>

The session timed out.

</dd> <dt>

<span id="SR_CANCEL_BEFORE_CONNECT"></span><span id="sr_cancel_before_connect"></span>**SR\_CANCEL\_BEFORE\_CONNECT**
</dt> <dd>

The session canceled before the connection was made.

</dd> <dt>

<span id="SR_NOT_INVITEE"></span><span id="sr_not_invitee"></span>**SR\_NOT\_INVITEE**
</dt> <dd>

The recipient is not the invitee.

</dd> <dt>

<span id="SR_NOT_INVITER"></span><span id="sr_not_inviter"></span>**SR\_NOT\_INVITER**
</dt> <dd>

The recipient is not the inviter.

</dd> <dt>

<span id="SR_APP_ALREADY_REGISTERED"></span><span id="sr_app_already_registered"></span>**SR\_APP\_ALREADY\_REGISTERED**
</dt> <dd>

The application is already registered.

</dd> <dt>

<span id="SR_APP_NOT_REGISTERED"></span><span id="sr_app_not_registered"></span>**SR\_APP\_NOT\_REGISTERED**
</dt> <dd>

The application is not registered.

</dd> <dt>

<span id="SR_NOT_VALID_FOR_APP_INVITE"></span><span id="sr_not_valid_for_app_invite"></span>**SR\_NOT\_VALID\_FOR\_APP\_INVITE**
</dt> <dd>

The application does not allow a session to be created.

</dd> <dt>

<span id="SR_APP_NOT_SPECIFIED"></span><span id="sr_app_not_specified"></span>**SR\_APP\_NOT\_SPECIFIED**
</dt> <dd>

The application is not specified for the session.

</dd> <dt>

<span id="SR_CONTEXT_DATA_OVER_LIMIT"></span><span id="sr_context_data_over_limit"></span>**SR\_CONTEXT\_DATA\_OVER\_LIMIT**
</dt> <dd>

The context data exceeds the maximum allowed.

</dd> <dt>

<span id="SR_NO_USER_INVITED"></span><span id="sr_no_user_invited"></span>**SR\_NO\_USER\_INVITED**
</dt> <dd>

No user invited.

</dd> <dt>

<span id="SR_INVITED_SELF"></span><span id="sr_invited_self"></span>**SR\_INVITED\_SELF**
</dt> <dd>

The inviter invited self.

</dd> <dt>

<span id="SR_SESSION_STATE_INVALID"></span><span id="sr_session_state_invalid"></span>**SR\_SESSION\_STATE\_INVALID**
</dt> <dd>

The session state is invalid.

</dd> <dt>

<span id="SR_INVITATION_SEND_FAILURE"></span><span id="sr_invitation_send_failure"></span>**SR\_INVITATION\_SEND\_FAILURE**
</dt> <dd>

Send failure.

</dd> <dt>

<span id="SR_CANCEL_SEND_FAILURE"></span><span id="sr_cancel_send_failure"></span>**SR\_CANCEL\_SEND\_FAILURE**
</dt> <dd>

The send failure was canceled.

</dd> <dt>

<span id="SR_DECLINE_SEND_FAILURE"></span><span id="sr_decline_send_failure"></span>**SR\_DECLINE\_SEND\_FAILURE**
</dt> <dd>

The send failure was declined.

</dd> <dt>

<span id="SR_ACCEPT_SEND_FAILURE"></span><span id="sr_accept_send_failure"></span>**SR\_ACCEPT\_SEND\_FAILURE**
</dt> <dd>

The send failure was accepted.

</dd> <dt>

<span id="SR_CONTEXT_DATA_SEND_FAILURE"></span><span id="sr_context_data_send_failure"></span>**SR\_CONTEXT\_DATA\_SEND\_FAILURE**
</dt> <dd>

The context data sent failed.

</dd> <dt>

<span id="SR_NETWORK_CONFIG_FAILURE"></span><span id="sr_network_config_failure"></span>**SR\_NETWORK\_CONFIG\_FAILURE**
</dt> <dd>

A network configuration operation failed.

</dd> <dt>

<span id="SR_NET_NOT_SUPPORTED"></span><span id="sr_net_not_supported"></span>**SR\_NET\_NOT\_SUPPORTED**
</dt> <dd>

An unsupported network was encountered.

</dd> <dt>

<span id="SR_REMOTE_NET_NOT_SUPPORTED"></span><span id="sr_remote_net_not_supported"></span>**SR\_REMOTE\_NET\_NOT\_SUPPORTED**
</dt> <dd>

An unsupported remote network was encountered.

</dd> <dt>

<span id="SR_FIREWALL_NOT_SUPPORTED"></span><span id="sr_firewall_not_supported"></span>**SR\_FIREWALL\_NOT\_SUPPORTED**
</dt> <dd>

An unsupported firewall was encountered.

</dd> <dt>

<span id="SR_OLD_SIP_STACK"></span><span id="sr_old_sip_stack"></span>**SR\_OLD\_SIP\_STACK**
</dt> <dd>

The SIP stack is out of date.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |



## See also

<dl> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





