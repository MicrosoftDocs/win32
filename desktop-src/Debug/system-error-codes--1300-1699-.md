---
description: Describes error codes 1300-1699 defined in the WinError.h header file and is intended for developers.
ms.assetid: 7b04a2ba-7bf9-4bff-93c8-cbb0060e069d
title: System Error Codes (1300-1699) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (1300-1699)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) for errors 1300 to 1699. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="ERROR_NOT_ALL_ASSIGNED"></span><span id="error_not_all_assigned"></span>**ERROR\_NOT\_ALL\_ASSIGNED**
</dt> <dd> <dl> <dt>

1300 (0x514)
</dt> <dt>



Not all privileges or groups referenced are assigned to the caller.


</dt> </dl> </dd> <dt>

<span id="ERROR_SOME_NOT_MAPPED"></span><span id="error_some_not_mapped"></span>**ERROR\_SOME\_NOT\_MAPPED**
</dt> <dd> <dl> <dt>

1301 (0x515)
</dt> <dt>



Some mapping between account names and security IDs was not done.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_QUOTAS_FOR_ACCOUNT"></span><span id="error_no_quotas_for_account"></span>**ERROR\_NO\_QUOTAS\_FOR\_ACCOUNT**
</dt> <dd> <dl> <dt>

1302 (0x516)
</dt> <dt>



No system quota limits are specifically set for this account.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOCAL_USER_SESSION_KEY"></span><span id="error_local_user_session_key"></span>**ERROR\_LOCAL\_USER\_SESSION\_KEY**
</dt> <dd> <dl> <dt>

1303 (0x517)
</dt> <dt>



No encryption key is available. A well-known encryption key was returned.


</dt> </dl> </dd> <dt>

<span id="ERROR_NULL_LM_PASSWORD"></span><span id="error_null_lm_password"></span>**ERROR\_NULL\_LM\_PASSWORD**
</dt> <dd> <dl> <dt>

1304 (0x518)
</dt> <dt>



The password is too complex to be converted to a LAN Manager password. The LAN Manager password returned is a **NULL** string.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_REVISION"></span><span id="error_unknown_revision"></span>**ERROR\_UNKNOWN\_REVISION**
</dt> <dd> <dl> <dt>

1305 (0x519)
</dt> <dt>



The revision level is unknown.


</dt> </dl> </dd> <dt>

<span id="ERROR_REVISION_MISMATCH"></span><span id="error_revision_mismatch"></span>**ERROR\_REVISION\_MISMATCH**
</dt> <dd> <dl> <dt>

1306 (0x51A)
</dt> <dt>



Indicates two revision levels are incompatible.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_OWNER"></span><span id="error_invalid_owner"></span>**ERROR\_INVALID\_OWNER**
</dt> <dd> <dl> <dt>

1307 (0x51B)
</dt> <dt>



This security ID may not be assigned as the owner of this object.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PRIMARY_GROUP"></span><span id="error_invalid_primary_group"></span>**ERROR\_INVALID\_PRIMARY\_GROUP**
</dt> <dd> <dl> <dt>

1308 (0x51C)
</dt> <dt>



This security ID may not be assigned as the primary group of an object.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_IMPERSONATION_TOKEN"></span><span id="error_no_impersonation_token"></span>**ERROR\_NO\_IMPERSONATION\_TOKEN**
</dt> <dd> <dl> <dt>

1309 (0x51D)
</dt> <dt>



An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_DISABLE_MANDATORY"></span><span id="error_cant_disable_mandatory"></span>**ERROR\_CANT\_DISABLE\_MANDATORY**
</dt> <dd> <dl> <dt>

1310 (0x51E)
</dt> <dt>



The group may not be disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_LOGON_SERVERS"></span><span id="error_no_logon_servers"></span>**ERROR\_NO\_LOGON\_SERVERS**
</dt> <dd> <dl> <dt>

1311 (0x51F)
</dt> <dt>



There are currently no logon servers available to service the logon request.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_LOGON_SESSION"></span><span id="error_no_such_logon_session"></span>**ERROR\_NO\_SUCH\_LOGON\_SESSION**
</dt> <dd> <dl> <dt>

1312 (0x520)
</dt> <dt>



A specified logon session does not exist. It may already have been terminated.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_PRIVILEGE"></span><span id="error_no_such_privilege"></span>**ERROR\_NO\_SUCH\_PRIVILEGE**
</dt> <dd> <dl> <dt>

1313 (0x521)
</dt> <dt>



A specified privilege does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRIVILEGE_NOT_HELD"></span><span id="error_privilege_not_held"></span>**ERROR\_PRIVILEGE\_NOT\_HELD**
</dt> <dd> <dl> <dt>

1314 (0x522)
</dt> <dt>



A required privilege is not held by the client.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ACCOUNT_NAME"></span><span id="error_invalid_account_name"></span>**ERROR\_INVALID\_ACCOUNT\_NAME**
</dt> <dd> <dl> <dt>

1315 (0x523)
</dt> <dt>



The name provided is not a properly formed account name.


</dt> </dl> </dd> <dt>

<span id="ERROR_USER_EXISTS"></span><span id="error_user_exists"></span>**ERROR\_USER\_EXISTS**
</dt> <dd> <dl> <dt>

1316 (0x524)
</dt> <dt>



The specified account already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_USER"></span><span id="error_no_such_user"></span>**ERROR\_NO\_SUCH\_USER**
</dt> <dd> <dl> <dt>

1317 (0x525)
</dt> <dt>



The specified account does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_GROUP_EXISTS"></span><span id="error_group_exists"></span>**ERROR\_GROUP\_EXISTS**
</dt> <dd> <dl> <dt>

1318 (0x526)
</dt> <dt>



The specified group already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_GROUP"></span><span id="error_no_such_group"></span>**ERROR\_NO\_SUCH\_GROUP**
</dt> <dd> <dl> <dt>

1319 (0x527)
</dt> <dt>



The specified group does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEMBER_IN_GROUP"></span><span id="error_member_in_group"></span>**ERROR\_MEMBER\_IN\_GROUP**
</dt> <dd> <dl> <dt>

1320 (0x528)
</dt> <dt>



Either the specified user account is already a member of the specified group, or the specified group cannot be deleted because it contains a member.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEMBER_NOT_IN_GROUP"></span><span id="error_member_not_in_group"></span>**ERROR\_MEMBER\_NOT\_IN\_GROUP**
</dt> <dd> <dl> <dt>

1321 (0x529)
</dt> <dt>



The specified user account is not a member of the specified group account.


</dt> </dl> </dd> <dt>

<span id="ERROR_LAST_ADMIN"></span><span id="error_last_admin"></span>**ERROR\_LAST\_ADMIN**
</dt> <dd> <dl> <dt>

1322 (0x52A)
</dt> <dt>



This operation is disallowed as it could result in an administration account being disabled, deleted or unable to log on.


</dt> </dl> </dd> <dt>

<span id="ERROR_WRONG_PASSWORD"></span><span id="error_wrong_password"></span>**ERROR\_WRONG\_PASSWORD**
</dt> <dd> <dl> <dt>

1323 (0x52B)
</dt> <dt>



Unable to update the password. The value provided as the current password is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_ILL_FORMED_PASSWORD"></span><span id="error_ill_formed_password"></span>**ERROR\_ILL\_FORMED\_PASSWORD**
</dt> <dd> <dl> <dt>

1324 (0x52C)
</dt> <dt>



Unable to update the password. The value provided for the new password contains values that are not allowed in passwords.


</dt> </dl> </dd> <dt>

<span id="ERROR_PASSWORD_RESTRICTION"></span><span id="error_password_restriction"></span>**ERROR\_PASSWORD\_RESTRICTION**
</dt> <dd> <dl> <dt>

1325 (0x52D)
</dt> <dt>



Unable to update the password. The value provided for the new password does not meet the length, complexity, or history requirements of the domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGON_FAILURE"></span><span id="error_logon_failure"></span>**ERROR\_LOGON\_FAILURE**
</dt> <dd> <dl> <dt>

1326 (0x52E)
</dt> <dt>



The user name or password is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCOUNT_RESTRICTION"></span><span id="error_account_restriction"></span>**ERROR\_ACCOUNT\_RESTRICTION**
</dt> <dd> <dl> <dt>

