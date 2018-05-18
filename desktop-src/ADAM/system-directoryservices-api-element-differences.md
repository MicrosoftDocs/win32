---
title: System.DirectoryServices API Element Differences
description: System.DirectoryServices API Element Differences
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '7e548434-8f6a-4a4e-9ca3-d564a26102c3'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-application-mode'
ms.tgt_platform: multiple
keywords: ["System.DirectoryServices API Element Differences ADAM"]
---

# System.DirectoryServices API Element Differences

The following table lists the differences in the [System.DirectoryServices](https://msdn.microsoft.com/library/system.directoryservices.aspx) programming elements when you use them to program for ADAM. For more information about the programming element, click the element name.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Programming element</th>
<th>Difference</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>ADS_OPTION_ENUM</strong>](https://msdn.microsoft.com/library/aa772273) enumeration<br/></td>
<td>Two values, [<strong>ADS_OPTION_PASSWORD_PORTNUMBER</strong>](https://msdn.microsoft.com/library/aa772273) and <strong>ADS_OPTION_PASSWORD_METHOD</strong>, added to facilitate the setting of passwords.<br/>
<blockquote>
[!Note]<br />
To use these elements, you must use the [DirectoryEntry.Invoke](Http://go.microsoft.com/fwlink/p/?linkid=83866) method. For more information, see [Invoking ADSI](http://go.microsoft.com/fwlink/p/?linkid=94273).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ADS_PASSWORD_ENCODING_ENUM</strong>](https://msdn.microsoft.com/library/aa772274) enumeration<br/></td>
<td>Enumeration added to facilitate the setting of passwords.<br/>
<blockquote>
[!Note]<br />
To use this element, you must use the [DirectoryEntry.Invoke](Http://go.microsoft.com/fwlink/p/?linkid=83866) method. For more information, see [Invoking ADSI](http://go.microsoft.com/fwlink/p/?linkid=94273).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[DirectoryEntry](Http://go.microsoft.com/fwlink/p/?linkid=83868) class<br/></td>
<td>[Path](Http://go.microsoft.com/fwlink/p/?linkid=83867) property includes a port number to specify an ADAM instance. For more information, see [LDAP ADsPath](https://msdn.microsoft.com/library/aa746384).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IADsUser::ChangePassword</strong>](https://msdn.microsoft.com/library/aa746341) and [<strong>IADsUser::SetPassword</strong>](https://msdn.microsoft.com/library/aa746344) methods<br/></td>
<td>Before using these methods, you must use the [<strong>IADsObjectOptions::SetOption</strong>](https://msdn.microsoft.com/library/aa706061) method to set port number ([<strong>ADS_OPTION_PASSWORD_PORTNUMBER</strong>](https://msdn.microsoft.com/library/aa772273)) and method (<strong>ADS_OPTION_PASSWORD_METHOD</strong>).<br/>
<blockquote>
[!Note]<br />
To use these elements, you must use the [DirectoryEntry.Invoke](Http://go.microsoft.com/fwlink/p/?linkid=83866) method. For more information, see [Invoking ADSI](http://go.microsoft.com/fwlink/p/?linkid=94273).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IADsAccessControlEntry::get_Trustee</strong>](https://msdn.microsoft.com/library/aa705952) and <strong>IADsAccessControlEntry::put_Trustee</strong> methods<br/></td>
<td>ADAM security principal names use a string security identifier (SID) rather than a friendly name.<br/>
<blockquote>
[!Note]<br />
System.DirectoryServices does not support the [<strong>IADsAccessControlEntry</strong>](https://msdn.microsoft.com/library/aa705951) interface or the [<strong>IADsAccessControList</strong>](https://msdn.microsoft.com/library/aa705953) or [<strong>IADsSecurityDescriptor</strong>](https://msdn.microsoft.com/library/aa706128) interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Miscellaneous</td>
<td>The WinNT, NDS, and NWCOMPAT providers do not apply for ADAM.<br/></td>
</tr>
</tbody>
</table>



 

 

 





