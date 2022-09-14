---
title: User-Account-Control attribute
description: Flags that control the behavior of the user account.
ms.assetid: fc81a16a-f537-44cc-957c-5d7ca66b9755
ms.tgt_platform: multiple
keywords:
- User-Account-Control attribute AD Schema
- userAccountControl attribute AD Schema
topic_type:
- apiref
api_name:
- User-Account-Control
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# User-Account-Control attribute

Flags that control the behavior of the user account.



| Entry | Value |
|-------------------|---------------------------------------|
| CN                | User-Account-Control                  |
| Ldap-Display-Name | userAccountControl                    |
| Size              | 4 bytes.                              |
| Update Privilege  | This value is set by the system.      |
| Update Frequency  | Each time the account policy changes. |
| Attribute-Id      | 1.2.840.113556.1.4.8                  |
| System-Id-Guid    | bf967a68-0de6-11d0-a285-00aa003049e2  |
| Syntax            | [**Enumeration**](s-enumeration.md)  |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000019                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000019                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000019                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000019                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000019                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000019                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Remarks

This attribute value can be zero or a combination of one or more of the following values.




| Hexadecimal value | Identifier (defined in iads.h) | Description | 
|-------------------|--------------------------------|-------------|
| 0x00000001 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_SCRIPT</strong></a> | The logon script is executed. | 
| 0x00000002 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_ACCOUNTDISABLE</strong></a> | The user account is disabled. | 
| 0x00000008 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_HOMEDIR_REQUIRED</strong></a> | The home directory is required. | 
| 0x00000010 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_LOCKOUT</strong></a> | The account is currently locked out. | 
| 0x00000020 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_PASSWD_NOTREQD</strong></a> | No password is required. | 
| 0x00000040 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_PASSWD_CANT_CHANGE</strong></a> | The user cannot change the password.<blockquote>[!Note]<br />You cannot assign the permission settings of PASSWD_CANT_CHANGE by directly modifying the UserAccountControl attribute. For more information and a code example that shows how to prevent a user from changing the password, see <a href="/windows/desktop/ADSI/user-cannot-change-password">User Cannot Change Password</a>.</blockquote><br /> : | 
| 0x00000080 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED</strong></a> | The user can send an encrypted password. | 
| 0x00000100 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_TEMP_DUPLICATE_ACCOUNT</strong></a> | This is an account for users whose primary account is in another domain. This account provides user access to this domain, but not to any domain that trusts this domain. Also known as a local user account. | 
| 0x00000200 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_NORMAL_ACCOUNT</strong></a> | This is a default account type that represents a typical user. | 
| 0x00000800 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_INTERDOMAIN_TRUST_ACCOUNT</strong></a> | This is a permit to trust account for a system domain that trusts other domains. | 
| 0x00001000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_WORKSTATION_TRUST_ACCOUNT</strong></a> | This is a computer account for a computer that is a member of this domain. | 
| 0x00002000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_SERVER_TRUST_ACCOUNT</strong></a> | This is a computer account for a system backup domain controller that is a member of this domain. | 
| 0x00004000 | N/A | Not used. | 
| 0x00008000 | N/A | Not used. | 
| 0x00010000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_DONT_EXPIRE_PASSWD</strong></a> | The password for this account will never expire. | 
| 0x00020000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_MNS_LOGON_ACCOUNT</strong></a> | This is an MNS logon account. | 
| 0x00040000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_SMARTCARD_REQUIRED</strong></a> | The user must log on using a smart card. | 
| 0x00080000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_TRUSTED_FOR_DELEGATION</strong></a> | The service account (user or computer account), under which a service runs, is trusted for Kerberos delegation. Any such service can impersonate a client requesting the service. | 
| 0x00100000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_NOT_DELEGATED</strong></a> | The security context of the user will not be delegated to a service even if the service account is set as trusted for Kerberos delegation. | 
| 0x00200000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_USE_DES_KEY_ONLY</strong></a> | Restrict this principal to use only Data Encryption Standard (DES) encryption types for keys. | 
| 0x00400000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_DONT_REQUIRE_PREAUTH</strong></a> | This account does not require Kerberos pre-authentication for logon. | 
| 0x00800000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_PASSWORD_EXPIRED</strong></a> | The user password has expired. This flag is created by the system using data from the <a href="a-pwdlastset.md"><strong>Pwd-Last-Set</strong></a> attribute and the domain policy. | 
| 0x01000000 | <a href="/windows/desktop/api/iads/ne-iads-ads_user_flag_enum"><strong>ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION</strong></a> | The account is enabled for delegation. This is a security-sensitive setting; accounts with this option enabled should be strictly controlled. This setting enables a service running under the account to assume a client identity and authenticate as that user to other remote servers on the network. | 




 