1327 (0x52F)
</dt> <dt>



Account restrictions are preventing this user from signing in. For example: blank passwords aren't allowed, sign-in times are limited, or a policy restriction has been enforced.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LOGON_HOURS"></span><span id="error_invalid_logon_hours"></span>**ERROR\_INVALID\_LOGON\_HOURS**
</dt> <dd> <dl> <dt>

1328 (0x530)
</dt> <dt>



Your account has time restrictions that keep you from signing in right now.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_WORKSTATION"></span><span id="error_invalid_workstation"></span>**ERROR\_INVALID\_WORKSTATION**
</dt> <dd> <dl> <dt>

1329 (0x531)
</dt> <dt>



This user isn't allowed to sign in to this computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_PASSWORD_EXPIRED"></span><span id="error_password_expired"></span>**ERROR\_PASSWORD\_EXPIRED**
</dt> <dd> <dl> <dt>

1330 (0x532)
</dt> <dt>



The password for this account has expired.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCOUNT_DISABLED"></span><span id="error_account_disabled"></span>**ERROR\_ACCOUNT\_DISABLED**
</dt> <dd> <dl> <dt>

1331 (0x533)
</dt> <dt>



This user can't sign in because this account is currently disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_NONE_MAPPED"></span><span id="error_none_mapped"></span>**ERROR\_NONE\_MAPPED**
</dt> <dd> <dl> <dt>

1332 (0x534)
</dt> <dt>



No mapping between account names and security IDs was done.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_LUIDS_REQUESTED"></span><span id="error_too_many_luids_requested"></span>**ERROR\_TOO\_MANY\_LUIDS\_REQUESTED**
</dt> <dd> <dl> <dt>

1333 (0x535)
</dt> <dt>



Too many local user identifiers (LUIDs) were requested at one time.


</dt> </dl> </dd> <dt>

<span id="ERROR_LUIDS_EXHAUSTED"></span><span id="error_luids_exhausted"></span>**ERROR\_LUIDS\_EXHAUSTED**
</dt> <dd> <dl> <dt>

1334 (0x536)
</dt> <dt>



No more local user identifiers (LUIDs) are available.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SUB_AUTHORITY"></span><span id="error_invalid_sub_authority"></span>**ERROR\_INVALID\_SUB\_AUTHORITY**
</dt> <dd> <dl> <dt>

1335 (0x537)
</dt> <dt>



The subauthority part of a security ID is invalid for this particular use.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ACL"></span><span id="error_invalid_acl"></span>**ERROR\_INVALID\_ACL**
</dt> <dd> <dl> <dt>

1336 (0x538)
</dt> <dt>



The access control list (ACL) structure is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SID"></span><span id="error_invalid_sid"></span>**ERROR\_INVALID\_SID**
</dt> <dd> <dl> <dt>

1337 (0x539)
</dt> <dt>



The security ID structure is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SECURITY_DESCR"></span><span id="error_invalid_security_descr"></span>**ERROR\_INVALID\_SECURITY\_DESCR**
</dt> <dd> <dl> <dt>

1338 (0x53A)
</dt> <dt>



The security descriptor structure is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_INHERITANCE_ACL"></span><span id="error_bad_inheritance_acl"></span>**ERROR\_BAD\_INHERITANCE\_ACL**
</dt> <dd> <dl> <dt>

1340 (0x53C)
</dt> <dt>



The inherited access control list (ACL) or access control entry (ACE) could not be built.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVER_DISABLED"></span><span id="error_server_disabled"></span>**ERROR\_SERVER\_DISABLED**
</dt> <dd> <dl> <dt>

1341 (0x53D)
</dt> <dt>



The server is currently disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVER_NOT_DISABLED"></span><span id="error_server_not_disabled"></span>**ERROR\_SERVER\_NOT\_DISABLED**
</dt> <dd> <dl> <dt>

1342 (0x53E)
</dt> <dt>



The server is currently enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ID_AUTHORITY"></span><span id="error_invalid_id_authority"></span>**ERROR\_INVALID\_ID\_AUTHORITY**
</dt> <dd> <dl> <dt>

1343 (0x53F)
</dt> <dt>



The value provided was an invalid value for an identifier authority.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALLOTTED_SPACE_EXCEEDED"></span><span id="error_allotted_space_exceeded"></span>**ERROR\_ALLOTTED\_SPACE\_EXCEEDED**
</dt> <dd> <dl> <dt>

1344 (0x540)
</dt> <dt>



No more memory is available for security information updates.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_GROUP_ATTRIBUTES"></span><span id="error_invalid_group_attributes"></span>**ERROR\_INVALID\_GROUP\_ATTRIBUTES**
</dt> <dd> <dl> <dt>

1345 (0x541)
</dt> <dt>



The specified attributes are invalid, or incompatible with the attributes for the group as a whole.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_IMPERSONATION_LEVEL"></span><span id="error_bad_impersonation_level"></span>**ERROR\_BAD\_IMPERSONATION\_LEVEL**
</dt> <dd> <dl> <dt>

1346 (0x542)
</dt> <dt>



Either a required impersonation level was not provided, or the provided impersonation level is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_OPEN_ANONYMOUS"></span><span id="error_cant_open_anonymous"></span>**ERROR\_CANT\_OPEN\_ANONYMOUS**
</dt> <dd> <dl> <dt>

1347 (0x543)
</dt> <dt>



Cannot open an anonymous level security token.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_VALIDATION_CLASS"></span><span id="error_bad_validation_class"></span>**ERROR\_BAD\_VALIDATION\_CLASS**
</dt> <dd> <dl> <dt>

1348 (0x544)
</dt> <dt>



The validation information class requested was invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_TOKEN_TYPE"></span><span id="error_bad_token_type"></span>**ERROR\_BAD\_TOKEN\_TYPE**
</dt> <dd> <dl> <dt>

1349 (0x545)
</dt> <dt>



The type of the token is inappropriate for its attempted use.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SECURITY_ON_OBJECT"></span><span id="error_no_security_on_object"></span>**ERROR\_NO\_SECURITY\_ON\_OBJECT**
</dt> <dd> <dl> <dt>

1350 (0x546)
</dt> <dt>



Unable to perform a security operation on an object that has no associated security.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_ACCESS_DOMAIN_INFO"></span><span id="error_cant_access_domain_info"></span>**ERROR\_CANT\_ACCESS\_DOMAIN\_INFO**
</dt> <dd> <dl> <dt>

1351 (0x547)
</dt> <dt>



Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SERVER_STATE"></span><span id="error_invalid_server_state"></span>**ERROR\_INVALID\_SERVER\_STATE**
</dt> <dd> <dl> <dt>

1352 (0x548)
</dt> <dt>



The security account manager (SAM) or local security authority (LSA) server was in the wrong state to perform the security operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DOMAIN_STATE"></span><span id="error_invalid_domain_state"></span>**ERROR\_INVALID\_DOMAIN\_STATE**
</dt> <dd> <dl> <dt>

1353 (0x549)
</dt> <dt>



The domain was in the wrong state to perform the security operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DOMAIN_ROLE"></span><span id="error_invalid_domain_role"></span>**ERROR\_INVALID\_DOMAIN\_ROLE**
</dt> <dd> <dl> <dt>

1354 (0x54A)
</dt> <dt>



This operation is only allowed for the Primary Domain Controller of the domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_DOMAIN"></span><span id="error_no_such_domain"></span>**ERROR\_NO\_SUCH\_DOMAIN**
</dt> <dd> <dl> <dt>

1355 (0x54B)
</dt> <dt>



The specified domain either does not exist or could not be contacted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOMAIN_EXISTS"></span><span id="error_domain_exists"></span>**ERROR\_DOMAIN\_EXISTS**
</dt> <dd> <dl> <dt>

1356 (0x54C)
</dt> <dt>



The specified domain already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOMAIN_LIMIT_EXCEEDED"></span><span id="error_domain_limit_exceeded"></span>**ERROR\_DOMAIN\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

1357 (0x54D)
</dt> <dt>



An attempt was made to exceed the limit on the number of domains per server.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNAL_DB_CORRUPTION"></span><span id="error_internal_db_corruption"></span>**ERROR\_INTERNAL\_DB\_CORRUPTION**
</dt> <dd> <dl> <dt>

