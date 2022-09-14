---
title: Conversion
description: Used by the Convert dialog box to determine the formats an application can read and write.
ms.assetid: ff12c4b3-9548-4135-aaf4-d8b49f9aed41
keywords:
- Conversion registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# Conversion

Used by the **Convert** dialog box to determine the formats an application can read and write.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      Conversion
         Readable
            Main = rformat, ...
         ReadWritable
            Main = rwformat, ...
```

## Remarks

Conversion information is used by the **Convert** dialog box to determine what formats an application can read and write. A comma-delimited file format is indicated by a number if it is one of the Clipboard formats defined in Windows.h. A string indicates the format is not one defined in Windows.h (private). In this case, the readable and writable format is CF\_OUTLINE (private).

The *rformat* value specifies the file format an application can read (convert from).

The *rwformat* value specifies the file format an application can read and write (activate as).

 

 




