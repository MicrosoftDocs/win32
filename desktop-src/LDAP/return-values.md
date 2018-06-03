---
title: Return Values
description: Error codes encountered in LDAP applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 822411b7-fc49-4b93-8e54-353350ed5de9
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- LDAP_ADMIN_LIMIT_EXCEEDED
- LDAP_AFFECTS_MULTIPLE_DSAS
- LDAP_ALIAS_DEREF_PROBLEM
- LDAP_ALIAS_PROBLEM
- LDAP_ALREADY_EXISTS
- LDAP_ATTRIBUTE_OR_VALUE_EXISTS
- LDAP_AUTH_METHOD_NOT_SUPPORTED
- LDAP_AUTH_UNKNOWN
- LDAP_BUSY
- LDAP_CLIENT_LOOP
- LDAP_COMPARE_FALSE
- LDAP_COMPARE_TRUE
- LDAP_CONFIDENTIALITY_REQUIRED
- LDAP_CONNECT_ERROR
- LDAP_CONSTRAINT_VIOLATION
- LDAP_CONTROL_NOT_FOUND
- LDAP_DECODING_ERROR
- LDAP_ENCODING_ERROR
- LDAP_FILTER_ERROR
- LDAP_INAPPROPRIATE_AUTH
- LDAP_INAPPROPRIATE_MATCHING
- LDAP_INSUFFICIENT_RIGHTS
- LDAP_INVALID_CREDENTIALS
- LDAP_INVALID_DN_SYNTAX
- LDAP_INVALID_SYNTAX
- LDAP_IS_LEAF
- LDAP_LOCAL_ERROR
- LDAP_LOOP_DETECT
- LDAP_MORE_RESULTS_TO_RETURN
- LDAP_NAMING_VIOLATION
- LDAP_NO_MEMORY
- LDAP_NO_OBJECT_CLASS_MODS
- LDAP_NO_RESULTS_RETURNED
- LDAP_NO_SUCH_ATTRIBUTE
- LDAP_NO_SUCH_OBJECT
- LDAP_NOT_ALLOWED_ON_NONLEAF
- LDAP_NOT_ALLOWED_ON_RDN
- LDAP_NOT_SUPPORTED
- LDAP_OBJECT_CLASS_VIOLATION
- LDAP_OPERATIONS_ERROR
- LDAP_OTHER
- LDAP_PARAM_ERROR
- LDAP_PARTIAL_RESULTS
- LDAP_PROTOCOL_ERROR
- LDAP_REFERRAL
- LDAP_REFERRAL_LIMIT_EXCEEDED
- LDAP_REFERRAL_V2
- LDAP_RESULTS_TOO_LARGE
- LDAP_SERVER_DOWN
- LDAP_SIZELIMIT_EXCEEDED
- LDAP_STRONG_AUTH_REQUIRED
- LDAP_SUCCESS
- LDAP_TIMELIMIT_EXCEEDED
- LDAP_TIMEOUT
- LDAP_UNAVAILABLE
- LDAP_UNAVAILABLE_CRIT_EXTENSION
- LDAP_UNDEFINED_TYPE
- LDAP_UNWILLING_TO_PERFORM
- LDAP_USER_CANCELLED
- LDAP_VIRTUAL_LIST_VIEW_ERROR
api_location:
- Winldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Return Values

The following list lists error codes encountered in LDAP applications. For more information about error handling, see the set of links following this list.

<dl> <dt>

<span id="LDAP_ADMIN_LIMIT_EXCEEDED"></span><span id="ldap_admin_limit_exceeded"></span>**LDAP\_ADMIN\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

0x0b
</dt> <dt>



Administration limit on the server was exceeded.


</dt> </dl> </dd> <dt>

<span id="LDAP_AFFECTS_MULTIPLE_DSAS"></span><span id="ldap_affects_multiple_dsas"></span>**LDAP\_AFFECTS\_MULTIPLE\_DSAS**
</dt> <dd> <dl> <dt>