1358 (0x54E)
</dt> <dt>



Unable to complete the requested operation because of either a catastrophic media failure or a data structure corruption on the disk.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNAL_ERROR"></span><span id="error_internal_error"></span>**ERROR\_INTERNAL\_ERROR**
</dt> <dd> <dl> <dt>

1359 (0x54F)
</dt> <dt>



An internal error occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_GENERIC_NOT_MAPPED"></span><span id="error_generic_not_mapped"></span>**ERROR\_GENERIC\_NOT\_MAPPED**
</dt> <dd> <dl> <dt>

1360 (0x550)
</dt> <dt>



Generic access types were contained in an access mask which should already be mapped to nongeneric types.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_DESCRIPTOR_FORMAT"></span><span id="error_bad_descriptor_format"></span>**ERROR\_BAD\_DESCRIPTOR\_FORMAT**
</dt> <dd> <dl> <dt>

1361 (0x551)
</dt> <dt>



A security descriptor is not in the right format (absolute or self-relative).


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_LOGON_PROCESS"></span><span id="error_not_logon_process"></span>**ERROR\_NOT\_LOGON\_PROCESS**
</dt> <dd> <dl> <dt>

1362 (0x552)
</dt> <dt>



The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGON_SESSION_EXISTS"></span><span id="error_logon_session_exists"></span>**ERROR\_LOGON\_SESSION\_EXISTS**
</dt> <dd> <dl> <dt>

1363 (0x553)
</dt> <dt>



Cannot start a new logon session with an ID that is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_PACKAGE"></span><span id="error_no_such_package"></span>**ERROR\_NO\_SUCH\_PACKAGE**
</dt> <dd> <dl> <dt>

1364 (0x554)
</dt> <dt>



A specified authentication package is unknown.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_LOGON_SESSION_STATE"></span><span id="error_bad_logon_session_state"></span>**ERROR\_BAD\_LOGON\_SESSION\_STATE**
</dt> <dd> <dl> <dt>

1365 (0x555)
</dt> <dt>



The logon session is not in a state that is consistent with the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGON_SESSION_COLLISION"></span><span id="error_logon_session_collision"></span>**ERROR\_LOGON\_SESSION\_COLLISION**
</dt> <dd> <dl> <dt>

1366 (0x556)
</dt> <dt>



The logon session ID is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LOGON_TYPE"></span><span id="error_invalid_logon_type"></span>**ERROR\_INVALID\_LOGON\_TYPE**
</dt> <dd> <dl> <dt>

1367 (0x557)
</dt> <dt>



A logon request contained an invalid logon type value.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_IMPERSONATE"></span><span id="error_cannot_impersonate"></span>**ERROR\_CANNOT\_IMPERSONATE**
</dt> <dd> <dl> <dt>

1368 (0x558)
</dt> <dt>



Unable to impersonate using a named pipe until data has been read from that pipe.


</dt> </dl> </dd> <dt>

<span id="ERROR_RXACT_INVALID_STATE"></span><span id="error_rxact_invalid_state"></span>**ERROR\_RXACT\_INVALID\_STATE**
</dt> <dd> <dl> <dt>

1369 (0x559)
</dt> <dt>



The transaction state of a registry subtree is incompatible with the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_RXACT_COMMIT_FAILURE"></span><span id="error_rxact_commit_failure"></span>**ERROR\_RXACT\_COMMIT\_FAILURE**
</dt> <dd> <dl> <dt>

1370 (0x55A)
</dt> <dt>



An internal security database corruption has been encountered.


</dt> </dl> </dd> <dt>

<span id="ERROR_SPECIAL_ACCOUNT"></span><span id="error_special_account"></span>**ERROR\_SPECIAL\_ACCOUNT**
</dt> <dd> <dl> <dt>

1371 (0x55B)
</dt> <dt>



Cannot perform this operation on built-in accounts.


</dt> </dl> </dd> <dt>

<span id="ERROR_SPECIAL_GROUP"></span><span id="error_special_group"></span>**ERROR\_SPECIAL\_GROUP**
</dt> <dd> <dl> <dt>

1372 (0x55C)
</dt> <dt>



Cannot perform this operation on this built-in special group.


</dt> </dl> </dd> <dt>

<span id="ERROR_SPECIAL_USER"></span><span id="error_special_user"></span>**ERROR\_SPECIAL\_USER**
</dt> <dd> <dl> <dt>

1373 (0x55D)
</dt> <dt>



Cannot perform this operation on this built-in special user.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEMBERS_PRIMARY_GROUP"></span><span id="error_members_primary_group"></span>**ERROR\_MEMBERS\_PRIMARY\_GROUP**
</dt> <dd> <dl> <dt>

1374 (0x55E)
</dt> <dt>



The user cannot be removed from a group because the group is currently the user's primary group.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOKEN_ALREADY_IN_USE"></span><span id="error_token_already_in_use"></span>**ERROR\_TOKEN\_ALREADY\_IN\_USE**
</dt> <dd> <dl> <dt>

1375 (0x55F)
</dt> <dt>



The token is already in use as a primary token.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_ALIAS"></span><span id="error_no_such_alias"></span>**ERROR\_NO\_SUCH\_ALIAS**
</dt> <dd> <dl> <dt>

1376 (0x560)
</dt> <dt>



The specified local group does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEMBER_NOT_IN_ALIAS"></span><span id="error_member_not_in_alias"></span>**ERROR\_MEMBER\_NOT\_IN\_ALIAS**
</dt> <dd> <dl> <dt>

1377 (0x561)
</dt> <dt>



The specified account name is not a member of the group.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEMBER_IN_ALIAS"></span><span id="error_member_in_alias"></span>**ERROR\_MEMBER\_IN\_ALIAS**
</dt> <dd> <dl> <dt>

1378 (0x562)
</dt> <dt>



The specified account name is already a member of the group.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALIAS_EXISTS"></span><span id="error_alias_exists"></span>**ERROR\_ALIAS\_EXISTS**
</dt> <dd> <dl> <dt>

1379 (0x563)
</dt> <dt>



The specified local group already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGON_NOT_GRANTED"></span><span id="error_logon_not_granted"></span>**ERROR\_LOGON\_NOT\_GRANTED**
</dt> <dd> <dl> <dt>

1380 (0x564)
</dt> <dt>



Logon failure: the user has not been granted the requested logon type at this computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_SECRETS"></span><span id="error_too_many_secrets"></span>**ERROR\_TOO\_MANY\_SECRETS**
</dt> <dd> <dl> <dt>

1381 (0x565)
</dt> <dt>



The maximum number of secrets that may be stored in a single system has been exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECRET_TOO_LONG"></span><span id="error_secret_too_long"></span>**ERROR\_SECRET\_TOO\_LONG**
</dt> <dd> <dl> <dt>

1382 (0x566)
</dt> <dt>



The length of a secret exceeds the maximum length allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNAL_DB_ERROR"></span><span id="error_internal_db_error"></span>**ERROR\_INTERNAL\_DB\_ERROR**
</dt> <dd> <dl> <dt>

1383 (0x567)
</dt> <dt>



The local security authority database contains an internal inconsistency.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_CONTEXT_IDS"></span><span id="error_too_many_context_ids"></span>**ERROR\_TOO\_MANY\_CONTEXT\_IDS**
</dt> <dd> <dl> <dt>

1384 (0x568)
</dt> <dt>



During a logon attempt, the user's security context accumulated too many security IDs.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGON_TYPE_NOT_GRANTED"></span><span id="error_logon_type_not_granted"></span>**ERROR\_LOGON\_TYPE\_NOT\_GRANTED**
</dt> <dd> <dl> <dt>

1385 (0x569)
</dt> <dt>



Logon failure: the user has not been granted the requested logon type at this computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_NT_CROSS_ENCRYPTION_REQUIRED"></span><span id="error_nt_cross_encryption_required"></span>**ERROR\_NT\_CROSS\_ENCRYPTION\_REQUIRED**
</dt> <dd> <dl> <dt>

1386 (0x56A)
</dt> <dt>



A cross-encrypted password is necessary to change a user password.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_MEMBER"></span><span id="error_no_such_member"></span>**ERROR\_NO\_SUCH\_MEMBER**
</dt> <dd> <dl> <dt>

