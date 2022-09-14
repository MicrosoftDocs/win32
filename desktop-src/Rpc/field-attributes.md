---
title: Field Attributes
description: Field attributes (attributes applied to fields of an array, structure, union, or character array) and Remote Procedure Call (RPC).
ms.assetid: 4508479d-ff0a-4698-94aa-588837032067
ms.topic: article
ms.date: 05/31/2018
---

# Field Attributes

Field attributes are the attributes that can be applied to fields of an array, structure, union, or character array:

-   **\[**[**ignore**](/windows/desktop/Midl/ignore)**\]**, **\[**[**size\_is**](/windows/desktop/Midl/size-is)**\]**
-   **\[**[**max\_is**](/windows/desktop/Midl/max-is)**\]**
-   **\[**[**length\_is**](/windows/desktop/Midl/length-is)**\]**
-   **\[**[**first\_is**](/windows/desktop/Midl/first-is)**\]**
-   **\[**[**last\_is**](/windows/desktop/Midl/last-is)**\]**
-   **\[**[**switch\_is**](/windows/desktop/Midl/switch-is)**\]**
-   **\[**[**string**](/windows/desktop/Midl/string)**\]**
-   [pointer attributes](three-pointer-types.md)

For example, field attributes are used in conjunction with array declarations to specify either the size of the array or the portion of the array that contains valid data. This is done by associating another parameter, structure field, or a constant expression with the array.

The **\[**[**ignore**](/windows/desktop/Midl/ignore)**\]** attribute designates pointer fields to be ignored during the marshaling process. Such an ignored field is set to **NULL** on the receiver side.

MIDL provides *conformant*, *varying*, and *open* arrays. An array is called conformant if its bounds are determined at run time. The **\[**[**size\_is**](/windows/desktop/Midl/size-is)**\]** attribute designates the upper bound on the allocation size of the array and the **\[**[**max\_is**](/windows/desktop/Midl/max-is)**\]** attribute designates the upper bound on the value of a valid array index. For more information, see **\[**[**arrays**](arrays.md)**\]**.

An array is called varying if its bounds are determined at compile time, but the range of transmitted elements is determined at run time. An open array (also called a conformant varying array) is an array whose upper bound and range of transmitted elements are determined at run time. To determine the range of transmitted elements of an array, the array declaration must include a **\[**[**length\_is**](/windows/desktop/Midl/length-is)**\]**, **\[**[**first\_is**](/windows/desktop/Midl/first-is)**\]**, or **\[**[**last\_is**](/windows/desktop/Midl/last-is)**\]** attribute.

The **\[length\_is\]** attribute designates the number of array elements to be transmitted and the **\[first\_is\]** attribute designates the index of the first array element to be transmitted. The **\[last\_is\]** attribute designates the index of the last array element to be transmitted.

The **\[**[**switch\_is**](/windows/desktop/Midl/switch-is)**\]** field attribute designates a union discriminator. When the union is a procedure parameter, the union discriminator must be another parameter of the same procedure. When the union is a field of a structure, the discriminator must be another field of the structure at the same level as the union field. The discriminator must be a [**Boolean**](/windows/desktop/Midl/boolean), [**char**](/windows/desktop/Midl/char-idl), [**int**](/windows/desktop/Midl/int), or [**enum**](/windows/desktop/Midl/enum) type, or a type that resolves to one of these types. For more information, see [Nonencapsulated Unions](/windows/desktop/Midl/nonencapsulated-unions) and **\[switch\_is\]**.

The **\[**[**string**](/windows/desktop/Midl/string)**\]** field attribute designates that a one-dimensional character or byte array, or a pointer to a zero-terminated character or byte stream, is to be treated as a string. The string attribute applies only to one-dimensional arrays and pointers. The element type is limited to [**char**](/windows/desktop/Midl/char-idl), [**byte**](/windows/desktop/Midl/byte), [**wchar\_t**](/windows/desktop/Midl/wchar-t), or a named type that resolves to one of these types.

For information about the context in which field attributes appear, see [MIDL Arrays](/windows/desktop/Midl/midl-arrays), [MIDL Structures](/windows/desktop/Midl/midl-structures), and [MIDL Unions](/windows/desktop/Midl/midl-unions).

 

 