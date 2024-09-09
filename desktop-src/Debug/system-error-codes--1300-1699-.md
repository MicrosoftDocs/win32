---
description: Describes error codes 1300-1699 defined in the WinError.h header file and is intended for developers.
ms.assetid: 7b04a2ba-7bf9-4bff-93c8-cbb0060e069d
title: System Error Codes (1300-1699) (WinError.h)
ms.topic: reference
ms.date: 07/15/2024
---

# System Error Codes (1300-1699)

The following list describes [system error codes](system-error-codes.md) for errors 1300 to 1699. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, see the list of resources on the [Error codes](system-error-codes.md) page.

 

<span id="ERROR_NOT_ALL_ASSIGNED"></span><span id="error_not_all_assigned"></span>**ERROR\_NOT\_ALL\_ASSIGNED**
   

1300 (0x514)
 



Not all privileges or groups referenced are assigned to the caller.


   

<span id="ERROR_SOME_NOT_MAPPED"></span><span id="error_some_not_mapped"></span>**ERROR\_SOME\_NOT\_MAPPED**
   

1301 (0x515)
 



Some mapping between account names and security IDs was not done.


   

<span id="ERROR_NO_QUOTAS_FOR_ACCOUNT"></span><span id="error_no_quotas_for_account"></span>**ERROR\_NO\_QUOTAS\_FOR\_ACCOUNT**
   

1302 (0x516)
 



No system quota limits are specifically set for this account.


   

<span id="ERROR_LOCAL_USER_SESSION_KEY"></span><span id="error_local_user_session_key"></span>**ERROR\_LOCAL\_USER\_SESSION\_KEY**
   

1303 (0x517)
 



No encryption key is available. A well-known encryption key was returned.


   

<span id="ERROR_NULL_LM_PASSWORD"></span><span id="error_null_lm_password"></span>**ERROR\_NULL\_LM\_PASSWORD**
   

1304 (0x518)
 



The password is too complex to be converted to a LAN Manager password. The LAN Manager password returned is a **NULL** string.


   

<span id="ERROR_UNKNOWN_REVISION"></span><span id="error_unknown_revision"></span>**ERROR\_UNKNOWN\_REVISION**
   

1305 (0x519)
 



The revision level is unknown.


   

<span id="ERROR_REVISION_MISMATCH"></span><span id="error_revision_mismatch"></span>**ERROR\_REVISION\_MISMATCH**
   

1306 (0x51A)
 



Indicates two revision levels are incompatible.


   

<span id="ERROR_INVALID_OWNER"></span><span id="error_invalid_owner"></span>**ERROR\_INVALID\_OWNER**
   

1307 (0x51B)
 



This security ID may not be assigned as the owner of this object.


   

<span id="ERROR_INVALID_PRIMARY_GROUP"></span><span id="error_invalid_primary_group"></span>**ERROR\_INVALID\_PRIMARY\_GROUP**
   

1308 (0x51C)
 



This security ID may not be assigned as the primary group of an object.


   

<span id="ERROR_NO_IMPERSONATION_TOKEN"></span><span id="error_no_impersonation_token"></span>**ERROR\_NO\_IMPERSONATION\_TOKEN**
   

1309 (0x51D)
 



An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.


   

<span id="ERROR_CANT_DISABLE_MANDATORY"></span><span id="error_cant_disable_mandatory"></span>**ERROR\_CANT\_DISABLE\_MANDATORY**
   

1310 (0x51E)
 



The group may not be disabled.


   

<span id="ERROR_NO_LOGON_SERVERS"></span><span id="error_no_logon_servers"></span>**ERROR\_NO\_LOGON\_SERVERS**
   

1311 (0x51F)
 



There are currently no logon servers available to service the logon request.


   

<span id="ERROR_NO_SUCH_LOGON_SESSION"></span><span id="error_no_such_logon_session"></span>**ERROR\_NO\_SUCH\_LOGON\_SESSION**
   

1312 (0x520)
 



A specified logon session does not exist. It may already have been terminated.


   

<span id="ERROR_NO_SUCH_PRIVILEGE"></span><span id="error_no_such_privilege"></span>**ERROR\_NO\_SUCH\_PRIVILEGE**
   

1313 (0x521)
 



A specified privilege does not exist.


   

<span id="ERROR_PRIVILEGE_NOT_HELD"></span><span id="error_privilege_not_held"></span>**ERROR\_PRIVILEGE\_NOT\_HELD**
   

1314 (0x522)
 



A required privilege is not held by the client.


   

<span id="ERROR_INVALID_ACCOUNT_NAME"></span><span id="error_invalid_account_name"></span>**ERROR\_INVALID\_ACCOUNT\_NAME**
   

1315 (0x523)
 



The name provided is not a properly formed account name.


   

<span id="ERROR_USER_EXISTS"></span><span id="error_user_exists"></span>**ERROR\_USER\_EXISTS**
   

1316 (0x524)
 



The specified account already exists.


   

<span id="ERROR_NO_SUCH_USER"></span><span id="error_no_such_user"></span>**ERROR\_NO\_SUCH\_USER**
   

1317 (0x525)
 



The specified account does not exist.


   

<span id="ERROR_GROUP_EXISTS"></span><span id="error_group_exists"></span>**ERROR\_GROUP\_EXISTS**
   

1318 (0x526)
 



The specified group already exists.


   

<span id="ERROR_NO_SUCH_GROUP"></span><span id="error_no_such_group"></span>**ERROR\_NO\_SUCH\_GROUP**
   

1319 (0x527)
 



The specified group does not exist.


   

<span id="ERROR_MEMBER_IN_GROUP"></span><span id="error_member_in_group"></span>**ERROR\_MEMBER\_IN\_GROUP**
   

1320 (0x528)
 



Either the specified user account is already a member of the specified group, or the specified group cannot be deleted because it contains a member.


   

<span id="ERROR_MEMBER_NOT_IN_GROUP"></span><span id="error_member_not_in_group"></span>**ERROR\_MEMBER\_NOT\_IN\_GROUP**
   

1321 (0x529)
 



The specified user account is not a member of the specified group account.


   

<span id="ERROR_LAST_ADMIN"></span><span id="error_last_admin"></span>**ERROR\_LAST\_ADMIN**
   

1322 (0x52A)
 



This operation is disallowed as it could result in an administration account being disabled, deleted or unable to log on.


   

<span id="ERROR_WRONG_PASSWORD"></span><span id="error_wrong_password"></span>**ERROR\_WRONG\_PASSWORD**
   

1323 (0x52B)
 



Unable to update the password. The value provided as the current password is incorrect.


   

<span id="ERROR_ILL_FORMED_PASSWORD"></span><span id="error_ill_formed_password"></span>**ERROR\_ILL\_FORMED\_PASSWORD**
   

1324 (0x52C)
 



Unable to update the password. The value provided for the new password contains values that are not allowed in passwords.


   

<span id="ERROR_PASSWORD_RESTRICTION"></span><span id="error_password_restriction"></span>**ERROR\_PASSWORD\_RESTRICTION**
   

1325 (0x52D)
 



Unable to update the password. The value provided for the new password does not meet the length, complexity, or history requirements of the domain.


   

<span id="ERROR_LOGON_FAILURE"></span><span id="error_logon_failure"></span>**ERROR\_LOGON\_FAILURE**
   

1326 (0x52E)
 



The user name or password is incorrect.


   

<span id="ERROR_ACCOUNT_RESTRICTION"></span><span id="error_account_restriction"></span>**ERROR\_ACCOUNT\_RESTRICTION**
   

