---
description: The moniker string format is similar to that of a standard WMI object path. For more information, see WMI Object Path Requirements.
ms.assetid: 1aacc523-2a2f-43f5-96a3-aa0387cbae3e
ms.tgt_platform: multiple
title: Constructing a Moniker String
ms.topic: article
ms.date: 05/31/2018
---

# Constructing a Moniker String

The moniker string format is similar to that of a standard WMI object path. For more information, see [WMI Object Path Requirements](wmi-object-path-requirements.md).

A moniker has the following parts:

-   The prefix WinMgmts: (mandatory). The prefix instructs the Windows Script Host (WSH) that the following code will be using the [Scripting API objects](scripting-api-objects.md).
-   A security settings component (optional)
-   A WMI object path component (optional)

You cannot specify a password in a WMI moniker string. If you must change the password (*strPassword* parameter) or the type of authentication (*strAuthority* parameter) when connecting to WMI, then call [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md). Be aware that you can only specify the password and authority in connections to remote computers. Attempting to set these in a script that is running on the local computer results in a error. For more information about when the security settings and object path components are used, see [WMI Security Settings](/previous-versions/tn-archive/ee156574(v=technet.10)).

The following moniker specifies the [**SWbemServices**](swbemservices.md) object that represents the namespace root\\default, with impersonation on and the wbemPrivilegeDebug (SeDebugPrivilege) privilege enabled, and the wbemPrivilegeSecurity (SeSecurityPrivilege) privilege disabled.


```VB
"winmgmts:{impersonationLevel=impersonate," & "(debug,!security)}!root\default"
```



> [!Note]
>
> All string literals are case-insensitive.
>
> The "!" prefix on a privilege indicates that the privilege is to be disabled; the omission of this prefix implies that the privilege is to be enabled.
>
> The "!" prefix is used on the computer name or namespace when security settings are specified in brackets before the computer name or namespace.

 

The following default assignments are allowed when specifying the object path:

-   The computer machine name can be omitted from the object path, in which case the local machine name is assumed.
-   The namespace can be omitted from the object path, in which case the default namespace is assumed.

    This is determined by the value of the registry key **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\**Scripting**\\**Default Namespace**, the default value is "Root\\CIMv2".

-   A class or instance can also be specified, in which case the returned object is a WMI object rather than a services object.

> [!Note]  
> If a class or instance is specified, you cannot omit the namespace when specifying the computer machine name.

 

For a reference of the Privilege Constants used on WMI moniker string, see [Privilege Constants](privilege-constants.md), and the "Scripting short name" descriptors.

## Valid Moniker Strings

The following examples show valid moniker strings.

The following moniker identifies the default namespace on the local computer. An [**SWbemServices**](swbemservices.md) object is returned.


```VB
WinMgmts:
```



The following moniker identifies the default namespace on the computer myServer. An [**SWbemServices**](swbemservices.md) object is returned.


```VB
"WinMgmts://myServer"
```



The following moniker identifies the root\\cimv2 namespace on the myServer computer. An [**SWbemServices**](swbemservices.md) object is returned.


```VB
"WinMgmts://myServer/root/cimv2"
```



The following moniker identifies the root\\cimv2 namespace on the local server. An [**SWbemServices**](swbemservices.md) object is returned.


```VB
"WinMgmts:root/cimv2"
```



The following moniker identifies the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class in the root\\cimv2 namespace on the myServer server. An [**SWbemObject**](swbemobject.md) object is returned.


```VB
"WinMgmts:{impersonationLevel=impersonate}" _
    & "!//myServer/root/cimv2:Win32_LogicalDisk"
```



The following moniker identifies the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class in the root\\cimv2 namespace on the local server. An [**SWbemObject**](swbemobject.md) object is returned.


```VB
"WinMgmts:{impersonationLevel=impersonate}" & "!root/cimv2:Win32_LogicalDisk"
```



The following moniker identifies the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class in the default namespace on the local server. An [**SWbemObject**](swbemobject.md) object is returned.


```VB
"WinMgmts:{impersonationLevel=impersonate}" & "!Win32_LogicalDisk"
```



The following moniker identifies the instance of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) corresponding to drive C: in the default scripting namespace on the local server. An [**SWbemObject**](swbemobject.md) object is returned. The default namespace for scripting is determined by the default namespace configuration setting as specified in the WMI Control. For more information, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md).


```VB
"WinMgmts::Win32_LogicalDisk='C:'"
```



The following moniker identifies the instance of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) corresponding to drive C: in the root\\cimv2 namespace on the myServer server. An [**SWbemObject**](swbemobject.md) object is returned.


```VB
"WinMgmts:{impersonationLevel=impersonate}" & "!//myServer/root/cimv2:Win32_LogicalDisk="C:""
```



The following moniker identifies the instance of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) corresponding to drive C: in the root\\cimv2 namespace on the local server. An [**SWbemObject**](swbemobject.md) object is returned.


```VB
"WinMgmts:{impersonationLevel=impersonate}" & "!root/cimv2:Win32_LogicalDisk="C:""
```



The following moniker identifies the instance of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) corresponding to drive C: in the default namespace on the local server. An [**SWbemObject**](swbemobject.md) object is returned.


```VB
"WinMgmts:{impersonationLevel=impersonate}" & "!Win32_LogicalDisk="C:""
```



The following moniker sets the impersonation level to impersonate and sets the SE\_DEBUG privilege.


```VB
"WinMgmts:{impersonationLevel=impersonate, (Debug)}"
```



The following moniker sets the impersonation level to impersonate and sets the SE\_DEBUG privilege. It also revokes the SE\_SHUTDOWN privilege.


```VB
"WinMgmts:{impersonate,(Debug,!Shutdown)}"
```



The following moniker retrieves American English localized descriptions for the **myclass** class from the root\\wmi namespace.


```VB
"WinMgmts:[locale=ms_409]!root/wmi:myclass"
```



The following moniker requests Kerberos authentication using the principal mydomain\\server.


```VB
"Winmgmts:{impersonationLevel=delegate," _
    & "authority=kerberos:mydomain\server}" _
    & "!//myserver/root/default:__cimomidentification=@"
```



The following moniker requests NTLM authentication using the mydomain domain.


```VB
"Winmgmts:{impersonationLevel=impersonate," & _
    "authority=ntlmdomain:mydomain} " & _
    "!//myserver/root/default:__cimomidentification=@
```



The following VBScript code example shows how to combine security and locale parameters in a moniker.


```VB
'*****************************************************************
'   Name    :  Moniker.vbs
'
'   Purpose :  This example shows how to set various 
'              parameters in a moniker. 
'****************************************************************

Set myobj = GetObject("WINMGMTS:" _
            & "{impersonationLevel=impersonate," _
            & "authenticationLevel=pktPrivacy," _
            & "authority=ntlmdomain:mydomain," _
            & "(Debug,!Shutdown)}" _
            & "[locale=ms_409]" _
            & "!\\User1\ROOT\CIMV2:Win32_LogicalDisk=""C:""")

wscript.echo "File system = " & myobj.filesystem
```



> [!Note]
>
> Although monikers provide more direct access to objects, in certain circumstances, repeated use of monikers may be less efficient than the equivalent code that explicitly connects to WMI. If application performance is a consideration, consider using the alternative mechanisms.
>
> It is not possible to use the **GetObject** function provided by VBScript to update or set data when running scripts embedded within an HTML page, as Microsoft Internet Explorer denies the use of this call for security reasons.

 

 

 
