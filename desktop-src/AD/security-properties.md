---
title: User Security Attributes
description: In addition to naming properties for user objects, for example, objectGUID, objectSid, cn, distinguishedName, and so on, there are other security properties used for logon, network access, and access control.
ms.assetid: eeb16938-4380-4622-804f-6b2ff19aa68d
ms.tgt_platform: multiple
keywords:
- Security Attributes, Using AD
- User Security Attributes AD
ms.topic: article
ms.date: 08/29/2022
---

# User Security Attributes

In addition to naming properties for user objects, for example, [**objectGUID**](/windows/win32/ADSchema/a-objectguid), [**objectSid**](/windows/win32/ADSchema/a-objectsid), [**cn**](/windows/win32/ADSchema/a-cn), [**distinguishedName**](/windows/win32/ADSchema/a-distinguishedname), and so on, there are other security properties used for logon, network access, and access control. These properties are used by the Windows security system and can be viewed and managed by the _Active Directory User and Computers_ snap-in.

## accountExpires

The [**accountExpires**](/windows/win32/ADSchema/a-accountexpires) attribute specifies when an account expires. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). A value of **TIMEQ\_FOREVER** (defined in Lmaccess.h) indicates that an account never expires.

## altSecurityIdentities

The [**altSecurityIdentities**](/windows/win32/ADSchema/a-altsecurityidentities) attribute is a multi-valued attribute that contains mappings for X.509 certificates or external Kerberos user accounts to this user for the purpose of authentication. Various security packages, including Public Key authentication package and Kerberos, use this data to authenticate users when they present the alternative form of identification such as certificate, UNIX Kerberos ticket, and so on. Build a Windows 2000 token based on the corresponding user account such that they can access system resources.

For X.509 certificates, the values should be the Issuer and Subject names in 509v3 certificates, issued by an external public certification authority, that map to the user account used to find an account for authentication. The SSL (Schannel) package uses the following syntax: X509:&lt;somecertinfotype&gt;somecertinfo. For example, the following value specifies the issuer DN "\<I\>" with the DN "C=US,O=InternetCA,CN=APublicCertificateAuthority" and the subject DN "\<S\>" with the DN "C=US,O=Fabrikam,OU=Sales,CN=Jeff Smith".

``` cpp
X509:<I>C=US,O=InternetCA,CN=APublicCertificateAuthority<S>C=US,O=Fabrikam,OU=Sales,CN=Jeff Smith
```

Be aware that "\<S\>" or "\<I>" and "\<S\>" are supported. Having only "\<I\>" is not supported. Applications should not modify the values within "\<I\>" or "\<S\>" because partial DN matching is not supported.

For external Kerberos accounts, the values should be the Kerberos account name. The Kerberos package uses the following syntax: `Kerberos:MITaccountname`. For example, the following is the value for an account at `Fabrikam.com`:

``` cpp
Kerberos:Jeff.Smith@Fabrikam.com
```

## badPasswordTime

Non-replicated. The [**badPasswordTime**](/windows/win32/ADSchema/a-badpasswordtime) attribute specifies the last time the user attempted to log on to the account using an incorrect password. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). This attribute is maintained separately on each domain controller in the domain. A value of zero means that the last bad password time is unknown. To get an accurate value for the user's last bad password time in the domain, each domain controller in the domain must be queried and the largest value should be used.

## badPwdCount

Non-replicated. The [**badPwdCount**](/windows/win32/ADSchema/a-badpwdcount) attribute specifies the number of times the user attempted to log on to the account using an incorrect password. This attribute is maintained separately on each domain controller in the domain. A value of `0` indicates that the value is unknown. To get an accurate value for the user's total bad password attempts in the domain, each domain controller in the domain must be queried and the sum of the values should be used.

## codePage

The [**codePage**](/windows/win32/ADSchema/a-codepage) attribute specifies the code page for the user's chosen language. This value is not used by Windows.

## countryCode

The [**countryCode**](/windows/win32/ADSchema/a-countrycode) attribute specifies the country/region code for the user's language. This value is not used by Windows.

## homeDirectory

The [**homeDirectory**](/windows/win32/ADSchema/a-homedirectory) attribute specifies the path of the home directory for the user. The string can be null.

