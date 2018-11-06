---
Description: Network DDE provides functions that allow you to delete a share, get or set share information, or enumerate shares.
ms.assetid: d7924e93-75e4-4f94-b159-02408535170d
title: Managing DDE Shares
ms.topic: article
ms.date: 05/31/2018
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
<td>Use the <a href="nddesharedel"><strong>NDdeShareDel</strong></a> function.</td>
</tr>
<tr class="even">
<td>Get DDE share information</td>
<td>Use the <a href="nddesharegetinfo"><strong>NDdeShareGetInfo</strong></a> function.</td>
</tr>
<tr class="odd">
<td>Set DDE share information</td>
<td>Use the <a href="nddesharesetinfo"><strong>NDdeShareSetInfo</strong></a> function.</td>
</tr>
<tr class="even">
<td>Enumerate DDE shares</td>
<td>Use the <a href="nddeshareenum"><strong>NDdeShareEnum</strong></a> function. You can also enumerate the trusted DDE shares by using the <a href="nddetrustedshareenum"><strong>NDdeTrustedShareEnum</strong></a> function.<br/></td>
</tr>
<tr class="odd">
<td>Enumerate connected users</td>
<td>Use the <a href="https://msdn.microsoft.com/library/windows/desktop/bb525382"><strong>NetSessionEnum</strong></a> function.</td>
</tr>
<tr class="even">
<td>Change the DDE share name</td>
<td>Delete the old share and create a new share.
<p><img src="../common/wedge.gif" /><strong>To change the share name</strong><br/></p>
<ol>
<li>Retrieve the share information using <a href="nddesharegetinfo"><strong>NDdeShareGetInfo</strong></a>.</li>
<li>Remove the share using <a href="nddesharedel"><strong>NDdeShareDel</strong></a>.</li>
<li>Change the <strong>lpszShareName</strong> member of the <a href="nddeshareinfo-str"><strong>NDDESHAREINFO</strong></a> structure returned by <a href="nddesharegetinfo"><strong>NDdeShareGetInfo</strong></a>.</li>
<li>Pass the modified <a href="nddeshareinfo-str"><strong>NDDESHAREINFO</strong></a> structure to <a href="nddeshareadd"><strong>NDdeShareAdd</strong></a>.</li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 




