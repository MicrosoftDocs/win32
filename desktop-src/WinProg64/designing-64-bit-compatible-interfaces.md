---
title: Designing 64-bit-Compatible Interfaces
description: Backward compatibility issues arise when you add new data types or methods to an interface, change old data types, or use data types inappropriately.
ms.assetid: 676affd8-a155-4ac2-9647-0c7352c87a31
keywords:
- backward compatibility 64-bit Windows Programming
- 64-bit-compatible interfaces 64-bit Windows Programming
- 64-bit Windows programming guide 64-bit Windows Programming , compatibility
- compatibility 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Designing 64-bit-Compatible Interfaces

Porting from 32-bit Windows to 64-bit Windows should not, by itself, create any problems for distributed applications, whether they use Remote Procedure Calls (RPC) directly or through DCOM. The RPC programming model specifies well-defined data sizes and integer types that are the same size on each end of the connection. Also, in the LLP64 abstract data model developed for 64-bit Windows, only the pointers expand to 64 bits—all other integer data types remain 32 bits. Because pointers are local to each side of the client/server connection and are usually transmitted as **NULL** or non-**NULL** markers, the marshaling engine can handle different pointer sizes on either end of a connection transparently.

However, backward compatibility issues arise when you add new data types or methods to an interface, change old data types, or use data types inappropriately. The following topics discuss how to avoid these situations (when possible) and how to design robust workarounds when it is not possible to avoid them.

## In this Section

-   [Changing an Existing Interface](changing-an-existing-interface.md)
-   [Avoiding Information Hiding](avoiding-information-hiding.md)
-   [Avoiding Polymorphism](avoiding-polymorphism.md)
-   [Using New Data Types in Your IDL File](using-new-data-types-in-your-idl-file.md)
-   [Preparing Your Application for 64-bit Windows](preparing-your-application-for-64-bit-windows.md)

## Related Sections

If you are not already familiar with the new data types, working environment, and API changes for 64-bit Windows, see [Getting Ready for 64-bit Windows](getting-ready-for-64-bit-windows.md).

 

 




