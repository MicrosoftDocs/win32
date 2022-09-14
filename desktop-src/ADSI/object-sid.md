---
title: Object SID (WinNT Provider)
description: The user security identifier (SID) can be retrieved using the objectSID attribute. The objectSID is returned as a VARIANT array of characters that form the SID string.
ms.assetid: 15845e6d-ea30-4d6c-9f35-b2abc1a564ba
ms.tgt_platform: multiple
keywords:
- WinNT provider ADSI ,user management examples,Object SID
ms.topic: article
ms.date: 05/31/2018
---

# Object SID (WinNT Provider)

The user security identifier (SID) can be retrieved using the **objectSID** attribute. The **objectSID** is returned as a **VARIANT** array of characters that form the SID string.

## Example Code


```VB
sid = usr.Get("objectSID")
For i = LBound(sid) To UBound(sid)
    Debug.Print sid(i)
Next
```



 

 




