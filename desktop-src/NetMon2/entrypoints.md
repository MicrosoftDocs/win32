---
description: The ENTRYPOINTS structure defines the entry points to the export functions that Network Monitor uses to operate the parser.
ms.assetid: e2ac118d-e04b-489f-877f-84cc9888f8af
title: ENTRYPOINTS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ENTRYPOINTS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# ENTRYPOINTS structure

The **ENTRYPOINTS** structure defines the entry points to the export functions that Network Monitor uses to operate the parser.

## Syntax


```C++
typedef struct __ENTRYPOINTS {
  REGISTER         Register;
  DEREGISTER       Deregister;
  RECOGNIZEFRAME   RecognizeFrame;
  ATTACHPROPERTIES AttachProperties;
  FORMATPROPERTIES FormatProperties;
} ENTRYPOINTS, *LPENTRYPOINTS;
```



## Members

<dl> <dt>

**Register**
</dt> <dd>

Pointer to the implementation of the [*Register expert*](register-expert.md) function.

</dd> <dt>

**Deregister**
</dt> <dd>

Pointer to the implementation of the [**Deregister**](deregister.md) function.

</dd> <dt>

**RecognizeFrame**
</dt> <dd>

Pointer to the implementation of the [**RecognizeFrame**](recognizeframe.md) export function.

</dd> <dt>

**AttachProperties**
</dt> <dd>

Pointer to the implementation of the [**AttachProperties**](attachproperties.md) export function.

</dd> <dt>

**FormatProperties**
</dt> <dd>

Pointer to the implementation of the [**FormatProperties**](formatproperties.md) export function.

</dd> </dl>

## Remarks

The **CreateProtocol** function uses the **ENTRYPOINTS** structure to provide pointers to Network Monitor. The pointers must be specified in the order identified in the previous Members section.

The [**FormatProperties**](formatproperties.md) function does not need to be implemented if Network Monitor will never display the protocol data. For example, **FormatProperties** does not need to be implemented if an export application uses the output from the parser, and Network Monitor does not display the output.



| For information on                                        | See                                                     |
|-----------------------------------------------------------|---------------------------------------------------------|
| What parsers are, and how they work with Network Monitor. | [Parsers](parsers.md)                                  |
| How to implement **DllMain**  includes an example.        | [Implementing DllMain](implementing-dllmain-parser.md) |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[AttachProperties](attachproperties.md)
</dt> <dt>

[CreateProtocol](createprotocol.md)
</dt> <dt>

[Deregister](deregister.md)
</dt> <dt>

[FormatProperties](formatproperties.md)
</dt> <dt>

[RecognizeFrame](recognizeframe.md)
</dt> <dt>

[Register](register-parser.md)
</dt> </dl>

 

 




