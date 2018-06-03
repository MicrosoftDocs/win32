---
title: GUID Locations in Automation
description: Describes where GUIDs for Automation are located.
ms.assetid: 091b7a1d-a13f-43c4-97ef-b58fd537df4b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GUID Locations in Automation

GUIDs appear in the following locations:

-   **.reg files** — When an application is created, usually one or more .reg files are created. The .reg files contain the GUIDs for the classes that an application exposes. These GUIDs are added to the registry when you run Regedit.exe to register the classes, or when you register type information with [**LoadTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-loadtypelib).

-   **The system registry** — Contains the GUIDs for classes in multiple locations. This is where OLE and applications get information about classes.

-   .[odl](odl.md) files — When objects are described in an Object Description Language (.odl) file, a GUID needs to be provided for each object. Compiling the .odl file with the Microsoft Interface Definition Language (MIDL) compiler places the GUIDs in a type library, which usually exists as a file with a .tlb extension. If a GUID is changed in an .odl file, you should run MIDL again.

-   **.tlb files** — Type libraries describe classes, and this information includes the GUIDs for the classes. The .tlb files can be browsed using the Tlbrowse.exe sample application supplied with OLE.

-   **.h files** — Most application developers will declare class IDs (CLSIDs) for their classes in a header file by using the DEFINE\_GUID macro.

 

 