1327 (0x52F)
 



Account restrictions are preventing this user from signing in. For example: blank passwords aren't allowed, sign-in times are limited, or a policy restriction has been enforced.


   

<span id="ERROR_INVALID_LOGON_HOURS"></span><span id="error_invalid_logon_hours"></span>**ERROR\_INVALID\_LOGON\_HOURS**
   

1328 (0x530)
 



Your account has time restrictions that keep you from signing in right now.


   

<span id="ERROR_INVALID_WORKSTATION"></span><span id="error_invalid_workstation"></span>**ERROR\_INVALID\_WORKSTATION**
   

1329 (0x531)
 



This user isn't allowed to sign in to this computer.


   

<span id="ERROR_PASSWORD_EXPIRED"></span><span id="error_password_expired"></span>**ERROR\_PASSWORD\_EXPIRED**
   

1330 (0x532)
 



The password for this account has expired.


   

<span id="ERROR_ACCOUNT_DISABLED"></span><span id="error_account_disabled"></span>**ERROR\_ACCOUNT\_DISABLED**
   

1331 (0x533)
 



This user can't sign in because this account is currently disabled.


   

<span id="ERROR_NONE_MAPPED"></span><span id="error_none_mapped"></span>**ERROR\_NONE\_MAPPED**
   

1332 (0x534)
 



No mapping between account names and security IDs was done.


   

<span id="ERROR_TOO_MANY_LUIDS_REQUESTED"></span><span id="error_too_many_luids_requested"></span>**ERROR\_TOO\_MANY\_LUIDS\_REQUESTED**
   

1333 (0x535)
 



Too many local user identifiers (LUIDs) were requested at one time.


   

<span id="ERROR_LUIDS_EXHAUSTED"></span><span id="error_luids_exhausted"></span>**ERROR\_LUIDS\_EXHAUSTED**
   

1334 (0x536)
 



No more local user identifiers (LUIDs) are available.


   

<span id="ERROR_INVALID_SUB_AUTHORITY"></span><span id="error_invalid_sub_authority"></span>**ERROR\_INVALID\_SUB\_AUTHORITY**
   

1335 (0x537)
 



The subauthority part of a security ID is invalid for this particular use.


   

<span id="ERROR_INVALID_ACL"></span><span id="error_invalid_acl"></span>**ERROR\_INVALID\_ACL**
   

1336 (0x538)
 



The access control list (ACL) structure is invalid.


   

<span id="ERROR_INVALID_SID"></span><span id="error_invalid_sid"></span>**ERROR\_INVALID\_SID**
   

1337 (0x539)
 



The security ID structure is invalid.


   

<span id="ERROR_INVALID_SECURITY_DESCR"></span><span id="error_invalid_security_descr"></span>**ERROR\_INVALID\_SECURITY\_DESCR**
   

1338 (0x53A)
 



The security descriptor structure is invalid.


   

<span id="ERROR_BAD_INHERITANCE_ACL"></span><span id="error_bad_inheritance_acl"></span>**ERROR\_BAD\_INHERITANCE\_ACL**
   

1340 (0x53C)
 



The inherited access control list (ACL) or access control entry (ACE) could not be built.


   

<span id="ERROR_SERVER_DISABLED"></span><span id="error_server_disabled"></span>**ERROR\_SERVER\_DISABLED**
   

1341 (0x53D)
 



The server is currently disabled.


   

<span id="ERROR_SERVER_NOT_DISABLED"></span><span id="error_server_not_disabled"></span>**ERROR\_SERVER\_NOT\_DISABLED**
   

1342 (0x53E)
 



The server is currently enabled.


   

<span id="ERROR_INVALID_ID_AUTHORITY"></span><span id="error_invalid_id_authority"></span>**ERROR\_INVALID\_ID\_AUTHORITY**
   

1343 (0x53F)
 



The value provided was an invalid value for an identifier authority.


   

<span id="ERROR_ALLOTTED_SPACE_EXCEEDED"></span><span id="error_allotted_space_exceeded"></span>**ERROR\_ALLOTTED\_SPACE\_EXCEEDED**
   

1344 (0x540)
 



No more memory is available for security information updates.


   

<span id="ERROR_INVALID_GROUP_ATTRIBUTES"></span><span id="error_invalid_group_attributes"></span>**ERROR\_INVALID\_GROUP\_ATTRIBUTES**
   

1345 (0x541)
 



The specified attributes are invalid, or incompatible with the attributes for the group as a whole.


   

<span id="ERROR_BAD_IMPERSONATION_LEVEL"></span><span id="error_bad_impersonation_level"></span>**ERROR\_BAD\_IMPERSONATION\_LEVEL**
   

1346 (0x542)
 



Either a required impersonation level was not provided, or the provided impersonation level is invalid.


   

<span id="ERROR_CANT_OPEN_ANONYMOUS"></span><span id="error_cant_open_anonymous"></span>**ERROR\_CANT\_OPEN\_ANONYMOUS**
   

1347 (0x543)
 



Cannot open an anonymous level security token.


   

<span id="ERROR_BAD_VALIDATION_CLASS"></span><span id="error_bad_validation_class"></span>**ERROR\_BAD\_VALIDATION\_CLASS**
   

1348 (0x544)
 



The validation information class requested was invalid.


   

<span id="ERROR_BAD_TOKEN_TYPE"></span><span id="error_bad_token_type"></span>**ERROR\_BAD\_TOKEN\_TYPE**
   

1349 (0x545)
 



The type of the token is inappropriate for its attempted use.


   

<span id="ERROR_NO_SECURITY_ON_OBJECT"></span><span id="error_no_security_on_object"></span>**ERROR\_NO\_SECURITY\_ON\_OBJECT**
   

1350 (0x546)
 



Unable to perform a security operation on an object that has no associated security.


   

<span id="ERROR_CANT_ACCESS_DOMAIN_INFO"></span><span id="error_cant_access_domain_info"></span>**ERROR\_CANT\_ACCESS\_DOMAIN\_INFO**
   

1351 (0x547)
 



Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.


   

<span id="ERROR_INVALID_SERVER_STATE"></span><span id="error_invalid_server_state"></span>**ERROR\_INVALID\_SERVER\_STATE**
   

1352 (0x548)
 



The security account manager (SAM) or local security authority (LSA) server was in the wrong state to perform the security operation.


   

<span id="ERROR_INVALID_DOMAIN_STATE"></span><span id="error_invalid_domain_state"></span>**ERROR\_INVALID\_DOMAIN\_STATE**
   

1353 (0x549)
 



The domain was in the wrong state to perform the security operation.


   

<span id="ERROR_INVALID_DOMAIN_ROLE"></span><span id="error_invalid_domain_role"></span>**ERROR\_INVALID\_DOMAIN\_ROLE**
   

1354 (0x54A)
 



This operation is only allowed for the Primary Domain Controller of the domain.


   

<span id="ERROR_NO_SUCH_DOMAIN"></span><span id="error_no_such_domain"></span>**ERROR\_NO\_SUCH\_DOMAIN**
   

1355 (0x54B)
 



The specified domain either does not exist or could not be contacted.


   

<span id="ERROR_DOMAIN_EXISTS"></span><span id="error_domain_exists"></span>**ERROR\_DOMAIN\_EXISTS**
   

1356 (0x54C)
 



The specified domain already exists.


   

<span id="ERROR_DOMAIN_LIMIT_EXCEEDED"></span><span id="error_domain_limit_exceeded"></span>**ERROR\_DOMAIN\_LIMIT\_EXCEEDED**
   

