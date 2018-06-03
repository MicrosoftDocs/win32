---
Description: Returns one or more AD RMS templates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3b47801f-e5bd-4cd6-b170-8035b470d361
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireTemplates method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AcquireTemplates method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireTemplates** SOAP web method returns one or more AD RMS templates.

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For more information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public GuidTemplate[] AcquireTemplates(
  String[] guids
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Public Function AcquireTemplates( _
  ByVal guids() As String _
) As GuidTemplate()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*guids* 
</dt> <dd>

An array of strings that contain GUIDs, one for each template. No more than 25 GUIDs can be specified for each request. That is, to retrieve more than 25 templates, you must call this method more than once. For example, to retrieve 52 templates, call this method three times, twice with 25 GUIDs and once more with 2 GUIDS.

</dd> </dl>

## Return value

An array of [**GuidTemplate**](-guidtemplate.md) objects, each of which contains a GUID, a hash of the template, and the XML template data.

## Web Service URL

*ServerURL*/\_wmcs/Licensing/TemplateDistribution.asmx

## Remarks

Only active templates can be distributed by an AD RMS server. You can call the [**AcquireTemplateInformation**](-acquiretemplateinformation.md) method to determine the number of templates stored on the server.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**AcquireTemplateInformation**](-acquiretemplateinformation.md)
</dt> </dl>

 

 




