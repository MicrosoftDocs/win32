---
title: IMsTscAxEvents OnLogonError method
description: Called when a logon error or other logon event occurs.
ms.assetid: 5af9656b-f99b-4535-ab83-6ecc9bc41808
ms.tgt_platform: multiple
keywords:
- OnLogonError method Remote Desktop Services
- OnLogonError method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnLogonError method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnLogonError
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnLogonError method

Called when a logon error or other logon event occurs.

## Syntax


```C++
void OnLogonError(
  [in] LONG lError
);
```



## Parameters

<dl> <dt>

*lError* \[in\]
</dt> <dd>

The logon error code. This list of codes is not exhaustive.

<dt>

<span id="ARBITRATION_CODE_BUMP_OPTIONS"></span><span id="arbitration_code_bump_options"></span>

<span id="ARBITRATION_CODE_BUMP_OPTIONS"></span><span id="arbitration_code_bump_options"></span>**ARBITRATION\_CODE\_BUMP\_OPTIONS** (-5 (0xFFFFFFFB))


</dt> <dd>

Winlogon is displaying the **Session Contention** dialog box.

</dd> <dt>

<span id="ARBITRATION_CODE_CONTINUE_LOGON"></span><span id="arbitration_code_continue_logon"></span>

<span id="ARBITRATION_CODE_CONTINUE_LOGON"></span><span id="arbitration_code_continue_logon"></span>**ARBITRATION\_CODE\_CONTINUE\_LOGON** (-2 (0xFFFFFFFE))


</dt> <dd>

Winlogon is continuing with the logon process.

</dd> <dt>

<span id="ARBITRATION_CODE_CONTINUE_TERMINATE"></span><span id="arbitration_code_continue_terminate"></span>

<span id="ARBITRATION_CODE_CONTINUE_TERMINATE"></span><span id="arbitration_code_continue_terminate"></span>**ARBITRATION\_CODE\_CONTINUE\_TERMINATE** (-3 (0xFFFFFFFD))


</dt> <dd>

Winlogon is ending silently.

</dd> <dt>

<span id="ARBITRATION_CODE_NOPERM_DIALOG"></span><span id="arbitration_code_noperm_dialog"></span>

<span id="ARBITRATION_CODE_NOPERM_DIALOG"></span><span id="arbitration_code_noperm_dialog"></span>**ARBITRATION\_CODE\_NOPERM\_DIALOG** (-6 (0xFFFFFFFA))


</dt> <dd>

Winlogon is displaying the **No Permissions** dialog box.

</dd> <dt>

<span id="ARBITRATION_CODE_REFUSED_DIALOG"></span><span id="arbitration_code_refused_dialog"></span>

<span id="ARBITRATION_CODE_REFUSED_DIALOG"></span><span id="arbitration_code_refused_dialog"></span>**ARBITRATION\_CODE\_REFUSED\_DIALOG** (-7 (0xFFFFFFF9))


</dt> <dd>

Winlogon is displaying the **Disconnect Refused** dialog box.

</dd> <dt>

<span id="ARBITRATION_CODE_RECONN_OPTIONS"></span><span id="arbitration_code_reconn_options"></span>

<span id="ARBITRATION_CODE_RECONN_OPTIONS"></span><span id="arbitration_code_reconn_options"></span>**ARBITRATION\_CODE\_RECONN\_OPTIONS** (-4 (0xFFFFFFFC))


</dt> <dd>

Winlogon is displaying the **Reconnect** dialog box.

</dd> <dt>

<span id="ERROR_CODE_ACCESS_DENIED"></span><span id="error_code_access_denied"></span>

<span id="ERROR_CODE_ACCESS_DENIED"></span><span id="error_code_access_denied"></span>**ERROR\_CODE\_ACCESS\_DENIED** (-1 (0xFFFFFFFF))


</dt> <dd>

The user was denied access.

</dd> <dt>

<span id="LOGON_FAILED_BAD_PASSWORD"></span><span id="logon_failed_bad_password"></span>

<span id="LOGON_FAILED_BAD_PASSWORD"></span><span id="logon_failed_bad_password"></span>**LOGON\_FAILED\_BAD\_PASSWORD** (0 (0x0))


</dt> <dd>

The logon failed because the logon credentials are not valid.

</dd> <dt>

<span id="LOGON_FAILED_OTHER"></span><span id="logon_failed_other"></span>

<span id="LOGON_FAILED_OTHER"></span><span id="logon_failed_other"></span>**LOGON\_FAILED\_OTHER** (2 (0x2))


</dt> <dd>

Another logon or post-logon error occurred. The Remote Desktop client displays a logon screen to the user.

</dd> <dt>

<span id="LOGON_FAILED_UPDATE_PASSWORD"></span><span id="logon_failed_update_password"></span>

<span id="LOGON_FAILED_UPDATE_PASSWORD"></span><span id="logon_failed_update_password"></span>**LOGON\_FAILED\_UPDATE\_PASSWORD** (1 (0x1))


</dt> <dd>

The password is expired. The user must update their password to continue logging on.

</dd> <dt>

<span id="LOGON_WARNING"></span><span id="logon_warning"></span>

<span id="LOGON_WARNING"></span><span id="logon_warning"></span>**LOGON\_WARNING** (3 (0x3))


</dt> <dd>

The Remote Desktop client displays a dialog box that contains important information for the user.

</dd> <dt>

<span id="STATUS_ACCOUNT_RESTRICTION"></span><span id="status_account_restriction"></span>

<span id="STATUS_ACCOUNT_RESTRICTION"></span><span id="status_account_restriction"></span>**STATUS\_ACCOUNT\_RESTRICTION** (-1073741714 (0xC000006E))


</dt> <dd>

The user name and authentication information are valid, but authentication was blocked due to restrictions on the user account, such as time-of-day restrictions.

</dd> <dt>

<span id="STATUS_LOGON_FAILURE"></span><span id="status_logon_failure"></span>

<span id="STATUS_LOGON_FAILURE"></span><span id="status_logon_failure"></span>**STATUS\_LOGON\_FAILURE** (-1073741715 (0xC000006D))


</dt> <dd>

The attempted logon is not valid. This is due to either an incorrect user name or incorrect authentication information.

</dd> <dt>

<span id="STATUS_PASSWORD_MUST_CHANGE"></span><span id="status_password_must_change"></span>

<span id="STATUS_PASSWORD_MUST_CHANGE"></span><span id="status_password_must_change"></span>**STATUS\_PASSWORD\_MUST\_CHANGE** (-1073741276 (0xC0000224))


</dt> <dd>

The password is expired. The user must update their password to continue logging on.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

Implement this method in your event sink to receive notification that a logon error has occurred.

This list of codes is not exhaustive.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





