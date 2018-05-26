---
title: The ACF Header
description: The ACF header contains platform-specific attributes that apply to the interface as a whole. Attributes applied to individual types and functions in the ACF body override the attributes in the ACF header. No attributes are required in the ACF header.
ms.assetid: c09ec0f2-2302-450a-b74b-c9008beca325
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The ACF Header

The ACF header contains platform-specific attributes that apply to the interface as a whole. Attributes applied to individual types and functions in the ACF body override the attributes in the ACF header. No attributes are required in the ACF header.

The ACF header can include one of the following attributes: **\[**[**auto\_handle**](https://msdn.microsoft.com/library/windows/desktop/aa366736)**\]**, **\[**[**implicit\_handle**](https://msdn.microsoft.com/library/windows/desktop/aa367046)**\]**, or [**explicit\_handle**](https://msdn.microsoft.com/library/windows/desktop/aa366825)**\]**. If **\[auto\_handle\]** or **\[implicit\_handle\]** is used, it specifies the type of binding handle that will be used for binding when a remote function does not have an explicit binding-handle parameter. When the ACF is not present or does not specify an automatic, implicit, or explicit binding handle, MIDL uses **\[auto\_handle\]** for implicit binding.

Either **\[**[**code**](https://msdn.microsoft.com/library/windows/desktop/aa366752)**\]** or **\[**[**nocode**](https://msdn.microsoft.com/library/windows/desktop/aa367116)**\]** can appear in the interface header, but the one you choose can appear only once. When neither attribute is present, the compiler uses **\[code\]** as a default.

For more information, see [ACF Attributes](https://msdn.microsoft.com/library/windows/desktop/aa366717).

 

 




