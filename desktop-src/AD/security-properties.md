---
title: User Security Attributes
description: In addition to naming properties for user objects, for example, objectGUID, objectSid, cn, distinguishedName, and so on, there are other security properties used for logon, network access, and access control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: eeb16938-4380-4622-804f-6b2ff19aa68d
ms.tgt_platform: multiple
keywords:
- Security Attributes, Using AD
- User Security Attributes AD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# User Security Attributes

In addition to naming properties for user objects, for example, [**objectGUID**](https://msdn.microsoft.com/library/ms679021), [**objectSid**](https://msdn.microsoft.com/library/ms679024), [**cn**](https://msdn.microsoft.com/library/ms675449), [**distinguishedName**](https://msdn.microsoft.com/library/ms675516), and so on, there are other security properties used for logon, network access, and access control. These properties are used by the Windows 2000 security system. These properties can be viewed and managed by the Active Directory User and Computers snap-in.

<dl> <dt>

<span id="accountExpires"></span><span id="accountexpires"></span><span id="ACCOUNTEXPIRES"></span>[**accountExpires**](https://msdn.microsoft.com/library/ms675098)
</dt> <dd>

The [**accountExpires**](https://msdn.microsoft.com/library/ms675098) attribute specifies when an account expires. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). A value of **TIMEQ\_FOREVER** (defined in Lmaccess.h) indicates that an account never expires.

</dd> <dt>

<span id="altSecurityIdentities"></span><span id="altsecurityidentities"></span><span id="ALTSECURITYIDENTITIES"></span>[**altSecurityIdentities**](https://msdn.microsoft.com/library/ms675221)
</dt> <dd>

The [**altSecurityIdentities**](https://msdn.microsoft.com/library/ms675221) attribute is a multi-valued attribute that contains mappings for X.509 certificates or external Kerberos user accounts to this user for the purpose of authentication. Various security packages, including Public Key authentication package and Kerberos, use this data to authenticate users when they present the alternative form of identification such as certificate, UNIX Kerberos ticket, and so on. Build a Windows 2000 token based on the corresponding user account such that they can access system resources.

For X.509 certificates, the values should be the Issuer and Subject names in 509v3 certificates, issued by an external public certification authority, that map to the user account used to find an account for authentication. The SSL (Schannel) package uses the following syntax: X509:<somecertinfotype>somecertinfo. For example, the following value specifies the issuer DN "\<I\>" with the DN "C=US,O=InternetCA,CN=APublicCertificateAuthority" and the subject DN "\<S\>" with the DN "C=US,O=Fabrikam,OU=Sales,CN=Jeff Smith".


```C++
X509:<I>C=US,O=InternetCA,CN=APublicCertificateAuthority<S>C=US,O=Fabrikam,OU=Sales,CN=Jeff Smith
```



Be aware that "\<I\>" or "\<I>" and "\<S\>" are supported. Having only "\<S\>" is not supported. Applications should not modify the values within "\<I\>" or "\<S\>" because partial DN matching is not supported.

For external Kerberos accounts, the values should be the Kerberos account name. The Kerberos package uses the following syntax: "Kerberos:MITaccountname". For example, the following is the value for an account at Fabrikam.com:


```C++
Kerberos:Jeff.Smith@Fabrikam.com
```



</dd> <dt>

<span id="badPasswordTime"></span><span id="badpasswordtime"></span><span id="BADPASSWORDTIME"></span>[**badPasswordTime**](https://msdn.microsoft.com/library/ms675243)
</dt> <dd>

Non-replicated. The [**badPasswordTime**](https://msdn.microsoft.com/library/ms675243) attribute specifies the last time the user attempted to log on to the account using an incorrect password. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). This attribute is maintained separately on each domain controller in the domain. A value of zero means that the last bad password time is unknown. To get an accurate value for the user's last bad password time in the domain, each domain controller in the domain must be queried and the largest value should be used.

</dd> <dt>

<span id="badPwdCount"></span><span id="badpwdcount"></span><span id="BADPWDCOUNT"></span>[**badPwdCount**](https://msdn.microsoft.com/library/ms675244)
</dt> <dd>

Non-replicated. The [**badPwdCount**](https://msdn.microsoft.com/library/ms675244) attribute specifies the number of times the user attempted to log on to the account using an incorrect password. This attribute is maintained separately on each domain controller in the domain. A value of 0 indicates that the value is unknown. To get an accurate value for the user's total bad password attempts in the domain, each domain controller in the domain must be queried and the sum of the values should be used.

</dd> <dt>

<span id="codePage"></span><span id="codepage"></span><span id="CODEPAGE"></span>[**codePage**](https://msdn.microsoft.com/library/ms675451)
</dt> <dd>

The [**codePage**](https://msdn.microsoft.com/library/ms675451) attribute specifies the code page for the user's chosen language. This value is not used by Windows 2000.

</dd> <dt>

<span id="countryCode"></span><span id="countrycode"></span><span id="COUNTRYCODE"></span>[**countryCode**](https://msdn.microsoft.com/library/ms675466)
</dt> <dd>

The [**countryCode**](https://msdn.microsoft.com/library/ms675466) attribute specifies the country/region code for the user's language. This value is not used by Windows 2000.

</dd> <dt>

<span id="homeDirectory"></span><span id="homedirectory"></span><span id="HOMEDIRECTORY"></span>[**homeDirectory**](https://msdn.microsoft.com/library/ms676190)
</dt> <dd>

The [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) attribute specifies the path of the home directory for the user. The string can be null.

If [**homeDrive**](https://msdn.microsoft.com/library/ms676191) is set and specifies a drive letter, [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) should be a UNC path. The path must be a network UNC path of the form \\\\server\\share\\directory. This value can be a null string.

If [**homeDrive**](https://msdn.microsoft.com/library/ms676191) is not set, [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) should be a local path, for example, C:\\mylocaldir.

</dd> <dt>

<span id="homeDrive"></span><span id="homedrive"></span><span id="HOMEDRIVE"></span>[**homeDrive**](https://msdn.microsoft.com/library/ms676191)
</dt> <dd>

The [**homeDrive**](https://msdn.microsoft.com/library/ms676191) attribute specifies the drive letter to which to map the UNC path specified by **homeDirectory**. The drive letter must be specified in the following form:


```C++
<drive letter>:
```



where "\<drive letter\>" is the letter of the drive to map. For example:


```C++
Z:
```



If this attribute is not set, the [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) should be a local path, for example, C:\\mylocaldir.

</dd> <dt>

<span id="lastLogoff"></span><span id="lastlogoff"></span><span id="LASTLOGOFF"></span>[**lastLogoff**](https://msdn.microsoft.com/library/ms676822)
</dt> <dd>

Non-replicated. The [**lastLogoff**](https://msdn.microsoft.com/library/ms676822) attribute specifies when the last logoff occurred. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). The high part of this large integer corresponds to the **dwHighDateTime** member of the [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284) structure and the low part corresponds to the **dwLowDateTime** member of the **FILETIME** structure. This attribute is maintained separately on each domain controller in the domain. A value of zero means that the last logoff time is unknown. To get an accurate value for the user's last logoff in the domain, each domain controller in the domain must be queried and the largest value should be used.

</dd> <dt>

<span id="lastLogon"></span><span id="lastlogon"></span><span id="LASTLOGON"></span>[**lastLogon**](https://msdn.microsoft.com/library/ms676823)
</dt> <dd>

Non-replicated. The [**lastLogon**](https://msdn.microsoft.com/library/ms676823) attribute specifies when the last logon occurred. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). The high part of this large integer corresponds to the **dwHighDateTime** member of the [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284) structure and the low part corresponds to the **dwLowDateTime** member of the **FILETIME** structure. This attribute is maintained separately on each domain controller in the domain. A value of zero means that the last logon time is unknown. To get an accurate value for the user's last logon in the domain, each domain controller in the domain must be queried and the largest value should be used.

</dd> <dt>

<span id="lmPwdHistory"></span><span id="lmpwdhistory"></span><span id="LMPWDHISTORY"></span>[**lmPwdHistory**](https://msdn.microsoft.com/library/ms676833)
</dt> <dd>

The [**lmPwdHistory**](https://msdn.microsoft.com/library/ms676833) attribute is the password history of the user in LAN Manager (LM) one-way format (OWF). The LM OWF is used for compatibility with LAN Manager 2.x clients, Windows 95, and Windows 98. This attribute is used only by the operating system. Be aware that you cannot derive the plaintext password from the OWF form of the password.

</dd> <dt>

<span id="logonCount"></span><span id="logoncount"></span><span id="LOGONCOUNT"></span>[**logonCount**](https://msdn.microsoft.com/library/ms676845)
</dt> <dd>

Non-replicated. The [**logonCount**](https://msdn.microsoft.com/library/ms676845) attribute counts the number of successful times that the user tried to log on to this account. This attribute is maintained on each domain controller in the domain. A value of 0 indicates that the value is unknown. To get an accurate value for the user's total number of successful logon attempts in the domain, each domain controller in the domain must be queried and the sum of the values should be used.

</dd> <dt>

<span id="mail"></span><span id="MAIL"></span>[**mail**](https://msdn.microsoft.com/library/ms676855)
</dt> <dd>

The [**mail**](https://msdn.microsoft.com/library/ms676855) attribute is a single-valued attribute that contains the SMTP address for the user, for example, "jeff@Fabrikam.com".

</dd> <dt>

<span id="maxStorage"></span><span id="maxstorage"></span><span id="MAXSTORAGE"></span>[**maxStorage**](https://msdn.microsoft.com/library/ms676865)
</dt> <dd>

The [**maxStorage**](https://msdn.microsoft.com/library/ms676865) attribute specifies the maximum amount of hard-disk drive space that the user can use. Use the **USER\_MAXSTORAGE\_UNLIMITED** (defined in Lmaccess.h) value to use all available disk space.

</dd> <dt>

<span id="memberOf"></span><span id="memberof"></span><span id="MEMBEROF"></span>[**memberOf**](https://msdn.microsoft.com/library/ms677099)
</dt> <dd>

The [**memberOf**](https://msdn.microsoft.com/library/ms677099) attribute is a multi-valued attribute that contains groups of which the user is a direct member, except for the primary group, which is represented by the [**primaryGroupId**](https://msdn.microsoft.com/library/ms679375). Group membership is dependent on the domain controller (DC) from which this attribute is retrieved:

-   At a DC for the domain that contains the user, [**memberOf**](https://msdn.microsoft.com/library/ms677099) for the user is complete with respect to membership for groups in that domain; however, **memberOf** does not contain the user's membership in domain local and global groups in other domains.
-   At a GC server, [**memberOf**](https://msdn.microsoft.com/library/ms677099) for the user is complete with respect to all universal group memberships.

If both conditions are true for the DC, both sets of data are contained in [**memberOf**](https://msdn.microsoft.com/library/ms677099).

Be aware that this attribute lists the groups that contain the user in their member attribute—it does not contain the recursive list of nested predecessors. For example, if user O is a member of group C and group B and group B were nested in group A, the [**memberOf**](https://msdn.microsoft.com/library/ms677099) attribute of user O would list group C and group B, but not group A.

This attribute is not stored—it is a computed back-link attribute.

</dd> <dt>

<span id="ntPwdHistory"></span><span id="ntpwdhistory"></span><span id="NTPWDHISTORY"></span>[**ntPwdHistory**](https://msdn.microsoft.com/library/ms679004)
</dt> <dd>

The [**ntPwdHistory**](https://msdn.microsoft.com/library/ms679004) attribute is the password history of the user in Windows NT one-way format (OWF). Windows 2000 uses the Windows NT OWF. This attribute is used only by the operating system. Be aware that you cannot derive the plaintext password back from the OWF form of the password.

</dd> <dt>

<span id="otherMailbox"></span><span id="othermailbox"></span><span id="OTHERMAILBOX"></span>[**otherMailbox**](https://msdn.microsoft.com/library/ms679091)
</dt> <dd>

The [**otherMailbox**](https://msdn.microsoft.com/library/ms679091) attribute is a multi-valued attribute that contains other additional mail addresses in a form, for example, "CCMAIL: JeffSmith".

</dd> <dt>

<span id="PasswordExpirationDate"></span><span id="passwordexpirationdate"></span><span id="PASSWORDEXPIRATIONDATE"></span>[**PasswordExpirationDate**](https://msdn.microsoft.com/library/aa746343)
</dt> <dd>

The password expiration date is not an attribute on the user object. It is a calculated value based on the sum of [**pwdLastSet**](https://msdn.microsoft.com/library/ms679430) for the user and [**maxPwdAge**](https://msdn.microsoft.com/library/ms676863) of the user's domain. To get the password expiration date, get the [**IADsUser.PasswordExpirationDate**](https://msdn.microsoft.com/library/aa746343) property. You cannot modify this attribute for a user; instead, set the [**IADsDomain.MaxPasswordAge**](https://msdn.microsoft.com/library/aa706003) property to change the setting for the domain.

</dd> <dt>

<span id="primaryGroupID"></span><span id="primarygroupid"></span><span id="PRIMARYGROUPID"></span>[**primaryGroupID**](https://msdn.microsoft.com/library/ms679375)
</dt> <dd>

The [**primaryGroupID**](https://msdn.microsoft.com/library/ms679375) attribute is a single-valued attribute that contains the [**primaryGroupToken**](https://msdn.microsoft.com/library/ms679376) of the group that is the primary group of the object. The primary group of the object is not included in the [**memberOf**](https://msdn.microsoft.com/library/ms677099) attribute. For example, by default, the primary group of a user object is the **primaryGroupToken** of the Domain Users group, but the Domain Users group is not part of the user object's **memberOf** attribute.

</dd> <dt>

<span id="profilePath"></span><span id="profilepath"></span><span id="PROFILEPATH"></span>[**profilePath**](https://msdn.microsoft.com/library/ms679422)
</dt> <dd>

The [**profilePath**](https://msdn.microsoft.com/library/ms679422) attribute specifies a path to the user's profile. This value can be a null string, a local absolute path, or a UNC path.

</dd> <dt>

<span id="pwdLastSet"></span><span id="pwdlastset"></span><span id="PWDLASTSET"></span>[**pwdLastSet**](https://msdn.microsoft.com/library/ms679430)
</dt> <dd>

The [**pwdLastSet**](https://msdn.microsoft.com/library/ms679430) attribute specifies when the password was last changed. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC).

The system uses the value of this attribute and the [**maxPwdAge**](https://msdn.microsoft.com/library/ms676863) attribute of the domain that contains the user object to calculate the password expiration date. That is, the sum of [**pwdLastSet**](https://msdn.microsoft.com/library/ms679430) for the user and **maxPwdAge** of the user's domain.

This attribute controls whether the user must change the password when the user logs on next. If [**pwdLastSet**](https://msdn.microsoft.com/library/ms679430) is zero, the default, the user must change the password at next logon. The value -1 indicates that the user is not required to change the password at next logon. The system sets this value to -1 after user has set the password.

</dd> <dt>

<span id="sAMAccountType"></span><span id="samaccounttype"></span><span id="SAMACCOUNTTYPE"></span>[**sAMAccountType**](https://msdn.microsoft.com/library/ms679637)
</dt> <dd>

The [**sAMAccountType**](https://msdn.microsoft.com/library/ms679637) attribute specifies an integer that represents the account type. This is set by the operating system when the object is created.

</dd> <dt>

<span id="scriptPath"></span><span id="scriptpath"></span><span id="SCRIPTPATH"></span>[**scriptPath**](https://msdn.microsoft.com/library/ms679656)
</dt> <dd>

The [**scriptPath**](https://msdn.microsoft.com/library/ms679656) attribute specifies the path of the user's logon script, .cmd, .exe, or .bat file. The string can be null.

</dd> <dt>

<span id="unicodePwd"></span><span id="unicodepwd"></span><span id="UNICODEPWD"></span>[**unicodePwd**](https://msdn.microsoft.com/library/ms680513)
</dt> <dd>

The [**unicodePwd**](https://msdn.microsoft.com/library/ms680513) attribute is the user password.

To set the user password, use the [**IADsUser.ChangePassword**](https://msdn.microsoft.com/library/aa746341) method, if your script or application enables the user to change his/her own password, or [**IADsUser.SetPassword**](https://msdn.microsoft.com/library/aa746344) method, if your script or application is allowing an administrator to reset a password.

The password of the user in Windows NT one-way format (OWF). Windows 2000 uses the Windows NT OWF. This attribute is used only by operating system. Be aware that you cannot derive the plaintext password back from the OWF form of the password.

</dd> <dt>

<span id="userAccountControl"></span><span id="useraccountcontrol"></span><span id="USERACCOUNTCONTROL"></span>[**userAccountControl**](https://msdn.microsoft.com/library/ms680832)
</dt> <dd>

The [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute specifies flags that control password, lockout, disable/enable, script, and home directory behavior for the user. This attribute also contains a flag that indicates the account type of the object. The user object usually has the UF\_NORMAL\_ACCOUNT set.

The following flags are defined in Lmaccess.h.



| Flag                     | Description                                                                                                                                                      |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UF\_SCRIPT               | The logon script executed. This value must be set for LAN Manager 2.0 or Windows NT.                                                                             |
| UF\_ACCOUNTDISABLE       | The user account is disabled.                                                                                                                                    |
| UF\_HOMEDIR\_REQUIRED    | The home directory is required. This value is ignored in Windows NT and Windows 2000.                                                                            |
| UF\_PASSWD\_NOTREQD      | No password is required.                                                                                                                                         |
| UF\_PASSWD\_CANT\_CHANGE | The user cannot change the password.                                                                                                                             |
| UF\_LOCKOUT              | The account is currently locked. This value can be cleared to unlock a previously locked account. This value cannot be used to lock a previously locked account. |
| UF\_DONT\_EXPIRE\_PASSWD | Represents the password, which should never expire on the account.                                                                                               |



 

The following flags describe the account type. Only one value can be set. You cannot change the account type.



| Flag                            | Description                                                                                                                                                                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UF\_NORMAL\_ACCOUNT             | This is a default account type that represents a typical user.                                                                                                                                                                                  |
| UF\_TEMP\_DUPLICATE\_ACCOUNT    | This is an account for users whose primary account is in another domain. This account provides user access to this domain, but not to any domain that trusts this domain. The User Manager refers to this account type as a local user account. |
| UF\_WORKSTATION\_TRUST\_ACCOUNT | This is a computer account for a Windows NT Workstation/Windows 2000 Professional or Windows NT Server/Windows 2000 Server that is a member of this domain.                                                                                     |
| UF\_SERVER\_TRUST\_ACCOUNT      | This is a computer account for a Windows NT Backup Domain Controller that is a member of this domain.                                                                                                                                           |
| UF\_INTERDOMAIN\_TRUST\_ACCOUNT | This is a permit to trust account for a Windows NT domain that trusts other domains.                                                                                                                                                            |



 

</dd> <dt>

<span id="userCertificate"></span><span id="usercertificate"></span><span id="USERCERTIFICATE"></span>[**userCertificate**](https://msdn.microsoft.com/library/ms680837)
</dt> <dd>

The [**userCertificate**](https://msdn.microsoft.com/library/ms680837) attribute is a multi-valued attribute that contains the DER-encoded X509v3 certificates issued to the user. Be aware that this attribute contains the public key certificates issued to this user by Microsoft Certificate Service.

</dd> <dt>

<span id="userSharedFolder"></span><span id="usersharedfolder"></span><span id="USERSHAREDFOLDER"></span>[**userSharedFolder**](https://msdn.microsoft.com/library/ms680859)
</dt> <dd>

The [**userSharedFolder**](https://msdn.microsoft.com/library/ms680859) attribute specifies a UNC path to the user's shared documents folder. The path must be a network UNC path of the form \\\\server\\share\\directory. This value can be a null string.

</dd> <dt>

<span id="userWorkstations"></span><span id="userworkstations"></span><span id="USERWORKSTATIONS"></span>[**userWorkstations**](https://msdn.microsoft.com/library/ms680868)
</dt> <dd>

The [**userWorkstations**](https://msdn.microsoft.com/library/ms680868) attribute is a single-valued attribute that contains the NetBIOS names of the workstations from which the user can log on to. Each NetBIOS name is separated by a comma.

If no values are set, this indicates that there is no restriction. To disable logons from all workstations to this account, set the UF\_ACCOUNTDISABLE value (defined in Lmaccess.h) in [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute.

</dd> </dl>

 

 




