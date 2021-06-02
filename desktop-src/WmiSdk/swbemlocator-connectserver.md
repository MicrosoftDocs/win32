---
description: Connects to the namespace on the computer that is specified in the strServer parameter.
ms.assetid: 31364c68-b031-4cf0-851f-b4e302f077e0
ms.tgt_platform: multiple
title: SWbemLocator.ConnectServer method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemLocator.ConnectServer
- ISWbemLocator.ConnectServer
- ISWbemLocator.ConnectServer
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemLocator.ConnectServer method

The **ConnectServer** method of the [**SWbemLocator**](swbemlocator.md) object connects to the namespace on the computer that is specified in the *strServer* parameter. The target computer can be either local or remote, but it must have WMI installed. For examples and a comparison with the moniker type of connection, see [Creating a WMI Script](creating-a-wmi-script.md).

Starting with Windows Vista, **SWbemLocator.ConnectServer** can connect with computers running IPv6 using an IPv6 address in the *strServer* parameter. For more information, see [IPv6 and IPv4 Support in WMI](ipv6-and-ipv4-support-in-wmi.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objwbemServices = .ConnectServer( _
  [ ByVal strServer ], _
  [ ByVal strNamespace ], _
  [ ByVal strUser ], _
  [ ByVal strPassword ], _
  [ ByVal strLocale ], _
  [ ByVal strAuthority ], _
  [ ByVal iSecurityFlags ], _
  [ ByVal objwbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strServer* \[in, optional\]
</dt> <dd>

Computer name to which you are connecting. If the remote computer is in a different domain than the user account under which you log in, then use the fully qualified computer name. If you do not provide this parameter, the call defaults to the local computer.

Example: `server1.network.fabrikam`

You also can use an IP address in this parameter. If the IP address is in IPv6 format, the target computer must be running IPv6. An address in IPv4 looks like `123.123.123.123`

An IP address in IPv6 format looks like `2010:836B:4179::836B:4179`

For more information on DNS and IPv4, see the Remarks section.

</dd> <dt>

*strNamespace* \[in, optional\]
</dt> <dd>

String that specifies the namespace to which you log on. For example, to log on to the root\\default namespace, use root\\default. If you do not specify this parameter, it defaults to the namespace that is configured as the default namespace for scripting. For more information, see [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md).

Example: "root\\CIMV2"

</dd> <dt>

*strUser* \[in, optional\]
</dt> <dd>

User name to use to connect. The string can be in the form of either a user name or a Domain\\Username. Leave this parameter blank to use the current security context. The *strUser* parameter should only be used with connections to remote WMI servers. If you attempt to specify *strUser* for a local WMI connection, the connection attempt fails. If Kerberos authentication is in use, then the username and password that is specified in *strUser* and *strPassword* cannot be intercepted on a network. You can use the UPN format to specify the *strUser*.

Example: "DomainName\\UserName"

> [!Note]  
> If a domain is specified in *strAuthority*, then the domain must not be specified here. Specifying the domain in both parameters results in an Invalid Parameter error.

 

</dd> <dt>

*strPassword* \[in, optional\]
</dt> <dd>

String that specifies the password to use when attempting to connect. Leave the parameter blank to use the current security context. The *strPassword* parameter should only be used with connections to remote WMI servers. If you attempt to specify *strPassword* for a local WMI connection, the connection attempt fails. If Kerberos authentication is in use then the username and password that is specified in *strUser* and *strPassword* cannot be intercepted on the network.

</dd> <dt>

*strLocale* \[in, optional\]
</dt> <dd>

String that specifies the localization code. If you want to use the current locale, leave it blank. If not blank, this parameter must be a string that indicates the desired locale where information must be retrieved. For Microsoft locale identifiers, the format of the string is "MS\_xxxx", where xxxx is a string in the hexadecimal form that indicates the LCID. For example, American English would appear as "MS\_409".

</dd> <dt>

*strAuthority* \[in, optional\]
</dt> <dd>

<dt>

""
</dt> <dd>

This parameter is optional. However, if it is specified, only Kerberos or NTLMDomain can be used.

</dd> <dt>

Kerberos:
</dt> <dd>

If the *strAuthority* parameter begins with the string "Kerberos:", then Kerberos authentication is used and this parameter should contain a Kerberos principal name. The Kerberos principal name is specified as Kerberos:*domain*, such as `Kerberos:fabrikam` where `fabrikam` is the server to which you are attempting to connect.

Example: "Kerberos:DOMAIN"

</dd> <dt>

NTLMDomain:
</dt> <dd>

To use NT Lan Manager (NTLM) authentication, you must specify it as NTLMDomain:*domain*, such as `NTLMDomain:fabrikam` where `fabrikam` is the name of the domain.

Example: "NTLMDomain:DOMAIN"

</dd> </dl>

If you leave this parameter blank, the operating system negotiates with COM to determine whether NTLM or Kerberos authentication is used. This parameter should only be used with connections to remote WMI servers. If you attempt to set the authority for a local WMI connection, the connection attempt fails.

> [!Note]  
> If the domain is specified in *strUser*, which is the preferred location, then it must not be specified here. Specifying the domain in both parameters results in an Invalid Parameter error.

 

</dd> <dt>

*iSecurityFlags* \[in, optional\]
</dt> <dd>

Used to pass flag values to **ConnectServer**.

<dt>

0 (0x0)
</dt> <dd>

A value of 0 for this parameter causes the call to **ConnectServer** to return only after the connection to the server is established. This could cause your program to stop responding indefinitely if the connection cannot be established.

</dd> <dt>

<span id="wbemConnectFlagUseMaxWait"></span><span id="wbemconnectflagusemaxwait"></span><span id="WBEMCONNECTFLAGUSEMAXWAIT"></span>

<span id="wbemConnectFlagUseMaxWait"></span><span id="wbemconnectflagusemaxwait"></span><span id="WBEMCONNECTFLAGUSEMAXWAIT"></span>****wbemConnectFlagUseMaxWait**** (128 (0x80))


</dt> <dd>

The **ConnectServer** call is guaranteed to return in 2 minutes or less. Use this flag to prevent your program from ceasing to respond indefinitely if the connection cannot be established.

</dd> </dl> </dd> <dt>

*objwbemNamedValueSet* \[in, optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If successful, WMI returns an [**SWbemServices**](swbemservices.md) object that is bound to the namespace that is specified in *strNamespace* on the computer that is specified in *strServer*.

## Error codes

After the completion of the **ConnectServer** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

The current or specified user name and password were not valid or authorized to make the connection.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidNamespace** - 2147749902 (0x8004100E)
</dt> <dd>

The specified namespace did not exist on the server.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

An invalid parameter was specified, or the namespace could not be parsed.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> <dt>

**wbemErrTransportFailure** - 2147749909
</dt> <dd>

A networking error occurred, preventing normal operation.

</dd> </dl>

## Remarks

The **ConnectServer** method is often used when connecting to an account with a different username and password credentials on a remote computer because you cannot specify a different password in a [moniker](constructing-a-moniker-string.md) string. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

Using an IPv4 address to connect to a remote server may result in unexpected behavior. The likely cause is stale DNS entries in your environment. In these circumstances, the stale PTR entry for the machine will be used, with unpredictable results. To avoid this behavior, you can append a period (".") to the IP address before calling ConnectServer. This causes the reverse DNS lookup to fail, but may allow the **ConnectServer** call to succeed on the correct machine.

## Examples

The following VBScript code example describes how to connect to a remote computer to obtain [**Win32\_IP4RouteTable**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4routetable) data. The domain name that is specified in *strDomain* is used in *strAuthority*.


```VB
Const intMin = 3600
strComputer = "RemoteComputer" 
strDomain = "DomainName"  
Wscript.StdOut.Write "Please enter your user name:"
strUser = Wscript.StdIn.ReadLine 
Set objPassword = CreateObject("ScriptPW.Password")
Wscript.StdOut.Write "Please enter your password:"
strPassword = objPassword.GetPassword()
Wscript.Echo

Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator") 
Set objWMIService = objSWbemLocator.ConnectServer(strComputer, _ 
                                                  "root\CIMV2", _ 
                                                  strUser, _ 
                                                  strPassword, _ 
                                                  "MS_409", _ 
                                                  "NTLMDomain:" + strDomain) 
Set colItems = objWMIService.ExecQuery("SELECT * FROM Win32_IP4RouteTable",,48) 
For Each objItem in colItems
    WScript.Echo "Age in Minutes: " & int(objItem.Age/intMin) & VBNewLine _
               & "Description:    " & objItem.Description & VBNewLine _
               & "Destination:    " & objItem.Destination & VBNewLine _
               & "InterfaceIndex: " & objItem.InterfaceIndex & VBNewLine _
               & "Mask:           " & objItem.Mask & VBNewLine _
               & "Metric1:        " & objItem.Metric1 & VBNewLine _
               & "Metric2:        " & objItem.Metric2 & VBNewLine _
               & "Metric3:        " & objItem.Metric3 & VBNewLine _
               & "Metric4:        " & objItem.Metric4 & VBNewLine _
               & "Metric5:        " & objItem.Metric5 & VBNewLine _
               & "Name:           " & objItem.Name & VBNewLine _
               & "NextHop:        " & objItem.NextHop & VBNewLine _
               & "Protocol:       " & objItem.Protocol & VBNewLine _
               & "Type: " & objItem.Type
    WScript.Echo
   </example>
Next
```



The following PowerShell snippet access a remote server and lists the available WMI classes.


```PowerShell
$NameSpace = 'root\ccm'
$ComputerName = 'sccm.company.com'
$WbemLocator = New-Object -ComObject "WbemScripting.SWbemLocator"
$WbemServices = $WbemLocator.ConnectServer($ComputerName, $Namespace)
$WbemClasses = $WbemServices.SubclassesOf()
$WbemClasses
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemLocator<br/>                                                          |
| IID<br/>                      | IID\_ISWbemLocator<br/>                                                           |



## See also

<dl> <dt>

[**SWbemLocator**](swbemlocator.md)
</dt> <dt>

[**SWbemServices**](swbemservices.md)
</dt> <dt>

[Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)
</dt> <dt>

[Creating a WMI Script](creating-a-wmi-script.md)
</dt> </dl>

 

