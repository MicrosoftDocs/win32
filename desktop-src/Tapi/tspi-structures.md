---
description: The data structures TSPI uses are identical to those defined in TAPI Structures, with the exception of TUISPICREATEDIALOGINSTANCEPARAMS.
ms.assetid: 99d966ea-49b5-4a84-83a1-99dc8465c751
title: TSPI Structures
ms.topic: article
ms.date: 05/31/2018
---

# TSPI Structures

The data structures TSPI uses are identical to those defined in [TAPI Structures](./tapi-structures.md), with the exception of [**TUISPICREATEDIALOGINSTANCEPARAMS**](/windows/win32/api/tspi/ns-tspi-tuispicreatedialoginstanceparams).

In the case of most of the larger data structures, the responsibility for filling in members is divided between the service provider and TAPI. The service provider must preserve the values present in members owned by TAPI. The description of which members must be set by the service provider and which must be preserved is provided in the Functions section in the functions that refer to that data structure.

For each structure, the reference section lists the following items:

-   The purpose of the structure
-   A description of the values or fields
-   A description of the structure's extensibility
-   Optional comments about using the structure
-   Optional references to other functions, messages, constants, or structures.

Memory for all data structures whose representation is published and shared by both TAPI and the service provider is allocated by TAPI or an application using TAPI. TAPI passes a pointer to the TSPI function that returns the information. TSPI fills the data structure with the requested information. If the operation is asynchronous, the information is not available until the asynchronous reply callback indicates success.

> [!Note]  
> Some structures include Size and Offset fields for defining the location and length of strings in the variable portion of the structure. If the service provider is requested to add a string but no string is available, the service provider must indicate this condition in one of these ways:
>
> -   Set both the Size and Offset fields to 0.
> -   Set the Offset field to nonzero but Size to 0.
> -   Set the Offset field to nonzero, Size to 1, and the byte at the Offset to 0.

 

 

 