1387 (0x56B)
</dt> <dt>



A member could not be added to or removed from the local group because the member does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MEMBER"></span><span id="error_invalid_member"></span>**ERROR\_INVALID\_MEMBER**
</dt> <dd> <dl> <dt>

1388 (0x56C)
</dt> <dt>



A new member could not be added to a local group because the member has the wrong account type.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_SIDS"></span><span id="error_too_many_sids"></span>**ERROR\_TOO\_MANY\_SIDS**
</dt> <dd> <dl> <dt>

1389 (0x56D)
</dt> <dt>



Too many security IDs have been specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_LM_CROSS_ENCRYPTION_REQUIRED"></span><span id="error_lm_cross_encryption_required"></span>**ERROR\_LM\_CROSS\_ENCRYPTION\_REQUIRED**
</dt> <dd> <dl> <dt>

1390 (0x56E)
</dt> <dt>



A cross-encrypted password is necessary to change this user password.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_INHERITANCE"></span><span id="error_no_inheritance"></span>**ERROR\_NO\_INHERITANCE**
</dt> <dd> <dl> <dt>

1391 (0x56F)
</dt> <dt>



Indicates an ACL contains no inheritable components.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_CORRUPT"></span><span id="error_file_corrupt"></span>**ERROR\_FILE\_CORRUPT**
</dt> <dd> <dl> <dt>

1392 (0x570)
</dt> <dt>



The file or directory is corrupted and unreadable.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_CORRUPT"></span><span id="error_disk_corrupt"></span>**ERROR\_DISK\_CORRUPT**
</dt> <dd> <dl> <dt>

1393 (0x571)
</dt> <dt>



The disk structure is corrupted and unreadable.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_USER_SESSION_KEY"></span><span id="error_no_user_session_key"></span>**ERROR\_NO\_USER\_SESSION\_KEY**
</dt> <dd> <dl> <dt>

1394 (0x572)
</dt> <dt>



There is no user session key for the specified logon session.


</dt> </dl> </dd> <dt>

<span id="ERROR_LICENSE_QUOTA_EXCEEDED"></span><span id="error_license_quota_exceeded"></span>**ERROR\_LICENSE\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

1395 (0x573)
</dt> <dt>



The service being accessed is licensed for a particular number of connections. No more connections can be made to the service at this time because there are already as many connections as the service can accept.


</dt> </dl> </dd> <dt>

<span id="ERROR_WRONG_TARGET_NAME"></span><span id="error_wrong_target_name"></span>**ERROR\_WRONG\_TARGET\_NAME**
</dt> <dd> <dl> <dt>

1396 (0x574)
</dt> <dt>



The target account name is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUTUAL_AUTH_FAILED"></span><span id="error_mutual_auth_failed"></span>**ERROR\_MUTUAL\_AUTH\_FAILED**
</dt> <dd> <dl> <dt>

1397 (0x575)
</dt> <dt>



Mutual Authentication failed. The server's password is out of date at the domain controller.


</dt> </dl> </dd> <dt>

<span id="ERROR_TIME_SKEW"></span><span id="error_time_skew"></span>**ERROR\_TIME\_SKEW**
</dt> <dd> <dl> <dt>

1398 (0x576)
</dt> <dt>



There is a time and/or date difference between the client and server.


</dt> </dl> </dd> <dt>

<span id="ERROR_CURRENT_DOMAIN_NOT_ALLOWED"></span><span id="error_current_domain_not_allowed"></span>**ERROR\_CURRENT\_DOMAIN\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

1399 (0x577)
</dt> <dt>



This operation cannot be performed on the current domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_WINDOW_HANDLE"></span><span id="error_invalid_window_handle"></span>**ERROR\_INVALID\_WINDOW\_HANDLE**
</dt> <dd> <dl> <dt>

1400 (0x578)
</dt> <dt>



Invalid window handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MENU_HANDLE"></span><span id="error_invalid_menu_handle"></span>**ERROR\_INVALID\_MENU\_HANDLE**
</dt> <dd> <dl> <dt>

1401 (0x579)
</dt> <dt>



Invalid menu handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_CURSOR_HANDLE"></span><span id="error_invalid_cursor_handle"></span>**ERROR\_INVALID\_CURSOR\_HANDLE**
</dt> <dd> <dl> <dt>

1402 (0x57A)
</dt> <dt>



Invalid cursor handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ACCEL_HANDLE"></span><span id="error_invalid_accel_handle"></span>**ERROR\_INVALID\_ACCEL\_HANDLE**
</dt> <dd> <dl> <dt>

1403 (0x57B)
</dt> <dt>



Invalid accelerator table handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_HOOK_HANDLE"></span><span id="error_invalid_hook_handle"></span>**ERROR\_INVALID\_HOOK\_HANDLE**
</dt> <dd> <dl> <dt>

1404 (0x57C)
</dt> <dt>



Invalid hook handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DWP_HANDLE"></span><span id="error_invalid_dwp_handle"></span>**ERROR\_INVALID\_DWP\_HANDLE**
</dt> <dd> <dl> <dt>

1405 (0x57D)
</dt> <dt>



Invalid handle to a multiple-window position structure.


</dt> </dl> </dd> <dt>

<span id="ERROR_TLW_WITH_WSCHILD"></span><span id="error_tlw_with_wschild"></span>**ERROR\_TLW\_WITH\_WSCHILD**
</dt> <dd> <dl> <dt>

1406 (0x57E)
</dt> <dt>



Cannot create a top-level child window.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_FIND_WND_CLASS"></span><span id="error_cannot_find_wnd_class"></span>**ERROR\_CANNOT\_FIND\_WND\_CLASS**
</dt> <dd> <dl> <dt>

1407 (0x57F)
</dt> <dt>



Cannot find window class.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINDOW_OF_OTHER_THREAD"></span><span id="error_window_of_other_thread"></span>**ERROR\_WINDOW\_OF\_OTHER\_THREAD**
</dt> <dd> <dl> <dt>

1408 (0x580)
</dt> <dt>



Invalid window; it belongs to other thread.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOTKEY_ALREADY_REGISTERED"></span><span id="error_hotkey_already_registered"></span>**ERROR\_HOTKEY\_ALREADY\_REGISTERED**
</dt> <dd> <dl> <dt>

1409 (0x581)
</dt> <dt>



Hot key is already registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLASS_ALREADY_EXISTS"></span><span id="error_class_already_exists"></span>**ERROR\_CLASS\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

1410 (0x582)
</dt> <dt>



Class already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLASS_DOES_NOT_EXIST"></span><span id="error_class_does_not_exist"></span>**ERROR\_CLASS\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

1411 (0x583)
</dt> <dt>



Class does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLASS_HAS_WINDOWS"></span><span id="error_class_has_windows"></span>**ERROR\_CLASS\_HAS\_WINDOWS**
</dt> <dd> <dl> <dt>

1412 (0x584)
</dt> <dt>



Class still has open windows.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_INDEX"></span><span id="error_invalid_index"></span>**ERROR\_INVALID\_INDEX**
</dt> <dd> <dl> <dt>

1413 (0x585)
</dt> <dt>



Invalid index.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ICON_HANDLE"></span><span id="error_invalid_icon_handle"></span>**ERROR\_INVALID\_ICON\_HANDLE**
</dt> <dd> <dl> <dt>

1414 (0x586)
</dt> <dt>



Invalid icon handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRIVATE_DIALOG_INDEX"></span><span id="error_private_dialog_index"></span>**ERROR\_PRIVATE\_DIALOG\_INDEX**
</dt> <dd> <dl> <dt>

1415 (0x587)
</dt> <dt>



Using private DIALOG window words.


</dt> </dl> </dd> <dt>

<span id="ERROR_LISTBOX_ID_NOT_FOUND"></span><span id="error_listbox_id_not_found"></span>**ERROR\_LISTBOX\_ID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1416 (0x588)
</dt> <dt>



The list box identifier was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_WILDCARD_CHARACTERS"></span><span id="error_no_wildcard_characters"></span>**ERROR\_NO\_WILDCARD\_CHARACTERS**
</dt> <dd> <dl> <dt>

