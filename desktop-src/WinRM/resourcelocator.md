---
title: ResourceLocator object (WSManDisp.h)
description: Supplies the path to a resource. You can use a ResourceLocator object instead of a resource URI in Session object operations such as Session.Get, Session.Put, or Session.Enumerate.
ms.assetid: 0904b7eb-d4ce-46a7-bf58-452e7c0d41e9
ms.tgt_platform: multiple
keywords:
- ResourceLocator object Windows Remote Management
- ResourceLocator object Windows Remote Management , described
topic_type:
- apiref
api_name:
- ResourceLocator
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ResourceLocator object

An object that supplies the path to a resource. You can use a **ResourceLocator** object instead of a [*resource URI*](windows-remote-management-glossary.md) in [**Session**](session.md) object operations such as [**Session.Get**](session-get.md), [**Session.Put**](session-put.md), or [**Session.Enumerate**](session-enumerate.md).

This object enables you to:

-   Add one or more [*selectors*](windows-remote-management-glossary.md) that identify a particular instance of a resource. This is the same as supplying a key value in the resource URI for a resource that uses keys. For more information, see [**ResourceLocator.AddSelector**](resourcelocator-addselector.md). You can do a similar operation using the *filter* parameter in a call to [**Session.Enumerate**](session-enumerate.md).
-   Specify a [*fragment*](windows-remote-management-glossary.md) path and dialect to get only one property of a resource. You can also specify one or all of the elements of an array property by supplying the array index. For more information, see [**ResourceLocator.FragmentPath**](resourcelocator-fragmentpath.md).
-   Add one or more [*options*](windows-remote-management-glossary.md) that a data source may require to process a request. For more information, see [**ResourceLocator.AddOption**](resourcelocator-addoption.md).

For more information, see [Querying for Specific Instances of a Resource](querying-for-specific-instances-of-a-resource.md).

## Members

The **ResourceLocator** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ResourceLocator** object has these methods.



| Method                                                   | Description                                                                                                                        |
|:---------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**AddOption**](resourcelocator-addoption.md)           | Adds additional data required to process the request.<br/>                                                                   |
| [**AddSelector**](resourcelocator-addselector.md)       | Adds a [*selector*](windows-remote-management-glossary.md) to the **ResourceLocator** object.<br/>     |
| [**ClearOptions**](resourcelocator-clearoptions.md)     | Removes any [*options*](windows-remote-management-glossary.md) from the **ResourceLocator** object.<br/> |
| [**ClearSelectors**](resourcelocator-clearselectors.md) | Removes all the selectors from a **ResourceLocator** object.<br/>                                                            |



 

### Properties

The **ResourceLocator** object has these properties.



| Property                                                                          | Access type           | Description                                                                                                                                                                                             |
|:----------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FragmentDialect**](resourcelocator-fragmentdialect.md)<br/>             | Read/write<br/> | Gets or sets the language dialect for a [*resource*](windows-remote-management-glossary.md) [*fragment*](windows-remote-management-glossary.md).<br/> |
| [**FragmentPath**](resourcelocator-fragmentpath.md)<br/>                   | Read/write<br/> | Gets or sets the path for a [*resource*](windows-remote-management-glossary.md) [*fragment*](windows-remote-management-glossary.md) or property.<br/> |
| [**MustUnderstandOptions**](resourcelocator-mustunderstandoptions.md)<br/> | Read/write<br/> | Gets or sets the **MustUnderstandOptions** value for the **ResourceLocator** object.<br/>                                                                                                         |
| [**ResourceURI**](resourcelocator-resourceuri.md)<br/>                     | Read/write<br/> | Gets or sets the [*resource URI*](windows-remote-management-glossary.md) in a **ResourceLocator** object.<br/>                                                          |



 

## Remarks

The **ResourceLocator** object corresponds to the **IWSManResourceLocator** interface.

## Examples

The following VBScript code example obtains the **NumberOfLogicalProcessors** and **NumberOfCores** properties from a specific instance of [**Win32\_Processor**](/windows/desktop/CIMWin32Prov/win32-processor).


```VB
Option Explicit
Dim strUri
strUri = "http://schemas.microsoft.com/wbem/wsman/1/" _
    & "wmi/root/cimv2/Win32_Processor"
Const FragmentDialect = _
    "https://www.w3.org/TR/1999/REC-xpath-19991116"

Dim WSMan
Set WSMan = CreateObject("WSMan.Automation")

Dim Session
Set Session = WSMan.CreateSession

Dim Locator
Set Locator = WSMan.CreateResourceLocator(strUri)

Locator.AddSelector "DeviceID", "CPU0"

Dim NumberOfCores_XML
Locator.FragmentPath = "NumberOfCores"
Locator.FragmentDialect = FragmentDialect
NumberOfCores_XML = Session.Get(Locator)
DisplayOutput NumberOfCores_XML

Dim NumberOfLogicalProcessors_XML
Locator.FragmentPath = "NumberOfLogicalProcessors"
Locator.FragmentDialect = FragmentDialect
NumberOfLogicalProcessors_XML = Session.Get(Locator)

DisplayOutput NumberOfLogicalProcessors_XML

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
</dt> </dl>

 

