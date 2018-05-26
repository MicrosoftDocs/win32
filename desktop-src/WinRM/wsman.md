---
title: WSMan object
description: Provides methods and properties used to create a session, represented by a Session object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 45895a4e-b7de-4469-ae78-6d1d3f9d6145
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
keywords:
- WSMan object Windows Remote Management
- WSMan object Windows Remote Management , described
topic_type:
- apiref
api_name:
- WSMan
api_location:
- WSMAuto.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# WSMan object

Provides methods and properties used to create a session, represented by a [**Session**](session.md) object. Any Windows Remote Management operations require creation of a [**Session**](session.md) that connects to a remote computer, [*base management controller*](windows-remote-management-glossary.md#winrm-gloss-baseboard-management-controller) (BMC), or the local computer. Operations include getting, writing, enumerating data, or invoking methods.

## Members

The **WSMan** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **WSMan** object has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>CreateConnectionOptions</strong>](wsman-createconnectionoptions.md)</td>
<td style="text-align: left;">Creates a [<strong>ConnectionOptions</strong>](connectionoptions.md) object that specifies the user name and password used when creating a remote session.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>CreateResourceLocator</strong>](wsman-createresourcelocator.md)</td>
<td style="text-align: left;">Creates a [<strong>ResourceLocator</strong>](resourcelocator.md) object that can specify:<br/>
<ul>
<li>The complete path to a [<em>resource</em>](windows-remote-management-glossary.md#winrm-gloss-resource) or a single piece of data.</li>
<li>A [<em>selector</em>](windows-remote-management-glossary.md#winrm-gloss-selector) for a specific instance of a resource.</li>
<li>An [<em>option</em>](windows-remote-management-glossary.md#winrm-gloss-option) that supplies additional data to the resource provider.</li>
</ul></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>CreateSession</strong>](wsman-createsession.md)</td>
<td style="text-align: left;">Creates a [<strong>Session</strong>](session.md) object that can then be used for subsequent network operations.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.EnumerationFlagHierarchyDeep</strong>](wsman-enumerationflaghierarchydeep.md)</td>
<td style="text-align: left;">Returns the value of the enumeration flag <strong>EnumerationFlagHierarchyDeep</strong> for use in the <em>flags</em> parameter of [<strong>Session.Enumerate</strong>](session-enumerate.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.EnumerationFlagHierarchyDeepBasePropsOnly</strong>](wsman-enumerationflaghierarchydeepbasepropsonly.md)</td>
<td style="text-align: left;">Returns the value of the enumeration flag <strong>EnumerationFlagHierarchyDeepBasePropsOnly</strong> for use in the <em>flags</em> parameter of [<strong>Session.Enumerate</strong>](session-enumerate.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.EnumerationFlagHierarchyShallow</strong>](wsman-enumerationflaghierarchyshallow.md)</td>
<td style="text-align: left;">Returns the value of the enumeration flag <strong>EnumerationFlagHierarchyShallow</strong> for use in the <em>flags</em> parameter of [<strong>Session.Enumerate</strong>](session-enumerate.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.EnumerationFlagNonXmlText</strong>](wsman-enumerationflagnonxmltext.md)</td>
<td style="text-align: left;">Returns the value of the enumeration constant <strong>WSManFlagNonXmlText</strong> for use in the <em>flags</em> parameter of the [<strong>Session.Enumerate</strong>](session-enumerate.md) method.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.EnumerationFlagReturnEPR</strong>](wsman-enumerationflagreturnepr.md)</td>
<td style="text-align: left;">Returns the value of the enumeration flag <strong>EnumerationFlagReturnEPR</strong> for use in the <em>flags</em> parameter of [<strong>Session.Enumerate</strong>](session-enumerate.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.EnumerationFlagReturnObject</strong>](wsman-enumerationflagreturnobject.md)</td>
<td style="text-align: left;">Returns the value of the enumeration flag <strong>EnumerationFlagReturnObject</strong> for use in the <em>flags</em> parameter of [<strong>Session.Enumerate</strong>](session-enumerate.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.EnumerationFlagReturnObjectAndEPR</strong>](wsman-enumerationflagreturnobjectandepr.md)</td>
<td style="text-align: left;">Returns the value of the enumeration flag <strong>EnumerationFlagReturnObjectAndEPR</strong> for use in the <em>flags</em> parameter of [<strong>Session.Enumerate</strong>](session-enumerate.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.GetErrorMessage</strong>](wsman-geterrormessage.md)</td>
<td style="text-align: left;">Returns a formatted string containing the text of an error number.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.SessionFlagCredUsernamePassword</strong>](wsman-sessionflagcredusernamepassword.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagCredUsernamePassword</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.SessionFlagEnableSPNServerPort</strong>](wsman-sessionflagenablespnserverport.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagEnableSPNServerPort</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.SessionFlagNoEncryption</strong>](wsman-sessionflagnoencryption.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagNoEncryption</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.SessionFlagSkipCACheck</strong>](wsman-sessionflagskipcacheck.md)</td>
<td style="text-align: left;">Returns the value of the <strong>WSManFlagSkipCACheck</strong> authentication flag for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.SessionFlagSkipCNCheck</strong>](wsman-sessionflagskipcncheck.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagSkipCNCheck</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.SessionFlagUseBasic</strong>](wsman-sessionflagusebasic.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagUseBasic</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.SessionFlagUseDigest</strong>](wsman-sessionflagusedigest.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagUseDigest</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.SessionFlagUseKerberos</strong>](wsman-sessionflagusekerberos.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagUseKerberos</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.SessionFlagUseNegotiate</strong>](wsman-sessionflagusenegotiate.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagUseNegotiate</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WSMan.SessionFlagUseNoAuthentication</strong>](wsman-sessionflagusenoauthentication.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagUseNoAuthentication</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WSMan.SessionFlagUTF8</strong>](wsman-sessionflagutf8.md)</td>
<td style="text-align: left;">Returns the value of the authentication flag <strong>WSManFlagUTF8</strong> for use in the <em>flags</em> parameter of [<strong>WSMan.CreateSession</strong>](wsman-createsession.md).<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **WSMan** object has these properties.