1417 (0x589)
</dt> <dt>



No wildcards were found.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLIPBOARD_NOT_OPEN"></span><span id="error_clipboard_not_open"></span>**ERROR\_CLIPBOARD\_NOT\_OPEN**
</dt> <dd> <dl> <dt>

1418 (0x58A)
</dt> <dt>



Thread does not have a clipboard open.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOTKEY_NOT_REGISTERED"></span><span id="error_hotkey_not_registered"></span>**ERROR\_HOTKEY\_NOT\_REGISTERED**
</dt> <dd> <dl> <dt>

1419 (0x58B)
</dt> <dt>



Hot key is not registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINDOW_NOT_DIALOG"></span><span id="error_window_not_dialog"></span>**ERROR\_WINDOW\_NOT\_DIALOG**
</dt> <dd> <dl> <dt>

1420 (0x58C)
</dt> <dt>



The window is not a valid dialog window.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONTROL_ID_NOT_FOUND"></span><span id="error_control_id_not_found"></span>**ERROR\_CONTROL\_ID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1421 (0x58D)
</dt> <dt>



Control ID not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_COMBOBOX_MESSAGE"></span><span id="error_invalid_combobox_message"></span>**ERROR\_INVALID\_COMBOBOX\_MESSAGE**
</dt> <dd> <dl> <dt>

1422 (0x58E)
</dt> <dt>



Invalid message for a combo box because it does not have an edit control.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINDOW_NOT_COMBOBOX"></span><span id="error_window_not_combobox"></span>**ERROR\_WINDOW\_NOT\_COMBOBOX**
</dt> <dd> <dl> <dt>

1423 (0x58F)
</dt> <dt>



The window is not a combo box.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_EDIT_HEIGHT"></span><span id="error_invalid_edit_height"></span>**ERROR\_INVALID\_EDIT\_HEIGHT**
</dt> <dd> <dl> <dt>

1424 (0x590)
</dt> <dt>



Height must be less than 256.


</dt> </dl> </dd> <dt>

<span id="ERROR_DC_NOT_FOUND"></span><span id="error_dc_not_found"></span>**ERROR\_DC\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1425 (0x591)
</dt> <dt>



Invalid device context (DC) handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_HOOK_FILTER"></span><span id="error_invalid_hook_filter"></span>**ERROR\_INVALID\_HOOK\_FILTER**
</dt> <dd> <dl> <dt>

1426 (0x592)
</dt> <dt>



Invalid hook procedure type.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FILTER_PROC"></span><span id="error_invalid_filter_proc"></span>**ERROR\_INVALID\_FILTER\_PROC**
</dt> <dd> <dl> <dt>

1427 (0x593)
</dt> <dt>



Invalid hook procedure.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOOK_NEEDS_HMOD"></span><span id="error_hook_needs_hmod"></span>**ERROR\_HOOK\_NEEDS\_HMOD**
</dt> <dd> <dl> <dt>

1428 (0x594)
</dt> <dt>



Cannot set nonlocal hook without a module handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_GLOBAL_ONLY_HOOK"></span><span id="error_global_only_hook"></span>**ERROR\_GLOBAL\_ONLY\_HOOK**
</dt> <dd> <dl> <dt>

1429 (0x595)
</dt> <dt>



This hook procedure can only be set globally.


</dt> </dl> </dd> <dt>

<span id="ERROR_JOURNAL_HOOK_SET"></span><span id="error_journal_hook_set"></span>**ERROR\_JOURNAL\_HOOK\_SET**
</dt> <dd> <dl> <dt>

1430 (0x596)
</dt> <dt>



The journal hook procedure is already installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOOK_NOT_INSTALLED"></span><span id="error_hook_not_installed"></span>**ERROR\_HOOK\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

1431 (0x597)
</dt> <dt>



The hook procedure is not installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LB_MESSAGE"></span><span id="error_invalid_lb_message"></span>**ERROR\_INVALID\_LB\_MESSAGE**
</dt> <dd> <dl> <dt>

1432 (0x598)
</dt> <dt>



Invalid message for single-selection list box.


</dt> </dl> </dd> <dt>

<span id="ERROR_SETCOUNT_ON_BAD_LB"></span><span id="error_setcount_on_bad_lb"></span>**ERROR\_SETCOUNT\_ON\_BAD\_LB**
</dt> <dd> <dl> <dt>

1433 (0x599)
</dt> <dt>



LB\_SETCOUNT sent to non-lazy list box.


</dt> </dl> </dd> <dt>

<span id="ERROR_LB_WITHOUT_TABSTOPS"></span><span id="error_lb_without_tabstops"></span>**ERROR\_LB\_WITHOUT\_TABSTOPS**
</dt> <dd> <dl> <dt>

1434 (0x59A)
</dt> <dt>



This list box does not support tab stops.


</dt> </dl> </dd> <dt>

<span id="ERROR_DESTROY_OBJECT_OF_OTHER_THREAD"></span><span id="error_destroy_object_of_other_thread"></span>**ERROR\_DESTROY\_OBJECT\_OF\_OTHER\_THREAD**
</dt> <dd> <dl> <dt>

1435 (0x59B)
</dt> <dt>



Cannot destroy object created by another thread.


</dt> </dl> </dd> <dt>

<span id="ERROR_CHILD_WINDOW_MENU"></span><span id="error_child_window_menu"></span>**ERROR\_CHILD\_WINDOW\_MENU**
</dt> <dd> <dl> <dt>

1436 (0x59C)
</dt> <dt>



Child windows cannot have menus.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SYSTEM_MENU"></span><span id="error_no_system_menu"></span>**ERROR\_NO\_SYSTEM\_MENU**
</dt> <dd> <dl> <dt>

1437 (0x59D)
</dt> <dt>



The window does not have a system menu.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MSGBOX_STYLE"></span><span id="error_invalid_msgbox_style"></span>**ERROR\_INVALID\_MSGBOX\_STYLE**
</dt> <dd> <dl> <dt>

1438 (0x59E)
</dt> <dt>



Invalid message box style.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SPI_VALUE"></span><span id="error_invalid_spi_value"></span>**ERROR\_INVALID\_SPI\_VALUE**
</dt> <dd> <dl> <dt>

1439 (0x59F)
</dt> <dt>



Invalid system-wide (SPI\_\*) parameter.


</dt> </dl> </dd> <dt>

<span id="ERROR_SCREEN_ALREADY_LOCKED"></span><span id="error_screen_already_locked"></span>**ERROR\_SCREEN\_ALREADY\_LOCKED**
</dt> <dd> <dl> <dt>

1440 (0x5A0)
</dt> <dt>



Screen already locked.


</dt> </dl> </dd> <dt>

<span id="ERROR_HWNDS_HAVE_DIFF_PARENT"></span><span id="error_hwnds_have_diff_parent"></span>**ERROR\_HWNDS\_HAVE\_DIFF\_PARENT**
</dt> <dd> <dl> <dt>

1441 (0x5A1)
</dt> <dt>



All handles to windows in a multiple-window position structure must have the same parent.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_CHILD_WINDOW"></span><span id="error_not_child_window"></span>**ERROR\_NOT\_CHILD\_WINDOW**
</dt> <dd> <dl> <dt>

1442 (0x5A2)
</dt> <dt>



The window is not a child window.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_GW_COMMAND"></span><span id="error_invalid_gw_command"></span>**ERROR\_INVALID\_GW\_COMMAND**
</dt> <dd> <dl> <dt>

1443 (0x5A3)
</dt> <dt>



Invalid GW\_\* command.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_THREAD_ID"></span><span id="error_invalid_thread_id"></span>**ERROR\_INVALID\_THREAD\_ID**
</dt> <dd> <dl> <dt>

1444 (0x5A4)
</dt> <dt>



Invalid thread identifier.


</dt> </dl> </dd> <dt>

<span id="ERROR_NON_MDICHILD_WINDOW"></span><span id="error_non_mdichild_window"></span>**ERROR\_NON\_MDICHILD\_WINDOW**
</dt> <dd> <dl> <dt>

1445 (0x5A5)
</dt> <dt>



Cannot process a message from a window that is not a multiple document interface (MDI) window.


</dt> </dl> </dd> <dt>

