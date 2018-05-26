---
title: Interface
description: An optional entry that specifies all interface IDs (IIDs) supported by the associated class.
ms.assetid: b62a780f-8ff9-4942-839c-9b38cd2a920b
keywords:
- Interface registry key COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interface

An optional entry that specifies all interface IDs (IIDs) supported by the associated class.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      Interface
         {IID1} = name1
         {IID2} = name2
         ...
```

## Remarks

If an interface name is not present in this list, the interface can never be supported by an instance of this class.

## Related topics

<dl> <dt>

[Interface Key](interface-key.md)
</dt> </dl>

 

 




