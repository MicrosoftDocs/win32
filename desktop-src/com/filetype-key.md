---
title: FileType Key
description: Used by GetClassFile to match patterns against various file bytes in a non-compound file.
ms.assetid: ced23cdb-c184-43fe-ba37-fe1af8664b66
keywords:
- FileType registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# FileType Key

Used by [**GetClassFile**](/windows/desktop/api/Objbase/nf-objbase-getclassfile) to match patterns against various file bytes in a non-compound file.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\FileType
   {CLSID}
      n = offset, cb, mask, value
```

<dl> <dt>

<span id="offset"></span><span id="OFFSET"></span>*offset*
</dt> <dd>

Determines how far from the beginning or end of the file to begin the comparison. If the offset is a negative value, the comparison begins from the end of the file minus the offset value. The offset value is a decimal type unless preceded by "0x".

</dd> <dt>

<span id="cb"></span><span id="CB"></span>*cb*
</dt> <dd>

Represents the length in bytes from the beginning to the end of the file. Represents the byte range in the file. The *cb* value is a decimal unless preceded by "0x".

</dd> <dt>

<span id="mask"></span><span id="MASK"></span>*mask*
</dt> <dd>

A binary value used for masking, which is performed by using a logical AND operation, and the byte range specified by *offset* and *cb*. If this value is omitted, the bytes are set to all ones. This value is always hexadecimal.

</dd> <dt>

<span id="value"></span><span id="VALUE"></span>*value*
</dt> <dd>

Represents the pattern that must match for a file to be of this file type. The pattern is used to properly identify a known file format from its contents, not by its extension.

</dd> </dl>

## Remarks

Entries are used by the [**GetClassFile**](/windows/desktop/api/Objbase/nf-objbase-getclassfile) function to match patterns against various file bytes in a non-compound file. **FileType** has CLSID subkeys, each of which has a series of subkeys **0**, **1**, **2**, **3**. These values contain patterns that, if one matches, yield the indicated CLSID. For example, a value of "0, 4, FFFFFFFF, ABCD1234" indicates that the first 4 bytes must be ABCD1234, in that order. A value of "-4, 4, FEFEFEFE " indicates that the last four bytes in the file must be FEFEFEFE. If either pattern matches, the CLSID is returned.

The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes** key corresponds to the **HKEY\_CLASSES\_ROOT** key, which was retained for compatibility with earlier versions of COM.

## Related topics

<dl> <dt>

[**<file\_extension>**](-file-extension--key.md)
</dt> <dt>

[**GetClassFile**](/windows/desktop/api/Objbase/nf-objbase-getclassfile)
</dt> </dl>

 

 




