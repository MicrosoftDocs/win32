---
description: This section describes the format of the records for each of the record-bearing tokens. Information is divided into the following sections.
ms.assetid: 4fdd8339-f660-4389-878a-e7ab067d8508
title: Token Records
ms.topic: article
ms.date: 05/31/2018
---

# Token Records

This section describes the format of the records for each of the record-bearing tokens. Information is divided into the following sections.

-   [TOKEN\_NAME](/windows)
-   [TOKEN\_STRING](/windows)
-   [TOKEN\_INTEGER](/windows)
-   [TOKEN\_GUID](/windows)
-   [TOKEN\_INTEGER\_LIST](/windows)
-   [TOKEN\_FLOAT\_LIST](/windows)

## TOKEN\_NAME

A variable-length record. The token is followed by a count value that specifies the number of bytes that follow in the name field. An ASCII name of length count completes the record.



| Field | Type       | Size (bytes) | Contents                       |
|-------|------------|--------------|--------------------------------|
| token | WORD       | 2            | token\_name                    |
| count | DWORD      | 4            | Length of name field, in bytes |
| name  | BYTE array | count        | ASCII name                     |



 

## TOKEN\_STRING

A variable-length record. The token is followed by a count value that specifies the number of bytes that follow in the string field. An ASCII string of length count continues the record, which is completed by a terminating token. The choice of terminator is determined by syntax issues discussed elsewhere.



| Field      | Type       | Size (bytes) | Contents                         |
|------------|------------|--------------|----------------------------------|
| token      | WORD       | 2            | token\_string                    |
| count      | DWORD      | 4            | Length of string field in bytes  |
| strinG     | BYTE array | count        | ASCII string                     |
| terminator | DWORD      | 4            | tOKEN\_SEMICOLON or TOKEN\_COMMA |



 

## TOKEN\_INTEGER

A fixed length record. The token is followed by the integer value required.



| Field | Type  | Size (bytes) | Contents       |
|-------|-------|--------------|----------------|
| token | WORD  | 2            | tOKEN\_INTEGER |
| valuE | DWORD | 4            | Single integer |



 

## TOKEN\_GUID

A fixed-length record. The token is followed by the four data fields as defined by the OSF DCE standard.



| Field | Type       | Size (bytes) | Contents          |
|-------|------------|--------------|-------------------|
| token | WORD       | 2            | tOKEN\_GUID       |
| Data1 | DWORD      | 4            | UUID data field 1 |
| Data2 | WORD       | 2            | UUID data field 2 |
| Data3 | WORD       | 2            | UUID data field 3 |
| Data4 | BYTE array | 8            | UUID data field 4 |



 

## TOKEN\_INTEGER\_LIST

A variable-length record. The token is followed by a count value that specifies the number of integers that follow in the list field. For efficiency, consecutive integer lists should be compounded into a single list.



| Field | Type  | Size (bytes) | Contents                         |
|-------|-------|--------------|----------------------------------|
| token | WORD  | 2            | tOKEN\_INTEGER\_LISt             |
| count | DWORD | 4            | Number of integers in list field |
| list  | DWORD | 4 x count    | Integer list                     |



 

## TOKEN\_FLOAT\_LIST

A variable-length record. The token is followed by a count value that specifies the number of floats or doubles that follow in the list field. The size of the floating point value (float or double) is determined by the value of float sizespecified in the file header. For efficiency, consecutive TOKEN\_FLOAT\_LISTs should be compounded into a single list.



| Field | Type               | Size (bytes)   | Contents                                  |
|-------|--------------------|----------------|-------------------------------------------|
| token | WORD               | 2              | tOKEN\_FLOAT\_LISt                        |
| count | DWORD              | 4              | Number of floats or doubles in list field |
| list  | float/double array | 4 or 8 x count | Float or double list                      |



 

## Related topics

<dl> <dt>

[Binary Encoding](binary-encoding.md)
</dt> </dl>

 

 
