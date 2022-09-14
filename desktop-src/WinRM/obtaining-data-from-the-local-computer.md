---
title: Obtaining Data from the Local Computer
description: Although Windows Remote Management and WS-Management protocol are explicitly designed for remote communication, establishing a session on the local computer is the simplest case.
ms.assetid: 7f08b557-bbd4-4f67-b5e5-b84e8af58657
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Obtaining Data from the Local Computer

Although Windows Remote Management and WS-Management protocol are explicitly designed for remote communication, establishing a session on the local computer is the simplest case. Some scripts may require access data on the local computer as well as remote computers.

**WinRM version 2.0:  **

All operations are considered remote and the WinRM service must be started before any operation is performed. If a remote destination is not specified, then the localhost is used by default, and all operations will be sent to the local WinRM service. For more information about starting the WinRM service, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md).

When using the WinRM service for local operations, the following factors should be considered:

-   The local WinRM configuration can only be read by administrators.
-   WMI namespaces must have remote enable permissions set. For more information, see [Securing a Remote WMI Connection](../wmisdk/securing-a-remote-wmi-connection.md).
-   If a WinRM [*listener*](windows-remote-management-glossary.md) is not created, then the WinRM service listens for local requests on port 47001.

Every WinRM script must start by establishing a session or connection to a computer by creating a [**Session**](session.md) object. After the session is created, you can use the **Session** object methods, such as [**Session.Enumerate**](session-enumerate.md) or [**Session.Invoke**](session-invoke.md) to obtain data or to execute methods.

The creation of a session is somewhat similar to [connecting](/windows/desktop/WmiSdk/wmi-tasks--connecting-to-the-wmi-service) to a Windows Management Instrumentation ([WMI](/windows/desktop/WmiSdk/wmi-start-page)) namespace. The session is essentially a layer that allows you to send and receive data through [*SOAP*](windows-remote-management-glossary.md) messages and the WS-Management protocol. For more information, see [WS-Management Protocol](ws-management-protocol.md).

Calling the [**WSMan.CreateSession**](wsman-createsession.md) method to create a [**Session**](session.md) object will start a [*session*](windows-remote-management-glossary.md) that connects to the local WinRM.

**To Create a WSMan Session and Obtain Data**

1.  Create a [**WSMan**](wsman.md) object.

    ```VB
    Set objWsman = CreateObject("Wsman.Automation")
    ```

    

2.  Create a session by calling the [**WSMan.CreateSession**](wsman-createsession.md) method. This session runs under your logon username and password and can obtain data through the local WinRM.

    ```VB
    Set objSession = objWsman.CreateSession()
    ```

    

3.  Create a resource [*URI*](windows-remote-management-glossary.md) to identify the [*resource*](windows-remote-management-glossary.md) you want to manage or for which you want to obtain data. For more information about formatting a URI, see [Resource URIs](resource-uris.md). This resource URI is for a specific instance of the WMI [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) class, the Winmgmt service. For more information, see [Windows Remote Management and WMI](windows-remote-management-and-wmi.md).

    ```VB
    strResource = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_Service?Name=Winmgmt"
    ```

    

4.  Call [**Session**](session.md) methods that get or enumerate data using the resource URI. For more information, see [WinRM Scripting API](winrm-scripting-api.md).

    ```VB
    strResponse = objSession.Get(strResource)
    Wscript.Echo strResponse
    ```

    

5.  To get or manage data from another computer or use different methods of authentication, see [Obtaining Data from a Remote Computer](obtaining-data-from-a-remote-computer.md).

The following VBScript code example shows the complete script that obtains the specific instance of the WMI [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) named "Winmgmt".


```VB
Set objWsman = CreateObject("Wsman.Automation")
Set objSession = objWsman.CreateSession()
strResource = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_Service?Name=Winmgmt"
strResponse = objSession.Get(strResource)
Wscript.Echo strResponse
```



The following VBScript code example shows the complete script with the data transform. For more information, see [Displaying XML Output from WinRM Scripts](displaying-xml-output-from-winrm-scripts.md).


```VB
Set objWsman = CreateObject("Wsman.Automation")
Set objSession = objWsman.CreateSession()
strResource = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_Service?Name=Winmgmt"
strResponse = objSession.Get(strResource)
Set xmlFile = CreateObject("MSXml.DOMDocument")
Set xslFile = CreateObject("MSXml.DOMDocument")
xmlFile.LoadXml(strResponse)
xslFile.Load("WsmTxt.xsl")
Wscript.Echo xmlFile.TransformNode(xslFile)

```



## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Using Windows Remote Management](using-windows-remote-management.md)
</dt> <dt>

[Windows Remote Management Reference](windows-remote-management-reference.md)
</dt> </dl>

 

 