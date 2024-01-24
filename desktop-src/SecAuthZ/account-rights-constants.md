---
description: Account rights determine the type of logon that a user account can perform. An administrator assigns account rights to user and group accounts. Each users account rights include those granted to the user and to the groups to which the user belongs.
ms.assetid: 42139d33-2d56-4d29-998f-5512bb795d44
title: Account Rights Constants (Ntsecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Account Rights Constants

Account rights determine the type of logon that a user account can perform. An administrator assigns account rights to user and group accounts. Each user's account rights include those granted to the user and to the groups to which the user belongs.

A system administrator can use the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) functions to work with account rights. The [**LsaAddAccountRights**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaaddaccountrights) and [**LsaRemoveAccountRights**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaremoveaccountrights) functions add or remove account rights from an account. The [**LsaEnumerateAccountRights**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaenumerateaccountrights) function enumerates the account rights held by a specified account. The [**LsaEnumerateAccountsWithUserRight**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaenumerateaccountswithuserright) function enumerates the accounts that hold a specified account right.

The following account right constants are used to control the logon ability of an account. The [**LogonUser**](/windows/desktop/api/winbase/nf-winbase-logonusera) or [**LsaLogonUser**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsalogonuser) functions fail if the account being logged on does not have the account rights required for the type of logon being performed.



| Constant/value                                                                                                                                                                                                                                                                                                                           | Description                                                                                            |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| <span id="SE_BATCH_LOGON_NAME"></span><span id="se_batch_logon_name"></span><dl> <dt>**SE\_BATCH\_LOGON\_NAME**</dt> <dt>TEXT("SeBatchLogonRight")</dt> </dl>                                                                         | Required for an account to log on using the batch logon type.<br/>                               |
| <span id="SE_DENY_BATCH_LOGON_NAME"></span><span id="se_deny_batch_logon_name"></span><dl> <dt>**SE\_DENY\_BATCH\_LOGON\_NAME**</dt> <dt>TEXT("SeDenyBatchLogonRight")</dt> </dl>                                                     | Explicitly denies an account the right to log on using the batch logon type.<br/>                |
| <span id="SE_DENY_INTERACTIVE_LOGON_NAME"></span><span id="se_deny_interactive_logon_name"></span><dl> <dt>**SE\_DENY\_INTERACTIVE\_LOGON\_NAME**</dt> <dt>TEXT("SeDenyInteractiveLogonRight")</dt> </dl>                             | Explicitly denies an account the right to log on using the interactive logon type.<br/>          |
| <span id="SE_DENY_NETWORK_LOGON_NAME"></span><span id="se_deny_network_logon_name"></span><dl> <dt>**SE\_DENY\_NETWORK\_LOGON\_NAME**</dt> <dt>TEXT("SeDenyNetworkLogonRight")</dt> </dl>                                             | Explicitly denies an account the right to log on using the network logon type.<br/>              |
| <span id="SE_DENY_REMOTE_INTERACTIVE_LOGON_NAME"></span><span id="se_deny_remote_interactive_logon_name"></span><dl> <dt>**SE\_DENY\_REMOTE\_INTERACTIVE\_LOGON\_NAME**</dt> <dt>TEXT("SeDenyRemoteInteractiveLogonRight")</dt> </dl> | Explicitly denies an account the right to log on remotely using the interactive logon type.<br/> |
| <span id="SE_DENY_SERVICE_LOGON_NAME"></span><span id="se_deny_service_logon_name"></span><dl> <dt>**SE\_DENY\_SERVICE\_LOGON\_NAME**</dt> <dt>TEXT("SeDenyServiceLogonRight")</dt> </dl>                                             | Explicitly denies an account the right to log on using the service logon type.<br/>              |
| <span id="SE_INTERACTIVE_LOGON_NAME"></span><span id="se_interactive_logon_name"></span><dl> <dt>**SE\_INTERACTIVE\_LOGON\_NAME**</dt> <dt>TEXT("SeInteractiveLogonRight")</dt> </dl>                                                 | Required for an account to log on using the interactive logon type.<br/>                         |
| <span id="SE_NETWORK_LOGON_NAME"></span><span id="se_network_logon_name"></span><dl> <dt>**SE\_NETWORK\_LOGON\_NAME**</dt> <dt>TEXT("SeNetworkLogonRight")</dt> </dl>                                                                 | Required for an account to log on using the network logon type.<br/>                             |
| <span id="SE_REMOTE_INTERACTIVE_LOGON_NAME"></span><span id="se_remote_interactive_logon_name"></span><dl> <dt>**SE\_REMOTE\_INTERACTIVE\_LOGON\_NAME**</dt> <dt>TEXT("SeRemoteInteractiveLogonRight")</dt> </dl>                     | Required for an account to log on remotely using the interactive logon type.<br/>                |
| <span id="SE_SERVICE_LOGON_NAME"></span><span id="se_service_logon_name"></span><dl> <dt>**SE\_SERVICE\_LOGON\_NAME**</dt> <dt>TEXT("SeServiceLogonRight")</dt> </dl>                                                                 | Required for an account to log on using the service logon type.<br/>                             |



## Remarks

The SE\_DENY rights override the corresponding account rights. An administrator can assign an SE\_DENY right to an account to override any logon rights that an account might have as a result of a group membership. For example, you could assign the SE\_NETWORK\_LOGON\_NAME right to Everyone but assign the SE\_DENY\_NETWORK\_LOGON\_NAME right to Administrators to prevent remote administration of computers.

All of the LSA functions mentioned in the introduction above support both account rights and [privileges](privilege-constants.md). Unlike privileges, however, account rights are not supported by the [**LookupPrivilegeValue**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegevaluea) and [**LookupPrivilegeName**](/windows/desktop/api/Winbase/nf-winbase-lookupprivilegenamea) functions. The [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) function will obtain information on account rights if TokenGroups, and not TokenPrivileges, is specified as the value of the *TokenInformationClass* parameter.

The preceding account right constants are defined as strings in Ntsecapi.h. For example, the SE\_INTERACTIVE\_LOGON\_NAME constant is defined as "SeInteractiveLogonRight".

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntsecapi.h</dt> </dl> |



 

