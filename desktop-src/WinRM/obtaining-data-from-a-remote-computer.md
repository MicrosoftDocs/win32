---
title: Obtaining Data from a Remote Computer
description: You can obtain data or manage resources on remote computers as well as the local computer. Connecting to a remote computer in a Windows Remote Management script is very similar to making a local connection.
ms.assetid: 578eee80-a6c1-4456-9683-14e0a3386248
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Obtaining Data from a Remote Computer

You can obtain data or manage resources on remote computers as well as the local computer. Connecting to a remote computer in a Windows Remote Management script is very similar to making a local connection. WMI instance data is available and, if the remote computer has BMC hardware that can communicate using the WS-Management protocol, then [Intelligent Platform Management Interface (IPMI)](/previous-versions/windows/desktop/ipmiprv/ipmi-provider) data is also available. For more information, see [Windows Remote Management and WMI](windows-remote-management-and-wmi.md) and [Remote Hardware Management](remote-hardware-management.md).

You may need to create a [**ConnectionOptions**](connectionoptions.md) object to specify information about the type of authentication requested for the logon.

If the account on the remote computer has the same logon username and password, the only extra information you need is the transport, the domain name, and the computer name. Because of [User Account Control (UAC)](https://support.microsoft.com/help/922708/how-to-use-user-account-control-uac-in-windows-vista), the remote account must be a domain account and a member of the remote computer Administrators group. If the account is a local computer member of the Administrators group, then UAC does not allow access to the WinRM service. To access a remote WinRM service in a workgroup, UAC filtering for local accounts must be disabled by creating the following DWORD registry entry and setting its value to 1: **\[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\] LocalAccountTokenFilterPolicy**.

**To connect to a remote computer using your logon username and password**

1.  Specify the target computer with a fully qualified domain name or an IP address and assign this to a constant. If an IPv6 address is specified, then the address must be enclosed in square brackets.

    ```VB
    Const RemoteComputer = "ComputerName.domain.com"
    ```

    

2.  Create a [**WSMan**](wsman.md) object.

    ```VB
    Set objWsman = CreateObject("WSMan.Automation")
    ```

    

3.  Create the session, specifying the transport, HTTP or HTTPS, and concatenating it with the constant representing the target computer.

    ```VB
    
    Set objSession = objWsman.CreateSession("https://" & RemoteComputer)
    ```

    

The following VBScript code example shows the complete script. The script includes a subroutine to transform the data from raw XML to human-readable form. For more information, see [Displaying XML Output from WinRM Scripts](displaying-xml-output-from-winrm-scripts.md).


```VB
Const RemoteComputer = "ComputerName.domain.com"

Set objWsman = CreateObject("WSMan.Automation")
Set objSession = objWsman.CreateSession("https://" & RemoteComputer)
strResource = "http://schemas.microsoft.com/wbem/wsman/1/" & _
  "wmi/root/cimv2/Win32_OperatingSystem"
Set objResponse = objSession.Enumerate(strResource)

While Not objResponse.AtEndOfStream
    DisplayOutput(objResponse.ReadItem) 
Wend

'****************************************************
' Displays WinRM XML message using built-in XSL
'****************************************************
Sub DisplayOutput(strWinRMXml)
    Dim xmlFile, xslFile
    Set xmlFile = CreateObject("MSXml.DOMDocument") 
    Set xslFile = CreateObject("MSXml.DOMDocument")
    xmlFile.LoadXml(strWinRMXml)
    xslFile.Load("WsmTxt.xsl")
    Wscript.Echo xmlFile.TransformNode(xslFile) 
End Sub
```



**To connect to a remote computer using a different account**

1.  Specify the target computer with a fully qualified domain name or an IP address and assign this to a constant. If an IPv6 address is specified, then the address must be enclosed in square brackets.

    ```VB
    Const RemoteComputer = "ComputerName.domain.com"
    ```

    

2.  Create a [**WSMan**](wsman.md) object.

    ```VB
    Set objWsman = CreateObject("Wsman.Automation")
    
    ```

    

3.  Call the [**WSMan.CreateConnectionOptions**](wsman-createconnectionoptions.md) method to create a [**ConnectionOptions**](connectionoptions.md) object. The account on the remote computer must be a member of the local computer administrators group.

    ```VB
    Set objConnectionOptions = objWsman.CreateConnectionOptions
    objConnectionOptions.UserName = "Username"
    objConnectionOptions.Password = "Password"
    ```

    

4.  On the [**WSman.CreateSession**](wsman-createsession.md) call, specify the appropriate session connection flags in the *flags* parameter. For more information, see [Session Constants](session-constants.md). Specify the target computer with a fully qualified computer name or an IP address and the transport—http or https. This script requests [*Kerberos*](windows-remote-management-glossary.md) authentication from the remote WinRM service.

    Unlike WMI scripts, you can use several methods of authentication in WinRM scripts. For more information, see [Authentication for Remote Connections](authentication-for-remote-connections.md).

    ```VB
    iFlags = objWsman.SessionFlagUseKerberos Or _
      objWsman.SessionFlagCredUserNamePassword
    Set objSession = objWsman.CreateSession("https://" & RemoteComputer, _
      iFlags, objConnectionOptions)
    ```

    

5.  After the session object is available, you can call any of the [**Session**](session.md) object methods to obtain data for a resource. You can get data for any resource that is available on the computer on which the session is running. For more information, see [Obtaining Data from the Local Computer](obtaining-data-from-the-local-computer.md).

The following VBScript code example shows the complete script. The script includes a subroutine to transform the data from raw XML to human-readable form. For more information, see [Displaying XML Output from WinRM Scripts](displaying-xml-output-from-winrm-scripts.md). The script specifies Kerberos authentication, but if the remote computer is in a workgroup rather than a domain, specifying Kerberos generates an error.


```VB
Const RemoteComputer = "ComputerName.domain.com"

Set objWsman = CreateObject("Wsman.Automation")
Set objConnectionOptions = objWsman.CreateConnectionOptions
objConnectionOptions.UserName = "Username"
objConnectionOptions.Password = "Password"
iFlags = objWsman.SessionFlagUseKerberos Or _
  objWsman.SessionFlagCredUserNamePassword
Set objSession = objWsman.CreateSession("https://" & RemoteComputer, _
  iFlags, objConnectionOptions)
strResource = "http://schemas.microsoft.com/wbem/wsman/1/" & _
  "wmi/root/cimv2/Win32_OperatingSystem"
Set objResponse = objSession.Enumerate(strResource)

While Not objResponse.AtEndOfStream
    DisplayOutput(objResponse.ReadItem) 
Wend

'****************************************************
' Displays WinRM XML message using built-in XSL
'****************************************************
Sub DisplayOutput(strWinRMXml)
    Dim xmlFile, xslFile
    Set xmlFile = CreateObject("MSXml2.DOMDocument.3.0") 
    Set xslFile = CreateObject("MSXml2.DOMDocument.3.0")
    xmlFile.LoadXml(strWinRMXml)
    xslFile.Load("WsmTxt.xsl")
    Wscript.Echo xmlFile.TransformNode(xslFile) 
End Sub
```



## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Using Windows Remote Management](using-windows-remote-management.md)
</dt> <dt>

[Windows Remote Management Reference](windows-remote-management-reference.md)
</dt> </dl>

 

 