1357 (0x54D)
 



An attempt was made to exceed the limit on the number of domains per server.


   

<span id="ERROR_INTERNAL_DB_CORRUPTION"></span><span id="error_internal_db_corruption"></span>**ERROR\_INTERNAL\_DB\_CORRUPTION**
   

1358 (0x54E)
 



Unable to complete the requested operation because of either a catastrophic media failure or a data structure corruption on the disk.


   

<span id="ERROR_INTERNAL_ERROR"></span><span id="error_internal_error"></span>**ERROR\_INTERNAL\_ERROR**
   

1359 (0x54F)
 



An internal error occurred.


   

<span id="ERROR_GENERIC_NOT_MAPPED"></span><span id="error_generic_not_mapped"></span>**ERROR\_GENERIC\_NOT\_MAPPED**
   

1360 (0x550)
 



Generic access types were contained in an access mask which should already be mapped to nongeneric types.


   

<span id="ERROR_BAD_DESCRIPTOR_FORMAT"></span><span id="error_bad_descriptor_format"></span>**ERROR\_BAD\_DESCRIPTOR\_FORMAT**
   

1361 (0x551)
 



A security descriptor is not in the right format (absolute or self-relative).


   

<span id="ERROR_NOT_LOGON_PROCESS"></span><span id="error_not_logon_process"></span>**ERROR\_NOT\_LOGON\_PROCESS**
   

1362 (0x552)
 



The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.


   

<span id="ERROR_LOGON_SESSION_EXISTS"></span><span id="error_logon_session_exists"></span>**ERROR\_LOGON\_SESSION\_EXISTS**
   

1363 (0x553)
 



Cannot start a new logon session with an ID that is already in use.


   

<span id="ERROR_NO_SUCH_PACKAGE"></span><span id="error_no_such_package"></span>**ERROR\_NO\_SUCH\_PACKAGE**
   

1364 (0x554)
 



A specified authentication package is unknown.


   

<span id="ERROR_BAD_LOGON_SESSION_STATE"></span><span id="error_bad_logon_session_state"></span>**ERROR\_BAD\_LOGON\_SESSION\_STATE**
   

1365 (0x555)
 



The logon session is not in a state that is consistent with the requested operation.


   

<span id="ERROR_LOGON_SESSION_COLLISION"></span><span id="error_logon_session_collision"></span>**ERROR\_LOGON\_SESSION\_COLLISION**
   

1366 (0x556)
 



The logon session ID is already in use.


   

<span id="ERROR_INVALID_LOGON_TYPE"></span><span id="error_invalid_logon_type"></span>**ERROR\_INVALID\_LOGON\_TYPE**
   

1367 (0x557)
 



A logon request contained an invalid logon type value.


   

<span id="ERROR_CANNOT_IMPERSONATE"></span><span id="error_cannot_impersonate"></span>**ERROR\_CANNOT\_IMPERSONATE**
   

1368 (0x558)
 



Unable to impersonate using a named pipe until data has been read from that pipe.


   

<span id="ERROR_RXACT_INVALID_STATE"></span><span id="error_rxact_invalid_state"></span>**ERROR\_RXACT\_INVALID\_STATE**
   

1369 (0x559)
 



The transaction state of a registry subtree is incompatible with the requested operation.


   

<span id="ERROR_RXACT_COMMIT_FAILURE"></span><span id="error_rxact_commit_failure"></span>**ERROR\_RXACT\_COMMIT\_FAILURE**
   

1370 (0x55A)
 



An internal security database corruption has been encountered.


   

<span id="ERROR_SPECIAL_ACCOUNT"></span><span id="error_special_account"></span>**ERROR\_SPECIAL\_ACCOUNT**
   

1371 (0x55B)
 



Cannot perform this operation on built-in accounts.


   

<span id="ERROR_SPECIAL_GROUP"></span><span id="error_special_group"></span>**ERROR\_SPECIAL\_GROUP**
   

1372 (0x55C)
 



Cannot perform this operation on this built-in special group.


   

<span id="ERROR_SPECIAL_USER"></span><span id="error_special_user"></span>**ERROR\_SPECIAL\_USER**
   

1373 (0x55D)
 



Cannot perform this operation on this built-in special user.


   

<span id="ERROR_MEMBERS_PRIMARY_GROUP"></span><span id="error_members_primary_group"></span>**ERROR\_MEMBERS\_PRIMARY\_GROUP**
   

1374 (0x55E)
 



The user cannot be removed from a group because the group is currently the user's primary group.


   

<span id="ERROR_TOKEN_ALREADY_IN_USE"></span><span id="error_token_already_in_use"></span>**ERROR\_TOKEN\_ALREADY\_IN\_USE**
   

1375 (0x55F)
 



The token is already in use as a primary token.


   

<span id="ERROR_NO_SUCH_ALIAS"></span><span id="error_no_such_alias"></span>**ERROR\_NO\_SUCH\_ALIAS**
   

1376 (0x560)
 



The specified local group does not exist.


   

<span id="ERROR_MEMBER_NOT_IN_ALIAS"></span><span id="error_member_not_in_alias"></span>**ERROR\_MEMBER\_NOT\_IN\_ALIAS**
   

1377 (0x561)
 



The specified account name is not a member of the group.


   

<span id="ERROR_MEMBER_IN_ALIAS"></span><span id="error_member_in_alias"></span>**ERROR\_MEMBER\_IN\_ALIAS**
   

1378 (0x562)
 



The specified account name is already a member of the group.


   

<span id="ERROR_ALIAS_EXISTS"></span><span id="error_alias_exists"></span>**ERROR\_ALIAS\_EXISTS**
   

1379 (0x563)
 



The specified local group already exists.


   

<span id="ERROR_LOGON_NOT_GRANTED"></span><span id="error_logon_not_granted"></span>**ERROR\_LOGON\_NOT\_GRANTED**
   

1380 (0x564)
 



Logon failure: the user has not been granted the requested logon type at this computer.


   

<span id="ERROR_TOO_MANY_SECRETS"></span><span id="error_too_many_secrets"></span>**ERROR\_TOO\_MANY\_SECRETS**
   

1381 (0x565)
 



The maximum number of secrets that may be stored in a single system has been exceeded.


   

<span id="ERROR_SECRET_TOO_LONG"></span><span id="error_secret_too_long"></span>**ERROR\_SECRET\_TOO\_LONG**
   

1382 (0x566)
 



The length of a secret exceeds the maximum length allowed.


   

<span id="ERROR_INTERNAL_DB_ERROR"></span><span id="error_internal_db_error"></span>**ERROR\_INTERNAL\_DB\_ERROR**
   

1383 (0x567)
 



The local security authority database contains an internal inconsistency.


   

<span id="ERROR_TOO_MANY_CONTEXT_IDS"></span><span id="error_too_many_context_ids"></span>**ERROR\_TOO\_MANY\_CONTEXT\_IDS**
   

1384 (0x568)
 



During a logon attempt, the user's security context accumulated too many security IDs.


   

<span id="ERROR_LOGON_TYPE_NOT_GRANTED"></span><span id="error_logon_type_not_granted"></span>**ERROR\_LOGON\_TYPE\_NOT\_GRANTED**
   

1385 (0x569)
 



Logon failure: the user has not been granted the requested logon type at this computer.


   

<span id="ERROR_NT_CROSS_ENCRYPTION_REQUIRED"></span><span id="error_nt_cross_encryption_required"></span>**ERROR\_NT\_CROSS\_ENCRYPTION\_REQUIRED**
   

1386 (0x56A)
 



