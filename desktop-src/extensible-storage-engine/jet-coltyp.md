---
description: "Learn more about: JET_COLTYP"
title: JET_COLTYP
TOCTitle: JET_COLTYP
ms:assetid: 2c30c025-629d-4b94-bcb9-9c8fc3d4e039
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269213(v=EXCHG.10)
ms:contentKeyID: 32765516
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_COLTYP


_**Applies to:** Windows | Windows Server_

## JET_COLTYP

The **JET_COLTYP** group of constants describe all possible column types that can be found in a table.


| <p>Constant/value</p> | <p>Description</p> | 
|-----------------------|--------------------|
| <p>JET_coltypNil<br />0</p> | <p>An invalid column type.</p> | 
| <p>JET_coltypBit<br />1</p> | <p>A column type that allows three values: <strong>True</strong>, <strong>False</strong>, or <strong>NULL</strong>. This type of column is one byte in length and is a fixed size. <strong>False</strong> sorts before <strong>True</strong>. Note that the size of this type does not match the size of the variant Boolean type.</p> | 
| <p>JET_coltypUnsignedByte<br />2</p> | <p>A 1-byte unsigned integer that can take on values between 0 (zero) and 255.</p> | 
| <p>JET_coltypShort<br />3</p> | <p>A 2-byte signed integer that can take on values between -32768 and 32767. Negative values sort before positive values.</p> | 
| <p>JET_coltypLong<br />4</p> | <p>A 4-byte signed integer that can take on values between - 2147483648 and 2147483647. Negative values sort before positive values.</p> | 
| <p>JET_coltypCurrency<br />5</p> | <p>An 8-byte signed integer that can take on values between - 9223372036854775808 and 9223372036854775807. Negative values sort before positive values. This column type is identical to the variant currency type. This column type can also be used as a native 8-byte signed integer.</p> | 
| <p>JET_coltypIEEESingle<br />6</p> | <p>A single-precision (4-byte) floating point number.</p> | 
| <p>JET_coltypIEEEDouble<br />7</p> | <p>A double-precision (8-byte) floating point number.</p> | 
| <p>JET_coltypDateTime<br />8</p> | <p>A double-precision (8-byte) floating point number that represents a date in fractional days since the year 1900. This column type is identical to the variant date type.</p> | 
| <p>JET_coltypBinary<br />9</p> | <p>A fixed or variable length, raw binary column that can be up to 255 bytes in length.</p><p>This column type can be used to implement a GUID if configured as a fixed length, 16-byte binary column. The only caveat is that the relative ordering of values in an index over such a column will not match the relative ordering of the standard registry-string rendering of a GUID (that is "{ 0d6cec99-3f3f-4dc7-a5e6-f87aefeb908b}").</p> | 
| <p>JET_coltypText<br />10</p> | <p>A fixed or variable length text column that can be up to 255 ASCII characters in length or 127 Unicode characters in length.</p><p>All strings are stored as a counted number of characters. The strings need not be null terminated. Further, it is not necessary for the count to include a null terminator. Finally, embedded null characters can be stored.</p><p>ASCII strings are always treated as case insensitive for sorting and searching purposes. Further, only the characters preceding the first null character (if any) are considered for sorting and searching.</p><p>Unicode strings use the Win32 API <a href="/windows/win32/api/winnls/nf-winnls-lcmapstringa">LCMapString</a> to create sort keys that are subsequently used for sorting and searching that data. By default, Unicode strings are considered to be in the U.S. English locale and are sorted and searched using the following normalization flags: NORM_IGNORECASE, NORM_IGNOREKANATYPE, and NORM_IGNOREWIDTH. In Windows 2000, it is possible to customize these flags per index to also include NORM_IGNORENONSPACE. In Windows XP and later releases, it is possible to request any combination of the following normalization flags per index: LCMAP_SORTKEY, LCMAP_BYTEREV, NORM_IGNORECASE, NORM_IGNORENONSPACE, NORM_IGNORESYMBOLS, NORM_IGNOREKANATYPE, NORM_IGNOREWIDTH, and SORT_STRINGSORT.</p><p>In all releases, it is possible to customize the locale per index. Any locale may be used as long as the appropriate language pack has been installed on the machine. Finally, any null characters encountered in a Unicode string are completely ignored.</p> | 
| <p>JET_coltypLongBinary<br />11</p> | <p>A fixed or variable length, raw binary column that can be up to 2147483647 bytes in length. This type is considered to be a Long Value. A Long Value is special because it can be large and because it can be accessed as a stream. This type is otherwise identical to JET_coltypBinary.</p> | 
| <p>JET_coltypLongText<br />12</p> | <p>A fixed or variable length, text column that can be up to 2147483647 ASCII characters in length or 1073741823 Unicode characters in length. This type is considered to be a Long Value. A Long Value is special because it can be large and because it can be accessed as a stream. This type is otherwise identical to JET_coltypText.</p> | 
| <p>JET_coltypSLV<br />13</p> | <p>This column type is obsolete.</p> | 
| <p>JET_coltypUnsignedLong<br />14</p> | <p>A 4-byte unsigned integer that can take on values between 0 (zero) and 4294967295.</p><p><strong>Windows Vista and Windows Server 2008:</strong>  This column type is supported on Windows Vista, Windows Server 2008 and later releases.</p> | 
| <p>JET_coltypLongLong<br />15</p> | <p>An 8-byte signed integer that can take on values between - 9223372036854775808 and 9223372036854775807. Negative values sort before positive values.</p><p><strong>Windows Vista and Windows Server 2008:</strong>  This column type is supported on Windows Vista, Windows Server 2008 and later releases.</p> | 
| <p>JET_coltypGUID<br />16</p> | <p>A fixed length 16 byte binary column that natively represents the GUID data type. GUID column values sort in the same way that those values would sort as strings when in standard form (i.e. {4999b5c0-7657-42d9-bdc1-4b779784e013}).</p><p><strong>Windows Vista and Windows Server 2008:</strong>  This column type is supported on Windows Vista, Windows Server 2008 and later releases.</p> | 
| <p>JET_coltypUnsignedShort<br />17</p> | <p>A 2-byte unsigned integer that can take on values between 0 and 65535.</p><p><strong>Windows Vista and Windows Server 2008:</strong>  This column type is supported on Windows Vista, Windows Server 2008 and later releases.</p> | 
| <p>JET_coltypMax<br />18</p> | <p>A constant describing the maximum (that is, one beyond the largest valid) column type supported by the engine.</p><p>This value should be used with care because it will change as new column types are supported. For example, it has a different literal value on Windows 2000 than it does on Windows XP and later releases.</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetAddColumn](./jetaddcolumn-function.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)