| Property                                            | Access type          | Description                                                                   |
|:----------------------------------------------------|:---------------------|:------------------------------------------------------------------------------|
| [**CommandLine**](wsman-commandline.md)<br/> | Read-only<br/> | Gets the unprocessed command line for the current hosting process.<br/> |
| [**Error**](wsman-error.md)<br/>             | Read-only<br/> | Gets error information.<br/>                                            |



 

## Remarks

The **WSMan** object corresponds to the [**IWSMan**](/windows/win32/WSManDisp/nn-wsmandisp-iwsman?branch=master) and [**IWSManEx**](/windows/win32/WSManDisp/nn-wsmandisp-iwsmanex?branch=master) interfaces. **WSMan** is the only object that can be created directly using [CreateObject](https://msdn.microsoft.com/library/xzysf6hc.aspx).

## Examples

The following code example shows how to instantiate a **WSMan** object.


```VB
Dim objWsman
Dim Session, Resource 
Set objWsman = CreateObject( "WSMAN.Automation" )
Set Session = objWsman.CreateSession
strResource = "http://schemas.microsoft.com/wbem/wsman/1/wmi/Root/CIMv2/Win32_OperatingSystem"
```



## Requirements



|                                     |                                                                                          |
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

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Using Windows Remote Management](using-windows-remote-management.md)
</dt> <dt>

[Scripting in Windows Remote Management](scripting-in-windows-remote-management.md)
</dt> <dt>

[Obtaining Data from the Local Computer](obtaining-data-from-the-local-computer.md)
</dt> <dt>

[Obtaining Data from a Remote Computer](obtaining-data-from-a-remote-computer.md)
</dt> </dl>

 

 





