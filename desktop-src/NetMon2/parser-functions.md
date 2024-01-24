---
description: The following helper functions are called by parsers.
ms.assetid: 4e9a9314-8d64-46c0-ad98-bdb9dc4c225a
title: Parser Functions
ms.topic: article
ms.date: 05/31/2018
---

# Parser Functions

The following helper functions are called by parsers.



| Function                                                 | Description                                                                                                    |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [AddressToString](addresstostring.md)                   | Converts an address to a string.                                                                               |
| [LookupByteSetString](lookupbytesetstring.md)           | Retrieves the string corresponding to the specified value of a labeled set.                                    |
| [SetCCInstPtr](setccinstptr.md)                         | Captures a context instance pointer.                                                                           |
| [StringToAddress](stringtoaddress.md)                   | Converts a string to an address.                                                                               |
| [VarLenSmallIntToDword](varlensmallinttodword.md)       | Converts a variable-length, small integer to a **DWORD**.                                                      |
| [LookupDwordSetString](lookupdwordsetstring.md)         | Retrieves the string corresponding to the specified value of a labeled set.                                    |
| [LookupWordSetString](lookupwordsetstring.md)           | Retrieves the string corresponding to the given value from a labeled set.                                      |
| [BERGetHeader](bergetheader.md)                         | Decodes a choice header.                                                                                       |
| [BERGetInteger](bergetinteger.md)                       | Decodes a BER-encoded integer.                                                                                 |
| [BERGetString](bergetstring.md)                         | Decodes a BER-encoded string.                                                                                  |
| [CCHeapAlloc](ccheapalloc.md)                           | Allocates memory on a capture-by-capture basis.                                                                |
| [CCHeapFree](ccheapfree.md)                             | Releases the memory allocated by the **CCHeapAlloc** function.                                                 |
| [CCHeapReAlloc](ccheaprealloc.md)                       | Reallocates memory allocated by the **CCHeapAlloc** function.                                                  |
| [CCHeapSize](ccheapsize.md)                             | Retrieves the size of the memory allocated by the **CCHeapAlloc** function.                                    |
| [GetCCInstPtr](getccinstptr.md)                         | Retrieves the pointer to the instance data added to the capture context.                                       |
| [CreateProtocol](createprotocol.md)                     | Informs the Network Monitor API that a specific protocol parser exists.                                        |
| [DestroyProtocol](destroyprotocol.md)                   | Destroys the protocol created by the **CreateProtocol** function.                                              |
| [BuildINIPath](buildinipath.md)                         | Retrieves a fully qualified path to the initialization (INI) file that corresponds to information you enter.   |
| [CreateHandoffTable](createhandofftable.md)             | Creates a handoff table based on information in an given INI file.                                             |
| [DestroyHandoffTable](destroyhandofftable.md)           | Destroys a handoff table created with the **CreateHandoffTable** function.                                     |
| [GetProtocolFromTable](getprotocolfromtable.md)         | Retrieves the protocol of a given handoff table.                                                               |
| [AddProperty](/previous-versions/bb251873(v=msdn.10))                           | Adds a **PROPERTYINFO** structure to the property database.                                                    |
| [AttachPropertyInstance](attachpropertyinstance.md)     | Attaches a property instance to a frame.                                                                       |
| [AttachPropertyInstanceEx](attachpropertyinstanceex.md) | Attaches a property instance to a frame.                                                                       |
| [CreatePropertyDatabase](createpropertydatabase.md)     | Creates a property database that describes properties that the parser uses to describe its data.               |
| [DestroyPropertyDatabase](destroypropertydatabase.md)   | Destroys a property database created by calls to the **CreatePropertyDatabase** and **AddProperty** functions. |
| [FindNextFrame](findnextframe.md)                       | Finds the next frame in the current capture context that matches a given filter.                               |
| [FindPreviousFrame](findpreviousframe.md)               | Finds the previous frame in the current capture context that matches a given filter.                           |
| [FormatPropertyInstance](formatpropertyinstance.md)     | Formats the property instance in a generic manner.                                                             |
| [GetFrameDestAddress](getframedestaddress.md)           | Retrieves the destination address of a frame.                                                                  |
| [GetFrameSourceAddress](getframesourceaddress.md)       | Retrieves the source address of a frame.                                                                       |
| [GetProtocolStartOffset](getprotocolstartoffset.md)     | Retrieves the offset to a given protocol in the frame.                                                         |
| [ParserTemporaryLockFrame](parsertemporarylockframe.md) | Locks a frame when it enters a parser and unlocks the frame when it exits.                                     |



 

For information about export functions (helper functions that can be called by experts and parsers), structures, and enumerations, see the following topics.



| For information about                                  | See                                                                          |
|--------------------------------------------------------|------------------------------------------------------------------------------|
| Functions that parsers export.                         | [Parser DLL Export Functions](parser-dll-export-functions.md)               |
| Structures that parser functions use.                  | [Parser Structures](parser-structures.md)                                   |
| Common helper functions that parsers and experts call. | [Expert and Parser Common Functions](expert-and-parser-common-functions.md) |



 

 

 
