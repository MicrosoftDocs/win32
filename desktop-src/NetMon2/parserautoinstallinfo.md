---
description: The ParserAutoInstallInfo export function identifies the parser, or parsers that are located in a DLL. ParserAutoInstallInfo should be implemented in all parser DLLs.
ms.assetid: '7af3bf3c-d415-4af9-8f5c-c9a76535bd1a'
title: ParserAutoInstallInfo callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ParserAutoInstallInfo
api_type: 
- UserDefined
api_location: 
- Netmon.h
---

# ParserAutoInstallInfo callback function

The **ParserAutoInstallInfo** export function identifies the parser, or parsers that are located in a DLL. **ParserAutoInstallInfo** should be implemented in all parser DLLs.

## Syntax


```C++
PPF_PARSERDLLINFO WINAPI ParserAutoInstallInfo(void);
```



## Parameters

This callback function has no parameters.

## Return value

If the function is successful, the return value is a [PF\_PARSERDLLINFO](pf-parserdllinfo.md) structure that describes the parsers in the DLL.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

When Network Monitor loads for the first time, it calls **ParserAutoInstallInfo** (if it exists) to automatically install each parser, and then enumerate all the parser DLLs in the parser subdirectory.

The information returned in the **PF\_PARSERDLLINFO** structure includes the following:

-   The number of parsers in the DLL (typically one).
-   The name and a brief description of the protocol that each parser detects.
-   An optional Help file for each protocol.
-   The protocols that precede each protocol.
-   The protocols that follow each protocol.

Each parser DLL should contain one parser. However, Network Monitor allows you to create a DLL that contains more than one parser. For example, tcpip.dll is a Network Monitor DLL with more than one parser.



| For information on                                               | See                                                                          |
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| What parsers are, and how they work with Network Monitor.        | [Parsers](parsers.md)                                                       |
| Which entry points are included in the parser DLL.               | [Parser DLL Architecture](parser-dll-architecture.md)                       |
| How to implement **ParserAutoInstallInfo**  includes an example. | [Implementing ParserAutoInstallInfo](implementing-parserautoinstallinfo.md) |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PF\_PARSERDLLINFO](pf-parserdllinfo.md)
</dt> </dl>

 

 