<span id="ERROR_POPUP_ALREADY_ACTIVE"></span><span id="error_popup_already_active"></span>**ERROR\_POPUP\_ALREADY\_ACTIVE**
</dt> <dd> <dl> <dt>

1446 (0x5A6)
</dt> <dt>



Popup menu already active.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SCROLLBARS"></span><span id="error_no_scrollbars"></span>**ERROR\_NO\_SCROLLBARS**
</dt> <dd> <dl> <dt>

1447 (0x5A7)
</dt> <dt>



The window does not have scroll bars.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SCROLLBAR_RANGE"></span><span id="error_invalid_scrollbar_range"></span>**ERROR\_INVALID\_SCROLLBAR\_RANGE**
</dt> <dd> <dl> <dt>

1448 (0x5A8)
</dt> <dt>



Scroll bar range cannot be greater than MAXLONG.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SHOWWIN_COMMAND"></span><span id="error_invalid_showwin_command"></span>**ERROR\_INVALID\_SHOWWIN\_COMMAND**
</dt> <dd> <dl> <dt>

1449 (0x5A9)
</dt> <dt>



Cannot show or remove the window in the way specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SYSTEM_RESOURCES"></span><span id="error_no_system_resources"></span>**ERROR\_NO\_SYSTEM\_RESOURCES**
</dt> <dd> <dl> <dt>

1450 (0x5AA)
</dt> <dt>



Insufficient system resources exist to complete the requested service.


</dt> </dl> </dd> <dt>

<span id="ERROR_NONPAGED_SYSTEM_RESOURCES"></span><span id="error_nonpaged_system_resources"></span>**ERROR\_NONPAGED\_SYSTEM\_RESOURCES**
</dt> <dd> <dl> <dt>

1451 (0x5AB)
</dt> <dt>



Insufficient system resources exist to complete the requested service.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGED_SYSTEM_RESOURCES"></span><span id="error_paged_system_resources"></span>**ERROR\_PAGED\_SYSTEM\_RESOURCES**
</dt> <dd> <dl> <dt>

1452 (0x5AC)
</dt> <dt>



Insufficient system resources exist to complete the requested service.


</dt> </dl> </dd> <dt>

<span id="ERROR_WORKING_SET_QUOTA"></span><span id="error_working_set_quota"></span>**ERROR\_WORKING\_SET\_QUOTA**
</dt> <dd> <dl> <dt>

1453 (0x5AD)
</dt> <dt>



Insufficient quota to complete the requested service.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGEFILE_QUOTA"></span><span id="error_pagefile_quota"></span>**ERROR\_PAGEFILE\_QUOTA**
</dt> <dd> <dl> <dt>

1454 (0x5AE)
</dt> <dt>



Insufficient quota to complete the requested service.


</dt> </dl> </dd> <dt>

<span id="ERROR_COMMITMENT_LIMIT"></span><span id="error_commitment_limit"></span>**ERROR\_COMMITMENT\_LIMIT**
</dt> <dd> <dl> <dt>

1455 (0x5AF)
</dt> <dt>



The paging file is too small for this operation to complete.


</dt> </dl> </dd> <dt>

<span id="ERROR_MENU_ITEM_NOT_FOUND"></span><span id="error_menu_item_not_found"></span>**ERROR\_MENU\_ITEM\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1456 (0x5B0)
</dt> <dt>



A menu item was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_KEYBOARD_HANDLE"></span><span id="error_invalid_keyboard_handle"></span>**ERROR\_INVALID\_KEYBOARD\_HANDLE**
</dt> <dd> <dl> <dt>

1457 (0x5B1)
</dt> <dt>



Invalid keyboard layout handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOOK_TYPE_NOT_ALLOWED"></span><span id="error_hook_type_not_allowed"></span>**ERROR\_HOOK\_TYPE\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

1458 (0x5B2)
</dt> <dt>



Hook type not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION"></span><span id="error_requires_interactive_windowstation"></span>**ERROR\_REQUIRES\_INTERACTIVE\_WINDOWSTATION**
</dt> <dd> <dl> <dt>

1459 (0x5B3)
</dt> <dt>



This operation requires an interactive window station.


</dt> </dl> </dd> <dt>

<span id="ERROR_TIMEOUT"></span><span id="error_timeout"></span>**ERROR\_TIMEOUT**
</dt> <dd> <dl> <dt>

1460 (0x5B4)
</dt> <dt>



This operation returned because the timeout period expired.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MONITOR_HANDLE"></span><span id="error_invalid_monitor_handle"></span>**ERROR\_INVALID\_MONITOR\_HANDLE**
</dt> <dd> <dl> <dt>

1461 (0x5B5)
</dt> <dt>



Invalid monitor handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_INCORRECT_SIZE"></span><span id="error_incorrect_size"></span>**ERROR\_INCORRECT\_SIZE**
</dt> <dd> <dl> <dt>

1462 (0x5B6)
</dt> <dt>



Incorrect size argument.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYMLINK_CLASS_DISABLED"></span><span id="error_symlink_class_disabled"></span>**ERROR\_SYMLINK\_CLASS\_DISABLED**
</dt> <dd> <dl> <dt>

1463 (0x5B7)
</dt> <dt>



The symbolic link cannot be followed because its type is disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYMLINK_NOT_SUPPORTED"></span><span id="error_symlink_not_supported"></span>**ERROR\_SYMLINK\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

1464 (0x5B8)
</dt> <dt>



This application does not support the current operation on symbolic links.


</dt> </dl> </dd> <dt>

<span id="ERROR_XML_PARSE_ERROR"></span><span id="error_xml_parse_error"></span>**ERROR\_XML\_PARSE\_ERROR**
</dt> <dd> <dl> <dt>

1465 (0x5B9)
</dt> <dt>



Windows was unable to parse the requested XML data.


</dt> </dl> </dd> <dt>

<span id="ERROR_XMLDSIG_ERROR"></span><span id="error_xmldsig_error"></span>**ERROR\_XMLDSIG\_ERROR**
</dt> <dd> <dl> <dt>

1466 (0x5BA)
</dt> <dt>



An error was encountered while processing an XML digital signature.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESTART_APPLICATION"></span><span id="error_restart_application"></span>**ERROR\_RESTART\_APPLICATION**
</dt> <dd> <dl> <dt>

1467 (0x5BB)
</dt> <dt>



This application must be restarted.


</dt> </dl> </dd> <dt>

<span id="ERROR_WRONG_COMPARTMENT"></span><span id="error_wrong_compartment"></span>**ERROR\_WRONG\_COMPARTMENT**
</dt> <dd> <dl> <dt>

1468 (0x5BC)
</dt> <dt>



The caller made the connection request in the wrong routing compartment.


</dt> </dl> </dd> <dt>

<span id="ERROR_AUTHIP_FAILURE"></span><span id="error_authip_failure"></span>**ERROR\_AUTHIP\_FAILURE**
</dt> <dd> <dl> <dt>

1469 (0x5BD)
</dt> <dt>



There was an AuthIP failure when attempting to connect to the remote host.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_NVRAM_RESOURCES"></span><span id="error_no_nvram_resources"></span>**ERROR\_NO\_NVRAM\_RESOURCES**
</dt> <dd> <dl> <dt>

1470 (0x5BE)
</dt> <dt>



Insufficient NVRAM resources exist to complete the requested service. A reboot might be required.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_GUI_PROCESS"></span><span id="error_not_gui_process"></span>**ERROR\_NOT\_GUI\_PROCESS**
</dt> <dd> <dl> <dt>

1471 (0x5BF)
</dt> <dt>



Unable to finish the requested operation because the specified process is not a GUI process.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVENTLOG_FILE_CORRUPT"></span><span id="error_eventlog_file_corrupt"></span>**ERROR\_EVENTLOG\_FILE\_CORRUPT**
</dt> <dd> <dl> <dt>

1500 (0x5DC)
</dt> <dt>



The event log file is corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVENTLOG_CANT_START"></span><span id="error_eventlog_cant_start"></span>**ERROR\_EVENTLOG\_CANT\_START**
</dt> <dd> <dl> <dt>

1501 (0x5DD)
</dt> <dt>



No event log file could be opened, so the event logging service did not start.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOG_FILE_FULL"></span><span id="error_log_file_full"></span>**ERROR\_LOG\_FILE\_FULL**
</dt> <dd> <dl> <dt>

