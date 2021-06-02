---
description: The functions, listed in the following table, are entry points for parser DLLs. The functions are the entry points for calls from the operating system and Network Monitor.
ms.assetid: 67811ddb-1961-4306-a62f-b9fd2d2d2b55
title: Parser DLL Export Functions
ms.topic: article
ms.date: 05/31/2018
---

# Parser DLL Export Functions

The functions, listed in the following table, are entry points for parser DLLs. The functions are the entry points for calls from the operating system and Network Monitor.



| Function                                           | Description                                                                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DllMain Parser](dllmain-parser.md)               | Indicates to the parser DLL that it is loaded or unloaded. The operating system calls the **DllMain Parser** function when a process loads or unloads the DLL. |
| [AttachProperties](attachproperties.md)           | Notifies the parser to attach any properties that exist in a frame.                                                                                            |
| [Deregister](deregister.md)                       | Notifies the parser to clean up.                                                                                                                               |
| [FormatProperties](formatproperties.md)           | Notifies the parser to take all of the property instances in and build the **szPropertyText** member of each **PROPERTYINST** structure.                       |
| [RecognizeFrame](recognizeframe.md)               | Determines whether the parser can interpret the unprocessed frame data with the specified protocol.                                                            |
| [Register Parser](register-parser.md)             | Determines basic information about the parser within the DLL. Network Monitor calls the **Register Parser** function.                                          |
| [ParserAutoInstallInfo](parserautoinstallinfo.md) | Installs a parser automatically.                                                                                                                               |



 

Network Monitor provides structures and helper functions that the parser can call.



| For more information about                          | See                                                                          |
|-----------------------------------------------------|------------------------------------------------------------------------------|
| Helper functions that experts and parsers can call. | [Expert and Parser Common Functions](expert-and-parser-common-functions.md) |
| Helper functions that only parsers can call.        | [Parser Functions](parser-functions.md)                                     |
| Structures that parser functions use.               | [Parser Structures](parser-structures.md)                                   |



 

 

 



