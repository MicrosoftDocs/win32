---
description: The DllMain export function for the parser identifies the existence of the parser, and releases resources that Network Monitor uses for the parser. DllMain must be implemented in all parser DLLs.
ms.assetid: 2ce79d49-3aad-461f-99cf-cf632680efcc
title: DllMain Parser callback function (Process.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DllMain
api_type: 
- UserDefined
api_location: 
- process.h
---

# DllMain Parser callback function

The **DllMain** export function for the parser identifies the existence of the parser, and releases resources that Network Monitor uses for the parser. **DllMain** must be implemented in all parser DLLs.

## Syntax


```C++
BOOL WINAPI DllMain(
  _In_ HANDLE hInstance,
  _In_ ULONG  Command,
       LPVOID Reserved
);
```



## Parameters

<dl> <dt>

*hInstance* \[in\]
</dt> <dd>

Handle to an instance of the parser.

</dd> <dt>

*Command* \[in\]
</dt> <dd>

Indicator to determine why the function is called. For a list of all possible flags, see [DllMain](/windows/desktop/Dlls/dllmain). The parser implementation must process the following values.



| Value                                                                                                                                                                         | Meaning                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DLL_PROCESS_ATTACH"></span><span id="dll_process_attach"></span><dl> <dt>**DLL\_PROCESS\_ATTACH**</dt> </dl> | When **DllMain** is called for the first time, the DLL must call [CreateProtocol](createprotocol.md) to provide information to Network Monitor. <br/>   |
| <span id="DLL_PROCESS_DETACH"></span><span id="dll_process_detach"></span><dl> <dt>**DLL\_PROCESS\_DETACH**</dt> </dl> | When **DllMain** is called for the last time, the DLL must call [DestroyProtocol](destroyprotocol.md) to release the resources that the DLL uses. <br/> |



 

</dd> <dt>

*Reserved* 
</dt> <dd>

Not used now.

</dd> </dl>

## Return value

The parser DLL always returns **TRUE**.

## Remarks

The operating system calls **DllMain** to load and unload the parser DLL. This function is based on the dynamic-link library [DllMain](/windows/desktop/Dlls/dllmain) function.

You can also use the implementation of **DllMain** to store an instance of a parser for use in the future. For example, you can store a parser DLL instance, and then use it for a system call in the future.



| For information on                                        | See                                                     |
|-----------------------------------------------------------|---------------------------------------------------------|
| What parsers are, and how they work with Network Monitor. | [Parsers](parsers.md)                                  |
| Which entry points are included in the parser DLL.        | [Parser DLL Architecture](parser-dll-architecture.md)  |
| How to implement **DllMain**  includes an example.        | [Implementing DllMain](implementing-dllmain-parser.md) |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Process.h</dt> </dl> |



## See also

<dl> <dt>

[CreateProtocol](createprotocol.md)
</dt> <dt>

[DestroyProtocol](destroyprotocol.md)
</dt> <dt>

[DllMain](/windows/desktop/Dlls/dllmain)
</dt> </dl>

 

