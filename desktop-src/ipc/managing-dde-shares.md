---
description: Network DDE provides functions that allow you to delete a share, get or set share information, or enumerate shares.
ms.assetid: d7924e93-75e4-4f94-b159-02408535170d
title: Managing DDE Shares
ms.topic: article
ms.date: 05/31/2018
---

# Managing DDE Shares

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Network DDE provides functions that allow you to delete a share, get or set share information, or enumerate shares.




| Task | Procedure | 
|------|-----------|
| Delete a DDE share | Use the <a href="nddesharedel.md"><strong>NDdeShareDel</strong></a> function. | 
| Get DDE share information | Use the <a href="nddesharegetinfo.md"><strong>NDdeShareGetInfo</strong></a> function. | 
| Set DDE share information | Use the <a href="nddesharesetinfo.md"><strong>NDdeShareSetInfo</strong></a> function. | 
| Enumerate DDE shares | Use the <a href="nddeshareenum.md"><strong>NDdeShareEnum</strong></a> function. You can also enumerate the trusted DDE shares by using the <a href="nddetrustedshareenum.md"><strong>NDdeTrustedShareEnum</strong></a> function.<br /> | 
| Enumerate connected users | Use the <a href="/windows/desktop/api/lmshare/nf-lmshare-netsessionenum"><strong>NetSessionEnum</strong></a> function. | 
| Change the DDE share name | Delete the old share and create a new share.<ol><li>Retrieve the share information using <a href="nddesharegetinfo.md"><strong>NDdeShareGetInfo</strong></a>.</li><li>Remove the share using <a href="nddesharedel.md"><strong>NDdeShareDel</strong></a>.</li><li>Change the <strong>lpszShareName</strong> member of the <a href="nddeshareinfo-str.md"><strong>NDDESHAREINFO</strong></a> structure returned by <a href="nddesharegetinfo.md"><strong>NDdeShareGetInfo</strong></a>.</li><li>Pass the modified <a href="nddeshareinfo-str.md"><strong>NDDESHAREINFO</strong></a> structure to <a href="nddeshareadd.md"><strong>NDdeShareAdd</strong></a>.</li></ol> | 




 

 

