---
description: The table below shows which words are reserved and must not be used.
ms.assetid: 680211de-3f81-4ea7-b03e-741096b5dde0
title: Reserved Words, Header, and Comments
ms.topic: article
ms.date: 05/31/2018
---

# Reserved Words, Header, and Comments

The table below shows which words are reserved and must not be used.



|                  |          |           |
|------------------|----------|-----------|
| ARRAY            | DWORD    | UCHAR     |
| BINARY           | FLOAT    | ULONGLONG |
| BINARY\_RESOURCE | SDWORD   | UNICODE   |
| CHAR             | STRING   | WORD      |
| CSTRING          | SWORD    |           |
| DOUBLE           | TEMPLATE |           |



 

The variable-length header is compulsory and must be at the beginning of the data stream. The header contains the following data.



| Type           | Required | Size (in bytes) | Value | Description                  |
|----------------|----------|-----------------|-------|------------------------------|
| Magic Number   | x        | 4               | xof   |                              |
| Version Number | x        | 2               | 03    | Major version 3              |
|                |          |                 | 03    | Minor version 3              |
| Format Type    | x        | 4               | txt   | Text File                    |
|                |          |                 | bin   | Binary file                  |
|                |          |                 | tzip  | MSZip compressed text file   |
|                |          |                 | bzip  | MSZip compressed binary file |
| Float Size     | x        | 0064            |       | 64-bit floats                |
|                | x        | "0032"          |       | 32-bit floats                |



 

The values in the table are delimited by quotes to call attention to the number of characters in each value. Those with 4 bytes contain four characters, those with 2 bytes contain two characters.

Comments are applicable only in text files. Comments can occur anywhere in the data stream. A comment begins with either C++ style double-slashes (//), or a pound sign (\#). The comment runs to the next new line. The following example shows valid comments.


```
#  This is a comment.
// This is another comment.
```



## Related topics

<dl> <dt>

[Text Encoding](text-encoding.md)
</dt> </dl>

 

 