If [**homeDrive**](/windows/win32/ADSchema/a-homedrive) is set and specifies a drive letter, [**homeDirectory**](/windows/win32/ADSchema/a-homedirectory) should be a UNC path. The path must be a network UNC path of the form \\\\server\\share\\directory. This value can be a null string.

If [**homeDrive**](/windows/win32/ADSchema/a-homedrive) is not set, [**homeDirectory**](/windows/win32/ADSchema/a-homedirectory) should be a local path, for example, C:\\mylocaldir.

## homeDrive

The [**homeDrive**](/windows/win32/ADSchema/a-homedrive) attribute specifies the drive letter to which to map the UNC path specified by `homeDirectory`. The drive letter must be specified in the following form:

``` cpp
<drive letter>:
```

where "\<drive letter\>" is the letter of the drive to map. For example:

``` cpp
Z:
```

If this attribute is not set, the [**homeDirectory**](/windows/win32/ADSchema/a-homedirectory) should be a local path, for example, C:\\mylocaldir.

## lastLogoff

Non-replicated. The [**lastLogoff**](/windows/win32/ADSchema/a-lastlogoff) attribute specifies when the last logoff occurred. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). The high part of this large integer corresponds to the `dwHighDateTime` member of the [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure and the low part corresponds to the `dwLowDateTime` member of the `FILETIME` structure. This attribute is maintained separately on each domain controller in the domain. A value of zero means that the last logoff time is unknown. To get an accurate value for the user's last logoff in the domain, each domain controller in the domain must be queried and the largest value should be used.

## lastLogon

Non-replicated. The [**lastLogon**](/windows/win32/ADSchema/a-lastlogon) attribute specifies when the last logon occurred. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). The high part of this large integer corresponds to the `dwHighDateTime` member of the [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure and the low part corresponds to the `dwLowDateTime` member of the `FILETIME` structure. This attribute is maintained separately on each domain controller in the domain. A value of zero means that the last logon time is unknown. To get an accurate value for the user's last logon in the domain, each domain controller in the domain must be queried and the largest value should be used.

## lmPwdHistory

The [**lmPwdHistory**](/windows/win32/ADSchema/a-lmpwdhistory) attribute is the password history of the user in LAN Manager (LM) one-way format (OWF). The LM OWF is used for compatibility with LAN Manager 2.x clients, Windows 95, and Windows 98. This attribute is used only by the operating system. Be aware that you cannot derive the plaintext password from the OWF form of the password.

## logonCount

Non-replicated. The [**logonCount**](/windows/win32/ADSchema/a-logoncount) attribute counts the number of successful times that the user tried to log on to this account. This attribute is maintained on each domain controller in the domain. A value of `0` indicates that the value is unknown. To get an accurate value for the user's total number of successful logon attempts in the domain, each domain controller in the domain must be queried and the sum of the values should be used.

## mail

The [**mail**](/windows/win32/ADSchema/a-mail) attribute is a single-valued attribute that contains the SMTP address for the user, for example, `jeff@Fabrikam.com`.

## maxStorage

The [**maxStorage**](/windows/win32/ADSchema/a-maxstorage) attribute specifies the maximum amount of hard-disk drive space that the user can use. Use the **USER\_MAXSTORAGE\_UNLIMITED** (defined in Lmaccess.h) value to use all available disk space.

## memberOf

The [**memberOf**](/windows/win32/ADSchema/a-memberof) attribute is a multi-valued attribute that contains groups of which the user is a direct member, except for the primary group, which is represented by the [**primaryGroupId**](/windows/win32/ADSchema/a-primarygroupid). Group membership is dependent on the domain controller (DC) from which this attribute is retrieved:

- At a DC for the domain that contains the user, [**memberOf**](/windows/win32/ADSchema/a-memberof) for the user is complete with respect to membership for groups in that domain; however, `memberOf` does not contain the user's membership in domain local and global groups in other domains.
- At a GC server, [**memberOf**](/windows/win32/ADSchema/a-memberof) for the user is complete with respect to all universal group memberships.

If both conditions are true for the DC, both sets of data are contained in [**memberOf**](/windows/win32/ADSchema/a-memberof).

Be aware that this attribute lists the groups that contain the user in their member attribute—it does not contain the recursive list of nested predecessors. For example, if user O is a member of group C and group B and group B were nested in group A, the [**memberOf**](/windows/win32/ADSchema/a-memberof) attribute of user O would list group C and group B, but not group A.

This attribute is not stored—it is a computed back-link attribute.

## ntPwdHistory

The [**ntPwdHistory**](/windows/win32/ADSchema/a-ntpwdhistory) attribute is the password history of the user in Windows NT one-way format (OWF). Windows uses the Windows NT OWF. This attribute is used only by the operating system. Be aware that you cannot derive the plaintext password back from the OWF form of the password.

## otherMailbox

The [**otherMailbox**](/windows/win32/ADSchema/a-othermailbox) attribute is a multi-valued attribute that contains other additional mail addresses in a form, for example, `CCMAIL: JeffSmith`.

## PasswordExpirationDate

The password expiration date is not an attribute on the user object. It is a calculated value based on the sum of [**pwdLastSet**](/windows/win32/ADSchema/a-pwdlastset) for the user and [**maxPwdAge**](/windows/win32/ADSchema/a-maxpwdage) of the user's domain. To get the password expiration date, get the [**IADsUser.PasswordExpirationDate**](/windows/win32/ADSI/iadsuser-property-methods) property. You cannot modify this attribute for a user; instead, set the [**IADsDomain.MaxPasswordAge**](/windows/win32/ADSI/iadsdomain-property-methods) property to change the setting for the domain.

## primaryGroupId

The [**primaryGroupId**](/windows/win32/ADSchema/a-primarygroupid) attribute is a single-valued attribute that contains the [**primaryGroupToken**](/windows/win32/ADSchema/a-primarygrouptoken) of the group that is the primary group of the object. The primary group of the object is not included in the [**memberOf**](/windows/win32/ADSchema/a-memberof) attribute. For example, by default, the primary group of a user object is the `primaryGroupToken` of the Domain Users group, but the Domain Users group is not part of the user object's `memberOf` attribute.

## profilePath

The [**profilePath**](/windows/win32/ADSchema/a-profilepath) attribute specifies a path to the user's profile. This value can be a null string, a local absolute path, or a UNC path.

## pwdLastSet

The [**pwdLastSet**](/windows/win32/ADSchema/a-pwdlastset) attribute specifies when the password was last changed. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC).