A cross-encrypted password is necessary to change a user password.


   

<span id="ERROR_NO_SUCH_MEMBER"></span><span id="error_no_such_member"></span>**ERROR\_NO\_SUCH\_MEMBER**
   

1387 (0x56B)
 



A member could not be added to or removed from the local group because the member does not exist.


   

<span id="ERROR_INVALID_MEMBER"></span><span id="error_invalid_member"></span>**ERROR\_INVALID\_MEMBER**
   

1388 (0x56C)
 



A new member could not be added to a local group because the member has the wrong account type.


   

<span id="ERROR_TOO_MANY_SIDS"></span><span id="error_too_many_sids"></span>**ERROR\_TOO\_MANY\_SIDS**
   

1389 (0x56D)
 



Too many security IDs have been specified.


   

<span id="ERROR_LM_CROSS_ENCRYPTION_REQUIRED"></span><span id="error_lm_cross_encryption_required"></span>**ERROR\_LM\_CROSS\_ENCRYPTION\_REQUIRED**
   

1390 (0x56E)
 



A cross-encrypted password is necessary to change this user password.


   

<span id="ERROR_NO_INHERITANCE"></span><span id="error_no_inheritance"></span>**ERROR\_NO\_INHERITANCE**
   

1391 (0x56F)
 



Indicates an ACL contains no inheritable components.


   

<span id="ERROR_FILE_CORRUPT"></span><span id="error_file_corrupt"></span>**ERROR\_FILE\_CORRUPT**
   

1392 (0x570)
 



The file or directory is corrupted and unreadable.


   

<span id="ERROR_DISK_CORRUPT"></span><span id="error_disk_corrupt"></span>**ERROR\_DISK\_CORRUPT**
   

1393 (0x571)
 



The disk structure is corrupted and unreadable.


   

<span id="ERROR_NO_USER_SESSION_KEY"></span><span id="error_no_user_session_key"></span>**ERROR\_NO\_USER\_SESSION\_KEY**
   

1394 (0x572)
 



There is no user session key for the specified logon session.


   

<span id="ERROR_LICENSE_QUOTA_EXCEEDED"></span><span id="error_license_quota_exceeded"></span>**ERROR\_LICENSE\_QUOTA\_EXCEEDED**
   

1395 (0x573)
 



The service being accessed is licensed for a particular number of connections. No more connections can be made to the service at this time because there are already as many connections as the service can accept.


   

<span id="ERROR_WRONG_TARGET_NAME"></span><span id="error_wrong_target_name"></span>**ERROR\_WRONG\_TARGET\_NAME**
   

1396 (0x574)
 



The target account name is incorrect.


   

<span id="ERROR_MUTUAL_AUTH_FAILED"></span><span id="error_mutual_auth_failed"></span>**ERROR\_MUTUAL\_AUTH\_FAILED**
   

1397 (0x575)
 



Mutual Authentication failed. The server's password is out of date at the domain controller.


   

<span id="ERROR_TIME_SKEW"></span><span id="error_time_skew"></span>**ERROR\_TIME\_SKEW**
   

1398 (0x576)
 



There is a time and/or date difference between the client and server.


   

<span id="ERROR_CURRENT_DOMAIN_NOT_ALLOWED"></span><span id="error_current_domain_not_allowed"></span>**ERROR\_CURRENT\_DOMAIN\_NOT\_ALLOWED**
   

1399 (0x577)
 



This operation cannot be performed on the current domain.


   

<span id="ERROR_INVALID_WINDOW_HANDLE"></span><span id="error_invalid_window_handle"></span>**ERROR\_INVALID\_WINDOW\_HANDLE**
   

1400 (0x578)
 



Invalid window handle.


   

<span id="ERROR_INVALID_MENU_HANDLE"></span><span id="error_invalid_menu_handle"></span>**ERROR\_INVALID\_MENU\_HANDLE**
   

1401 (0x579)
 



Invalid menu handle.


   

<span id="ERROR_INVALID_CURSOR_HANDLE"></span><span id="error_invalid_cursor_handle"></span>**ERROR\_INVALID\_CURSOR\_HANDLE**
   

1402 (0x57A)
 



Invalid cursor handle.


   

<span id="ERROR_INVALID_ACCEL_HANDLE"></span><span id="error_invalid_accel_handle"></span>**ERROR\_INVALID\_ACCEL\_HANDLE**
   

1403 (0x57B)
 



Invalid accelerator table handle.


   

<span id="ERROR_INVALID_HOOK_HANDLE"></span><span id="error_invalid_hook_handle"></span>**ERROR\_INVALID\_HOOK\_HANDLE**
   

1404 (0x57C)
 



Invalid hook handle.


   

<span id="ERROR_INVALID_DWP_HANDLE"></span><span id="error_invalid_dwp_handle"></span>**ERROR\_INVALID\_DWP\_HANDLE**
   

1405 (0x57D)
 



Invalid handle to a multiple-window position structure.


   

<span id="ERROR_TLW_WITH_WSCHILD"></span><span id="error_tlw_with_wschild"></span>**ERROR\_TLW\_WITH\_WSCHILD**
   

1406 (0x57E)
 



Cannot create a top-level child window.


   

<span id="ERROR_CANNOT_FIND_WND_CLASS"></span><span id="error_cannot_find_wnd_class"></span>**ERROR\_CANNOT\_FIND\_WND\_CLASS**
   

1407 (0x57F)
 



Cannot find window class.


   

<span id="ERROR_WINDOW_OF_OTHER_THREAD"></span><span id="error_window_of_other_thread"></span>**ERROR\_WINDOW\_OF\_OTHER\_THREAD**
   

1408 (0x580)
 



Invalid window; it belongs to other thread.


   

<span id="ERROR_HOTKEY_ALREADY_REGISTERED"></span><span id="error_hotkey_already_registered"></span>**ERROR\_HOTKEY\_ALREADY\_REGISTERED**
   

1409 (0x581)
 



Hot key is already registered.


   

<span id="ERROR_CLASS_ALREADY_EXISTS"></span><span id="error_class_already_exists"></span>**ERROR\_CLASS\_ALREADY\_EXISTS**
   

1410 (0x582)
 



Class already exists.


   

<span id="ERROR_CLASS_DOES_NOT_EXIST"></span><span id="error_class_does_not_exist"></span>**ERROR\_CLASS\_DOES\_NOT\_EXIST**
   

1411 (0x583)
 



Class does not exist.


   

<span id="ERROR_CLASS_HAS_WINDOWS"></span><span id="error_class_has_windows"></span>**ERROR\_CLASS\_HAS\_WINDOWS**
   

1412 (0x584)
 



Class still has open windows.


   

<span id="ERROR_INVALID_INDEX"></span><span id="error_invalid_index"></span>**ERROR\_INVALID\_INDEX**
   

1413 (0x585)
 



Invalid index.


   

<span id="ERROR_INVALID_ICON_HANDLE"></span><span id="error_invalid_icon_handle"></span>**ERROR\_INVALID\_ICON\_HANDLE**
   

1414 (0x586)
 



Invalid icon handle.


   

<span id="ERROR_PRIVATE_DIALOG_INDEX"></span><span id="error_private_dialog_index"></span>**ERROR\_PRIVATE\_DIALOG\_INDEX**
   

1415 (0x587)
 



Using private DIALOG window words.


   

<span id="ERROR_LISTBOX_ID_NOT_FOUND"></span><span id="error_listbox_id_not_found"></span>**ERROR\_LISTBOX\_ID\_NOT\_FOUND**
   

1416 (0x588)
 



