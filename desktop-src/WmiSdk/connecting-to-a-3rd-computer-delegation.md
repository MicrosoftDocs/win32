---
description: When you run a script on a local system that obtains data from a remote system, WMI supplies your credentials to the provider of the data on the remote system.
ms.assetid: e27ff207-b067-47df-9706-e8af51646d28
ms.tgt_platform: multiple
title: Delegating with WMI
ms.topic: article
ms.date: 05/31/2018
---

# Delegating with WMI

When you run a script on a local system that obtains data from a remote system, WMI supplies your credentials to the provider of the data on the remote system. This requires only an impersonation level of **Impersonate**, because only one network hop is required. However, if the script connects to WMI on the remote system and attempts to open a log file on an additional remote system, then the script fails unless the impersonation level is **Delegate**. **Delegate** impersonation level is required by any operation that involves more than one network hop. For more information about DCOM security in WMI, see [Setting Client Application Process Security](setting-client-application-process-security.md). For more information about a one-network hop connection between two computers, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

**To use delegation to connect to a computer through another computer**

1.  Enable delegation in Active Directory (**Active Directory Users and Computers** in **Control Panel** **Administrative Tasks**) on the domain controller. The account on the remote system must be marked as **Trusted for delegation** and the account on the local system must not be marked as **Account is sensitive and cannot be delegated**. the local system, the remote system, and the domain controller must be members of the same domain or in trusted domains.

    **Note**  Using delegation is a security risk because it gives processes outside of your direct control the ability to use your credentials.

2.  Modify your code in the following manner to indicate that you want to use delegation.

    <dl> <dt>

    <span id="PowerShell"></span><span id="powershell"></span><span id="POWERSHELL"></span>PowerShell
    </dt> <dd>

    Set the *-Impersonation* parameter on the WMI cmdlet to **Delegate**.

    </dd> <dt>

    <span id="VBScript"></span><span id="vbscript"></span><span id="VBSCRIPT"></span>VBScript
    </dt> <dd>

    Set the *impersonationLevel* parameter to **Delegate** in the call to [SWbemLocator.ConnectServer](swbemlocator-connectserver.md) or **Delegate**in the [moniker](constructing-a-moniker-string.md) string. You can also set the impersonation in a [**SWbemSecurity**](swbemsecurity.md)object.

    </dd> <dt>

    <span id="C__"></span><span id="c__"></span>C++
    </dt> <dd>

    Set the impersonation level parameter to **RPC\_C\_IMP\_LEVEL\_DELEGATE** in the call to [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) or [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket). For more information about when to make these calls, see [Initializing COM for a WMI Application](initializing-com-for-a-wmi-application.md).

    To pass the client identity to remote COM servers in C++, set cloaking in the call to [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket). For more information, see [Cloaking](../com/cloaking.md).

    </dd> </dl>

## Examples

The following code example shows a moniker string that sets the impersonation to **Delegate**. Be aware that the authority must be set to Kerberos.


```vb
set objWMIServices = Getobject("winmgmts:{impersonationLevel=Delegate,authority=kerberos:MyDomain\Computer_B}!\\ComputerB\Root\CIMv2")
```



The following code example shows how to set impersonation to **Delegate** (a value of 4) using [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md).


```vb
Set objLocator = CreateObject("WbemScripting.SWbemLocator")
Set objWMIService = objLocator.ConnectServer(Computer_B, _
                                             "Root\CIMv2", _
                                             AdminAccount, _
                                             MyPassword, _
                                             "kerberos:Domain\Computer_B")
objWMIService.Security_.ImpersonationLevel = 4
```



## Related topics

<dl> <dt>

[Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md)
</dt> <dt>

[Creating Processes Remotely with WMI](creating-processes-remotely.md)
</dt> </dl>

 

 
