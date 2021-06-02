---
description: ICE custom actions communicate by calling MsiProcessMessage and posting an INSTALLMESSAGE\_USER type message.
ms.assetid: 36307589-de0e-4eaf-b439-e7ba3cd96fb3
title: ICE Message Guidelines
ms.topic: article
ms.date: 05/31/2018
---

# ICE Message Guidelines

ICE custom actions communicate by calling [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) and posting an INSTALLMESSAGE\_USER type message.

When authoring a message string for an ICE custom action, format the string as follows.

*Name of ICE* <tab> *Message Type* <tab> *Description* <tab> *Help URL or location* <tab> *Table Name* <tab> *Column Name* <tab> *Primary Key* <tab> *Primary Key* <tab> *Primary Key* . . . (repeat for as many primary keys as needed)

The first three fields of the string are required in every message.

The Message Type field specifies whether the ICE reports a Failure, Error, Warning, or Informational message.



| Value | Message type                                                                                                                                                          |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Failure message reporting the failure of the ICE custom action.                                                                                                       |
| 1     | Error message reporting database authoring that cause incorrect behavior.                                                                                             |
| 2     | Warning message reporting database authoring that causes incorrect behavior in certain cases. Warnings can also report unexpected side-effects of database authoring. |
| 3     | Informational message.                                                                                                                                                |



 

If help is not available, the Help URL field may be the empty string.

Error and Warning messages should provide the Table Name, Column Name, and Primary Key fields. If any of these fields are omitted, all of the fields following the first blank field must be left out of the message. For example, a table name is provided without a column name and primary keys or a table name and a column name is provided with no primary keys. However a column name and primary keys cannot be used without a table name. Multiple primary keys may be listed until all the primary keys in that table have been given values.

## Examples

The first message illustrated by the [Sample ICE in C++](sample-ice-in-c-.md):

"ICE01\\t3\\tCreated 04/29/1998 by <insert author's name here>."

The second message posted by the sample ICE:

"ICE01\\t3\\tLast modified 05/06/1999 by <insert author's name here>."

The third message posted by the sample ICE.

"ICE01\\t3\\tSimple ICE to illustrating the ICE concept".

 

 



