---
title: Enumerator object (WSManDisp.h)
description: Represents a stream of results returned from operations, such as a Pull operation.
ms.assetid: 8d8b461d-06a7-4600-8b68-2faf741a394b
ms.tgt_platform: multiple
keywords:
- Enumerator object Windows Remote Management
- Enumerator object Windows Remote Management , described
topic_type:
- apiref
api_name:
- Enumerator
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Enumerator object

Represents a stream of results returned from operations, such as a Pull operation. For example, the [**Session.Enumerate**](session-enumerate.md) method returns multiple results.

## Members

The **Enumerator** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Enumerator** object has these methods.



| Method                                  | Description                                                                                   |
|:----------------------------------------|:----------------------------------------------------------------------------------------------|
| [**ReadItem**](enumerator-readitem.md) | Retrieves an item from the resource and returns an XML representation of the item.<br/> |



 

### Properties

The **Enumerator** object has these properties.



| Property                                                     | Description                                                                                    |
|:-------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**AtEndOfStream**](enumerator-atendofstream.md)<br/> | Gets a Boolean value that indicates whether there are more items in the collection.<br/> |
| [**Error**](enumerator-error.md)<br/>                 | Gets an XML representation of additional error information.<br/>                         |



 

## Remarks

To start an enumeration, use [**Session.Enumerate**](session-enumerate.md). To do a [*WS-Enumeration:*](windows-remote-management-glossary.md)[*Pull*](windows-remote-management-glossary.md) operation that continues reading items in the enumeration, use [**Enumerator.ReadItem**](enumerator-readitem.md).

The **Enumerator** object corresponds to the [**IWSManEnumerator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanenumerator) interface.

## Examples

The following VBScript code example enumerates all the disks on a remote computer specified by the fully qualified domain name (servername.domain.com). The DisplayOutput subroutine formats the data output in the same way as the WinRM.cmd tool.


```VB
Option Explicit

Const RemoteComputer = "MIG50-64D.mig.net"

Dim objWsman, objSession, strResource
Dim objResultSet

Set objWsman = CreateObject( "WSMan.Automation" )
Set objSession = objWsman.CreateSession( "https://" _
    & RemoteComputer )
strResource = "http://schemas.microsoft.com/wbem/wsman/1/" _
     & "wmi/root/cimv2/Win32_OperatingSystem"
Dim iFlag
iFlag = objWsman.EnumerationFlagReturnObjectAndEPR or _
    objWsman.EnumerationFlagHierarchyDeep
Set objResultSet = _
    objSession.Enumerate( strResource, "", "",  iFlag)
While Not objResultSet.AtEndOfStream
    DisplayOutput( objResultSet.ReadItem ) 
Wend


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

[WinRM Scripting API](winrm-scripting-api.md)
</dt> <dt>

[Enumerating or Listing All of the Instances of a Resource](enumerating-or-listing-all-instances-of-a-resource.md)
</dt> <dt>

[Scripting in Windows Remote Management](scripting-in-windows-remote-management.md)
</dt> </dl>

 

 





