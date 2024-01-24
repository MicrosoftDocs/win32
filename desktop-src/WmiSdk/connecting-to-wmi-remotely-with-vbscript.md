---
description: You can create a remote connection to WMI with VBScript by creating a connection object. This object contains the name of the computer, the WMI namespace you want to connect to, as well as any relevant credentials and authentication levels.
ms.assetid: b2ad262b-148d-47cc-8be7-6df99245aa7f
ms.tgt_platform: multiple
title: Connecting to WMI Remotely with VBScript
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Connecting to WMI Remotely with VBScript

You can create a remote connection to WMI with VBScript by creating a connection object. This object contains the name of the computer, the WMI namespace you want to connect to, as well as any relevant credentials and authentication levels.

**To connect to a remote system using VBScript**

1.  Specify the connection information such as the remote computer name, credentials, and the authentication level for the connection.

    If you are connecting to a remote computer using the same credentials (domain and user name) you are logged on with, then you can specify the connection information in a [**GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject)[moniker](constructing-a-moniker-string.md), as described in the following code sample.

    ```VB
    strComputer = "Computer_B"
    Set objWMIService = GetObject("winmgmts:{impersonationLevel=Impersonate}!\\" & strComputer & "\Root\CIMv2")
    ```

    

    Generally speaking, you should specify the WMI namespace to connect to on the remote computer. This is because it is possible that the default namespace is not the same on different computers. Specifying the namespace ensures that you connect to the same namespace on all computers.

    For more information on VBScript constants and scripting strings for using the moniker connection, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

2.  If you connect to a remote computer in a different domain or using a different user name and password, then you must use the [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) method.

    As with a moniker, you use **ConnectServer** to specify the credentials, authentication level, and namespace for the remote connection. The following code sample describes using ConnectServer to access a remote computer using an administrator account and password.

    ```VB
    strComputer = "Computer_B"
    Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
    Set objSWbemServices = objSWbemLocator.ConnectServer(strComputer, _
                                                         "Root\CIMv2", _
                                                         "fabrikam\administrator", _
                                                         "password")
    ```

    

3.  When using the [**ConnectServer**](swbemlocator-connectserver.md) function for remote connections, set impersonation and authentication on the security object obtained by a call to [**SWbemServices.Security**](swbemservices-security-.md). You can use the enumeration [WbemImpersonationLevelEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemimpersonationlevelenum) to specify impersonation level.

    The following code sample sets the impersonation level for the previous VBScript code sample.

    ```VB
    objSWbemServices.Security_.ImpersonationLevel = 3
    ```

    

    Note that some connections require a specific authentication level. For more information, see [Setting Client Application Process Security](setting-client-application-process-security.md) and [Securing Scripting Clients](securing-scripting-clients.md).

    In particular, you should set the authentication level to **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** or 6 if the namespace to which you are connecting on the remote computer requires an encrypted connection before it will return data. You can also use this authentication level, even if the namespace does not require it. This ensures that data is encrypted as it crosses the network. If you attempt to set a lower authentication level than is allowed, an access denied message will be returned. For more information, see [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

Once you have made your connection, you can continue to access WMI data. For more information, see [WMI Tasks for Scripts and Applications](wmi-tasks-for-scripts-and-applications.md).

## Examples

For a larger VBScript sample, see the Examples section in the [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) reference page.

The following VBScript code example connects to a group of remote computers in the same domain by creating an array of remote computer names and then displaying names of the Plug and Play devices—instances of [**Win32\_PnPEntity**](/windows/desktop/CIMWin32Prov/win32-pnpentity)—on each computer. To run the script below, you must be an administrator on the remote computers. Note that the "\\\\" required before the remote computer name is added by the script following the impersonation level setting. For more information about WMI paths, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).


```VB
On Error Resume Next 
arrComputers = Array("Computer1","Computer2","Computer3")
For Each strComputer In arrComputers
    WScript.Echo
    WScript.Echo "===================================="
    WScript.Echo "Computer: "& strComputer
    WScript.Echo "===================================="

    Set objWMIService = GetObject("winmgmts:\\" & strComputer& "\Root\CIMv2") 
    Set colItems = objWMIService.ExecQuery("SELECT * FROM Win32_PnPEntity",,48) 
    For Each objItem in colItems 
        Wscript.Echo "-----------------------------------"
        Wscript.Echo "Win32_PnPEntity instance"
        Wscript.Echo "-----------------------------------"
        Wscript.Echo "Name: "& objItem.Name
        Wscript.Echo "Status: "& objItem.Status
    Next
Next
```



The following VBScript code example enables you to connect to a remote computer using different credentials. For example, a remote computer in a different domain or connecting to a remote computer requiring a different user name and password. In this case, use the [**SWbemServices.ConnectServer**](swbemlocator-connectserver.md) connection.


```VB
' Full Computer Name
' can be found by right-clicking My Computer,
' then click Properties, then click the Computer Name tab)
' or use the computer's IP address
strComputer = "FullComputerName" 
strDomain = "DOMAIN" 
Wscript.StdOut.Write "Please enter your user name:"
strUser = Wscript.StdIn.ReadLine 
Set objPassword = CreateObject("ScriptPW.Password")
Wscript.StdOut.Write "Please enter your password:"
strPassword = objPassword.GetPassword()
 
Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
Set objSWbemServices = objSWbemLocator.ConnectServer(strComputer, _
                                                     "Root\CIMv2", _
                                                     strUser, _
                                                     strPassword, _
                                                     "MS_409", _
                                                     "ntlmdomain:" + strDomain)
Set colSwbemObjectSet = objSWbemServices.ExecQuery("Select * From Win32_Process")
For Each objProcess in colSWbemObjectSet
    Wscript.Echo "Process Name: " & objProcess.Name 
Next
```



## Related topics

<dl> <dt>

[Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)
</dt> </dl>

 

 
