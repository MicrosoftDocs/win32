---
title: Interface (COM)
description: An optional entry that specifies all interface IDs (IIDs) supported by the associated class.
ms.assetid: '212a6500-14ce-4a9b-9e6a-38d83a5630c8'
keywords:
- Interface registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# Interface (COM)

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

 

 




