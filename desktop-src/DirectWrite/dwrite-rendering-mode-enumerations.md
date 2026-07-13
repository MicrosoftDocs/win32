---
title: DWRITE_RENDERING_MODE enumerations
description: Starting in Windows 8, the DWRITE\_RENDERING\_MODE enumeration added new enumeration values and deprecated others.
ms.assetid: 3EA568B4-310D-4F70-9530-5916419282E5
ms.topic: reference
ms.date: 05/31/2018
---

# DWRITE\_RENDERING\_MODE enumerations

Starting in Windows 8, the **DWRITE\_RENDERING\_MODE** enumeration added new enumeration values and deprecated others.

Starting in Windows 8, the [**DWRITE\_TEXT\_ANTIALIAS\_MODE**](/windows/win32/api/Dwrite_1/ne-dwrite_1-dwrite_text_antialias_mode) enumeration determines whether text is rendered using ClearType. As a result, all the ClearType rendering modes in the **DWRITE\_RENDERING\_MODE** enumeration are deprecated. These enumeration values now map to new rendering modes.

The table here shows the old enumeration values and the new values they are mapped to. For descriptions of the new values, see [**DWRITE\_RENDERING\_MODE**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode).



| Old mode                                                                                | New mode                                                                                |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_GDI\_CLASSIC**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)       | [**DWRITE\_RENDERING\_MODE\_GDI\_CLASSIC**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)                  |
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_GDI\_NATURAL**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)       | [**DWRITE\_RENDERING\_MODE\_GDI\_NATURAL**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)                  |
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)            | [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)            |
| [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL\_SYMMETRIC**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode) | [**DWRITE\_RENDERING\_MODE\_CLEARTYPE\_NATURAL\_SYMMETRIC**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode) |



 

## In this section




| Topic | Description | 
|-------|-------------|
| [**DWRITE_RENDERING_MODE (Windows 8 and later)**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)<br> | Represents a method of rendering glyphs. <br> **Note:** This topic is about [**DWRITE_RENDERING_MODE**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode) in Windows 8 and later. For info on the previous version see [**this topic**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode).<br> | 
| [**DWRITE_RENDERING_MODE**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode)<br> | Represents a method of rendering glyphs. <br> **Note:** This topic is about [**DWRITE_RENDERING_MODE**](/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode) previous to Windows 8 and later. For info on the newer version see **this topic**.<br> | 




 

 

 





