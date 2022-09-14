---
description: When accessing a Windows Management Instrumentation (WMI) server with a script, you can choose between NT LAN Manager (NTLM) or Kerberos authentication protocols.
ms.assetid: db2dc750-bfdd-4f6c-859b-e104814f0800
ms.tgt_platform: multiple
title: Setting the Authentication Service Using VBScript
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Setting the Authentication Service Using VBScript

When accessing a Windows Management Instrumentation (WMI) server with a script, you can choose between NT LAN Manager (NTLM) or Kerberos authentication protocols. Specifying Kerberos is not required except when using delegation. For more information, see [Connecting to a 3rd Computer-Delegation](connecting-to-a-3rd-computer-delegation.md).

Because operating system versions differ in which authentication service they use, it is recommended that you do not specify a value for the authority field when connecting to a remote system. Instead, allow the operating system and distributed version of Component Object Model (DCOM) to select NTLM or Kerberos. If an authentication service is specified, the syntax requires the server principal name, which is the name of the target computer rather than the domain controller.

You can use the authority parameter only with connections to remote WMI servers. The connection attempt fails if you attempt to set authorization levels as part of a moniker or with a call to [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) for a local connection.

Perform the following procedure to specify the authentication service that you want to use in the *strAuthority* parameter of the [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) method or the [moniker](constructing-a-moniker-string.md) string connection.

**To specify NTLM or Kerberos authentication with the Scripting API for WMI**

1.  If the *strAuthority* parameter begins with the string "kerberos:", WMI assumes the string refers to a Kerberos principal name and Kerberos authentication is used. If the *strAuthority* parameter begins with the string "ntlmdomain:", WMI uses NTLM authentication instead.
2.  Alternately, You can use the authority part of a moniker to specify the type of authentication used to connect to WMI. To use Kerberos authentication when using a moniker include the string, "authority=kerberos:" followed by the principal name. To use NTLM authentication, include the string, "authority=ntlmdomain:" followed by the NTLM domain name.

    The following example shows you a moniker that requests Kerberos authentication using the principal "mydomain\\server".

    ```VB
    winmgmts:{impersonationLevel=delegate, _
            authority=kerberos:mydomain\server} _
            !//myserver/root/default:__cimomidentification=@
    ```

    

    In contrast, the following example shows you a moniker that requests NTLM authentication using the domain "mydomain".

    ```VB
    winmgmts:{impersonationLevel=impersonate, _
            authority=ntlmdomain:mydomain} _
            !//myserver/root/default:__cimomidentification=@
    ```

    

 

 



