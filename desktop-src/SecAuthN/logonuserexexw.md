---
Description: The LogonUserExExW function attempts to log a user on to the local computer.
ms.assetid: d90db4c6-a711-4519-8b91-5069cee07738
title: LogonUserExExW function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LogonUserExExW function

The **LogonUserExExW** function attempts to log a user on to the local computer. The local computer is the computer from which **LogonUserExExW** was called. You cannot use **LogonUserExExW** to log on to a remote computer. Specify the user by using a user name and domain and [*authenticate*](security.a_gly#-security-authentication-gly) the user by using a plaintext password. If the function succeeds, it receives a handle to a token that represents the logged-on user. You can then use this token handle to impersonate the specified user or, in most cases, to create a [*process*](security.p_gly#-security-process-gly) that runs in the context of the specified user.

This function is similar to the [**LogonUserEx**](/windows/win32/Winbase/nf-winbase-logonuserexa?branch=master) function, except that it takes the additional parameter, *pTokenGroups*, which is a set of one or more [*security identifiers*](security.s_gly#-security-security-identifier-gly) (SIDs) that are added to the token returned to the caller when the logon is successful.

This function is not declared in a public header and has no associated import library. You must use the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions to dynamically link to Advapi32.dll.

## Syntax


```C++
BOOL WINAPI LogonUserExExW(
  _In_      LPTSTR        lpszUsername,
  _In_opt_  LPTSTR        lpszDomain,
  _In_opt_  LPTSTR        lpszPassword,
  _In_      DWORD         dwLogonType,
  _In_      DWORD         dwLogonProvider,
  _In_opt_  PTOKEN_GROUPS pTokenGroups,
  _Out_opt_ PHANDLE       phToken,
  _Out_opt_ PSID          *ppLogonSid,
  _Out_opt_ PVOID         *ppProfileBuffer,
  _Out_opt_ LPDWORD       pdwProfileLength,
  _Out_opt_ PQUOTA_LIMITS pQuotaLimits
);
```



## Parameters

<dl> <dt>

*lpszUsername* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the user. This is the name of the user account to log on to. If you use the [*user principal name*](security.u_gly#-security-user-principal-name-gly) (UPN) format, the *lpszDomain* parameter must be **NULL**.

</dd> <dt>

*lpszDomain* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the domain or server whose account database contains the *lpszUsername* account. If this parameter is **NULL**, the user name must be specified in UPN format. If this parameter is ".", the function validates the account by using only the local account database.

</dd> <dt>

*lpszPassword* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string that specifies the plaintext password for the user account specified by *lpszUsername*. When you have finished using the password, clear the password from memory by calling the [**SecureZeroMemory**](base.securezeromemory) function. For more information about protecting passwords, see [Handling Passwords](security.handling_passwords).

</dd> <dt>

*dwLogonType* \[in\]
</dt> <dd>

The type of logon operation to perform. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LOGON32_LOGON_INTERACTIVE"></span><span id="logon32_logon_interactive"></span><dl> <dt>**LOGON32\_LOGON\_INTERACTIVE**</dt> <dt>2</dt> </dl>                    | This logon type is intended for users who will be interactively using the computer, such as a user being logged on by a [*terminal*](security.t_gly#-security-terminal-gly) server, remote shell, or similar process. This logon type has the additional expense of caching logon information for disconnected operations; therefore, it is inappropriate for some client/server applications, such as a mail server.<br/>                                  |
| <span id="LOGON32_LOGON_NETWORK"></span><span id="logon32_logon_network"></span><dl> <dt>**LOGON32\_LOGON\_NETWORK**</dt> <dt>3</dt> </dl>                                | This logon type is intended for high performance servers to authenticate plaintext passwords. The **LogonUserExExW** function does not cache credentials for this logon type.<br/>                                                                                                                                                                                                                                                                                                 |
| <span id="LOGON32_LOGON_BATCH"></span><span id="logon32_logon_batch"></span><dl> <dt>**LOGON32\_LOGON\_BATCH**</dt> <dt>4</dt> </dl>                                      | This logon type is intended for batch servers, where processes may be executing on behalf of a user without their direct intervention. This type is also for higher performance servers that process many plaintext authentication attempts at a time, such as mail or web servers. The **LogonUserExExW** function does not cache credentials for this logon type.<br/>                                                                                                           |
| <span id="LOGON32_LOGON_SERVICE"></span><span id="logon32_logon_service"></span><dl> <dt>**LOGON32\_LOGON\_SERVICE**</dt> <dt>5</dt> </dl>                                | Indicates a service-type logon. The account provided must have the service privilege enabled.<br/>                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="LOGON32_LOGON_UNLOCK"></span><span id="logon32_logon_unlock"></span><dl> <dt>**LOGON32\_LOGON\_UNLOCK**</dt> <dt>7</dt> </dl>                                   | This logon type is for [*GINA*](security.g_gly#-security-gina-gly) DLLs that log on users who will be interactively using the computer. This logon type can generate a unique audit record that shows when the workstation was unlocked.<br/>                                                                                                                                                                                                                   |
| <span id="LOGON32_LOGON_NETWORK_CLEARTEXT"></span><span id="logon32_logon_network_cleartext"></span><dl> <dt>**LOGON32\_LOGON\_NETWORK\_CLEARTEXT**</dt> <dt>8</dt> </dl> | This logon type preserves the name and password in the [*authentication package*](security.a_gly#-security-authentication-package-gly), which allows the server to make connections to other network servers while impersonating the client. A server can accept plaintext credentials from a client, call **LogonUserExExW**, verify that the user can access the system across the network, and still communicate with other servers. <br/> |
| <span id="LOGON32_LOGON_NEW_CREDENTIALS"></span><span id="logon32_logon_new_credentials"></span><dl> <dt>**LOGON32\_LOGON\_NEW\_CREDENTIALS**</dt> <dt>9</dt> </dl>       | This logon type allows the caller to clone its current token and specify new credentials for outbound connections. The new logon session has the same local identifier but uses different credentials for other network connections.<br/> This logon type is supported only by the **LOGON32\_PROVIDER\_WINNT50** logon provider.<br/>                                                                                                                                       |



 

</dd> <dt>

*dwLogonProvider* \[in\]
</dt> <dd>

The logon provider. This parameter can be one of the following values.



| Value                                                                                                                                                                                           | Meaning                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LOGON32_PROVIDER_DEFAULT"></span><span id="logon32_provider_default"></span><dl> <dt>**LOGON32\_PROVIDER\_DEFAULT**</dt> </dl> | Use the standard logon provider for the system. The default [*security provider*](security.s_gly#-security-security-support-provider-gly) is NTLM.<br/> |
| <span id="LOGON32_PROVIDER_WINNT50"></span><span id="logon32_provider_winnt50"></span><dl> <dt>**LOGON32\_PROVIDER\_WINNT50**</dt> </dl> | Use the negotiate logon provider. <br/>                                                                                                                                                         |
| <span id="LOGON32_PROVIDER_WINNT40"></span><span id="logon32_provider_winnt40"></span><dl> <dt>**LOGON32\_PROVIDER\_WINNT40**</dt> </dl> | Use the NTLM logon provider.<br/>                                                                                                                                                               |



 

</dd> <dt>

*pTokenGroups* \[in, optional\]
</dt> <dd>

A pointer to a [**TOKEN\_GROUPS**](security.token_groups) structure that specifies a list of group SIDs that are added to the token that this function receives upon successful logon. Any SIDs added to the token also effect group expansion. For example, if the added SIDs are members of local groups, those groups are also added to the received access token.

If this parameter is not **NULL**, the caller of this function must have the **SE\_TCB\_PRIVILEGE** privilege granted and enabled.

</dd> <dt>

*phToken* \[out, optional\]
</dt> <dd>

A pointer to a handle variable that receives a handle to a token that represents the specified user.

You can use the returned handle in calls to the [**ImpersonateLoggedOnUser**](security.impersonateloggedonuser) function.

In most cases, the returned handle is a [*primary token*](security.p_gly#-security-primary-token-gly) that you can use in calls to the [**CreateProcessAsUser**](base.createprocessasuser) function. However, if you specify the LOGON32\_LOGON\_NETWORK flag, **LogonUserExExW** returns an [*impersonation token*](security.i_gly#-security-impersonation-token-gly) that you cannot use in **CreateProcessAsUser** unless you call [**DuplicateTokenEx**](security.duplicatetokenex) to convert the impersonation token to a primary token.

When you no longer need this handle, close it by calling the [**CloseHandle**](base.closehandle) function.

</dd> <dt>

*ppLogonSid* \[out, optional\]
</dt> <dd>

A pointer to a pointer to a SID that receives the SID of the user logged on.

When you have finished using the SID, free it by calling the [**LocalFree**](base.localfree) function.

</dd> <dt>

*ppProfileBuffer* \[out, optional\]
</dt> <dd>

A pointer to a pointer that receives the address of a buffer that contains the logged on user's profile.

</dd> <dt>

*pdwProfileLength* \[out, optional\]
</dt> <dd>

A pointer to a **DWORD** that receives the length of the profile buffer.

</dd> <dt>

*pQuotaLimits* \[out, optional\]
</dt> <dd>

A pointer to a [**QUOTA\_LIMITS**](/windows/win32/Winnt/ns-winnt-_quota_limits?branch=master) structure that receives information about the quotas for the logged on user.

</dd> </dl>

## Return value

If the function succeeds, the function returns nonzero.

If the function fails, it returns zero. To get extended error information, call [**GetLastError**](base.getlasterror).

## Remarks

The **LOGON32\_LOGON\_NETWORK** logon type is fastest, but it has the following limitations:

-   The function returns an [*impersonation token*](security.i_gly#-security-impersonation-token-gly), not a primary token. You cannot use this token directly in the [**CreateProcessAsUser**](base.createprocessasuser) function. However, you can call the [**DuplicateTokenEx**](security.duplicatetokenex) function to convert the token to a primary token, and then use it in **CreateProcessAsUser**.
-   If you convert the token to a primary token and use it in [**CreateProcessAsUser**](base.createprocessasuser) to start a process, the new process cannot access other network resources, such as remote servers or printers, through the redirector. An exception is that if the network resource is not access controlled, then the new process will be able to access it.

The account specified by *lpszUsername* must have the necessary account rights. For example, to log on a user with the **LOGON32\_LOGON\_INTERACTIVE** flag, the user (or a group to which the user belongs) must have the **SE\_INTERACTIVE\_LOGON\_NAME** account right. For a list of the account rights that affect the various logon operations, see [Account Object Access Rights](security.account_object_access_rights).

A user is considered logged on if at least one token exists. If you call [**CreateProcessAsUser**](base.createprocessasuser) and then close the token, the user is still logged on until the process (and all child processes) have ended.

If the optional *pTokenGroups* parameter is supplied, LSA will not add either the local SID or the logon SID automatically.

## Requirements



|                                     |                                                                                                                       |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                  |
| Version<br/>                  | LogonUserExExW is also available onWindows Server 2003 or Windows XPwith the General Distribution Release.<br/> |
| Header<br/>                   | <dl> <dt>Winbasep.h</dt> </dl>                                 |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl>                               |



## See also

<dl> <dt>

[Client/Server Access Control](security.client_server_access_control)
</dt> <dt>

[Client/Server Access Control Functions](security.authorization_functions#client-server-access-control-functions)
</dt> <dt>

[**CloseHandle**](base.closehandle)
</dt> <dt>

[**CreateProcessAsUser**](base.createprocessasuser)
</dt> <dt>

[**DuplicateTokenEx**](security.duplicatetokenex)
</dt> <dt>

[**ImpersonateLoggedOnUser**](security.impersonateloggedonuser)
</dt> <dt>

[**LogonUserEx**](/windows/win32/Winbase/nf-winbase-logonuserexa?branch=master)
</dt> <dt>

[**QUOTA\_LIMITS**](/windows/win32/Winnt/ns-winnt-_quota_limits?branch=master)
</dt> </dl>

 

 




