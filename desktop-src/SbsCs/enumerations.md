---
description: Learn about the enumerations that are used in the side-by-side assembly API, such as ASM_CMP_FLAGS and CREATE_ASM_NAME_OBJ_FLAGS.
ms.assetid: e73c37e3-7879-4754-b39c-91be64fc8d73
title: Side-by-Side Assembly Enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Side-by-Side Assembly Enumerations

The side-by-side assembly API uses the following enumerations.



| Enumeration                                                         | Description                                                                                                                                                                                |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ASM\_CMP\_FLAGS**](/windows/win32/api/winsxs/ne-winsxs-asm_cmp_flags)                           | Used by the [**IsEqual**](/windows/desktop/api/winsxs/nf-winsxs-iassemblyname-isequal) method to specify which parts of two assembly names to compare.                                                                       |
| [**ASM\_DISPLAY\_FLAGS**](/windows/win32/api/winsxs/ne-winsxs-asm_display_flags)                   | Used by the [**GetDisplayName**](/windows/desktop/api/winsxs/nf-winsxs-iassemblyname-getdisplayname) method to specify which portions of the side-by-side assembly name to include in the string representation of the name. |
| [**ASM\_NAME**](/windows/win32/api/winsxs/ne-winsxs-asm_name)                                      | Property IDs for the name-value pairs in an side-by-side assembly name.                                                                                                                    |
| [**CREATE\_ASM\_NAME\_OBJ\_FLAGS**](/windows/win32/api/winsxs/ne-winsxs-create_asm_name_obj_flags) | Used by the [**CreateAssemblyNameObject**](/windows/desktop/api/Winsxs/nf-winsxs-createassemblynameobject) function to specify the side-by-side assembly name.                                                               |



 

 

 



