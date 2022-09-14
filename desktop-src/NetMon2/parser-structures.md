---
description: This section describes structures you can use to develop parsers. These structures are used by functions you can use to develop parsers and functions you can use to develop either parsers or experts.
ms.assetid: ce45a8ef-4355-46fd-909e-3ab4d63a3bf1
title: Parser Structures
ms.topic: article
ms.date: 05/31/2018
---

# Parser Structures

This section describes structures you can use to develop parsers. These structures are used by functions you can use to develop parsers and functions you can use to develop either parsers or experts.



| Structure                                 | Description                                                                                                                     |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [MACFRAME](macframe.md)                  | Defines the most commonly used initial protocols.                                                                               |
| [ENTRYPOINTS](entrypoints.md)            | Specifies pointers to the entry points for the Parser DLL.                                                                      |
| [PF\_FOLLOWENTRY](pf-followentry.md)     | Specifies the protocol that follows the current protocol.                                                                       |
| [PF\_FOLLOWSET](pf-followset.md)         | Specifies the set of protocols that follows the current protocol.                                                               |
| [PF\_HANDOFFENTRY](pf-handoffentry.md)   | Specifies either the protocol that hands off to the current protocol or the protocol that the current protocol hands off to.    |
| [PF\_HANDOFFSET](pf-handoffset.md)       | Specifies the set of protocols that hand off to the current protocol or the set of protocols the current protocol hands off to. |
| [PF\_PARSERDLLINFO](pf-parserdllinfo.md) | Specifies the number of parsers in the parser DLL and information about each parser.                                            |
| [PF\_PARSERINFO](pf-parserinfo.md)       | Specifies information about a specific parser.                                                                                  |
| [LABELED\_BIT](labeled-bit.md)           | Specifies handles, BIT fields, or flags.                                                                                        |
| [LABELED\_BYTE](labeled-byte.md)         | Specifies a **BYTE** label pair.                                                                                                |
| [LABELED\_DWORD](labeled-dword.md)       | Specifies a **DWORD** label pair.                                                                                               |
| [LABELED\_WORD](labeled-word.md)         | Specifies a **WORD** label pair.                                                                                                |
| [PROPERTYINFO](propertyinfo.md)          | Specifies the properties that the protocol parser requires to describe frames.                                                  |
| [PROPERTYINST](propertyinst.md)          | Specifies an instance of a property in a frame.                                                                                 |
| [PROPERTYINSTEX](propertyinstex.md)      | Specifies a free-form, extended property instance.                                                                              |
| [PROTOCOLINFO](protocolinfo.md)          | Specifies a protocol.                                                                                                           |
| [RANGE](range.md)                        | Specifies a range for a number.                                                                                                 |
| [SET](set.md)                            | Specifies a table of values for a property.                                                                                     |



 

For information about functions used to develop parser DLLs, see the following topics.



| For information about                                         | See                                                                          |
|---------------------------------------------------------------|------------------------------------------------------------------------------|
| Functions that the parser DLLs export.                        | [Parser DLL Export Functions](parser-dll-export-functions.md)               |
| Functions that you can use to develop parser DLLs.            | [Parser Functions](parser-functions.md)                                     |
| Functions that you can use to develop parser and expert DLLs. | [Expert and Parser Common Functions](expert-and-parser-common-functions.md) |



 

 

 



