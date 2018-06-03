---
title: Session Options
description: Session options can be specified after the LDAP session is initialized. The session option constants identify which session options to access.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a968e66d-933f-44b7-b74d-d18a92d7de3f
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- LDAP_OPT_API_INFO
- LDAP_OPT_API_FEATURE_INFO
- LDAP_OPT_AREC_EXCLUSIVE
- LDAP_OPT_AUTO_RECONNECT
- LDAP_OPT_CACHE_ENABLE
- LDAP_OPT_CACHE_FN_PTRS
- LDAP_OPT_CACHE_STRATEGY
- LDAP_OPT_CLIENT_CERTIFICATE
- LDAP_OPT_DEREF
- LDAP_OPT_DESC
- LDAP_OPT_DNSDOMAIN_NAME
- LDAP_OPT_ENCRYPT
- LDAP_OPT_ERROR_NUMBER
- LDAP_OPT_ERROR_STRING
- LDAP_OPT_FAST_CONCURRENT_BIND
- LDAP_OPT_GETDSNAME_FLAGS
- LDAP_OPT_HOST_NAME
- LDAP_OPT_HOST_REACHABLE
- LDAP_OPT_IO_FN_PTRS
- LDAP_OPT_PING_KEEP_ALIVE
- LDAP_OPT_PING_LIMIT
- LDAP_OPT_PING_WAIT_TIME
- LDAP_OPT_PROMPT_CREDENTIALS
- LDAP_OPT_PROTOCOL_VERSION
- LDAP_OPT_VERSION
- LDAP_OPT_REBIND_ARG
- LDAP_OPT_REBIND_FN
- LDAP_OPT_REF_DEREF_CONN_PER_MSG
- LDAP_OPT_REFERRAL_CALLBACK
- LDAP_OPT_REFERRAL_HOP_LIMIT
- LDAP_OPT_REFERRALS
- LDAP_OPT_RESTART
- LDAP_OPT_ROOTDSE_CACHE
- LDAP_OPT_SASL_METHOD
- LDAP_OPT_SECURITY_CONTEXT
- LDAP_OPT_SEND_TIMEOUT
- LDAP_OPT_SCH_FLAGS
- LDAP_OPT_SOCKET_BIND_ADDRESSES
- LDAP_OPT_SERVER_CERTIFICATE
- LDAP_OPT_SERVER_ERROR
- LDAP_OPT_SERVER_EXT_ERROR
- LDAP_OPT_SIGN
- LDAP_OPT_SIZELIMIT
- LDAP_OPT_SSL
- LDAP_OPT_SSL_INFO
- LDAP_OPT_SSPI_FLAGS
- LDAP_OPT_TCP_KEEPALIVE
- LDAP_OPT_THREAD_FN_PTRS
- LDAP_OPT_TIMELIMIT
api_location:
- Winldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Session Options

Session options can be specified after the LDAP session is initialized. The session option constants identify which session options to access.

The LDAP session handle, returned by the [**ldap\_init**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_init) function, is a pointer to an opaque data type that represents an LDAP session.

In earlier versions of LDAP, this data type was a structure exposed to the caller, and various fields in the structure could be set to control attributes of the session, such as result set size and search time limit.

To protect callers from inevitable changes to this structure, these session attributes are now accessed through a pair of accessor functions.

Call [**ldap\_get\_option**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_option) to access the current value of session-wide optional parameters. In the following list, the Output Values column provides information about the data returned from calling the **ldap\_get\_option** function. Call [**ldap\_set\_option**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_set_option) to set the value of these parameters. For more information about how to use these functions, see [Getting and Setting Session Options](getting-and-setting-session-options.md).

The options, listed in the following list, are defined, where **LDAP\_OPT\_ON** = 1 and **LDAP\_OPT\_OFF** = 0.

<dl> <dt>

<span id="LDAP_OPT_API_INFO"></span><span id="ldap_opt_api_info"></span>**LDAP\_OPT\_API\_INFO**
</dt> <dd> <dl> <dt>

0x00
</dt> <dt>



Sets or retrieves the pointer to an [**LDAPAPIInfo**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapapiinfoa) structure. This structure holds the current API information (including supported extensions).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_API_FEATURE_INFO"></span><span id="ldap_opt_api_feature_info"></span>**LDAP\_OPT\_API\_FEATURE\_INFO**
</dt> <dd> <dl> <dt>

0x15
</dt> <dt>