1502 (0x5DE)
</dt> <dt>



The event log file is full.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVENTLOG_FILE_CHANGED"></span><span id="error_eventlog_file_changed"></span>**ERROR\_EVENTLOG\_FILE\_CHANGED**
</dt> <dd> <dl> <dt>

1503 (0x5DF)
</dt> <dt>



The event log file has changed between read operations.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_TASK_NAME"></span><span id="error_invalid_task_name"></span>**ERROR\_INVALID\_TASK\_NAME**
</dt> <dd> <dl> <dt>

1550 (0x60E)
</dt> <dt>



The specified task name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_TASK_INDEX"></span><span id="error_invalid_task_index"></span>**ERROR\_INVALID\_TASK\_INDEX**
</dt> <dd> <dl> <dt>

1551 (0x60F)
</dt> <dt>



The specified task index is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_THREAD_ALREADY_IN_TASK"></span><span id="error_thread_already_in_task"></span>**ERROR\_THREAD\_ALREADY\_IN\_TASK**
</dt> <dd> <dl> <dt>

1552 (0x610)
</dt> <dt>



The specified thread is already joining a task.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_SERVICE_FAILURE"></span><span id="error_install_service_failure"></span>**ERROR\_INSTALL\_SERVICE\_FAILURE**
</dt> <dd> <dl> <dt>

1601 (0x641)
</dt> <dt>



The Windows Installer Service could not be accessed. This can occur if the Windows Installer is not correctly installed. Contact your support personnel for assistance.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_USEREXIT"></span><span id="error_install_userexit"></span>**ERROR\_INSTALL\_USEREXIT**
</dt> <dd> <dl> <dt>

1602 (0x642)
</dt> <dt>



User cancelled installation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_FAILURE"></span><span id="error_install_failure"></span>**ERROR\_INSTALL\_FAILURE**
</dt> <dd> <dl> <dt>

1603 (0x643)
</dt> <dt>



Fatal error during installation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_SUSPEND"></span><span id="error_install_suspend"></span>**ERROR\_INSTALL\_SUSPEND**
</dt> <dd> <dl> <dt>

1604 (0x644)
</dt> <dt>



Installation suspended, incomplete.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_PRODUCT"></span><span id="error_unknown_product"></span>**ERROR\_UNKNOWN\_PRODUCT**
</dt> <dd> <dl> <dt>

1605 (0x645)
</dt> <dt>



This action is only valid for products that are currently installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_FEATURE"></span><span id="error_unknown_feature"></span>**ERROR\_UNKNOWN\_FEATURE**
</dt> <dd> <dl> <dt>

1606 (0x646)
</dt> <dt>



Feature ID not registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_COMPONENT"></span><span id="error_unknown_component"></span>**ERROR\_UNKNOWN\_COMPONENT**
</dt> <dd> <dl> <dt>

1607 (0x647)
</dt> <dt>



Component ID not registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_PROPERTY"></span><span id="error_unknown_property"></span>**ERROR\_UNKNOWN\_PROPERTY**
</dt> <dd> <dl> <dt>

1608 (0x648)
</dt> <dt>



Unknown property.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_HANDLE_STATE"></span><span id="error_invalid_handle_state"></span>**ERROR\_INVALID\_HANDLE\_STATE**
</dt> <dd> <dl> <dt>

1609 (0x649)
</dt> <dt>



Handle is in an invalid state.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_CONFIGURATION"></span><span id="error_bad_configuration"></span>**ERROR\_BAD\_CONFIGURATION**
</dt> <dd> <dl> <dt>

1610 (0x64A)
</dt> <dt>



The configuration data for this product is corrupt. Contact your support personnel.


</dt> </dl> </dd> <dt>

<span id="ERROR_INDEX_ABSENT"></span><span id="error_index_absent"></span>**ERROR\_INDEX\_ABSENT**
</dt> <dd> <dl> <dt>

1611 (0x64B)
</dt> <dt>



Component qualifier not present.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_SOURCE_ABSENT"></span><span id="error_install_source_absent"></span>**ERROR\_INSTALL\_SOURCE\_ABSENT**
</dt> <dd> <dl> <dt>

1612 (0x64C)
</dt> <dt>



The installation source for this product is not available. Verify that the source exists and that you can access it.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PACKAGE_VERSION"></span><span id="error_install_package_version"></span>**ERROR\_INSTALL\_PACKAGE\_VERSION**
</dt> <dd> <dl> <dt>

1613 (0x64D)
</dt> <dt>



This installation package cannot be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRODUCT_UNINSTALLED"></span><span id="error_product_uninstalled"></span>**ERROR\_PRODUCT\_UNINSTALLED**
</dt> <dd> <dl> <dt>

1614 (0x64E)
</dt> <dt>



Product is uninstalled.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_QUERY_SYNTAX"></span><span id="error_bad_query_syntax"></span>**ERROR\_BAD\_QUERY\_SYNTAX**
</dt> <dd> <dl> <dt>

1615 (0x64F)
</dt> <dt>



SQL query syntax invalid or unsupported.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FIELD"></span><span id="error_invalid_field"></span>**ERROR\_INVALID\_FIELD**
</dt> <dd> <dl> <dt>

1616 (0x650)
</dt> <dt>



Record field does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_REMOVED"></span><span id="error_device_removed"></span>**ERROR\_DEVICE\_REMOVED**
</dt> <dd> <dl> <dt>

1617 (0x651)
</dt> <dt>



The device has been removed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_ALREADY_RUNNING"></span><span id="error_install_already_running"></span>**ERROR\_INSTALL\_ALREADY\_RUNNING**
</dt> <dd> <dl> <dt>

1618 (0x652)
</dt> <dt>



Another installation is already in progress. Complete that installation before proceeding with this install.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PACKAGE_OPEN_FAILED"></span><span id="error_install_package_open_failed"></span>**ERROR\_INSTALL\_PACKAGE\_OPEN\_FAILED**
</dt> <dd> <dl> <dt>

1619 (0x653)
</dt> <dt>



This installation package could not be opened. Verify that the package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer package.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PACKAGE_INVALID"></span><span id="error_install_package_invalid"></span>**ERROR\_INSTALL\_PACKAGE\_INVALID**
</dt> <dd> <dl> <dt>

1620 (0x654)
</dt> <dt>



This installation package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer package.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_UI_FAILURE"></span><span id="error_install_ui_failure"></span>**ERROR\_INSTALL\_UI\_FAILURE**
</dt> <dd> <dl> <dt>

1621 (0x655)
</dt> <dt>



There was an error starting the Windows Installer service user interface. Contact your support personnel.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_LOG_FAILURE"></span><span id="error_install_log_failure"></span>**ERROR\_INSTALL\_LOG\_FAILURE**
</dt> <dd> <dl> <dt>

1622 (0x656)
</dt> <dt>



Error opening installation log file. Verify that the specified log file location exists and that you can write to it.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_LANGUAGE_UNSUPPORTED"></span><span id="error_install_language_unsupported"></span>**ERROR\_INSTALL\_LANGUAGE\_UNSUPPORTED**
</dt> <dd> <dl> <dt>

1623 (0x657)
</dt> <dt>



The language of this installation package is not supported by your system.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_TRANSFORM_FAILURE"></span><span id="error_install_transform_failure"></span>**ERROR\_INSTALL\_TRANSFORM\_FAILURE**
</dt> <dd> <dl> <dt>

1624 (0x658)
</dt> <dt>



Error applying transforms. Verify that the specified transform paths are valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PACKAGE_REJECTED"></span><span id="error_install_package_rejected"></span>**ERROR\_INSTALL\_PACKAGE\_REJECTED**
</dt> <dd> <dl> <dt>

1625 (0x659)
</dt> <dt>



This installation is forbidden by system policy. Contact your system administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_FUNCTION_NOT_CALLED"></span><span id="error_function_not_called"></span>**ERROR\_FUNCTION\_NOT\_CALLED**
</dt> <dd> <dl> <dt>

1626 (0x65A)
</dt> <dt>



Function could not be executed.


</dt> </dl> </dd> <dt>

