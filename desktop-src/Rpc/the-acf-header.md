---
title: The ACF Header
description: The ACF header contains platform-specific attributes that apply to the interface as a whole. Attributes applied to individual types and functions in the ACF body override the attributes in the ACF header. No attributes are required in the ACF header.
ms.assetid: c09ec0f2-2302-450a-b74b-c9008beca325
ms.topic: article
ms.date: 05/31/2018
---

# The ACF Header

The ACF header contains platform-specific attributes that apply to the interface as a whole. Attributes applied to individual types and functions in the ACF body override the attributes in the ACF header. No attributes are required in the ACF header.

The ACF header can include one of the following attributes: **\[**[**auto\_handle**](/windows/desktop/Midl/auto-handle)**\]**, **\[**[**implicit\_handle**](/windows/desktop/Midl/implicit-handle)**\]**, or [**explicit\_handle**](/windows/desktop/Midl/explicit-handle)**\]**. If **\[auto\_handle\]** or **\[implicit\_handle\]** is used, it specifies the type of binding handle that will be used for binding when a remote function does not have an explicit binding-handle parameter. When the ACF is not present or does not specify an automatic, implicit, or explicit binding handle, MIDL uses **\[auto\_handle\]** for implicit binding.

Either **\[**[**code**](/windows/desktop/Midl/code)**\]** or **\[**[**nocode**](/windows/desktop/Midl/nocode)**\]** can appear in the interface header, but the one you choose can appear only once. When neither attribute is present, the compiler uses **\[code\]** as a default.

For more information, see [ACF Attributes](/windows/desktop/Midl/acf-attributes).

 

 