Sets or retrieves the pointer to an [**LDAPAPIFeatureInfo**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldap_apifeature_infoa) structure. This structure holds data about the extensions supported by the current API.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_AREC_EXCLUSIVE"></span><span id="ldap_opt_arec_exclusive"></span>**LDAP\_OPT\_AREC\_EXCLUSIVE**
</dt> <dd> <dl> <dt>

0x98
</dt> <dt>



When connected to the server, an A-Record only DNS lookup is performed on the supplied host string. Use this flag when passing a fully qualified, DNS hostname as opposed to a domain name for the hostname parameter. Using this option can help reduce dial-up traffic for branch sites by avoiding a query to the remote DNS server for SRV records lookup.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** or **LDAP\_OPT\_OFF** (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_AUTO_RECONNECT"></span><span id="ldap_opt_auto_reconnect"></span>**LDAP\_OPT\_AUTO\_RECONNECT**
</dt> <dd> <dl> <dt>

0x91
</dt> <dt>



Enables/disables auto-reconnect.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** (default) or **LDAP\_OPT\_OFF**.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_CACHE_ENABLE"></span><span id="ldap_opt_cache_enable"></span>**LDAP\_OPT\_CACHE\_ENABLE**
</dt> <dd> <dl> <dt>

0x0F
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to set or retrieve the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_CACHE_FN_PTRS"></span><span id="ldap_opt_cache_fn_ptrs"></span>**LDAP\_OPT\_CACHE\_FN\_PTRS**
</dt> <dd> <dl> <dt>

0x0D
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to set or retrieve the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_CACHE_STRATEGY"></span><span id="ldap_opt_cache_strategy"></span>**LDAP\_OPT\_CACHE\_STRATEGY**
</dt> <dd> <dl> <dt>

0x0E
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to set or retrieve the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_CLIENT_CERTIFICATE"></span><span id="ldap_opt_client_certificate"></span>**LDAP\_OPT\_CLIENT\_CERTIFICATE**
</dt> <dd> <dl> <dt>

0x80
</dt> <dt>



Sets or retrieves the pointer to a [**QUERYCLIENTCERT**](/previous-versions/windows/desktop/api/Winldap/nc-winldap-queryclientcert) callback routine. The routine specifies client certificates while establishing an SSL connection.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_DEREF"></span><span id="ldap_opt_deref"></span>**LDAP\_OPT\_DEREF**
</dt> <dd> <dl> <dt>

0x02
</dt> <dt>



Determines how aliases are handled during search.



| Constant                                    | Value           | Description                                                                                                       |
|---------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------|
| **LDAP\_DEREF\_NEVER** (default)<br/> | 0x00<br/> | Aliases should never be dereferenced.<br/>                                                                  |
| **LDAP\_DEREF\_SEARCHING**<br/>       | 0x01<br/> | Aliases should be dereferenced during the search, but not when locating the base object of the search.<br/> |
| **LDAP\_DEREF\_FINDING**<br/>         | 0x02<br/> | Aliases should be dereferenced when locating the base object, but not during the search.<br/>               |
| **LDAP\_DEREF\_ALWAYS**<br/>          | 0x03<br/> | Aliases should always be dereferenced.<br/>                                                                 |



 


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_DESC"></span><span id="ldap_opt_desc"></span>**LDAP\_OPT\_DESC**
</dt> <dd> <dl> <dt>

0x01
</dt> <dt>



Sets or retrieves the value of the underlying **SOCKET** descriptor that corresponds to the default LDAP connection.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_DNSDOMAIN_NAME"></span><span id="ldap_opt_dnsdomain_name"></span>**LDAP\_OPT\_DNSDOMAIN\_NAME**
</dt> <dd> <dl> <dt>

0x3B
</dt> <dt>



Sets or retrieves the pointer to a **TCHAR** string giving the DNS domain name.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_ENCRYPT"></span><span id="ldap_opt_encrypt"></span>**LDAP\_OPT\_ENCRYPT**
</dt> <dd> <dl> <dt>

0x96
</dt> <dt>



Enables/disables Kerberos encryption prior to binding using the **LDAP\_AUTH\_NEGOTIATE** flag. Cannot be used over an SSL connection. NTLM encryption is also supported.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** or **LDAP\_OPT\_OFF** (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_ERROR_NUMBER"></span><span id="ldap_opt_error_number"></span>**LDAP\_OPT\_ERROR\_NUMBER**
</dt> <dd> <dl> <dt>

0x31
</dt> <dt>



Sets or retrieves a **ULONG** value that contains the code of the most recent LDAP error that occurred for this session.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_ERROR_STRING"></span><span id="ldap_opt_error_string"></span>**LDAP\_OPT\_ERROR\_STRING**
</dt> <dd> <dl> <dt>

0x32
</dt> <dt>



Sets or retrieves the pointer to a **TCHAR** string giving the error message of the most recent LDAP error that occurred for this session. The error string returned by this option should not be freed by the user.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_FAST_CONCURRENT_BIND"></span><span id="ldap_opt_fast_concurrent_bind"></span>**LDAP\_OPT\_FAST\_CONCURRENT\_BIND**
</dt> <dd> <dl> <dt>

0x41
</dt> <dt>



Enables fast/concurrent binds on a previously unbound LDAP session. Cannot be enabled if either **LDAP\_OPT\_SIGN** or **LDAP\_OPT\_ENCRYPT** have been set, and all binds performed in the session must be simple binds once this option is set for a session.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** or **LDAP\_OPT\_OFF** (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_GETDSNAME_FLAGS"></span><span id="ldap_opt_getdsname_flags"></span>**LDAP\_OPT\_GETDSNAME\_FLAGS**
</dt> <dd> <dl> <dt>

0x3D
</dt> <dt>



Sets or retrieves a **ULONG** value that contains flags to control the behavior of the [**DsGetDcName**](https://msdn.microsoft.com/library/ms675983) function.

The flags include:

-   **DS\_FORCE\_REDISCOVERY**
-   **DS\_DIRECTORY\_SERVICE\_REQUIRED**
-   **DS\_DIRECTORY\_SERVICE\_PREFERRED**
-   **DS\_GC\_SERVER\_REQUIRED**
-   **DS\_PDC\_REQUIRED**
-   **DS\_WRITABLE\_REQUIRED**
-   **DS\_FDC\_REQUIRED**
-   **DS\_IP\_REQUIRED**
-   **DS\_KDC\_REQUIRED**
-   **DS\_TIMESERV\_REQUIRED**
-   **DS\_IS\_FLAT\_NAME**
-   **DS\_IS\_DNS\_NAME**


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_HOST_NAME"></span><span id="ldap_opt_host_name"></span>**LDAP\_OPT\_HOST\_NAME**
</dt> <dd> <dl> <dt>

0x30
</dt> <dt>



Sets or retrieves the pointer to a **TCHAR** string giving the name of the LDAP server associated with the connection. The server-name string returned by this option should not be freed by the user, as it is automatically freed when [**ldap\_unbind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_unbind) is called.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_HOST_REACHABLE"></span><span id="ldap_opt_host_reachable"></span>**LDAP\_OPT\_HOST\_REACHABLE**
</dt> <dd> <dl> <dt>

0x3E
</dt> <dt>



Indicates whether the server can be reached.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** (default) or **LDAP\_OPT\_OFF**.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_IO_FN_PTRS"></span><span id="ldap_opt_io_fn_ptrs"></span>**LDAP\_OPT\_IO\_FN\_PTRS**
</dt> <dd> <dl> <dt>

0x0B
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to get or set the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_PING_KEEP_ALIVE"></span><span id="ldap_opt_ping_keep_alive"></span>**LDAP\_OPT\_PING\_KEEP\_ALIVE**
</dt> <dd> <dl> <dt>

0x36
</dt> <dt>



Sets or retrieves a **ULONG** value giving the minimum number of seconds the run time waits, after the last response from the server, before sending a keep-alive ping. The default value is 120 seconds.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_PING_LIMIT"></span><span id="ldap_opt_ping_limit"></span>**LDAP\_OPT\_PING\_LIMIT**
</dt> <dd> <dl> <dt>

0x38
</dt> <dt>



Sets or retrieves a **ULONG** value giving the number of unanswered pings that the run time sends before closing a connection. The default value is 4.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_PING_WAIT_TIME"></span><span id="ldap_opt_ping_wait_time"></span>**LDAP\_OPT\_PING\_WAIT\_TIME**
</dt> <dd> <dl> <dt>

0x37
</dt> <dt>



Sets or retrieves a **ULONG** value giving the number of milliseconds that the run time waits for the response to come back after sending a ping. The default value is 2000 milliseconds.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_PROMPT_CREDENTIALS"></span><span id="ldap_opt_prompt_credentials"></span>**LDAP\_OPT\_PROMPT\_CREDENTIALS**
</dt> <dd> <dl> <dt>

0x3F
</dt> <dt>



Indicates whether to prompt for credentials. Required only for distributed password authentication (DPA) and NTLM if no credentials are loaded.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** (default) or **LDAP\_OPT\_OFF**.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_PROTOCOL_VERSION"></span><span id="ldap_opt_protocol_version"></span>**LDAP\_OPT\_PROTOCOL\_VERSION**
</dt> <dd> <dl> <dt>

0x11
</dt> <dt>



Sets or retrieves a **ULONG** value that indicates the version of the default LDAP server, either **LDAP\_VERSION2** or **LDAP\_VERSION3**. If no version is set, the default is **LDAP\_VERSION2**.

**LDAP\_OPT\_VERSION** and **LDAP\_OPT\_PROTOCOL\_VERSION** are equivalent.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_VERSION"></span><span id="ldap_opt_version"></span>**LDAP\_OPT\_VERSION**
</dt> <dd> <dl> <dt>

0x11
</dt> <dt>



Sets or retrieves a **ULONG** value that indicates the version of the default LDAP server, either **LDAP\_VERSION2** or **LDAP\_VERSION3**. If no version is set, the default is **LDAP\_VERSION2**.

**LDAP\_OPT\_VERSION** and **LDAP\_OPT\_PROTOCOL\_VERSION** are equivalent.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_REBIND_ARG"></span><span id="ldap_opt_rebind_arg"></span>**LDAP\_OPT\_REBIND\_ARG**
</dt> <dd> <dl> <dt>

0x07
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to get or set the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_REBIND_FN"></span><span id="ldap_opt_rebind_fn"></span>**LDAP\_OPT\_REBIND\_FN**
</dt> <dd> <dl> <dt>

0x06
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to get or set the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_REF_DEREF_CONN_PER_MSG"></span><span id="ldap_opt_ref_deref_conn_per_msg"></span>**LDAP\_OPT\_REF\_DEREF\_CONN\_PER\_MSG**
</dt> <dd> <dl> <dt>

0x94
</dt> <dt>



Enables/disables the referencing of the connection on a per message basis. Must be set before calling the [**ldap\_conn\_from\_msg**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_conn_from_msg) function.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** or **LDAP\_OPT\_OFF** (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_REFERRAL_CALLBACK"></span><span id="ldap_opt_referral_callback"></span>**LDAP\_OPT\_REFERRAL\_CALLBACK**
</dt> <dd> <dl> <dt>

0x70
</dt> <dt>



Sets or retrieves the pointer to an [**LDAP\_REFERRAL\_CALLBACK**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapreferralcallback) structure. This structure contains the default callback routines required when chasing referrals.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_REFERRAL_HOP_LIMIT"></span><span id="ldap_opt_referral_hop_limit"></span>**LDAP\_OPT\_REFERRAL\_HOP\_LIMIT**
</dt> <dd> <dl> <dt>

0x10
</dt> <dt>



The maximum number of referrals that will be followed when automatically chasing a referral for a particular request.

Sets or retrieves a **ULONG** value in the range between 0 and 2  -1. A value of **LDAP\_NO\_LIMIT** (zero) means that there is no limit. For more information, see the **LDAP\_OPT\_REFERRALS** session option. The default value is 32.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_REFERRALS"></span><span id="ldap_opt_referrals"></span>**LDAP\_OPT\_REFERRALS**
</dt> <dd> <dl> <dt>

0x08
</dt> <dt>



Controls whether the LDAP library automatically follows referrals returned by LDAP servers.

Sets or retrieves one of the following **ULONG** values:

-   **LDAP\_OPT\_ON** (default)
-   **LDAP\_OPT\_OFF**
-   **LDAP\_CHASE\_SUBORDINATE\_REFERRALS** indicates that LDAP should chase subordinate referrals (or references) returned in a search (LDAP 3 or later).
-   **LDAP\_CHASE\_EXTERNAL\_REFERRALS** indicates that LDAP should chase external referrals.

These can be returned on any operation except a bind.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_RESTART"></span><span id="ldap_opt_restart"></span>**LDAP\_OPT\_RESTART**
</dt> <dd> <dl> <dt>

0x09
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to get or set the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_ROOTDSE_CACHE"></span><span id="ldap_opt_rootdse_cache"></span>**LDAP\_OPT\_ROOTDSE\_CACHE**
</dt> <dd> <dl> <dt>

0x9A
</dt> <dt>



Enable/disable the internal RootDSE cache.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** (default) or **LDAP\_OPT\_OFF**.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SASL_METHOD"></span><span id="ldap_opt_sasl_method"></span>**LDAP\_OPT\_SASL\_METHOD**
</dt> <dd> <dl> <dt>

0x97
</dt> <dt>



Sets or retrieves the preferred SASL binding method prior to binding using the **LDAP\_AUTH\_NEGOTIATE** flag.

Sets or retrieves the pointer to a **TCHAR** string giving the SASL method name. One example is "GSSAPI".


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SECURITY_CONTEXT"></span><span id="ldap_opt_security_context"></span>**LDAP\_OPT\_SECURITY\_CONTEXT**
</dt> <dd> <dl> <dt>

0x99
</dt> <dt>



Sets or retrieves the security context associated with the current connection.

Sets or retrieves the **PCtxtHandle** pointer to the **CtxtHandle** structure.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SEND_TIMEOUT"></span><span id="ldap_opt_send_timeout"></span>**LDAP\_OPT\_SEND\_TIMEOUT**
</dt> <dd> <dl> <dt>

0x42
</dt> <dt>



A limit on the number of seconds that the local LDAP client will wait while attempting to send data to a remote computer. If the send operation is not completed before the timeout period expires, the LDAP call will fail with an **LDAP\_TIMEOUT** error code.

Sets or retrieves a **ULONG** value in the range between 0 and 2  -1. A value of **LDAP\_NO\_LIMIT** (zero) means that send timeouts are disabled. The default value is 0.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SCH_FLAGS"></span><span id="ldap_opt_sch_flags"></span>**LDAP\_OPT\_SCH\_FLAGS**
</dt> <dd> <dl> <dt>

0x43
</dt> <dt>



Sets or retrieves a **ULONG** value that contains flags to control the behavior of [Schannel](http://go.microsoft.com/fwlink/p/?linkid=83970). See the [SCHANNEL\_CRED](http://go.microsoft.com/fwlink/p/?linkid=83958) structure's **dwFlags** for the possible values. Code automatically sets the appropriate flags (**SCH\_CRED\_AUTO\_CRED\_VALIDATION**, **SCH\_CRED\_MANUAL\_CRED\_VALIDATION**, **SCH\_CRED\_NO\_DEFAULT\_CREDS** and **SCH\_CRED\_USE\_DEFAULT\_CREDS**) for the provided client certificate routine (**LDAP\_OPT\_CLIENT\_CERTIFICATE**) and server certificate routine (**LDAP\_OPT\_SERVER\_CERTIFICATE**). Use this option to change the default behavior of Schannel.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SOCKET_BIND_ADDRESSES"></span><span id="ldap_opt_socket_bind_addresses"></span>**LDAP\_OPT\_SOCKET\_BIND\_ADDRESSES**
</dt> <dd> <dl> <dt>

0x44
</dt> <dt>



Sets or retrieves a pointer to a **TCHAR** string containing a list of space-separated addresses to be used by socket [bind](http://go.microsoft.com/fwlink/p/?linkid=83971). For a multihomed machine, use this option to set a particular network interface address to be used for socket bind. Socket bind will be performed before socket connect for the server address. See socket [bind](http://go.microsoft.com/fwlink/p/?linkid=83971) for more details.

You should provide both IPv4 and IPv6 local addresses, if available, because both IPv4 and IPv6 server addresses can be used for socket connect. Socket [bind](http://go.microsoft.com/fwlink/p/?linkid=83971) will fail if there is an address family mismatch. On the Domain Controller, for the default Server (*HostName*=NULL), loopback addresses will be used for socket connect. Set loopback addresses (for both IPv4 and IPv6) for this option to work.

This option can only be set before a connection is established. That is, just after [**ldap\_init**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_init).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SERVER_CERTIFICATE"></span><span id="ldap_opt_server_certificate"></span>**LDAP\_OPT\_SERVER\_CERTIFICATE**
</dt> <dd> <dl> <dt>

0x81
</dt> <dt>



Sets or retrieves the default callback routine for verifying server certificates while establishing an SSL connection.

Sets or retrieves the pointer to a [**VERIFYSERVERCERT**](/previous-versions/windows/desktop/api/Winldap/nc-winldap-verifyservercert) callback routine.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SERVER_ERROR"></span><span id="ldap_opt_server_error"></span>**LDAP\_OPT\_SERVER\_ERROR**
</dt> <dd> <dl> <dt>

0x33
</dt> <dt>



Sets or retrieves the pointer to a **TCHAR** string giving the most recent server error message that occurred for this session.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SERVER_EXT_ERROR"></span><span id="ldap_opt_server_ext_error"></span>**LDAP\_OPT\_SERVER\_EXT\_ERROR**
</dt> <dd> <dl> <dt>

0x34
</dt> <dt>



Provides a Win32 error-code message.

Sets or retrieves a **ULONG** value giving the most recent Win32 server error that occurred for this session.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SIGN"></span><span id="ldap_opt_sign"></span>**LDAP\_OPT\_SIGN**
</dt> <dd> <dl> <dt>

0x95
</dt> <dt>



Determines the Kerberos signing state or enables Kerberos signing. The **LDAP\_OPT\_SIGN** session option should be enabled prior to binding using the **LDAP\_AUTH\_NEGOTIATE** flag. Cannot be used over an SSL connection. When used with Windows Server, NTLM signing is also supported.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** or **LDAP\_OPT\_OFF** (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SIZELIMIT"></span><span id="ldap_opt_sizelimit"></span>**LDAP\_OPT\_SIZELIMIT**
</dt> <dd> <dl> <dt>

0x03
</dt> <dt>



The limit on the number of entries to return from a search.

Sets or retrieves a **ULONG** value in the range between 0 and 2  -1. A value of **LDAP\_NO\_LIMIT** (zero) indicates that there is no limit (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SSL"></span><span id="ldap_opt_ssl"></span>**LDAP\_OPT\_SSL**
</dt> <dd> <dl> <dt>

0x0A
</dt> <dt>



Enables Secure Socket Layer (SSL) on connection.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** or **LDAP\_OPT\_OFF** (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SSL_INFO"></span><span id="ldap_opt_ssl_info"></span>**LDAP\_OPT\_SSL\_INFO**
</dt> <dd> <dl> <dt>

0x93
</dt> <dt>



Sets or retrieves data about the current secure connection.

Sets or retrieves the pointer to a valid [**SecPkgContext\_ConnectionInfo**](https://msdn.microsoft.com/library/windows/desktop/aa379819) structure used to return the security information.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_SSPI_FLAGS"></span><span id="ldap_opt_sspi_flags"></span>**LDAP\_OPT\_SSPI\_FLAGS**
</dt> <dd> <dl> <dt>

0x92
</dt> <dt>



Sets or retrieves a **ULONG** value giving the flags to pass to the SSPI [**InitializeSecurityContext**](https://msdn.microsoft.com/library/windows/desktop/aa375506) function.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_TCP_KEEPALIVE"></span><span id="ldap_opt_tcp_keepalive"></span>**LDAP\_OPT\_TCP\_KEEPALIVE**
</dt> <dd> <dl> <dt>

0x40
</dt> <dt>



Turns on TCP keep-alives. This is separate from the ICMP ping keep-alive mechanism (**LDAP\_OPT\_PING\_KEEP\_ALIVE**), and enables the keep-alive mechanism built into the TCP protocol. This has no effect when using connectionless (UDP) LDAP. Keep-alives must be enabled before the connection is established, and last for the duration of the specific LDAP session.

Sets or retrieves a **ULONG** value of either **LDAP\_OPT\_ON** or **LDAP\_OPT\_OFF** (default).


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_THREAD_FN_PTRS"></span><span id="ldap_opt_thread_fn_ptrs"></span>**LDAP\_OPT\_THREAD\_FN\_PTRS**
</dt> <dd> <dl> <dt>

0x05
</dt> <dt>



Not supported. Returns **LDAP\_LOCAL\_ERROR** when an attempt is made to get or set the value of this parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPT_TIMELIMIT"></span><span id="ldap_opt_timelimit"></span>**LDAP\_OPT\_TIMELIMIT**
</dt> <dd> <dl> <dt>

0x04
</dt> <dt>



A limit on the number of seconds the server will wait to complete a bind. This also specifies the limit on the number of seconds the server spends on a search.

Sets or retrieves a **ULONG** value in the range between 0 and 2  -1. A value of 0 (zero) for a bind will cause the server to use its default value of 120 seconds. A value of **LDAP\_NO\_LIMIT** (zero) for a search operation means that there is no limit (default).


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winldap.h</dt> </dl> |



## See also

<dl> <dt>

[Getting and Setting Session Options](getting-and-setting-session-options.md)
</dt> </dl>

 

 





