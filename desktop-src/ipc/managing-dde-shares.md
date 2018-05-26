---
Description: Network DDE provides functions that allow you to delete a share, get or set share information, or enumerate shares.
ms.assetid: d7924e93-75e4-4f94-b159-02408535170d
title: Managing DDE Shares
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing DDE Shares

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Network DDE provides functions that allow you to delete a share, get or set share information, or enumerate shares.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Task</th>
<th>Procedure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Delete a DDE share</td>
<td>Use the [<strong>NDdeShareDel</strong>](nddesharedel.md) function.</td>
</tr>
<tr class="even">
<td>Get DDE share information</td>
<td>Use the [<strong>NDdeShareGetInfo</strong>](nddesharegetinfo.md) function.</td>
</tr>
<tr class="odd">
<td>Set DDE share information</td>
<td>Use the [<strong>NDdeShareSetInfo</strong>](nddesharesetinfo.md) function.</td>
</tr>
<tr class="even">
<td>Enumerate DDE shares</td>
<td>Use the [<strong>NDdeShareEnum</strong>](nddeshareenum.md) function. You can also enumerate the trusted DDE shares by using the [<strong>NDdeTrustedShareEnum</strong>](nddetrustedshareenum.md) function.<br/></td>
</tr>
<tr class="odd">
<td>Enumerate connected users</td>
<td>Use the [<strong>NetSessionEnum</strong>](https://msdn.microsoft.com/library/windows/desktop/bb525382) function.</td>
</tr>
<tr class="even">
<td>Change the DDE share name</td>
<td>Delete the old share and create a new share.
<p><img src="../common/wedge.gif" /><strong>To change the share name</strong><br/></p>
<ol>
<li>Retrieve the share information using [<strong>NDdeShareGetInfo</strong>](nddesharegetinfo.md).</li>
<li>Remove the share using [<strong>NDdeShareDel</strong>](nddesharedel.md).</li>
<li>Change the <strong>lpszShareName</strong> member of the [<strong>NDDESHAREINFO</strong>](nddeshareinfo-str.md) structure returned by [<strong>NDdeShareGetInfo</strong>](nddesharegetinfo.md).</li>
<li>Pass the modified [<strong>NDDESHAREINFO</strong>](nddeshareinfo-str.md) structure to [<strong>NDdeShareAdd</strong>](nddeshareadd.md).</li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 




