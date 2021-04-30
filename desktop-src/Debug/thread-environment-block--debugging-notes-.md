---
description: Thread Environment Block (Debugging Notes)
ms.assetid: 5040CB82-D32F-4C44-8C03-30238D5B897A
title: Thread Environment Block (Debugging Notes)
ms.topic: article
ms.date: 05/31/2018
---

# Thread Environment Block (Debugging Notes)

The Thread Environment Block ([**TEB structure**](/windows/win32/api/winternl/ns-winternl-teb)) holds context information for a thread.

In the following versions of Windows, the offset of the 32-bit TEB address within the 64-bit TEB is 0. This can be used to directly access the 32-bit TEB of a WOW64 thread. This might change in later versions of Windows



|               |                        |
|---------------|------------------------|
| Windows Vista | Windows Server 2008    |
| Windows 7     | Windows Server 2008 R2 |
| Windows 8     | Windows Server 2012    |
| Windows 8.1   | Windows Server 2012 R2 |



 

## Related topics

<dl> <dt>

[Debugging Structures](debugging-structures.md)
</dt> <dt>

[**WOW64\_CONTEXT**](/windows/desktop/api/WinNT/ns-winnt-wow64_context)
</dt> </dl>

 

 