The system uses the value of this attribute and the [**maxPwdAge**](/windows/win32/ADSchema/a-maxpwdage) attribute of the domain that contains the user object to calculate the password expiration date. That is, the sum of [**pwdLastSet**](/windows/win32/ADSchema/a-pwdlastset) for the user and `maxPwdAge` of the user's domain.

This attribute controls whether the user must change the password when the user logs on next. If [**pwdLastSet**](/windows/win32/ADSchema/a-pwdlastset) is zero, the default, the user must change the password at next logon. The value `-1` indicates that the user is not required to change the password at next logon. The system sets this value to `-1` after user has set the password.

## sAMAccountType

The [**sAMAccountType**](/windows/win32/ADSchema/a-samaccounttype) attribute specifies an integer that represents the account type. This is set by the operating system when the object is created.

## scriptPath

The [**scriptPath**](/windows/win32/ADSchema/a-scriptpath) attribute specifies the path of the user's logon script, .cmd, .exe, or .bat file. The string can be null.

## tokenGroups

The [**tokenGroups**](/windows/win32/ADSchema/a-tokengroups) attribute is a multi-valued attribute that contains the SID of all groups of which the user is a direct and indirect member, including for the primary group. This attribute can only be retrieved if a Global Catalog (GC) server is present to retrieve the transitive reverse memberships.

Be aware that this attribute lists the groups that contain the user in their member attribute, as well as groups that contain those groups in their member attribute, and so on recursively. For example, if user O is a member of group C and group B and group B were nested in group A, the [**tokenGroups**](/windows/win32/ADSchema/a-tokengroups) attribute of user O would list group C, group B, and group A.

