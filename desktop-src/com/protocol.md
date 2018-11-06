---
title: Protocol
description: Indicates that this OLE 2 class is insertable in OLE 1 containers.
ms.assetid: '320dff51-ac27-42f3-8c0f-353b29e289d9'
keywords:
- Protocol registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# Protocol

Indicates that this OLE 2 class is insertable in OLE 1 containers.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes
   {ProgID}
      Protocol
         StdFileEditing
            Server = path
            Verb
               0 = verb1
               1 = verb2
               ...
```

## Remarks

The **StdFileEditing** entry specifies OLE 1 compatibility information. It should be present only if objects of this class are insertable in OLE 1 containers.

**Server** specifies the full path to the OLE 2 server application and **Verb** specifies the verbs. Verb 0 is the primary verb and additional verbs must be numbered consecutively.

 

 




