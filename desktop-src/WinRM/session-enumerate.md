---
title: Session.Enumerate method (WSManDisp.h)
description: Enumerates a table, data collection, or log resource.
ms.assetid: ed8ad3ad-d033-45cb-b681-995c5f73b12e
ms.tgt_platform: multiple
keywords:
- Enumerate method Windows Remote Management
- Enumerate method Windows Remote Management , Session object
- Session object Windows Remote Management , Enumerate method
topic_type:
- apiref
api_name:
- Session.Enumerate
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Session.Enumerate method

Enumerates a table, data collection, or log resource. To create a query, include a *filter* parameter and a *dialect* parameter in an enumeration. You can also use a [**ResourceLocator**](resourcelocator.md) object to create queries. For more information, see [Enumerating or Listing All of the Instances of a Resource](enumerating-or-listing-all-instances-of-a-resource.md).

## Syntax


```VB
Session.Enumerate( _
  ByVal resourceUri, _
  [ ByVal filter ], _
  [ ByVal dialect ], _
  [ ByVal flags ] _
)
```



## Parameters

<dl> <dt>

*resourceUri* \[in\]
</dt> <dd>

The identifier of the resource to be retrieved.

This parameter can contain one of the following:

-   The URI of the resource.

    ```VB
    strResourceUri = "http://schemas.microsoft.com/" _ 
        & "wbem/wsman/1/wmi/root/cimv2/Win32_Service"
    ```

    

-   A [**ResourceLocator**](resourcelocator.md) object.
-   A [*WS-Addressing*](windows-remote-management-glossary.md) endpoint reference as described in the WS-Management protocol standard. For more information about the public specification for [WS-Management Protocol](ws-management-protocol.md), see [Management Specifications Index Page](/previous-versions/dotnet/articles/ms951267(v=msdn.10)).

</dd> <dt>

*filter* \[in, optional\]
</dt> <dd>

A filter that defines what items in the resource are returned by the enumeration. When the resource is enumerated, only those items that match the filter criteria are returned. Including a *filter* parameter and a *dialect* parameter in an enumeration converts the enumeration into a query. For an example, see [Querying for Specific Instances of a Resource](querying-for-specific-instances-of-a-resource.md).

If you have a [**ResourceLocator**](resourcelocator.md) object for the *resourceURI* parameter, then this parameter should not be used.

</dd> <dt>

*dialect* \[in, optional\]
</dt> <dd>

The language used by the filter. [WQL](/windows/desktop/WmiSdk/wql-sql-for-wmi), a subset of SQL used by WMI, is the only language supported.

If you have a [**ResourceLocator**](resourcelocator.md) object for the *resourceURI* parameter, then this parameter should not be used.

</dd> <dt>

*flags* \[in, optional\]
</dt> <dd>

A parameter that must contain a flag in the **\_\_WSManEnumFlags** enumeration. For more information, see [Enumeration Constants](enumeration-constants.md).

</dd> </dl>

## Return value

An [**Enumerator**](enumerator.md) object that contains the results of the enumeration.

## Remarks

For more information about limiting network calls during an enumeration, see the [**BatchItems**](session-batchitems.md) property.

Be aware that if the flags include the [**Enumeration Constants**](enumeration-constants.md) **WSManFlagHierarchyDeepBasePropsOnly** or **WSManFlagHierarchyShallow** then Windows Remote Management service returns the error code **ERROR\_WSMAN\_POLYMORPHISM\_MODE\_UNSUPPORTED**.

If a filter is specified, it must be a valid document with respect to the schema of the resource. The dialect parameter is optional. However, if the filter string begins with <, but is not an XML fragment, then either include the *dialect* parameter or set the **WSManFlagNonXmlText** flag in the *flags* parameter. For more information, see [**Enumeration Constants**](enumeration-constants.md).

The corresponding C++ method is [**IWSManSession::Enumerate**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmansession-enumerate).

## Examples

The following VBScript code example enumerates the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) instances on a remote computer specified by the fully qualified domain name (servername.domain.com). Be aware that freeing the enumeration object clears pending enumeration requests. The DisplayOutput subroutine uses the Winrm command-line tool XML transform file (WsmTxt.xsl) to output the data in a tabular form.


```VB
Const RemoteComputer = "servername.domain.com"
Set objWsman = CreateObject( "WSMan.Automation" )

Set objSession = objWsman.CreateSession( "https://" & REMOTECOMPUTER )

strResource = "http://schemas.microsoft.com/wbem/wsman/1/" &_
              "wmi/root/cimv2/Win32_LogicalDisk"

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

[**Session**](session.md)
</dt> <dt>

[Querying for Specific Instances of a Resource](querying-for-specific-instances-of-a-resource.md)
</dt> <dt>

[**BatchItems**](session-batchitems.md)
</dt> <dt>

[**ResourceLocator**](resourcelocator.md)
</dt> </dl>

 