0x47
</dt> <dt>



Multiple directory service agents are affected.


</dt> </dl> </dd> <dt>

<span id="LDAP_ALIAS_DEREF_PROBLEM"></span><span id="ldap_alias_deref_problem"></span>**LDAP\_ALIAS\_DEREF\_PROBLEM**
</dt> <dd> <dl> <dt>

0x24
</dt> <dt>



Cannot dereference the alias.


</dt> </dl> </dd> <dt>

<span id="LDAP_ALIAS_PROBLEM"></span><span id="ldap_alias_problem"></span>**LDAP\_ALIAS\_PROBLEM**
</dt> <dd> <dl> <dt>

0x21
</dt> <dt>



The alias is invalid.


</dt> </dl> </dd> <dt>

<span id="LDAP_ALREADY_EXISTS"></span><span id="ldap_already_exists"></span>**LDAP\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

0x44
</dt> <dt>



The object already exists.


</dt> </dl> </dd> <dt>

<span id="LDAP_ATTRIBUTE_OR_VALUE_EXISTS"></span><span id="ldap_attribute_or_value_exists"></span>**LDAP\_ATTRIBUTE\_OR\_VALUE\_EXISTS**
</dt> <dd> <dl> <dt>

0x14
</dt> <dt>



The attribute exists or the value has been assigned.


</dt> </dl> </dd> <dt>

<span id="LDAP_AUTH_METHOD_NOT_SUPPORTED"></span><span id="ldap_auth_method_not_supported"></span>**LDAP\_AUTH\_METHOD\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

0x07
</dt> <dt>



