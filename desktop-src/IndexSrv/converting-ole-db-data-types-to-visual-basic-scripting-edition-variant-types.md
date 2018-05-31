---
title: Converting OLE DB Data Types to Visual Basic Scripting Edition Variant Types
description: A table that lists the OLE DB data types supported, their equivalent Automation variant types, and any formatting restrictions imposed when displaying the data to an end user through VBScript.
ms.assetid: 7fe30f06-f70c-4171-9880-f61fd10b9e89
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Converting OLE DB Data Types to Visual Basic Scripting Edition Variant Types

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Because all programming access to Indexing Service is through the [OLE DB Provider](ole-db-provider-for-indexing-service.md), you can retrieve only supported OLE DB data types when you ask for information back from a query. VBScript supports certain Automation data types within its **VARIANT** data-type implementation. The following table lists the OLE DB data types supported, their equivalent Automation variant types, and any formatting restrictions imposed when displaying the data to an end user through VBScript.



| OLE DB data type | Automation Variant type | Formatting restrictions                                                                                                                                                                                                                                                                                |
|------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DBTYPE\_I1       | VT\_I1                  | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number, for example, 0xf8.                                                                                                                                                         |
| DBTYPE\_UI1      | VT\_UI1                 | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number.                                                                                                                                                                            |
| DBTYPE\_I2       | VT\_I2                  | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number.                                                                                                                                                                            |
| DBTYPE\_UI2      | VT\_UI2                 | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number.                                                                                                                                                                            |
| DBTYPE\_I4       | VT\_I4                  | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number.                                                                                                                                                                            |
| DBTYPE\_UI4      | VT\_UI4                 | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number.                                                                                                                                                                            |
| DBTYPE\_I8       | VT\_I8                  | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number.                                                                                                                                                                            |
| DBTYPE\_UI8      | VT\_UI8                 | Integer. Expressed either in decimal (base 10) or hexadecimal (base 16) notation. The latter requires 0x before the number.                                                                                                                                                                            |
| DBTYPE\_R4       | VT\_R4                  | Real number. Can be expressed in scientific notation.                                                                                                                                                                                                                                                  |
| DBTYPE\_R8       | VT\_R8                  | Real number. Can be expressed in scientific notation.                                                                                                                                                                                                                                                  |
| DBTYPE\_CY       | VT\_CY                  | Currency. Expressed as two integers, separated by a period; for example, 100.55. Cannot be preceded by $, ¥, £, or other such signs. This data type does not specify the currency format.                                                                                                              |
| DBTYPE\_DATE     | VT\_DATE                | Date. Expressed as an absolute in two forms: yyyy/mm/dd and yyyy/mm/dd hh:mm:ss. Also expressed as a relative date: -\#y, -\#m, -\#w, -\#d, -\#h, -\#n, -\#s where the letters correspond to year, month, week, day, hour, minute and second. Positive relative dates in the future are not supported. |
| DBTYPE\_BOOL     | VT\_BOOL                | Boolean. Expressed as TRUE or FALSE.                                                                                                                                                                                                                                                                   |
| DBTYPE\_STR      | VT\_LPSTR               | String. Any input accepted.                                                                                                                                                                                                                                                                            |
| DBTYPE\_WSTR     | VT\_LPWSTR              | Unicode string. Any input accepted.                                                                                                                                                                                                                                                                    |
| DBTYPE\_BSTR     | VT\_BSTR                | Basic string. Any input accepted.                                                                                                                                                                                                                                                                      |
| DBTYPE\_GUID     | VT\_CLSID               | Globally unique identifier (GUID). Expressed as XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.                                                                                                                                                                                                                  |
| DBTYPE\_BYREF    | (not applicable)        | For queries, this should be added to DBTYPE\_STR and DBTYPE\_WSTR string types. For example: DBTYPE\_WSTR \| DBTYPE\_BYREF.                                                                                                                                                                            |
| DBTYPE\_VECTOR   | VT\_VECTOR              | Vector properties are fully supported.                                                                                                                                                                                                                                                                 |
| VT\_FILETIME     | VT\_FILETIME            | Expressed as an absolute in two forms: yyyy/mm/dd and yyyy/mm/dd hh:mm:ss. Also expressed as a relative date: -\#y, -\#m, -\#w, -\#d, -\#h, -\#n, -\#s where the letters correspond to year, month, week, day, hour, minute and second. Positive relative dates into the future are not supported.     |



 

 

 