The list box identifier was not found.


   

<span id="ERROR_NO_WILDCARD_CHARACTERS"></span><span id="error_no_wildcard_characters"></span>**ERROR\_NO\_WILDCARD\_CHARACTERS**
   

1417 (0x589)
 



No wildcards were found.


   

<span id="ERROR_CLIPBOARD_NOT_OPEN"></span><span id="error_clipboard_not_open"></span>**ERROR\_CLIPBOARD\_NOT\_OPEN**
   

1418 (0x58A)
 



Thread does not have a clipboard open.


   

<span id="ERROR_HOTKEY_NOT_REGISTERED"></span><span id="error_hotkey_not_registered"></span>**ERROR\_HOTKEY\_NOT\_REGISTERED**
   

1419 (0x58B)
 



Hot key is not registered.


   

<span id="ERROR_WINDOW_NOT_DIALOG"></span><span id="error_window_not_dialog"></span>**ERROR\_WINDOW\_NOT\_DIALOG**
   

1420 (0x58C)
 



The window is not a valid dialog window.


   

<span id="ERROR_CONTROL_ID_NOT_FOUND"></span><span id="error_control_id_not_found"></span>**ERROR\_CONTROL\_ID\_NOT\_FOUND**
   

1421 (0x58D)
 



Control ID not found.


   

<span id="ERROR_INVALID_COMBOBOX_MESSAGE"></span><span id="error_invalid_combobox_message"></span>**ERROR\_INVALID\_COMBOBOX\_MESSAGE**
   

1422 (0x58E)
 



Invalid message for a combo box because it does not have an edit control.


   

<span id="ERROR_WINDOW_NOT_COMBOBOX"></span><span id="error_window_not_combobox"></span>**ERROR\_WINDOW\_NOT\_COMBOBOX**
   

1423 (0x58F)
 



The window is not a combo box.


   

<span id="ERROR_INVALID_EDIT_HEIGHT"></span><span id="error_invalid_edit_height"></span>**ERROR\_INVALID\_EDIT\_HEIGHT**
   

1424 (0x590)
 



Height must be less than 256.


   

<span id="ERROR_DC_NOT_FOUND"></span><span id="error_dc_not_found"></span>**ERROR\_DC\_NOT\_FOUND**
   

1425 (0x591)
 



Invalid device context (DC) handle.


   

<span id="ERROR_INVALID_HOOK_FILTER"></span><span id="error_invalid_hook_filter"></span>**ERROR\_INVALID\_HOOK\_FILTER**
   

1426 (0x592)
 



Invalid hook procedure type.


   

<span id="ERROR_INVALID_FILTER_PROC"></span><span id="error_invalid_filter_proc"></span>**ERROR\_INVALID\_FILTER\_PROC**
   

1427 (0x593)
 



Invalid hook procedure.


   

<span id="ERROR_HOOK_NEEDS_HMOD"></span><span id="error_hook_needs_hmod"></span>**ERROR\_HOOK\_NEEDS\_HMOD**
   

1428 (0x594)
 



Cannot set nonlocal hook without a module handle.


   

<span id="ERROR_GLOBAL_ONLY_HOOK"></span><span id="error_global_only_hook"></span>**ERROR\_GLOBAL\_ONLY\_HOOK**
   

1429 (0x595)
 



This hook procedure can only be set globally.


   

<span id="ERROR_JOURNAL_HOOK_SET"></span><span id="error_journal_hook_set"></span>**ERROR\_JOURNAL\_HOOK\_SET**
   

1430 (0x596)
 



The journal hook procedure is already installed.


   

<span id="ERROR_HOOK_NOT_INSTALLED"></span><span id="error_hook_not_installed"></span>**ERROR\_HOOK\_NOT\_INSTALLED**
   

1431 (0x597)
 



The hook procedure is not installed.


   

<span id="ERROR_INVALID_LB_MESSAGE"></span><span id="error_invalid_lb_message"></span>**ERROR\_INVALID\_LB\_MESSAGE**
   

1432 (0x598)
 



Invalid message for single-selection list box.


   

<span id="ERROR_SETCOUNT_ON_BAD_LB"></span><span id="error_setcount_on_bad_lb"></span>**ERROR\_SETCOUNT\_ON\_BAD\_LB**
   

1433 (0x599)
 



LB\_SETCOUNT sent to non-lazy list box.


   

<span id="ERROR_LB_WITHOUT_TABSTOPS"></span><span id="error_lb_without_tabstops"></span>**ERROR\_LB\_WITHOUT\_TABSTOPS**
   

1434 (0x59A)
 



This list box does not support tab stops.


   

<span id="ERROR_DESTROY_OBJECT_OF_OTHER_THREAD"></span><span id="error_destroy_object_of_other_thread"></span>**ERROR\_DESTROY\_OBJECT\_OF\_OTHER\_THREAD**
   

1435 (0x59B)
 



Cannot destroy object created by another thread.


   

<span id="ERROR_CHILD_WINDOW_MENU"></span><span id="error_child_window_menu"></span>**ERROR\_CHILD\_WINDOW\_MENU**
   

1436 (0x59C)
 



Child windows cannot have menus.


   

<span id="ERROR_NO_SYSTEM_MENU"></span><span id="error_no_system_menu"></span>**ERROR\_NO\_SYSTEM\_MENU**
   

1437 (0x59D)
 



The window does not have a system menu.


   

<span id="ERROR_INVALID_MSGBOX_STYLE"></span><span id="error_invalid_msgbox_style"></span>**ERROR\_INVALID\_MSGBOX\_STYLE**
   

1438 (0x59E)
 



Invalid message box style.


   

<span id="ERROR_INVALID_SPI_VALUE"></span><span id="error_invalid_spi_value"></span>**ERROR\_INVALID\_SPI\_VALUE**
   

1439 (0x59F)
 



Invalid system-wide (SPI\_\*) parameter.


   

<span id="ERROR_SCREEN_ALREADY_LOCKED"></span><span id="error_screen_already_locked"></span>**ERROR\_SCREEN\_ALREADY\_LOCKED**
   

1440 (0x5A0)
 



Screen already locked.


   

<span id="ERROR_HWNDS_HAVE_DIFF_PARENT"></span><span id="error_hwnds_have_diff_parent"></span>**ERROR\_HWNDS\_HAVE\_DIFF\_PARENT**
   

1441 (0x5A1)
 



All handles to windows in a multiple-window position structure must have the same parent.


   

<span id="ERROR_NOT_CHILD_WINDOW"></span><span id="error_not_child_window"></span>**ERROR\_NOT\_CHILD\_WINDOW**
   

1442 (0x5A2)
 



The window is not a child window.


   

<span id="ERROR_INVALID_GW_COMMAND"></span><span id="error_invalid_gw_command"></span>**ERROR\_INVALID\_GW\_COMMAND**
   

1443 (0x5A3)
 



Invalid GW\_\* command.


   

<span id="ERROR_INVALID_THREAD_ID"></span><span id="error_invalid_thread_id"></span>**ERROR\_INVALID\_THREAD\_ID**
   

1444 (0x5A4)
 



Invalid thread identifier.


   

<span id="ERROR_NON_MDICHILD_WINDOW"></span><span id="error_non_mdichild_window"></span>**ERROR\_NON\_MDICHILD\_WINDOW**
   

1445 (0x5A5)
 



Cannot process a message from a window that is not a multiple document interface (MDI) window.


   

<span id="ERROR_POPUP_ALREADY_ACTIVE"></span><span id="error_popup_already_active"></span>**ERROR\_POPUP\_ALREADY\_ACTIVE**
   

