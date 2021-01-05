---
description: Removes a computer system from a domain or workgroup.
ms.assetid: 79ee177e-81e2-441b-b39a-2fb53a0145bf
ms.tgt_platform: multiple
title: UnjoinDomainOrWorkgroup method of the Win32_ComputerSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ComputerSystem.UnjoinDomainOrWorkgroup
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# UnjoinDomainOrWorkgroup method of the Win32\_ComputerSystem class

The **UnjoinDomainOrWorkgroup** method removes a computer system from a domain or workgroup.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 UnjoinDomainOrWorkgroup(
  [in] string Password,
  [in] string UserName,
  [in] uint32 FUnjoinOptions = 
);
```



## Parameters

<dl> <dt>

*Password* \[in\]
</dt> <dd>

If the *UserName* parameter specifies an account name, the *Password* parameter must point to the password to use when connecting to the domain controller. Otherwise, this parameter must be **NULL**.

> [!Note]  
> *Password* must use a high authentication level, not less than **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**, when connecting to Winmgmt or [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) on the [**IWbemServices**](/windows/desktop/api/wbemcli/nn-wbemcli-iwbemservices) pointer. If local to Winmgmt, this is not a concern.

 

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

Pointer to a constant null-terminated character string that specifies the account name to use when connecting to the domain controller. Must specify a domain and user account, for example, "domain\\user" or "user@domain". If this parameter is **NULL**, the caller context is used.

> [!Note]  
> *UserName* must use a high authentication level, not less than **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**, when connecting to Winmgmt or [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) on the [**IWbemServices**](/windows/desktop/api/wbemcli/nn-wbemcli-iwbemservices) pointer. If local to Winmgmt, this is not a concern.

 

</dd> <dt>

*FUnjoinOptions* \[in\]
</dt> <dd>

Set of bit flags defining the unjoin options.

<dt>



 (0)


</dt> <dd>

Default. No options.

</dd> <dt>

<span id="NETSETUP_ACCT_DELETE"></span><span id="netsetup_acct_delete"></span>

<span id="NETSETUP_ACCT_DELETE"></span><span id="netsetup_acct_delete"></span>**NETSETUP\_ACCT\_DELETE** (4)


</dt> <dd>

Disable the Active Directory account after the unjoin operation, but do not delete the account.

</dd> </dl> </dd> </dl>

## Return value

The **UnjoinDomainOrWorkgroup** method returns 0 (zero) on success or when no options are involved. Any other value indicates an error. For error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Other** (1 4294967295)
</dt> </dl>

## Remarks

After calling this method, restart the affected computer to apply the changes.

## Examples

[The Unjoin a Computer from a Domain](https://Gallery.TechNet.Microsoft.Com/c2025ace-cb51-4136-9de9-db8871f79f62) VBScript sample unjoins the local computer from its current domain and disables the computer account.

The [Unjoin a Computer from a Domain using VBS script](https://Gallery.TechNet.Microsoft.Com/Unjoin-a-Computer-from-a-825249e1) sample unjoins a specified computer from a domain. .

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

[**JoinDomainOrWorkgroup method**](joindomainorworkgroup-method-in-class-win32-computersystem.md)
</dt> </dl>

 

