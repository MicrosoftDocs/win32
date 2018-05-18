---
title: Enumerator.ReadItem method
description: Retrieves an item from the resource and returns an XML representation of the item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4280ecb8-2449-41bd-868a-785e8ac3b3d5'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-remote-management'
ms.tgt_platform: multiple
keywords: ["ReadItem method Windows Remote Management", "ReadItem method Windows Remote Management , Enumerator object", "Enumerator object Windows Remote Management , ReadItem method"]
topic_type:
- apiref
api_name:
- Enumerator.ReadItem
api_location:
- WSMAuto.dll
api_type:
- COM
---

# Enumerator.ReadItem method

Retrieves an item from the resource and returns an XML representation of the item.

## Syntax


```VB
Enumerator.ReadItem( _
  ByVal resource _
)
```



## Parameters

<dl> <dt>

*resource* 
</dt> <dd>

The URI of the item.

</dd> </dl>

## Return value

The XML representation of the item.

## Remarks

To limit the number of items that are read, set the [**Session.BatchItems**](session-batchitems.md) property.

Note that the freeing of the enumeration object cleans up any pending enumeration requests.

The [**Session.Enumerate**](session-enumerate.md) method does not obtain a collection in the same way that a [WMI query](https://msdn.microsoft.com/library/aa392903), such as `SELECT * from Win32_LogicalDisk`, returns a collection in an [**SWbemObjectSet**](https://msdn.microsoft.com/library/aa393762). To read a file as a text stream, you create the scripting [TextStream](https://msdn.microsoft.com/library/312a5kbt.aspx) object and call the [TextStream.Readline](https://msdn.microsoft.com/library/h7se9d4f.aspx) method to read each line of the file. In a similar way, you call the **Session.Enumerate** method to obtain an [**Enumerator**](enumerator.md) object and then call the **Enumerator.ReadItem** method. As in reading from the text file, you can check the [**Enumerator.AtEndOfStream**](enumerator-atendofstream.md) property to check for whether you have reached the end of the data items.

## Examples

The following VBScript example calls the [**Session.Enumerate**](session-enumerate.md) method to obtain a list of scheduled jobs. The DisplayOutput subroutine uses the Winrm command line tool XML transform file (WsmTxt.xsl) to output the data in a tabular form.


```VB
Const RemoteComputer = "servername.domain.com"

Set objWsman = CreateObject( "WSMan.Automation" )
Set objSession = objWsman.CreateSession( "http://" & RemoteComputer )

strResource = "http://schemas.microsoft.com/wbem/wsman/1/" &amp;_
              "wmi/root/cimv2/Win32_ScheduledJob"

Set objResultSet = objSession.Enumerate( strResource )
NumOfJobs = 0

While Not objResultSet.AtEndOfStream
    NumOfJobs = NumOfJobs + 1
    DisplayOutput( objResultSet.ReadItem ) 
Wend

Wscript.Echo "There are " & NumOfJobs & " jobs scheduled."

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



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**Enumerator**](enumerator.md)
</dt> <dt>

[Enumerating or Listing All the Instances of a Resource](enumerating-or-listing-all-instances-of-a-resource.md)
</dt> </dl>

 

 





