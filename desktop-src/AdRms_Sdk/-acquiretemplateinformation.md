---
Description: Returns information about the templates stored on an AD RMS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 278bea4e-6aa0-4af8-a189-ff4448acaba5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AcquireTemplateInformation method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AcquireTemplateInformation method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **AcquireTemplateInformation** method returns information about the templates stored on an AD RMS server.

## Syntax


```CSharp
public TemplateInformation AcquireTemplateInformation();
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
<td><pre><code>Public Function AcquireTemplateInformation() As TemplateInformation</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Return value

A [**TemplateInformation**](-templateinformation.md) object that contains the server public key, the number of active templates, and an array of template hashes.

## Web Service URL

*ServerURL*/\_wmcs/Licensing/TemplateDistribution.asmx

## Remarks

You can call the [**AcquireTemplates**](-acquiretemplates.md) method to retrieve an array of active templates from the AD RMS server.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**AcquireTemplates**](-acquiretemplates.md)
</dt> <dt>

[**TemplateInformation**](-templateinformation.md)
</dt> </dl>

 

 




