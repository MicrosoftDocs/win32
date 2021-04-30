---
description: Joins a computer system to a domain or workgroup.
ms.assetid: b9421f04-9b56-4413-af5c-12dffeb6f0c8
ms.tgt_platform: multiple
title: JoinDomainOrWorkgroup method of the Win32_ComputerSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ComputerSystem.JoinDomainOrWorkgroup
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# JoinDomainOrWorkgroup method of the Win32\_ComputerSystem class

The **JoinDomainOrWorkgroup** method joins a computer system to a domain or workgroup.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 JoinDomainOrWorkgroup(
  [in] string Name,
  [in] string Password,
  [in] string UserName,
  [in] string AccountOU,
  [in] uint32 FJoinOptions = 
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the domain or workgroup to join. Cannot be **NULL**.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

If the *UserName* parameter specifies an account name, the *Password* parameter must point to the password to use when connecting to the domain controller. Otherwise, this parameter must be **NULL**.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

Pointer to a constant **null**-terminated character string that specifies the account name to use when connecting to the domain controller. Must specify a domain NetBIOS name and user account, for example, Domain\\user. If this parameter is **NULL**, the caller information is used.

You can also use the user principal name (UPPED) in the form user@domain.

</dd> <dt>

*AccountOU* \[in\]
</dt> <dd>

Specifies the pointer to a constant **null**-terminated character string that contains the [RFC 1779](https://www.ietf.org/rfc/rfc1779.txt) format name of the organizational unit (OU) for the computer account. If you specify this parameter, the string must contain a full path, otherwise *Accent* must be **NULL**.

Example: "OU=testOU; DC=domain; DC=Domain; DC=com"

</dd> <dt>

*FJoinOptions* \[in\]
</dt> <dd>

Set of bit flags that define the join options.

<dt>



 (0)


</dt> <dd>

Default. No join options.

</dd> <dt>

<span id="NETSETUP_JOIN_DOMAIN"></span><span id="netsetup_join_domain"></span>

<span id="NETSETUP_JOIN_DOMAIN"></span><span id="netsetup_join_domain"></span>**NETSETUP\_JOIN\_DOMAIN** (0x00000001)


</dt> <dd>

Joins the computer to a domain. If this value is not specified, joins the computer to a workgroup.

</dd> <dt>

<span id="NETSETUP_ACCT_CREATE"></span><span id="netsetup_acct_create"></span>

<span id="NETSETUP_ACCT_CREATE"></span><span id="netsetup_acct_create"></span>**NETSETUP\_ACCT\_CREATE** (0x00000002)


</dt> <dd>

Creates the account on the domain.

</dd> <dt>

<span id="NETSETUP_WIN9X_UPGRADE"></span><span id="netsetup_win9x_upgrade"></span>

<span id="NETSETUP_WIN9X_UPGRADE"></span><span id="netsetup_win9x_upgrade"></span>**NETSETUP\_WIN9X\_UPGRADE** (0x00000010)


</dt> <dd>

The join operation is occurring as part of an upgrade.

</dd> <dt>

<span id="NETSETUP_DOMAIN_JOIN_IF_JOINED"></span><span id="netsetup_domain_join_if_joined"></span>

<span id="NETSETUP_DOMAIN_JOIN_IF_JOINED"></span><span id="netsetup_domain_join_if_joined"></span>**NETSETUP\_DOMAIN\_JOIN\_IF\_JOINED** (0x00000020)


</dt> <dd>

Allows a join to a new domain even if the computer is already joined to a domain.

</dd> <dt>

<span id="NETSETUP_JOIN_UNSECURE"></span><span id="netsetup_join_unsecure"></span>

<span id="NETSETUP_JOIN_UNSECURE"></span><span id="netsetup_join_unsecure"></span>**NETSETUP\_JOIN\_UNSECURE** (0x00000040)


</dt> <dd>

Performs an unsecured join.

This option requests a domain join to a pre-created account without authenticating with domain user credentials. This option can be used in conjunction with **NETSETUP\_MACHINE\_PWD\_PASSED** option. In this case, *Password* is the password of the pre-created machine account.

Prior to Windows Vista with SP1 and Windows Server 2008, an unsecure join did not authenticate to the domain controller. All communication was performed using a null (unauthenticated) session. Starting with Windows Vista with SP1 and Windows Server 2008, the machine account name and password are used to authenticate to the domain controller.

</dd> <dt>

<span id="NETSETUP_MACHINE_PWD_PASSED"></span><span id="netsetup_machine_pwd_passed"></span>

<span id="NETSETUP_MACHINE_PWD_PASSED"></span><span id="netsetup_machine_pwd_passed"></span>**NETSETUP\_MACHINE\_PWD\_PASSED** (0x00000080)


</dt> <dd>

Indicates that the *Password* parameter specifies a local machine account password rather than a user password. This flag is valid only for unsecured joins, which you must indicate by also setting the NETSETUP\_JOIN\_UNSECURE flag.

If you set this flag, then after the join operation succeeds, the machine password will be set to the value of *Password*, if that value is a valid machine password.

</dd> <dt>

<span id="NETSETUP_DEFER_SPN_SET"></span><span id="netsetup_defer_spn_set"></span>

<span id="NETSETUP_DEFER_SPN_SET"></span><span id="netsetup_defer_spn_set"></span>**NETSETUP\_DEFER\_SPN\_SET** (0x00000100)


</dt> <dd>

Indicates that the service principal name (SPN) and the DnsHostName properties on the computer object should not be updated at this time.

Typically, these properties are updated during the join operation. Instead, these properties should be updated during a subsequent call to the [**Rename**](rename-method-in-class-win32-computersystem.md) method. These properties are always updated during the rename operation.

</dd> <dt>

<span id="NETSETUP_JOIN_DC_ACCOUNT"></span><span id="netsetup_join_dc_account"></span>

<span id="NETSETUP_JOIN_DC_ACCOUNT"></span><span id="netsetup_join_dc_account"></span>**NETSETUP\_JOIN\_DC\_ACCOUNT** (0x00000200)


</dt> <dd>

Allow the domain join if existing account is a domain controller.

> [!Note]  
> This flag is supported on Windows Vista and later.

 

</dd> <dt>

<span id="NETSETUP_AMBIGUOUS_DC"></span><span id="netsetup_ambiguous_dc"></span>

<span id="NETSETUP_AMBIGUOUS_DC"></span><span id="netsetup_ambiguous_dc"></span>**NETSETUP\_AMBIGUOUS\_DC** (0x00001000)


</dt> <dd>

When joining the domain don't try to set the preferred domain controller in the registry.

> [!Note]  
> This flag is supported on Windows 7, Windows Server 2008 R2, and later.

 

</dd> <dt>

<span id="NETSETUP_NO_NETLOGON_CACHE"></span><span id="netsetup_no_netlogon_cache"></span>

<span id="NETSETUP_NO_NETLOGON_CACHE"></span><span id="netsetup_no_netlogon_cache"></span>**NETSETUP\_NO\_NETLOGON\_CACHE** (0x00002000)


</dt> <dd>

When joining the domain don't create the Netlogon cache.

> [!Note]  
> This flag is supported on Windows 7, Windows Server 2008 R2, and later.

 

</dd> <dt>

<span id="NETSETUP_DONT_CONTROL_SERVICES"></span><span id="netsetup_dont_control_services"></span>

<span id="NETSETUP_DONT_CONTROL_SERVICES"></span><span id="netsetup_dont_control_services"></span>**NETSETUP\_DONT\_CONTROL\_SERVICES** (0x00004000)


</dt> <dd>

When joining the domain don't force Netlogon service to start.

> [!Note]  
> This flag is supported on Windows 7, Windows Server 2008 R2, and later.

 

</dd> <dt>

<span id="NETSETUP_SET_MACHINE_NAME"></span><span id="netsetup_set_machine_name"></span>

<span id="NETSETUP_SET_MACHINE_NAME"></span><span id="netsetup_set_machine_name"></span>**NETSETUP\_SET\_MACHINE\_NAME** (0x00008000)


</dt> <dd>

When joining the domain for offline join only, set target machine hostname and NetBIOS name.

> [!Note]  
> This flag is supported on Windows 7, Windows Server 2008 R2, and later.

 

</dd> <dt>

<span id="NETSETUP_FORCE_SPN_SET"></span><span id="netsetup_force_spn_set"></span>

<span id="NETSETUP_FORCE_SPN_SET"></span><span id="netsetup_force_spn_set"></span>**NETSETUP\_FORCE\_SPN\_SET** (0x00010000)


</dt> <dd>

When joining the domain, override other settings during domain join and set the service principal name (SPN).

> [!Note]  
> This flag is supported on Windows 7, Windows Server 2008 R2, and later.

 

</dd> <dt>

<span id="NETSETUP_NO_ACCT_REUSE"></span><span id="netsetup_no_acct_reuse"></span>

<span id="NETSETUP_NO_ACCT_REUSE"></span><span id="netsetup_no_acct_reuse"></span>**NETSETUP\_NO\_ACCT\_REUSE** (0x00020000)


</dt> <dd>

When joining the domain, do not reuse an existing account.

> [!Note]  
> This flag is supported on Windows 7, Windows Server 2008 R2, and later.

 

</dd> <dt>

<span id="NETSETUP_IGNORE_UNSUPPORTED_FLAGS"></span><span id="netsetup_ignore_unsupported_flags"></span>

<span id="NETSETUP_IGNORE_UNSUPPORTED_FLAGS"></span><span id="netsetup_ignore_unsupported_flags"></span>**NETSETUP\_IGNORE\_UNSUPPORTED\_FLAGS** (0x10000000)


</dt> <dd>

If this bit is set, unrecognized flags will be ignored by the **JoinDomainOrWorkgroup** function and [**NetJoinDomain**](/windows/desktop/api/lmjoin/nf-lmjoin-netjoindomain) will behave as if the flags were not set.

</dd> </dl> </dd> </dl>

## Return value

Returns a [system error code](/windows/desktop/Debug/system-error-codes), which may include one of the following numeric values. Any other number indicates an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum).

<dl> <dt>

**Success**
</dt> <dd>

0

</dd> <dt>

**5**
</dt> <dd>

Access is denied.

</dd> <dt>

**87**
</dt> <dd>

The parameter is incorrect.

</dd> <dt>

**110**
</dt> <dd>

he system cannot open the specified object.

</dd> <dt>

**1323**
</dt> <dd>

Unable to update the password.

</dd> <dt>

**1326**
</dt> <dd>

Logon failure: unknown username or bad password.

</dd> <dt>

**1355**
</dt> <dd>

The specified domain either does not exist or could not be contacted.

</dd> <dt>

**2224**
</dt> <dd>

The account already exists.

</dd> <dt>

**2691**
</dt> <dd>

The machine is already joined to the domain.

</dd> <dt>

**2692**
</dt> <dd>

The machine is not currently joined to a domain.

</dd> <dt>

**WBEM\_E\_ENCRYPTED\_CONNECTION\_REQUIRED**
</dt> <dd>

0x80041087

*Password* and *UserName* are specified but the authentication level is not **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. For Visual Basic, **wbemErrEncryptedConnectionRequired** is returned.

</dd> <dt>

**Other**
</dt> <dd>

1 4294967295

</dd> </dl>

## Remarks

When moving a computer from a domain to a workgroup, you must remove the computer from the domain (with a call to [**UnjoinDomainOrWorkgroup**](unjoindomainorworkgroup-method-in-class-win32-computersystem.md)) before calling this method to join a workgroup (with a call to **JoinDomainOrWorkgroup**). After calling this method, restart the affected computer to apply the changes.

*UserName* and *Password* can be left **null**. However, the authentication of the connection to WMI must be 6 in script or **WbemAuthenticationLevelPktPrivacy** in Visual Basic and other languages that can use the [wbemdisp.dll](/windows/desktop/WmiSdk/using-the-wmi-scripting-type-library) library. For more information, see [Setting the Default Process Security Level Using VBScript](/windows/desktop/WmiSdk/setting-the-default-process-security-level-using-vbscript).

In C++, set the authentication at **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** either in [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity), for the entire process, or in [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket), for a connection to the [**IWbemServices**](/windows/desktop/api/wbemcli/nn-wbemcli-iwbemservices) proxy. For more information, see [Setting Authentication Using C++](/windows/desktop/WmiSdk/setting-authentication-using-c-) and [Setting the Security on IWbemServices and Other Proxies](/windows/desktop/WmiSdk/setting-the-security-on-iwbemservices-and-other-proxies).

## Examples

The [Join a computer to a domain](https://Gallery.TechNet.Microsoft.Com/Join-a-computer-to-a-domain-6e19d905) PowerShell example joins a computer to a domain.

The following VBScript code example joins a computer to a domain and creates the computer's account in Active Directory.


```VB
Const JOIN_DOMAIN             = 1
Const ACCT_CREATE             = 2
Const ACCT_DELETE             = 4
Const WIN9X_UPGRADE           = 16
Const DOMAIN_JOIN_IF_JOINED   = 32
Const JOIN_UNSECURE           = 64
Const MACHINE_PASSWORD_PASSED = 128
Const DEFERRED_SPN_SET        = 256
Const INSTALL_INVOCATION      = 262144
strDomain   = "FABRIKAM"
strPassword = "ls4k5ywA"
strUser     = "shenalan"
Set objNetwork = CreateObject("WScript.Network")
strComputer = objNetwork.ComputerName
Set objComputer = GetObject("winmgmts:{impersonationLevel=Impersonate}!\\" & strComputer & _
                            "\root\cimv2:Win32_ComputerSystem.Name='" & strComputer & "'")
ReturnValue = objComputer.JoinDomainOrWorkGroup(strDomain, _
                                                strPassword, _
                                                strDomain & "\" & strUser, _
                                                NULL, _
                                                JOIN_DOMAIN + ACCT_CREATE)
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ComputerSystem**](win32-computersystem.md)
</dt> <dt>

[**UnjoinDomainOrWorkgroup method**](unjoindomainorworkgroup-method-in-class-win32-computersystem.md)
</dt> </dl>

 

