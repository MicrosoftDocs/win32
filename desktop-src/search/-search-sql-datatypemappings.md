---
description: The following table lists the mappings between variant data types and OLE DB data types.
ms.assetid: 213458bf-b847-4ced-8a92-686b4eee6d07
title: Data Type Mappings
ms.topic: article
ms.date: 05/31/2018
---

# Data Type Mappings

The following table lists the mappings between variant data types and OLE DB data types.




| Variant data type | OLE DB data type |
|-------------------|------------------|
| VT\_BOOL          | DBTYPE\_BOOL     |
| VT\_BSTR          | DBTYPE\_BSTR     |
| VT\_BYREF         | DBTYPE\_BYREF    |
| VT\_CY            | DBTYPE\_CY       |
| VT\_DATE          | DBTYPE\_DATE     |
| VT\_DECIMAL       | DBTYPE\_DECIMAL  |
| VT\_EMPTY         | DBTYPE\_EMPTY    |
| VT\_FILETIME      | DBTYPE\_FILETIME |
| VT\_GUID          | DBTYPE\_GUID     |
| VT\_I1            | DBTYPE\_I1       |
| VT\_I2            | DBTYPE\_I2       |
| VT\_I4            | DBTYPE\_I4       |
| VT\_I8            | DBTYPE\_I8       |
| VT\_NULL          | DBTYPE\_NULL     |
| VT\_R4            | DBTYPE\_R4       |
| VT\_R8            | DBTYPE\_UI8      |
| VT\_VECTOR        | DBTYPE\_VECTOR   |
| VT\_WSTR          | DBTYPE\_WSTR     |



 

The following table lists the mappings between XML data types and OLE DB data types.



| Variant data type | OLE DB data type |
|-------------------|------------------|
| BIN.BASE64        | DBTYPE\_BYTES    |
| BIN.HEX           | DBTYPE\_I8       |
| BOOLEAN           | DBTYPE\_BOOL     |
| CHAR              | DBTYPE\_STR      |
| DATE              | DBTYPE\_DATE     |
| DATETIME          | DBTYPE\_DATE     |
| DATETIME.TZ       | DBTYPE\_DATE     |
| FIXED.14.4        | DBTYPE\_R4       |
| FLOAT             | DBTYPE\_R8       |
| I1                | DBTYPE\_I1       |
| I2                | DBTYPE\_I2       |
| I4                | DBTYPE\_I4       |
| I8                | DBTYPE\_I8       |
| INT               | DBTYPE\_I8       |
| LONG              | DBTYPE\_I4       |
| NUMBER            | DBTYPE\_R8       |
| R4                | DBTYPE\_R4       |
| R8                | DBTYPE\_R8       |
| STRING            | DBTYPE\_WSTR     |
| TIME              | DBTYPE\_FILETIME |
| TIME.TZ           | DBTYPE\_FILETIME |
| UI1               | DBTYPE\_UI2      |
| UI2               | DBTYPE\_UI2      |
| UI4               | DBTYPE\_UI4      |
| UI8               | DBTYPE\_UI8      |
| URI               | DBTYPE\_WSTR     |
| UUID              | DBTYPE\_GUID     |



 

You can cast string data to other data types. For more information,refer to [Casting the Data Type of a Column](-search-sql-castingdatacolumntype.md).

 

 



