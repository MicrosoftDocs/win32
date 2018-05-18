---
title: Close the Parent Recordset Object
description: Close the Parent Recordset Object
ms.assetid: '03738755-de3a-4330-a91e-7079ee00e0eb'
---

# Close the Parent Recordset Object

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This code segment uses the [**Close**](mdmthclose) method of the objRS\_Parent [**Recordset**](mdobjodbrec) object to free the system resources of the parent recordset. Setting the objRS\_Parent **Recordset** object to Null removes the parent object from memory.


```JScript
objRS_Parent.Close;
objRS_Parent = null;
```



 

 