The [**tokenGroups**](/windows/win32/ADSchema/a-tokengroups) attribute is a useful attribute for obtaining a list of group memberships in just two LDAP queries: the first to get the list of group SIDs from the tokenGroups attribute of the user, the second using that list of SIDs to get the name attribute of each group. It avoids the need to make multiple searches to expand the primaryGroupId attribute and recursively expand the memberOf attribute.  

## unicodePwd

The [**unicodePwd**](/windows/win32/ADSchema/a-unicodepwd) attribute is the user password.

To set the user password, use the [**IADsUser.ChangePassword**](/windows/win32/api/iads/nf-iads-iadsuser-changepassword) method, if your script or application enables the user to change his/her own password, or [**IADsUser.SetPassword**](/windows/win32/api/iads/nf-iads-iadsuser-setpassword) method, if your script or application is allowing an administrator to reset a password.

The password of the user in Windows NT one-way format (OWF). Windows uses the Windows NT OWF. This attribute is used only by operating system. Be aware that you cannot derive the plaintext password back from the OWF form of the password.

## userAccountControl

The [**userAccountControl**](/windows/win32/ADSchema/a-useraccountcontrol) attribute specifies flags that control password, lockout, disable/enable, script, and home directory behavior for the user. This attribute also contains a flag that indicates the account type of the object. The user object usually has the UF\_NORMAL\_ACCOUNT set.

The following flags are defined in Lmaccess.h.

| Flag | Description |
|--------|--------|
| UF\_SCRIPT               | The logon script executed. This value must be set for LAN Manager 2.0 or Windows NT. |
| UF\_ACCOUNTDISABLE       | The user account is disabled. |
| UF\_HOMEDIR\_REQUIRED    | The home directory is required. This value is ignored in Windows NT and Windows 2000. |
| UF\_PASSWD\_NOTREQD      | No password is required. |
| UF\_PASSWD\_CANT\_CHANGE | The user cannot change the password. |
| UF\_LOCKOUT              | The account is currently locked. This value can be cleared to unlock a previously locked account. This value cannot be used to lock a previously locked account. |
| UF\_DONT\_EXPIRE\_PASSWD | Represents the password, which should never expire on the account. |

The following flags describe the account type. Only one value can be set. You cannot change the account type.

| Flag | Description |
|--------|--------|
| UF\_NORMAL\_ACCOUNT             | This is a default account type that represents a typical user. |
| UF\_TEMP\_DUPLICATE\_ACCOUNT    | This is an account for users whose primary account is in another domain. This account provides user access to this domain, but not to any domain that trusts this domain. The User Manager refers to this account type as a local user account. |
| UF\_WORKSTATION\_TRUST\_ACCOUNT | This is a computer account for a Windows NT Workstation/Windows 2000 Professional or Windows NT Server/Windows 2000 Server that is a member of this domain. |
| UF\_SERVER\_TRUST\_ACCOUNT      | This is a computer account for a Windows NT Backup Domain Controller that is a member of this domain. |
| UF\_INTERDOMAIN\_TRUST\_ACCOUNT | This is a permit to trust account for a Windows NT domain that trusts other domains. |

## userCertificate

The [**userCertificate**](/windows/win32/ADSchema/a-usercertificate) attribute is a multi-valued attribute that contains the DER-encoded X509v3 certificates issued to the user. Be aware that this attribute contains the public key certificates issued to this user by Microsoft Certificate Service.

## userSharedFolder

The [**userSharedFolder**](/windows/win32/ADSchema/a-usersharedfolder) attribute specifies a UNC path to the user's shared documents folder. The path must be a network UNC path of the form \\\\server\\share\\directory. This value can be a null string.

## userWorkstations

The [**userWorkstations**](/windows/win32/ADSchema/a-userworkstations) attribute is a single-valued attribute that contains the NetBIOS names of the workstations from which the user can log on to. Each NetBIOS name is separated by a comma.

If no values are set, this indicates that there is no restriction. To disable logons from all workstations to this account, set the UF\_ACCOUNTDISABLE value (defined in Lmaccess.h) in [**userAccountControl**](/windows/win32/ADSchema/a-useraccountcontrol) attribute.