1446 (0x5A6)
 



Popup menu already active.


   

<span id="ERROR_NO_SCROLLBARS"></span><span id="error_no_scrollbars"></span>**ERROR\_NO\_SCROLLBARS**
   

1447 (0x5A7)
 



The window does not have scroll bars.


   

<span id="ERROR_INVALID_SCROLLBAR_RANGE"></span><span id="error_invalid_scrollbar_range"></span>**ERROR\_INVALID\_SCROLLBAR\_RANGE**
   

1448 (0x5A8)
 



Scroll bar range cannot be greater than MAXLONG.


   

<span id="ERROR_INVALID_SHOWWIN_COMMAND"></span><span id="error_invalid_showwin_command"></span>**ERROR\_INVALID\_SHOWWIN\_COMMAND**
   

1449 (0x5A9)
 



Cannot show or remove the window in the way specified.


   

<span id="ERROR_NO_SYSTEM_RESOURCES"></span><span id="error_no_system_resources"></span>**ERROR\_NO\_SYSTEM\_RESOURCES**
   

1450 (0x5AA)
 



Insufficient system resources exist to complete the requested service.


   

<span id="ERROR_NONPAGED_SYSTEM_RESOURCES"></span><span id="error_nonpaged_system_resources"></span>**ERROR\_NONPAGED\_SYSTEM\_RESOURCES**
   

1451 (0x5AB)
 



Insufficient system resources exist to complete the requested service.


   

<span id="ERROR_PAGED_SYSTEM_RESOURCES"></span><span id="error_paged_system_resources"></span>**ERROR\_PAGED\_SYSTEM\_RESOURCES**
   

1452 (0x5AC)
 



Insufficient system resources exist to complete the requested service.


   

<span id="ERROR_WORKING_SET_QUOTA"></span><span id="error_working_set_quota"></span>**ERROR\_WORKING\_SET\_QUOTA**
   

1453 (0x5AD)
 



Insufficient quota to complete the requested service.


   

<span id="ERROR_PAGEFILE_QUOTA"></span><span id="error_pagefile_quota"></span>**ERROR\_PAGEFILE\_QUOTA**
   

1454 (0x5AE)
 



Insufficient quota to complete the requested service.


   

<span id="ERROR_COMMITMENT_LIMIT"></span><span id="error_commitment_limit"></span>**ERROR\_COMMITMENT\_LIMIT**
   

1455 (0x5AF)
 



The paging file is too small for this operation to complete.


   

<span id="ERROR_MENU_ITEM_NOT_FOUND"></span><span id="error_menu_item_not_found"></span>**ERROR\_MENU\_ITEM\_NOT\_FOUND**
   

1456 (0x5B0)
 



A menu item was not found.


   

<span id="ERROR_INVALID_KEYBOARD_HANDLE"></span><span id="error_invalid_keyboard_handle"></span>**ERROR\_INVALID\_KEYBOARD\_HANDLE**
   

1457 (0x5B1)
 



Invalid keyboard layout handle.


   

<span id="ERROR_HOOK_TYPE_NOT_ALLOWED"></span><span id="error_hook_type_not_allowed"></span>**ERROR\_HOOK\_TYPE\_NOT\_ALLOWED**
   

1458 (0x5B2)
 



Hook type not allowed.


   

<span id="ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION"></span><span id="error_requires_interactive_windowstation"></span>**ERROR\_REQUIRES\_INTERACTIVE\_WINDOWSTATION**
   

1459 (0x5B3)
 



This operation requires an interactive window station.


   

<span id="ERROR_TIMEOUT"></span><span id="error_timeout"></span>**ERROR\_TIMEOUT**
   

1460 (0x5B4)
 



This operation returned because the timeout period expired.


   

<span id="ERROR_INVALID_MONITOR_HANDLE"></span><span id="error_invalid_monitor_handle"></span>**ERROR\_INVALID\_MONITOR\_HANDLE**
   

1461 (0x5B5)
 



Invalid monitor handle.


   

<span id="ERROR_INCORRECT_SIZE"></span><span id="error_incorrect_size"></span>**ERROR\_INCORRECT\_SIZE**
   

1462 (0x5B6)
 



Incorrect size argument.


   

<span id="ERROR_SYMLINK_CLASS_DISABLED"></span><span id="error_symlink_class_disabled"></span>**ERROR\_SYMLINK\_CLASS\_DISABLED**
   

1463 (0x5B7)
 



The symbolic link cannot be followed because its type is disabled.


   

<span id="ERROR_SYMLINK_NOT_SUPPORTED"></span><span id="error_symlink_not_supported"></span>**ERROR\_SYMLINK\_NOT\_SUPPORTED**
   

1464 (0x5B8)
 



This application does not support the current operation on symbolic links.


   

<span id="ERROR_XML_PARSE_ERROR"></span><span id="error_xml_parse_error"></span>**ERROR\_XML\_PARSE\_ERROR**
   

1465 (0x5B9)
 



Windows was unable to parse the requested XML data.


   

<span id="ERROR_XMLDSIG_ERROR"></span><span id="error_xmldsig_error"></span>**ERROR\_XMLDSIG\_ERROR**
   

1466 (0x5BA)
 



An error was encountered while processing an XML digital signature.


   

<span id="ERROR_RESTART_APPLICATION"></span><span id="error_restart_application"></span>**ERROR\_RESTART\_APPLICATION**
   

1467 (0x5BB)
 



This application must be restarted.


   

<span id="ERROR_WRONG_COMPARTMENT"></span><span id="error_wrong_compartment"></span>**ERROR\_WRONG\_COMPARTMENT**
   

1468 (0x5BC)
 



The caller made the connection request in the wrong routing compartment.


   

<span id="ERROR_AUTHIP_FAILURE"></span><span id="error_authip_failure"></span>**ERROR\_AUTHIP\_FAILURE**
   

1469 (0x5BD)
 



There was an AuthIP failure when attempting to connect to the remote host.


   

<span id="ERROR_NO_NVRAM_RESOURCES"></span><span id="error_no_nvram_resources"></span>**ERROR\_NO\_NVRAM\_RESOURCES**
   

1470 (0x5BE)
 



Insufficient NVRAM resources exist to complete the requested service. A reboot might be required.


   

<span id="ERROR_NOT_GUI_PROCESS"></span><span id="error_not_gui_process"></span>**ERROR\_NOT\_GUI\_PROCESS**
   

1471 (0x5BF)
 



Unable to finish the requested operation because the specified process is not a GUI process.


   

<span id="ERROR_EVENTLOG_FILE_CORRUPT"></span><span id="error_eventlog_file_corrupt"></span>**ERROR\_EVENTLOG\_FILE\_CORRUPT**
   

1500 (0x5DC)
 



The event log file is corrupted.


   

<span id="ERROR_EVENTLOG_CANT_START"></span><span id="error_eventlog_cant_start"></span>**ERROR\_EVENTLOG\_CANT\_START**
   

1501 (0x5DD)
 



No event log file could be opened, so the event logging service did not start.


   

<span id="ERROR_LOG_FILE_FULL"></span><span id="error_log_file_full"></span>**ERROR\_LOG\_FILE\_FULL**
   

1502 (0x5DE)
 



The event log file is full.


   

<span id="ERROR_EVENTLOG_FILE_CHANGED"></span><span id="error_eventlog_file_changed"></span>**ERROR\_EVENTLOG\_FILE\_CHANGED**
   

1503 (0x5DF)
 



The event log file has changed between read operations.


   

