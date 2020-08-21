---
title: Implicit vs. Explicit Handles
description: To declare a serialization handle, use the primitive handle type handle\_t.
ms.assetid: 70d8665f-d793-46fc-bcbf-ecb24e746786
ms.topic: article
ms.date: 05/31/2018
---

# Implicit vs. Explicit Handles

To declare a serialization handle, use the primitive handle type [**handle\_t**](/windows/desktop/Midl/handle-t). Serialization handles can be explicit or implicit. Specify implicit handles in your application's ACF by using the **\[implicit\_handle\]** attribute. The MIDL compiler will generate a global serialization handle variable. Serialization procedures with an implicit handle use this global variable in order to access a valid serializing context.

When using type encoding, the generated routines supporting serialization of a particular type use the global implicit handle to access the serialization context. Note that remote routines may need to use the implicit handle as a binding handle. Be sure that the implicit handle is set to a valid serializing handle prior to making a serializing call.

An explicit handle is specified as a parameter of the serialization procedure prototype in the IDL file, or it can also be specified by using the **\[explicit\_handle\]** attribute in the ACF. The explicit handle parameter is used to establish the proper serialization context for the procedure. To establish the correct context in the case of type serialization, the compiler generates the supporting routines that use explicit [**handle\_t**](/windows/desktop/Midl/handle-t) parameter as the serialization handle. You must supply a valid serializing handle when calling a serialization procedure or serialization type support routine.

 

 