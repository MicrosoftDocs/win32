---
title: NONREDIST
description: Adds names to the list of files that should not be exported when COM+ applications are packaged for installation on other computers. Note that this is a subkey, not a value.
ms.assetid: c50e20e4-1a25-4978-ab84-8f7b4b2f6069
keywords:
- NONREDIST registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# NONREDIST

Adds names to the list of files that should not be exported when COM+ applications are packaged for installation on other computers. Note that this is a subkey, not a value.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole
   NONREDIST
      name1
      name2
```

## Remarks

The files you add to the list are represented by name/value pairs stored under this key. In each name/value pair, the name is the file name and the value is reserved.

 

 




