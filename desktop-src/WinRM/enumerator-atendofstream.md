---
title: Enumerator.AtEndOfStream property (WSManDisp.h)
description: Gets a Boolean value that indicates whether there are any more items in the collection.
ms.assetid: 5e80674a-7889-4753-b0dd-4d7b44eba00a
ms.tgt_platform: multiple
keywords:
- AtEndOfStream property Windows Remote Management
- AtEndOfStream property Windows Remote Management , Enumerator object
- Enumerator object Windows Remote Management , AtEndOfStream property
topic_type:
- apiref
api_name:
- Enumerator.AtEndOfStream
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Enumerator.AtEndOfStream property

Gets a Boolean value that indicates whether there are any more items in the collection.

This property is read-only.

## Syntax


```VB
Enumerator.AtEndOfStream As BOOLEAN
```



## Property value

<dt>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>**True**


</dt> <dd>

No more items are in the collection.

</dd> <dt>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>**False**


</dt> <dd>

More items are available.

</dd> </dl>

## Remarks

If you free the [**Enumerator**](enumerator.md) object after you have obtained all the data required, then any pending enumeration requests are removed. For more information, see [Enumerating or Listing All of the Instances of a Resource](enumerating-or-listing-all-instances-of-a-resource.md).

## Examples

The following VBScript example enumerates operating system instances. Note that the freeing of the enumeration object cleans up any pending enumeration requests. The DisplayOutput subroutine formats the data output in the same way as the WinRM.cmd tool.


```VB
Const RemoteComputer = "servername.domain.com"

Set objWsman = CreateObject( "WSMan.Automation" )
Set objSession = objWsman.CreateSession( "https://" & _
    RemoteComputer )

strResource = "http://schemas.microsoft.com/wbem/wsman/1/" &_
    "wmi/root/cimv2/Win32_OperatingSystem"

Set objResultSet = objSession.Enumerate( strResource )

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

[**Enumerator**](enumerator.md)
</dt> <dt>

[Enumerating or Listing All of the Instances of a Resource](enumerating-or-listing-all-instances-of-a-resource.md)
</dt> </dl>

 

 