The authentication method is not supported. To determine the authentication methods supported by an Active Directory server, retrieve the **SupportedSASLMechanisms** property of rootDSE. For more information, see [Serverless Binding and RootDSE](https://msdn.microsoft.com/library/ms677945).


</dt> </dl> </dd> <dt>

<span id="LDAP_AUTH_UNKNOWN"></span><span id="ldap_auth_unknown"></span>**LDAP\_AUTH\_UNKNOWN**
</dt> <dd> <dl> <dt>

0x56
</dt> <dt>



Unknown authentication error occurred.


</dt> </dl> </dd> <dt>

<span id="LDAP_BUSY"></span><span id="ldap_busy"></span>**LDAP\_BUSY**
</dt> <dd> <dl> <dt>

0x33
</dt> <dt>



The server is busy.


</dt> </dl> </dd> <dt>

<span id="LDAP_CLIENT_LOOP"></span><span id="ldap_client_loop"></span>**LDAP\_CLIENT\_LOOP**
</dt> <dd> <dl> <dt>

0x60
</dt> <dt>



Client loop was detected.


</dt> </dl> </dd> <dt>

<span id="LDAP_COMPARE_FALSE"></span><span id="ldap_compare_false"></span>**LDAP\_COMPARE\_FALSE**
</dt> <dd> <dl> <dt>

0x05
</dt> <dt>



For [**ldap\_compare\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare_ext_s) and [**ldap\_compare\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare_s), this message is returned if the function succeeds, and the attribute and known values do not match.


</dt> </dl> </dd> <dt>

<span id="LDAP_COMPARE_TRUE"></span><span id="ldap_compare_true"></span>**LDAP\_COMPARE\_TRUE**
</dt> <dd> <dl> <dt>

0x06
</dt> <dt>



For [**ldap\_compare\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare_ext_s) and [**ldap\_compare\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare_s), this message is returned if the function succeeds, and the attribute and known values match.


</dt> </dl> </dd> <dt>

<span id="LDAP_CONFIDENTIALITY_REQUIRED"></span><span id="ldap_confidentiality_required"></span>**LDAP\_CONFIDENTIALITY\_REQUIRED**
</dt> <dd> <dl> <dt>

0x0d
</dt> <dt>



Confidentiality is required.


</dt> </dl> </dd> <dt>

<span id="LDAP_CONNECT_ERROR"></span><span id="ldap_connect_error"></span>**LDAP\_CONNECT\_ERROR**
</dt> <dd> <dl> <dt>

0x5b
</dt> <dt>



Cannot establish the connection.


</dt> </dl> </dd> <dt>

<span id="LDAP_CONSTRAINT_VIOLATION"></span><span id="ldap_constraint_violation"></span>**LDAP\_CONSTRAINT\_VIOLATION**
</dt> <dd> <dl> <dt>

0x13
</dt> <dt>



There was a constraint violation.


</dt> </dl> </dd> <dt>

<span id="LDAP_CONTROL_NOT_FOUND"></span><span id="ldap_control_not_found"></span>**LDAP\_CONTROL\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x5d
</dt> <dt>



The LDAP function ([**ldap\_parse\_page\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_page_control), [**ldap\_parse\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_sort_control), or [**ldap\_parse\_vlv\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_vlv_controla)) did not find the specified control.


</dt> </dl> </dd> <dt>

<span id="LDAP_DECODING_ERROR"></span><span id="ldap_decoding_error"></span>**LDAP\_DECODING\_ERROR**
</dt> <dd> <dl> <dt>

0x54
</dt> <dt>



Decoding error occurred.


</dt> </dl> </dd> <dt>

<span id="LDAP_ENCODING_ERROR"></span><span id="ldap_encoding_error"></span>**LDAP\_ENCODING\_ERROR**
</dt> <dd> <dl> <dt>

0x53
</dt> <dt>



Encoding error occurred.


</dt> </dl> </dd> <dt>

<span id="LDAP_FILTER_ERROR"></span><span id="ldap_filter_error"></span>**LDAP\_FILTER\_ERROR**
</dt> <dd> <dl> <dt>

0x57
</dt> <dt>



The search filter is bad.


</dt> </dl> </dd> <dt>

<span id="LDAP_INAPPROPRIATE_AUTH"></span><span id="ldap_inappropriate_auth"></span>**LDAP\_INAPPROPRIATE\_AUTH**
</dt> <dd> <dl> <dt>

0x30
</dt> <dt>



Authentication is inappropriate.


</dt> </dl> </dd> <dt>

<span id="LDAP_INAPPROPRIATE_MATCHING"></span><span id="ldap_inappropriate_matching"></span>**LDAP\_INAPPROPRIATE\_MATCHING**
</dt> <dd> <dl> <dt>

0x12
</dt> <dt>



There was an inappropriate matching.


</dt> </dl> </dd> <dt>

<span id="LDAP_INSUFFICIENT_RIGHTS"></span><span id="ldap_insufficient_rights"></span>**LDAP\_INSUFFICIENT\_RIGHTS**
</dt> <dd> <dl> <dt>

0x32
</dt> <dt>



The user has insufficient access rights.


</dt> </dl> </dd> <dt>

<span id="LDAP_INVALID_CREDENTIALS"></span><span id="ldap_invalid_credentials"></span>**LDAP\_INVALID\_CREDENTIALS**
</dt> <dd> <dl> <dt>

0x31
</dt> <dt>



The supplied credential is invalid.


</dt> </dl> </dd> <dt>

<span id="LDAP_INVALID_DN_SYNTAX"></span><span id="ldap_invalid_dn_syntax"></span>**LDAP\_INVALID\_DN\_SYNTAX**
</dt> <dd> <dl> <dt>

0x22
</dt> <dt>



The distinguished name has an invalid syntax.


</dt> </dl> </dd> <dt>

<span id="LDAP_INVALID_SYNTAX"></span><span id="ldap_invalid_syntax"></span>**LDAP\_INVALID\_SYNTAX**
</dt> <dd> <dl> <dt>

0x15
</dt> <dt>



The syntax is invalid.


</dt> </dl> </dd> <dt>

<span id="LDAP_IS_LEAF"></span><span id="ldap_is_leaf"></span>**LDAP\_IS\_LEAF**
</dt> <dd> <dl> <dt>

0x23
</dt> <dt>



The object is a leaf.


</dt> </dl> </dd> <dt>

<span id="LDAP_LOCAL_ERROR"></span><span id="ldap_local_error"></span>**LDAP\_LOCAL\_ERROR**
</dt> <dd> <dl> <dt>

0x52
</dt> <dt>



Local error occurred. If this error occurs during a binding operation, for more information, see [**ldap\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind_s).


</dt> </dl> </dd> <dt>

<span id="LDAP_LOOP_DETECT"></span><span id="ldap_loop_detect"></span>**LDAP\_LOOP\_DETECT**
</dt> <dd> <dl> <dt>

0x36
</dt> <dt>



The chain of referrals has looped back to a referring server.


</dt> </dl> </dd> <dt>

<span id="LDAP_MORE_RESULTS_TO_RETURN"></span><span id="ldap_more_results_to_return"></span>**LDAP\_MORE\_RESULTS\_TO\_RETURN**
</dt> <dd> <dl> <dt>

0x5f
</dt> <dt>



More results are to be returned.


</dt> </dl> </dd> <dt>

<span id="LDAP_NAMING_VIOLATION"></span><span id="ldap_naming_violation"></span>**LDAP\_NAMING\_VIOLATION**
</dt> <dd> <dl> <dt>

0x40
</dt> <dt>



There was a naming violation.


</dt> </dl> </dd> <dt>

<span id="LDAP_NO_MEMORY"></span><span id="ldap_no_memory"></span>**LDAP\_NO\_MEMORY**
</dt> <dd> <dl> <dt>

0x5a
</dt> <dt>



The system is out of memory.


</dt> </dl> </dd> <dt>

<span id="LDAP_NO_OBJECT_CLASS_MODS"></span><span id="ldap_no_object_class_mods"></span>**LDAP\_NO\_OBJECT\_CLASS\_MODS**
</dt> <dd> <dl> <dt>

0x45
</dt> <dt>



Cannot modify object class.


</dt> </dl> </dd> <dt>

<span id="LDAP_NO_RESULTS_RETURNED"></span><span id="ldap_no_results_returned"></span>**LDAP\_NO\_RESULTS\_RETURNED**
</dt> <dd> <dl> <dt>

0x5e
</dt> <dt>



Results are not returned.


</dt> </dl> </dd> <dt>

<span id="LDAP_NO_SUCH_ATTRIBUTE"></span><span id="ldap_no_such_attribute"></span>**LDAP\_NO\_SUCH\_ATTRIBUTE**
</dt> <dd> <dl> <dt>

0x10
</dt> <dt>



Requested attribute does not exist.


</dt> </dl> </dd> <dt>

<span id="LDAP_NO_SUCH_OBJECT"></span><span id="ldap_no_such_object"></span>**LDAP\_NO\_SUCH\_OBJECT**
</dt> <dd> <dl> <dt>

0x20
</dt> <dt>



Object does not exist.


</dt> </dl> </dd> <dt>

<span id="LDAP_NOT_ALLOWED_ON_NONLEAF"></span><span id="ldap_not_allowed_on_nonleaf"></span>**LDAP\_NOT\_ALLOWED\_ON\_NONLEAF**
</dt> <dd> <dl> <dt>

0x42
</dt> <dt>



Operation is not allowed on a nonleaf object.


</dt> </dl> </dd> <dt>

<span id="LDAP_NOT_ALLOWED_ON_RDN"></span><span id="ldap_not_allowed_on_rdn"></span>**LDAP\_NOT\_ALLOWED\_ON\_RDN**
</dt> <dd> <dl> <dt>

0x43
</dt> <dt>



Operation is not allowed on RDN.


</dt> </dl> </dd> <dt>

<span id="LDAP_NOT_SUPPORTED"></span><span id="ldap_not_supported"></span>**LDAP\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

0x5c
</dt> <dt>



The feature is not supported.


</dt> </dl> </dd> <dt>

<span id="LDAP_OBJECT_CLASS_VIOLATION"></span><span id="ldap_object_class_violation"></span>**LDAP\_OBJECT\_CLASS\_VIOLATION**
</dt> <dd> <dl> <dt>

0x41
</dt> <dt>



There was an object class violation.


</dt> </dl> </dd> <dt>

<span id="LDAP_OPERATIONS_ERROR"></span><span id="ldap_operations_error"></span>**LDAP\_OPERATIONS\_ERROR**
</dt> <dd> <dl> <dt>

0x01
</dt> <dt>



Operations error occurred.


</dt> </dl> </dd> <dt>

<span id="LDAP_OTHER"></span><span id="ldap_other"></span>**LDAP\_OTHER**
</dt> <dd> <dl> <dt>

0x50
</dt> <dt>



Unknown error occurred.


</dt> </dl> </dd> <dt>

<span id="LDAP_PARAM_ERROR"></span><span id="ldap_param_error"></span>**LDAP\_PARAM\_ERROR**
</dt> <dd> <dl> <dt>

0x59
</dt> <dt>



A bad parameter was passed to a routine.


</dt> </dl> </dd> <dt>

<span id="LDAP_PARTIAL_RESULTS"></span><span id="ldap_partial_results"></span>**LDAP\_PARTIAL\_RESULTS**
</dt> <dd> <dl> <dt>

0x09
</dt> <dt>



Partial results and referrals received.

Note: Same error code as **LDAP\_REFERRAL\_V2**. The server returns the same result code for these two similar instances, v2 referral and continuation references.

For further information, see the protocol reference, [Referrals in LDAPv2 and LDAPv3](https://msdn.microsoft.com/library/cc223246.aspx).


</dt> </dl> </dd> <dt>

<span id="LDAP_PROTOCOL_ERROR"></span><span id="ldap_protocol_error"></span>**LDAP\_PROTOCOL\_ERROR**
</dt> <dd> <dl> <dt>

0x02
</dt> <dt>



Protocol error occurred.


</dt> </dl> </dd> <dt>

<span id="LDAP_REFERRAL"></span><span id="ldap_referral"></span>**LDAP\_REFERRAL**
</dt> <dd> <dl> <dt>

0x0a
</dt> <dt>



A referral was returned from the server.


</dt> </dl> </dd> <dt>

<span id="LDAP_REFERRAL_LIMIT_EXCEEDED"></span><span id="ldap_referral_limit_exceeded"></span>**LDAP\_REFERRAL\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

0x61
</dt> <dt>



The referral limit has been exceeded.


</dt> </dl> </dd> <dt>

<span id="LDAP_REFERRAL_V2"></span><span id="ldap_referral_v2"></span>**LDAP\_REFERRAL\_V2**
</dt> <dd> <dl> <dt>

0x09
</dt> <dt>



A referral was returned from the server.

Note: Same error code as **LDAP\_PARTIAL\_RESULTS**. The server returns the same result code for these two similar instances, v2 referral and continuation references.

For further information, see the protocol reference, [Referrals in LDAPv2 and LDAPv3](https://msdn.microsoft.com/library/cc223246.aspx).


</dt> </dl> </dd> <dt>

<span id="LDAP_RESULTS_TOO_LARGE"></span><span id="ldap_results_too_large"></span>**LDAP\_RESULTS\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

0x46
</dt> <dt>



Results returned are too large.


</dt> </dl> </dd> <dt>

<span id="LDAP_SERVER_DOWN"></span><span id="ldap_server_down"></span>**LDAP\_SERVER\_DOWN**
</dt> <dd> <dl> <dt>

0x51
</dt> <dt>



Cannot contact the LDAP server.


</dt> </dl> </dd> <dt>

<span id="LDAP_SIZELIMIT_EXCEEDED"></span><span id="ldap_sizelimit_exceeded"></span>**LDAP\_SIZELIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

0x04
</dt> <dt>



Size limit was exceeded.


</dt> </dl> </dd> <dt>

<span id="LDAP_STRONG_AUTH_REQUIRED"></span><span id="ldap_strong_auth_required"></span>**LDAP\_STRONG\_AUTH\_REQUIRED**
</dt> <dd> <dl> <dt>

0x08
</dt> <dt>



Strong authentication is required.


</dt> </dl> </dd> <dt>

<span id="LDAP_SUCCESS"></span><span id="ldap_success"></span>**LDAP\_SUCCESS**
</dt> <dd> <dl> <dt>

0x00
</dt> <dt>



The call completed successfully.


</dt> </dl> </dd> <dt>

<span id="LDAP_TIMELIMIT_EXCEEDED"></span><span id="ldap_timelimit_exceeded"></span>**LDAP\_TIMELIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

0x03
</dt> <dt>



Time limit, set by the server side time limit parameter, was exceeded.


</dt> </dl> </dd> <dt>

<span id="LDAP_TIMEOUT"></span><span id="ldap_timeout"></span>**LDAP\_TIMEOUT**
</dt> <dd> <dl> <dt>

0x55
</dt> <dt>



The search was aborted due to exceeding the limit of the client side timeout parameter.


</dt> </dl> </dd> <dt>

<span id="LDAP_UNAVAILABLE"></span><span id="ldap_unavailable"></span>**LDAP\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

0x34
</dt> <dt>



The server is unavailable.


</dt> </dl> </dd> <dt>

<span id="LDAP_UNAVAILABLE_CRIT_EXTENSION"></span><span id="ldap_unavailable_crit_extension"></span>**LDAP\_UNAVAILABLE\_CRIT\_EXTENSION**
</dt> <dd> <dl> <dt>

0x0c
</dt> <dt>



The control is critical and the server does not support the control.


</dt> </dl> </dd> <dt>

<span id="LDAP_UNDEFINED_TYPE"></span><span id="ldap_undefined_type"></span>**LDAP\_UNDEFINED\_TYPE**
</dt> <dd> <dl> <dt>

0x11
</dt> <dt>



Type is not defined.


</dt> </dl> </dd> <dt>

<span id="LDAP_UNWILLING_TO_PERFORM"></span><span id="ldap_unwilling_to_perform"></span>**LDAP\_UNWILLING\_TO\_PERFORM**
</dt> <dd> <dl> <dt>

0x35
</dt> <dt>



The server is not willing to handle directory requests.


</dt> </dl> </dd> <dt>

<span id="LDAP_USER_CANCELLED"></span><span id="ldap_user_cancelled"></span>**LDAP\_USER\_CANCELLED**
</dt> <dd> <dl> <dt>

0x58
</dt> <dt>



The user has canceled the operation.


</dt> </dl> </dd> <dt>

<span id="LDAP_VIRTUAL_LIST_VIEW_ERROR"></span><span id="ldap_virtual_list_view_error"></span>**LDAP\_VIRTUAL\_LIST\_VIEW\_ERROR**
</dt> <dd> <dl> <dt>

0x4c
</dt> <dt>



An error occurred when attempting to perform a requested Virtual List View operation. A detailed error code is returned in the **ldctl\_value** field of the [LDAP\_CONTROL\_VLVRESPONSE](ldap-control-vlvresponse.md) control.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winldap.h</dt> </dl> |



## See also

<dl> <dt>

[Understanding Return Values](understanding-return-values.md)
</dt> <dt>

[**ldap\_err2string**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_err2string)
</dt> <dt>

[**LdapGetLastError**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldapgetlasterror)
</dt> <dt>

[**LdapMapErrorToWin32**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldapmaperrortowin32)
</dt> <dt>

[**ldap\_result2error**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_result2error)
</dt> </dl>

 

 





