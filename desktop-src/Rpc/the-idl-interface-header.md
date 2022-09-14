---
title: The IDL Interface Header
description: The IDL interface header specifies information about the interface as a whole. Unlike the ACF, the interface header contains attributes that are platform-independent.
ms.assetid: 667e5228-3ea7-4910-90b9-999e6fd705e9
ms.topic: article
ms.date: 05/31/2018
---

# The IDL Interface Header

The IDL interface header specifies information about the interface as a whole. Unlike the ACF, the interface header contains attributes that are platform-independent.

Attributes in the interface header are global to the entire interface. That is, they apply to the interface and all of its parts. These attributes are enclosed in square brackets at the beginning of the interface definition. An example is shown in the following interface definition:

``` syntax
[
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(1.0)
]
interface INTERFACENAME
{

}
```

Notice that the interface header contains the **\[**[**uuid**](/windows/desktop/Midl/uuid)**\]** and **\[**[**version**](/windows/desktop/Midl/version)**\]** attributes. Since these represent the UUID and version number of the interface respectively, they are attributes of the entire interface.

The interface body can also contain attributes. However, they are not applicable to the entire interface. They refer to specific items in the interface such as remote procedure parameters.

For a complete discussion of the IDL header attributes, see the [MIDL Language Reference](/windows/desktop/Midl/midl-language-reference).

 

 