<span id="ERROR_FUNCTION_FAILED"></span><span id="error_function_failed"></span>**ERROR\_FUNCTION\_FAILED**
</dt> <dd> <dl> <dt>

1627 (0x65B)
</dt> <dt>



Function failed during execution.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_TABLE"></span><span id="error_invalid_table"></span>**ERROR\_INVALID\_TABLE**
</dt> <dd> <dl> <dt>

1628 (0x65C)
</dt> <dt>



Invalid or unknown table specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_DATATYPE_MISMATCH"></span><span id="error_datatype_mismatch"></span>**ERROR\_DATATYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

1629 (0x65D)
</dt> <dt>



Data supplied is of wrong type.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNSUPPORTED_TYPE"></span><span id="error_unsupported_type"></span>**ERROR\_UNSUPPORTED\_TYPE**
</dt> <dd> <dl> <dt>

1630 (0x65E)
</dt> <dt>



Data of this type is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_CREATE_FAILED"></span><span id="error_create_failed"></span>**ERROR\_CREATE\_FAILED**
</dt> <dd> <dl> <dt>

1631 (0x65F)
</dt> <dt>



The Windows Installer service failed to start. Contact your support personnel.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_TEMP_UNWRITABLE"></span><span id="error_install_temp_unwritable"></span>**ERROR\_INSTALL\_TEMP\_UNWRITABLE**
</dt> <dd> <dl> <dt>

1632 (0x660)
</dt> <dt>



The Temp folder is on a drive that is full or is inaccessible. Free up space on the drive or verify that you have write permission on the Temp folder.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PLATFORM_UNSUPPORTED"></span><span id="error_install_platform_unsupported"></span>**ERROR\_INSTALL\_PLATFORM\_UNSUPPORTED**
</dt> <dd> <dl> <dt>

1633 (0x661)
</dt> <dt>



This installation package is not supported by this processor type. Contact your product vendor.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_NOTUSED"></span><span id="error_install_notused"></span>**ERROR\_INSTALL\_NOTUSED**
</dt> <dd> <dl> <dt>

1634 (0x662)
</dt> <dt>



Component not used on this computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_PACKAGE_OPEN_FAILED"></span><span id="error_patch_package_open_failed"></span>**ERROR\_PATCH\_PACKAGE\_OPEN\_FAILED**
</dt> <dd> <dl> <dt>

1635 (0x663)
</dt> <dt>



This update package could not be opened. Verify that the update package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer update package.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_PACKAGE_INVALID"></span><span id="error_patch_package_invalid"></span>**ERROR\_PATCH\_PACKAGE\_INVALID**
</dt> <dd> <dl> <dt>

1636 (0x664)
</dt> <dt>



This update package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer update package.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_PACKAGE_UNSUPPORTED"></span><span id="error_patch_package_unsupported"></span>**ERROR\_PATCH\_PACKAGE\_UNSUPPORTED**
</dt> <dd> <dl> <dt>

1637 (0x665)
</dt> <dt>



This update package cannot be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRODUCT_VERSION"></span><span id="error_product_version"></span>**ERROR\_PRODUCT\_VERSION**
</dt> <dd> <dl> <dt>

1638 (0x666)
</dt> <dt>



Another version of this product is already installed. Installation of this version cannot continue. To configure or remove the existing version of this product, use Add/Remove Programs on the Control Panel.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_COMMAND_LINE"></span><span id="error_invalid_command_line"></span>**ERROR\_INVALID\_COMMAND\_LINE**
</dt> <dd> <dl> <dt>

1639 (0x667)
</dt> <dt>



Invalid command line argument. Consult the Windows Installer SDK for detailed command line help.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_REMOTE_DISALLOWED"></span><span id="error_install_remote_disallowed"></span>**ERROR\_INSTALL\_REMOTE\_DISALLOWED**
</dt> <dd> <dl> <dt>

1640 (0x668)
</dt> <dt>



Only administrators have permission to add, remove, or configure server software during a Terminal services remote session. If you want to install or configure software on the server, contact your network administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_SUCCESS_REBOOT_INITIATED"></span><span id="error_success_reboot_initiated"></span>**ERROR\_SUCCESS\_REBOOT\_INITIATED**
</dt> <dd> <dl> <dt>

1641 (0x669)
</dt> <dt>



The requested operation completed successfully. The system will be restarted so the changes can take effect.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_TARGET_NOT_FOUND"></span><span id="error_patch_target_not_found"></span>**ERROR\_PATCH\_TARGET\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1642 (0x66A)
</dt> <dt>



The upgrade cannot be installed by the Windows Installer service because the program to be upgraded may be missing, or the upgrade may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_PACKAGE_REJECTED"></span><span id="error_patch_package_rejected"></span>**ERROR\_PATCH\_PACKAGE\_REJECTED**
</dt> <dd> <dl> <dt>

1643 (0x66B)
</dt> <dt>



The update package is not permitted by software restriction policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_TRANSFORM_REJECTED"></span><span id="error_install_transform_rejected"></span>**ERROR\_INSTALL\_TRANSFORM\_REJECTED**
</dt> <dd> <dl> <dt>

1644 (0x66C)
</dt> <dt>



One or more customizations are not permitted by software restriction policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_REMOTE_PROHIBITED"></span><span id="error_install_remote_prohibited"></span>**ERROR\_INSTALL\_REMOTE\_PROHIBITED**
</dt> <dd> <dl> <dt>

1645 (0x66D)
</dt> <dt>



The Windows Installer does not permit installation from a Remote Desktop Connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_REMOVAL_UNSUPPORTED"></span><span id="error_patch_removal_unsupported"></span>**ERROR\_PATCH\_REMOVAL\_UNSUPPORTED**
</dt> <dd> <dl> <dt>

1646 (0x66E)
</dt> <dt>



Uninstallation of the update package is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_PATCH"></span><span id="error_unknown_patch"></span>**ERROR\_UNKNOWN\_PATCH**
</dt> <dd> <dl> <dt>

1647 (0x66F)
</dt> <dt>



The update is not applied to this product.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_NO_SEQUENCE"></span><span id="error_patch_no_sequence"></span>**ERROR\_PATCH\_NO\_SEQUENCE**
</dt> <dd> <dl> <dt>

1648 (0x670)
</dt> <dt>



No valid sequence could be found for the set of updates.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_REMOVAL_DISALLOWED"></span><span id="error_patch_removal_disallowed"></span>**ERROR\_PATCH\_REMOVAL\_DISALLOWED**
</dt> <dd> <dl> <dt>

1649 (0x671)
</dt> <dt>



Update removal was disallowed by policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PATCH_XML"></span><span id="error_invalid_patch_xml"></span>**ERROR\_INVALID\_PATCH\_XML**
</dt> <dd> <dl> <dt>

1650 (0x672)
</dt> <dt>



The XML update data is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT"></span><span id="error_patch_managed_advertised_product"></span>**ERROR\_PATCH\_MANAGED\_ADVERTISED\_PRODUCT**
</dt> <dd> <dl> <dt>

1651 (0x673)
</dt> <dt>



Windows Installer does not permit updating of managed advertised products. At least one feature of the product must be installed before applying the update.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_SERVICE_SAFEBOOT"></span><span id="error_install_service_safeboot"></span>**ERROR\_INSTALL\_SERVICE\_SAFEBOOT**
</dt> <dd> <dl> <dt>

1652 (0x674)
</dt> <dt>



The Windows Installer service is not accessible in Safe Mode. Please try again when your computer is not in Safe Mode or you can use System Restore to return your machine to a previous good state.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAIL_FAST_EXCEPTION"></span><span id="error_fail_fast_exception"></span>**ERROR\_FAIL\_FAST\_EXCEPTION**
</dt> <dd> <dl> <dt>

1653 (0x675)
</dt> <dt>



A fail fast exception occurred. Exception handlers will not be invoked and the process will be terminated immediately.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_REJECTED"></span><span id="error_install_rejected"></span>**ERROR\_INSTALL\_REJECTED**
</dt> <dd> <dl> <dt>

1654 (0x676)
</dt> <dt>



The app that you are trying to run is not supported on this version of Windows.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>WinError.h</dt> </dl> |



## See also

<dl> <dt>

[System Error Codes](system-error-codes.md)
</dt> </dl>

 

 