<span id="ERROR_INVALID_TASK_NAME"></span><span id="error_invalid_task_name"></span>**ERROR\_INVALID\_TASK\_NAME**
   

1550 (0x60E)
 



The specified task name is invalid.


   

<span id="ERROR_INVALID_TASK_INDEX"></span><span id="error_invalid_task_index"></span>**ERROR\_INVALID\_TASK\_INDEX**
   

1551 (0x60F)
 



The specified task index is invalid.


   

<span id="ERROR_THREAD_ALREADY_IN_TASK"></span><span id="error_thread_already_in_task"></span>**ERROR\_THREAD\_ALREADY\_IN\_TASK**
   

1552 (0x610)
 



The specified thread is already joining a task.


   

<span id="ERROR_INSTALL_SERVICE_FAILURE"></span><span id="error_install_service_failure"></span>**ERROR\_INSTALL\_SERVICE\_FAILURE**
   

1601 (0x641)
 



The Windows Installer Service could not be accessed. This can occur if the Windows Installer is not correctly installed. Contact your support personnel for assistance.


   

<span id="ERROR_INSTALL_USEREXIT"></span><span id="error_install_userexit"></span>**ERROR\_INSTALL\_USEREXIT**
   

1602 (0x642)
 



User cancelled installation.


   

<span id="ERROR_INSTALL_FAILURE"></span><span id="error_install_failure"></span>**ERROR\_INSTALL\_FAILURE**
   

1603 (0x643)
 



Fatal error during installation.


   

<span id="ERROR_INSTALL_SUSPEND"></span><span id="error_install_suspend"></span>**ERROR\_INSTALL\_SUSPEND**
   

1604 (0x644)
 



Installation suspended, incomplete.


   

<span id="ERROR_UNKNOWN_PRODUCT"></span><span id="error_unknown_product"></span>**ERROR\_UNKNOWN\_PRODUCT**
   

1605 (0x645)
 



This action is only valid for products that are currently installed.


   

<span id="ERROR_UNKNOWN_FEATURE"></span><span id="error_unknown_feature"></span>**ERROR\_UNKNOWN\_FEATURE**
   

1606 (0x646)
 



Feature ID not registered.


   

<span id="ERROR_UNKNOWN_COMPONENT"></span><span id="error_unknown_component"></span>**ERROR\_UNKNOWN\_COMPONENT**
   

1607 (0x647)
 



Component ID not registered.


   

<span id="ERROR_UNKNOWN_PROPERTY"></span><span id="error_unknown_property"></span>**ERROR\_UNKNOWN\_PROPERTY**
   

1608 (0x648)
 



Unknown property.


   

<span id="ERROR_INVALID_HANDLE_STATE"></span><span id="error_invalid_handle_state"></span>**ERROR\_INVALID\_HANDLE\_STATE**
   

1609 (0x649)
 



Handle is in an invalid state.


   

<span id="ERROR_BAD_CONFIGURATION"></span><span id="error_bad_configuration"></span>**ERROR\_BAD\_CONFIGURATION**
   

1610 (0x64A)
 



The configuration data for this product is corrupt. Contact your support personnel.


   

<span id="ERROR_INDEX_ABSENT"></span><span id="error_index_absent"></span>**ERROR\_INDEX\_ABSENT**
   

1611 (0x64B)
 



Component qualifier not present.


   

<span id="ERROR_INSTALL_SOURCE_ABSENT"></span><span id="error_install_source_absent"></span>**ERROR\_INSTALL\_SOURCE\_ABSENT**
   

1612 (0x64C)
 



The installation source for this product is not available. Verify that the source exists and that you can access it.


   

<span id="ERROR_INSTALL_PACKAGE_VERSION"></span><span id="error_install_package_version"></span>**ERROR\_INSTALL\_PACKAGE\_VERSION**
   

1613 (0x64D)
 



This installation package cannot be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.


   

<span id="ERROR_PRODUCT_UNINSTALLED"></span><span id="error_product_uninstalled"></span>**ERROR\_PRODUCT\_UNINSTALLED**
   

1614 (0x64E)
 



Product is uninstalled.


   

<span id="ERROR_BAD_QUERY_SYNTAX"></span><span id="error_bad_query_syntax"></span>**ERROR\_BAD\_QUERY\_SYNTAX**
   

1615 (0x64F)
 



SQL query syntax invalid or unsupported.


   

<span id="ERROR_INVALID_FIELD"></span><span id="error_invalid_field"></span>**ERROR\_INVALID\_FIELD**
   

1616 (0x650)
 



Record field does not exist.


   

<span id="ERROR_DEVICE_REMOVED"></span><span id="error_device_removed"></span>**ERROR\_DEVICE\_REMOVED**
   

1617 (0x651)
 



The device has been removed.


   

<span id="ERROR_INSTALL_ALREADY_RUNNING"></span><span id="error_install_already_running"></span>**ERROR\_INSTALL\_ALREADY\_RUNNING**
   

1618 (0x652)
 



Another installation is already in progress. Complete that installation before proceeding with this install.


   

<span id="ERROR_INSTALL_PACKAGE_OPEN_FAILED"></span><span id="error_install_package_open_failed"></span>**ERROR\_INSTALL\_PACKAGE\_OPEN\_FAILED**
   

1619 (0x653)
 



This installation package could not be opened. Verify that the package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer package.


   

<span id="ERROR_INSTALL_PACKAGE_INVALID"></span><span id="error_install_package_invalid"></span>**ERROR\_INSTALL\_PACKAGE\_INVALID**
   

1620 (0x654)
 



This installation package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer package.


   

<span id="ERROR_INSTALL_UI_FAILURE"></span><span id="error_install_ui_failure"></span>**ERROR\_INSTALL\_UI\_FAILURE**
   

1621 (0x655)
 



There was an error starting the Windows Installer service user interface. Contact your support personnel.


   

<span id="ERROR_INSTALL_LOG_FAILURE"></span><span id="error_install_log_failure"></span>**ERROR\_INSTALL\_LOG\_FAILURE**
   

1622 (0x656)
 



Error opening installation log file. Verify that the specified log file location exists and that you can write to it.


   

<span id="ERROR_INSTALL_LANGUAGE_UNSUPPORTED"></span><span id="error_install_language_unsupported"></span>**ERROR\_INSTALL\_LANGUAGE\_UNSUPPORTED**
   

1623 (0x657)
 



The language of this installation package is not supported by your system.


   

<span id="ERROR_INSTALL_TRANSFORM_FAILURE"></span><span id="error_install_transform_failure"></span>**ERROR\_INSTALL\_TRANSFORM\_FAILURE**
   

1624 (0x658)
 



Error applying transforms. Verify that the specified transform paths are valid.


   

<span id="ERROR_INSTALL_PACKAGE_REJECTED"></span><span id="error_install_package_rejected"></span>**ERROR\_INSTALL\_PACKAGE\_REJECTED**
   

1625 (0x659)
 



This installation is forbidden by system policy. Contact your system administrator.


   

<span id="ERROR_FUNCTION_NOT_CALLED"></span><span id="error_function_not_called"></span>**ERROR\_FUNCTION\_NOT\_CALLED**
   

1626 (0x65A)
 



Function could not be executed.


   

<span id="ERROR_FUNCTION_FAILED"></span><span id="error_function_failed"></span>**ERROR\_FUNCTION\_FAILED**
   

1627 (0x65B)
 



Function failed during execution.


   

<span id="ERROR_INVALID_TABLE"></span><span id="error_invalid_table"></span>**ERROR\_INVALID\_TABLE**
   

