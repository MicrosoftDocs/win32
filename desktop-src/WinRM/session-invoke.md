---
title: Session.Invoke method (WSManDisp.h)
description: Invokes a method and returns the results of the method call.
ms.assetid: c83d0631-2efb-47d9-abcf-ab0c8de06c36
ms.tgt_platform: multiple
keywords:
- Invoke method Windows Remote Management
- Invoke method Windows Remote Management , Session object
- Session object Windows Remote Management , Invoke method
topic_type:
- apiref
api_name:
- Session.Invoke
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Session.Invoke method

Invokes a method and returns the results of the method call.

## Syntax


```VB
Session.Invoke( _
  ByVal actionUri, _
  ByVal resourceUri, _
  ByVal parameters, _
  [ ByVal flags ] _
)
```



## Parameters

<dl> <dt>

*actionUri* \[in\]
</dt> <dd>

The URI of the method to invoke.

</dd> <dt>

*resourceUri* \[in\]
</dt> <dd>

The identifier of the resource to retrieve.

This parameter can contain one of the following:

-   URI with or without [*selectors*](windows-remote-management-glossary.md). In the following Visual Basic Scripting Edition (VBScript) example, the key is specified by `Win32_Service?Name=winmgmt`.

    ```VB
    strResourceUri = "http://schemas.microsoft.com/wbem/wsman/1/" _ 
       & "Win32_Service?Name=winmgmt"
    ```

    

-   [**ResourceLocator**](resourcelocator.md) object which may contain selectors, [*fragments*](windows-remote-management-glossary.md), or [*options*](windows-remote-management-glossary.md).
-   [*WS-Addressing*](windows-remote-management-glossary.md) endpoint reference as described in the [WS-Management Protocol](ws-management-protocol.md) standard. For more information about the public specification for WS-Management protocol, see [Management Specifications Index Page](/previous-versions/dotnet/articles/ms951267(v=msdn.10)).

</dd> <dt>

*parameters* \[in\]
</dt> <dd>

The XML representation of the input for the method. This string must be supplied or this method will fail.

</dd> <dt>

*flags* \[in, optional\]
</dt> <dd>

Reserved. Must be set to 0.

</dd> </dl>

## Return value

The XML representation of the method output.

## Examples

The following VBScript code example starts a Calc.exe process. The *strInputParameters* parameter contains the input parameters in XML format. The only required input parameter for the [**Create**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process) method of the WMI [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class is the command line to execute.


```VB
Set objWsman = CreateObject( "WSMan.Automation" )
If objWsman is Nothing Then
    WScript.Echo "Failed to create WSMAN Automation object"
    WScript.Quit
End If 

Set objSession = objWsman.CreateSession
If objSession is Nothing Then
    WScript.Echo "Failed to create WSMAN Session object"
    WScript.Quit
End If 

strResource = "http://schemas.microsoft.com/wbem/wsman/1/" & _
    "wmi/root/cimv2/Win32_Process"

strInputParameters = "<p:Create_INPUT " & _
    "xmlns:p=""http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_Process"">" & _
    "<p:CommandLine>" & "calc.exe" & _
    "</p:CommandLine>" & _
    "</p:Create_INPUT>"

strOutputParameters = objSession.Invoke( "Create", _
    strResource, strInputParameters )

DisplayOutput( strOutputParameters )

'****************************************************
' Displays WinRM XML message using built-in XSL
'****************************************************
Sub DisplayOutput( strWinRMXml )
    Dim xmlFile, xslFile
    Set xmlFile = CreateObject( "MSXml2.DOMDocument.3.0" ) 
    Set xslFile = CreateObject( "MSXml2.DOMDocument.3.0" )
    xmlFile.LoadXml( strWinRMXml )
    xslFile.Load( "WsmTxt.xsl" )
    Wscript.Echo xmlFile.TransformNode( xslFile ) 
End Sub
```



The following VBScript code example calls the **Session.Invoke** method to execute the [**StopService**](/windows/desktop/CIMWin32Prov/stopservice-method-in-class-win32-service) method of [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service). The **StopService** method does not have input parameters. However, the **Invoke** method requires an XML string in the *parameters* parameter.


```VB
Option Explicit

Dim objWsman
Dim objSession
Dim strResponse
Dim strActionURI
Dim strInputXml
Dim strResourceURI
Dim strMethodName

set objWsman = CreateObject("Wsman.Automation")
set objSession = objWsman.CreateSession
strResourceURI = "http://schemas.microsoft.com/wbem/wsman/1/"_
    & "wmi/root/cimv2/Win32_Service?Name=w32time"
strMethodName = "StopService"
strActionURI = strMethodName                                      

strInputXml = "<p:StopService_INPUT " _
    & "xmlns:p=""http://schemas.microsoft.com/wbem/wsman/1/"_
    & "wmi/root/cimv2/Win32_Service""/>"

strResponse = objSession.Invoke(strMethodName, strResourceURI, strInputXml)

call DisplayOutput(strResponse)
 
strMethodName = "StartService" 
strActionURI = strResourceURI & "/" & strMethodName  
strInputXml = "<p:StartService_INPUT " _
    & "xmlns:p=""http://schemas.microsoft.com/wbem/wsman/1/"_
    & "wmi/root/cimv2/Win32_Service""/>"
strResponse = objSession.Invoke(strMethodName, _
    strResourceURI, strInputXml)

call DisplayOutput(strResponse)

 
'****************************************************
' Displays WinRM XML message using built-in XSL
'****************************************************

Sub DisplayOutput( strWinRMXml )
    Dim xmlFile, xslFile
    Set xmlFile = CreateObject( "MSXml2.DOMDocument.3.0" )    
    Set xslFile = CreateObject( "MSXml2.DOMDocument.3.0" )
    xmlFile.LoadXml( strWinRMXml )
    xslFile.Load( "WsmTxt.xsl" )
    Wscript.Echo xmlFile.TransformNode( xslFile )           
End Sub
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

[**Session**](session.md)
</dt> </dl>

 

