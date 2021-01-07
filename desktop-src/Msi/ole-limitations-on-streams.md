---
description: Developers of installation databases need to be aware of two limitations on the handling of streams by the Win32 OLE structured storage implementation.
ms.assetid: ebd5fcac-0238-4f30-9fd5-a0c5cf9028ef
title: OLE Limitations on Streams
ms.topic: article
ms.date: 05/31/2018
---

# OLE Limitations on Streams

Developers of installation databases need to be aware of two limitations on the handling of streams by the Win32 OLE structured storage implementation. These limitations can affect installer functions indirectly through transforms and other data that may be stored in the database as a stream.

There are two relevant limitations:

-   Binary data is stored with an index name created by concatenating the table name and the values of the record's primary keys using a period delimiter. OLE limits stream names to 32 characters (31 + null terminator). Windows Installer uses a compression algorithm that can expand the limit to 62 characters depending upon the character. Note that double-byte characters count as 2.
-   Although you can have multiple streams open at one time, you cannot open a stream a second time until the first reference is closed. This means you cannot select the same binary data stream to be open in multiple records simultaneously. Attempts to read the binary data from the second record fail. Also you cannot rename the primary keys of a record while a binary data stream in that record is open.

 

 