1628 (0x65C)
 



Invalid or unknown table specified.


   

<span id="ERROR_DATATYPE_MISMATCH"></span><span id="error_datatype_mismatch"></span>**ERROR\_DATATYPE\_MISMATCH**
   

1629 (0x65D)
 



Data supplied is of wrong type.


   

<span id="ERROR_UNSUPPORTED_TYPE"></span><span id="error_unsupported_type"></span>**ERROR\_UNSUPPORTED\_TYPE**
   

1630 (0x65E)
 



Data of this type is not supported.


   

<span id="ERROR_CREATE_FAILED"></span><span id="error_create_failed"></span>**ERROR\_CREATE\_FAILED**
   

1631 (0x65F)
 



The Windows Installer service failed to start. Contact your support personnel.


   

<span id="ERROR_INSTALL_TEMP_UNWRITABLE"></span><span id="error_install_temp_unwritable"></span>**ERROR\_INSTALL\_TEMP\_UNWRITABLE**
   

1632 (0x660)
 



The Temp folder is on a drive that is full or is inaccessible. Free up space on the drive or verify that you have write permission on the Temp folder.


   

<span id="ERROR_INSTALL_PLATFORM_UNSUPPORTED"></span><span id="error_install_platform_unsupported"></span>**ERROR\_INSTALL\_PLATFORM\_UNSUPPORTED**
   

1633 (0x661)
 



This installation package is not supported by this processor type. Contact your product vendor.


   

<span id="ERROR_INSTALL_NOTUSED"></span><span id="error_install_notused"></span>**ERROR\_INSTALL\_NOTUSED**
   

1634 (0x662)
 



Component not used on this computer.


   

<span id="ERROR_PATCH_PACKAGE_OPEN_FAILED"></span><span id="error_patch_package_open_failed"></span>**ERROR\_PATCH\_PACKAGE\_OPEN\_FAILED**
   

1635 (0x663)
 



This update package could not be opened. Verify that the update package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer update package.


   

<span id="ERROR_PATCH_PACKAGE_INVALID"></span><span id="error_patch_package_invalid"></span>**ERROR\_PATCH\_PACKAGE\_INVALID**
   

1636 (0x664)
 



This update package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer update package.


   

<span id="ERROR_PATCH_PACKAGE_UNSUPPORTED"></span><span id="error_patch_package_unsupported"></span>**ERROR\_PATCH\_PACKAGE\_UNSUPPORTED**
   

1637 (0x665)
 



This update package cannot be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.


   

<span id="ERROR_PRODUCT_VERSION"></span><span id="error_product_version"></span>**ERROR\_PRODUCT\_VERSION**
   

1638 (0x666)
 



Another version of this product is already installed. Installation of this version cannot continue. To configure or remove the existing version of this product, use Add/Remove Programs on the Control Panel.


   

<span id="ERROR_INVALID_COMMAND_LINE"></span><span id="error_invalid_command_line"></span>**ERROR\_INVALID\_COMMAND\_LINE**
   

1639 (0x667)
 



Invalid command line argument. Consult the Windows Installer SDK for detailed command line help.


   

<span id="ERROR_INSTALL_REMOTE_DISALLOWED"></span><span id="error_install_remote_disallowed"></span>**ERROR\_INSTALL\_REMOTE\_DISALLOWED**
   

1640 (0x668)
 



Only administrators have permission to add, remove, or configure server software during a Terminal services remote session. If you want to install or configure software on the server, contact your network administrator.


   

<span id="ERROR_SUCCESS_REBOOT_INITIATED"></span><span id="error_success_reboot_initiated"></span>**ERROR\_SUCCESS\_REBOOT\_INITIATED**
   

1641 (0x669)
 



The requested operation completed successfully. The system will be restarted so the changes can take effect.


   

<span id="ERROR_PATCH_TARGET_NOT_FOUND"></span><span id="error_patch_target_not_found"></span>**ERROR\_PATCH\_TARGET\_NOT\_FOUND**
   

1642 (0x66A)
 



The upgrade cannot be installed by the Windows Installer service because the program to be upgraded may be missing, or the upgrade may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade.


   

<span id="ERROR_PATCH_PACKAGE_REJECTED"></span><span id="error_patch_package_rejected"></span>**ERROR\_PATCH\_PACKAGE\_REJECTED**
   

1643 (0x66B)
 



The update package is not permitted by software restriction policy.


   

<span id="ERROR_INSTALL_TRANSFORM_REJECTED"></span><span id="error_install_transform_rejected"></span>**ERROR\_INSTALL\_TRANSFORM\_REJECTED**
   

1644 (0x66C)
 



One or more customizations are not permitted by software restriction policy.


   

<span id="ERROR_INSTALL_REMOTE_PROHIBITED"></span><span id="error_install_remote_prohibited"></span>**ERROR\_INSTALL\_REMOTE\_PROHIBITED**
   

1645 (0x66D)
 



The Windows Installer does not permit installation from a Remote Desktop Connection.


   

<span id="ERROR_PATCH_REMOVAL_UNSUPPORTED"></span><span id="error_patch_removal_unsupported"></span>**ERROR\_PATCH\_REMOVAL\_UNSUPPORTED**
   

1646 (0x66E)
 



Uninstallation of the update package is not supported.


   

<span id="ERROR_UNKNOWN_PATCH"></span><span id="error_unknown_patch"></span>**ERROR\_UNKNOWN\_PATCH**
   

1647 (0x66F)
 



The update is not applied to this product.


   

<span id="ERROR_PATCH_NO_SEQUENCE"></span><span id="error_patch_no_sequence"></span>**ERROR\_PATCH\_NO\_SEQUENCE**
   

1648 (0x670)
 



No valid sequence could be found for the set of updates.


   

<span id="ERROR_PATCH_REMOVAL_DISALLOWED"></span><span id="error_patch_removal_disallowed"></span>**ERROR\_PATCH\_REMOVAL\_DISALLOWED**
   

1649 (0x671)
 



Update removal was disallowed by policy.


   

<span id="ERROR_INVALID_PATCH_XML"></span><span id="error_invalid_patch_xml"></span>**ERROR\_INVALID\_PATCH\_XML**
   

1650 (0x672)
 



The XML update data is invalid.


   

<span id="ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT"></span><span id="error_patch_managed_advertised_product"></span>**ERROR\_PATCH\_MANAGED\_ADVERTISED\_PRODUCT**
   

1651 (0x673)
 



Windows Installer does not permit updating of managed advertised products. At least one feature of the product must be installed before applying the update.


   

<span id="ERROR_INSTALL_SERVICE_SAFEBOOT"></span><span id="error_install_service_safeboot"></span>**ERROR\_INSTALL\_SERVICE\_SAFEBOOT**
   

1652 (0x674)
 



The Windows Installer service is not accessible in Safe Mode. Please try again when your computer is not in Safe Mode or you can use System Restore to return your machine to a previous good state.


   

<span id="ERROR_FAIL_FAST_EXCEPTION"></span><span id="error_fail_fast_exception"></span>**ERROR\_FAIL\_FAST\_EXCEPTION**
   

1653 (0x675)
 



A fail fast exception occurred. Exception handlers will not be invoked and the process will be terminated immediately.


   

<span id="ERROR_INSTALL_REJECTED"></span><span id="error_install_rejected"></span>**ERROR\_INSTALL\_REJECTED**
   

1654 (0x676)
 



The app that you are trying to run is not supported on this version of Windows.


   

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   |  WinError.h  |



## See also

 

[System Error Codes](system-error-codes.md)
 

 

 




