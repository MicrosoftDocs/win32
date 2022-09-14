---
title: Set the default process security level with VBScript
description: A script can use the default WMI authentication and impersonation settings. However, the script may need a connection with more security or may connect to a namespace that requires an encrypted connection.
ms.assetid: cb477224-3117-45e4-9271-613b58e48b6e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Set the default process security level with VBScript

A script can use the default WMI authentication and impersonation settings. However, the script may need a connection with more security or may connect to a namespace that requires an encrypted connection. For more information, see [Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md) and [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

In the simplest case, a script can use the default authentication and impersonation settings. WMI normally runs in a shared service host and shares the same authentication as other processes in the host. If you want to run the WMI process with a different level of authentication, run WMI with the [**winmgmt**](winmgmt.md) command with the **/standalonehost** switch and set the authentication level for WMI generally. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).

The following script uses default settings for impersonation and authentication levels.


```VB
strComputer = "." 
Set objServices = GetObject("winmgmts:\\" _
    & strComputer & "\root\CIMV2") 
set objProcessSet = objServices.ExecQuery _
     ("SELECT Name FROM Win32_Process",,48)
For Each Process in objProcessSet
    WScript.Echo Process.Name
Next
```



You can also use a [moniker](constructing-a-moniker-string.md) in a call to [**GetObject**](https://msdn.microsoft.com/library/e9waz863(v=VS.71).aspx), and set the default security settings, as in the following example.


```VB
strComputer = "." 
Set objServices = GetObject( _
    "winmgmts:{impersonationLevel=impersonate," _
    & "authenticationLevel=pktPrivacy}!root/cimv2")
set objProcessSet = objServices.ExecQuery _
     ("SELECT Name FROM Win32_Process",,48)
For Each Process in objProcessSet
    WScript.Echo Process.Name
Next
```



For more information about setting different impersonation or authentication levels in a script, or for setting the default values for a computer, see the following topics:

-   [Changing the Default Authentication Credentials Using VBScript](#changing-the-default-authentication-credentials-using-vbscript)
-   [Changing the Default Impersonation Settings Using VBScript](#changing-the-default-impersonation-levels-using-vbscript)
-   [Setting the Default Impersonation Level Using the Registry](#setting-the-default-impersonation-level-using-the-registry)
-   [Accessing the SWbemSecurity Object in VBScript](#accessing-the-swbemsecurity-object-in-vbscript)
-   [**SWbemSecurity**](swbemsecurity.md)

## Changing the Default Authentication Credentials Using VBScript

You can change the authentication level in a script using a [moniker](constructing-a-moniker-string.md) string, and the [**SWbemLocator**](swbemlocator.md) and [**SWbemSecurity**](swbemsecurity.md) objects.

The authentication level must be set according to the requirements of the target operating system to which you are connecting. For more information, see [Connecting Between Different Operating Systems](/windows/desktop/WmiSdk/troubleshooting-a-remote-wmi-connection).

The following VBScript code example shows how to change the authentication level in a script that obtains the free space data from a remote computer named "Server1".


```VB
strComputer = "Server1"
Set objWMIService = GetObject("winmgmts:{authenticationLevel=Pkt}!\\" _
    & strComputer & "\root\cimv2")
Set colDisks = objWMIService.ExecQuery ("Select * from Win32_LogicalDisk")
For each objDisk in colDisks
    Wscript.Echo "DeviceID: " & vbTab & objDisk.DeviceID & vbNewLine & _
        "FreeSpace: " & vbTab & objDisk.FreeSpace 
    NextstrComputer = "." 
    Set objServices = GetObject( "winmgmts:{impersonationLevel=impersonate," _
                               & "authenticationLevel=pktPrivacy}!root/cimv2")
    Set objProcessSet = objServices.ExecQuery("SELECT Name FROM Win32_Process",,48)
    For Each Process in objProcessSet
        WScript.Echo Process.Name
    Next
Next
```



In script moniker connections to WMI, use the short name shown in the "Moniker name/description" column of the table below. For example, in the following script, the authentication level is set to **WbemAuthenticationLevelPktIntegrity**.


```VB
SetobjWMIService = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!root\cimv2")
```



The following table lists the authentication levels you can set. These levels are defined in Wbemdisp.tlb in the enumeration [WbemAuthenticationLevelEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemauthenticationlevelenum).



| Name/value                                                      | Description                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WbemAuthenticationLevelDefault**<br/> 0<br/>      | Moniker: Default<br/> WMI uses the default Windows authentication setting. This is the recommended setting that allows WMI to negotiate to the level required by the server returning data. However, if the namespace requires encryption, use **WbemAuthenticationLevelPktPrivacy**.<br/> |
| **WbemAuthenticationLevelNone**<br/> 1<br/>         | Moniker: None<br/> Uses no authentication.<br/>                                                                                                                                                                                                                                            |
| **WbemAuthenticationLevelConnect**<br/> 2<br/>      | Moniker: Connect<br/> Authenticates the credentials of the client only when the client establishes a relationship with the server.<br/>                                                                                                                                                    |
| **WbemAuthenticationLevelCall**<br/> 3<br/>         | Call<br/> Authenticates only at the beginning of each call when the server receives the request.<br/>                                                                                                                                                                                      |
| **WbemAuthenticationLevelPkt**<br/> 4<br/>          | Moniker: Pkt<br/> Authenticates that all data received is from the expected client.<br/>                                                                                                                                                                                                   |
| **WbemAuthenticationLevelPktIntegrity**<br/> 5<br/> | Moniker: PktIntegrity<br/> Authenticates and verifies that none of the data transferred between client and server has been modified.<br/>                                                                                                                                                  |
| **WbemAuthenticationLevelPktPrivacy**<br/> 6<br/>   | Moniker: PktPrivacy<br/> Authenticates all previous impersonation levels and encrypts the argument value of each remote procedure call. Use this setting if the namespace to which you are connecting requires an encrypted connection.<br/>                                               |



 

To determine a successful call, check the return value after you change the authentication level.

For example, because local connections always have an authentication level of **wbemAuthenticationLevelPktPrivacy**, the following example fails to set the authentication level because it connects to the local computer.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate," _
    & "authenticationLevel=pktPrivacy}!" _
    & "\\" & strComputer & "\root\cimv2")
```



A provider can set the security on a namespace so that no data is returned unless you use packet privacy (PktPrivacy) in your connection to that namespace. This ensures that data is encrypted as it crosses the network. If you try to set a lower authentication level, you will get an access denied message. For more information, see [Securing WMI Namespaces](securing-wmi-namespaces.md).

## Changing the Default Impersonation Levels Using VBScript

When you make calls to the Scripting API for WMI, it is recommended that you use the defaults that WMI provides for the impersonation level. Remote calls and some providers with more than one network hop require a higher impersonation level than WMI uses. If the impersonation level is not sufficient, a provider might refuse a request or provide incomplete information.

If you do not set the impersonation level in either a moniker or by setting [**SWbemSecurity.ImpersonationLevel**](swbemsecurity-impersonationlevel.md) on a securable object, then set the default DCOM impersonation level for the operating system. The impersonation level must be set according to the requirements of the target operating system to which you are connecting. For more information, see [Connecting Between Different Operating Systems](/windows/desktop/WmiSdk/troubleshooting-a-remote-wmi-connection).

The following VBScript code example shows changing the impersonation level in the same script shown above.


```VB
strComputer = "Server1"
Set objWMIService = GetObject("winmgmts:{impersonationLevel=Impersonate}!\\" _
                              & strComputer & "\root\cimv2")
Set colDisks = objWMIService.ExecQuery("Select * from Win32_LogicalDisk")
For each objDisk in colDisks
Wscript.Echo "DeviceID: " & vbTab & objDisk.DeviceID & vbNewLine & _
             "FreeSpace: " & vbTab & objDisk.FreeSpace 
Next
```



The following table lists the authentication levels in [WbemImpersonationLevelEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemimpersonationlevelenum) that use.



| Name/value                                                    | Description                                                                                                                                                                                                                         |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **wbemImpersonationLevelAnonymous**<br/> 1<br/>   | Moniker: Anonymous<br/> Hides the credentials of the caller. Calls to WMI may fail with this impersonation level.<br/>                                                                                                  |
| **wbemImpersonationLevelIdentify**<br/> 2<br/>    | Moniker: Identify<br/> Allows objects to query the credentials of the caller. Calls to WMI may fail with this impersonation level.<br/>                                                                                 |
| **wbemImpersonationLevelImpersonate**<br/> 3<br/> | Moniker: Impersonate<br/> Allows objects to use the credentials of the caller. This is the recommended impersonation level for Scripting API for WMI calls.<br/>                                                        |
| **wbemImpersonationLevelDelegate**<br/> 4<br/>    | Moniker: Delegate<br/> Allows objects to permit other objects to use the credentials of the caller. This impersonation will work with Scripting API for WMI calls but may constitute an unnecessary security risk.<br/> |



 

The following example shows how to set the impersonation in a moniker string when obtaining a specific instance of [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process).


```VB
Set object = GetObject("winmgmts:{impersonationLevel=impersonate}!root\cimv2:Win32_Process.Handle='0'")
```



For more information, see [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md).

## Setting the Default Impersonation Level Using the Registry

If you have access to the registry, you can also set the default impersonation level registry key. This key specifies which impersonation level the Scripting API for WMI uses unless otherwise specified. The following path identifies the registry path.

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**Scripting**\\**Default Impersonation Level**

By default, the registry key is set to 3, specifying the Impersonate impersonation level. Some providers may require a higher level of impersonation.

## Accessing the SWbemSecurity Object in VBScript

The other way you can set the impersonation level is from the [**SWbemSecurity**](swbemsecurity.md) security object, which appears as the [**Security\_**](swbemservices-security-.md) property of the [**SWbemServices**](swbemservices.md), [**SWbemObject**](swbemobject.md), [**SWbemObjectSet**](swbemobjectset.md), [**SWbemEventSource**](swbemeventsource.md), [**SWbemObjectPath**](swbemobjectpath.md), and [**SwbemLocator**](swbemlocator.md) objects.

WMI passes the security setting of a parent object to the descendants of the original object. Therefore, you can set the impersonation level of an [**SWbemServices**](swbemservices.md) object after logging on to WMI and API calls using this object or objects created from it, such as objects of type [**SWbemObject**](swbemobject.md).

## Related topics

<dl> <dt>

[Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)
</dt> <dt>

[Securing Scripting Clients](securing-scripting-clients.md)
</dt> </dl>

 

