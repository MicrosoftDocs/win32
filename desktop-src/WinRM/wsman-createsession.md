---
title: WSMan.CreateSession method (WSManDisp.h)
description: Creates a Session object that can then be used for subsequent network operations.
ms.assetid: 299d9a95-bd30-414c-996d-6633e8b7ce52
ms.tgt_platform: multiple
keywords:
- CreateSession method Windows Remote Management
- CreateSession method Windows Remote Management , WSMan object
- WSMan object Windows Remote Management , CreateSession method
topic_type:
- apiref
api_name:
- WSMan.CreateSession
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WSMan.CreateSession method

Creates a [**Session**](session.md) object that can then be used for subsequent network operations.

## Syntax


```VB
WSMan.CreateSession( _
  [ ByVal connection ], _
  [ ByVal flags ], _
  [ ByVal connectionOptions ] _
)
```



## Parameters

<dl> <dt>

*connection* \[in, optional\]
</dt> <dd>

The protocol and service to connect to, including either IPv4 or IPv6. The format of the connection information is as follows: <*Transport*><*Address*><*Suffix*>. For examples, see Remarks. If no connection information is provided, the local computer is used.

</dd> <dt>

*flags* \[in, optional\]
</dt> <dd>

The session flags that specify the authentication method, such as [*Negotiate authentication*](windows-remote-management-glossary.md) or [*Digest authentication*](windows-remote-management-glossary.md), for connecting to a remote computer. These flags also specify other session connection information, such as encoding or encryption. This parameter must contain one or more of the flags in **\_\_WSManSessionFlags** for a remote connection. For more information, see [Session Constants](session-constants.md). No flag settings are required for a connection to WinRM on the local computer. The default is **WSManFlagUseNegotiate**.

For more information, see [Authentication for Remote Connections](authentication-for-remote-connections.md) and the *connectionOptions* parameter.

</dd> <dt>

*connectionOptions* \[in, optional\]
</dt> <dd>

A pointer to a [**ConnectionOptions**](connectionoptions.md) object that contains a user name and password. The default is **NULL**.

</dd> </dl>

## Return value

A [**Session**](session.md) object that can then be used to perform local or remote WinRM operations.

## Remarks

The **CreateSession** method initializes the [**Session**](session.md) object by gathering parameters, such as flags, credentials, and a connection string for the *connection* parameter. **CreateSession** does not actually connect to the local or remote computer. If the connection cannot be established, a failure occurs on the first **Session** operation, such as a [**Get**](session-get.md) or [**Enumerate**](session-enumerate.md), after the call to **CreateSession**. This behavior differs from a [*WMI*](windows-remote-management-glossary.md) connection to a [*namespace*](windows-remote-management-glossary.md) on a remote computer. For more information, see [Windows Remote Management and WMI](windows-remote-management-and-wmi.md).

The following VBScript code example is used to call this method.


```VB
Set session = _
    wsman.CreateSession("<Transport><Address><Suffix>")
```



The following examples show the different formats used to specify connection information in the *connection* parameter (when creating an HTTPS session, the <*Address*> field must match the server computer certificate name, otherwise a failure occurs):

-   "https://service"

    Uses HTTPS to connect to the default web service location.

-   "https://service.corp.com/websvcs/wsman"

    Uses HTTPS to connect to the specific web service location.

-   "https://\[E3D7:0000:0000:0000:51F4:9BC8:C0A8:6420\]"

    Uses HTTPS and IPv6 with the default port.

-   "https://\[E3D7:0000:0000:0000:51F4:9BC8:C0A8:6420\]:9999/wsman"

    Uses HTTPS and IPv6 with the given port.

## Examples

The following VBScript code example creates a session on the local computer.


```VB
 Set NewSession = Wsman.CreateSession   
   
```



The following VBScript code example creates a session on a remote computer that is identified by an IP address. The script supplies a user name and password for an account. The flags **WSManFlagCredUserNamePassword** and **WSManFlagUseBasic** are combined to indicate that the account is a local account on the remote computer. If the creation of the session fails, the script terminates. The script uses the methods that return the constant, such as [**WSMan.SessionFlagUseBasic**](wsman-sessionflagusebasic.md).

To run this script, be aware that you must configure the default configuration settings for both client and server to allow unencrypted traffic and Basic authentication (**AllowUnencrypted** set to **True** and Basic set to **True**). For more information, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md).


```VB
iFlags = WSMan.SessionFlagUseBasic Or WSMan.SessionFlagCredUsernamePassword
Set Options = Wsman.CreateConnectionOptions
Options.Username = "MyUserName"
Options.Password = "MyPassword"
Set NewSession = WSMan.CreateSession("127.0.51.1", iFlags, _
    Options) 
```



In the following VBScript code example, the account is a domain account and Negotiate authentication is used. With Negotiate authentication, you must specify the user name as `computername\username` or `ipaddress\username`.


```VB
iFlags = WSMan.SessionFlagUseNegotiate Or WSMan.SessionFlagCredUsernamePassword
Set Options = Wsman.CreateConnectionOptions
Options.Username = "MyComputer\MyUserName"
Options.Password = "MyPassword"
Set NewSession = WSMan.CreateSession("127.0.51.1", iFlags, _
    Options) 
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**WSMan**](wsman.md)
</dt> <dt>

[**ConnectionOptions**](connectionoptions.md)
</dt> <dt>

[**Session**](session.md)
</dt> <dt>

[Authentication for Remote Connections](authentication-for-remote-connections.md)
</dt> <dt>

[Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md)
</dt> </dl>

 

 





