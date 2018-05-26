---
Description: The Deregister export function frees the resources used to create the protocol property database. The parser DLL must implement Deregister.
ms.assetid: 80852aed-07aa-440f-a537-f6cce461292e
title: Deregister callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Deregister callback function

The **Deregister** export function frees the resources used to create the protocol [*property database*](p.md#-netmon-property-database-gly). The parser DLL must implement **Deregister**.

## Syntax


```C++
VOID Deregister(
  _In_ HPROTOCOL hProtocol
);
```



## Parameters

<dl> <dt>

*hProtocol* \[in\]
</dt> <dd>

Handle of the protocol for a specific database.

</dd> </dl>

## Return value

None.

## Remarks

Network Monitor calls **Deregister** after passing all the capture information to the parser DLL. The parser DLL must implement a **Deregister** function for each protocol that the parser supports.

When implementing **Deregister**, the parser DLL must call the [DestroyPropertyDatabase](destroypropertydatabase.md) function to release the [*property database*](p.md#-netmon-property-database-gly) resources.



| For information on                                        | See                                                    |
|-----------------------------------------------------------|--------------------------------------------------------|
| What parsers are, and how they work with Network Monitor. | [Parsers](parsers.md)                                 |
| Which entry points are included in the parser DLL.        | [Parser DLL Architecture](parser-dll-architecture.md) |
| How to implement **Deregister**  includes an example.     | [Implementing Deregister](implementing-deregister.md) |



 

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[DestroyPropertyDatabase](destroypropertydatabase.md)
</dt> </dl>

 

 




