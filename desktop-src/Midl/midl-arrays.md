---
title: MIDL Arrays
description: MIDL arrays.
ms.assetid: dee30788-0575-4b49-a6b8-5208ad295183
keywords:
- data types MIDL , arrays
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Arrays

Array declarators appear in the interface body of the IDL file as one of the following:

-   Part of a general declaration
-   A member of a structure or union declarator
-   A parameter to a remote procedure call

The bounds of each dimension of the array are expressed inside a separate pair of square brackets. An expression that evaluates to *n* signifies a lower bound of zero and an upper bound of *n - 1*. If the square brackets are empty or contain a single asterisk (\*), the lower bound is zero and the upper bound is determined at runtime.

The array can also contain two values separated by an ellipsis that represent the lower and upper bounds of the array, as in \[*lower*...*upper*\]. Microsoft RPC requires a lower bound of zero. The MIDL compiler does not recognize constructs that specify nonzero lower bounds.

Arrays can be associated with the field attributes [**size\_is**](size-is.md), [**max\_is**](max-is.md), [**length\_is**](length-is.md), [**first\_is**](first-is.md), and [**last\_is**](last-is.md) to specify the size of the array or the part of the array that contains valid data. These field attributes identify the parameter, structure field, or constant that specifies the array dimension or index.

The array must be associated with the identifier specified by the field attribute in the following way: When the array is a parameter, the identifier must also be a parameter to the same function; when the array is a structure field, the identifier must be another structure field of that same structure.

An array is called "conformant" if the upper bound of any dimension is determined at runtime. (Only upper bounds can be determined at runtime.) To determine the upper bound, the array declaration must include a [**size\_is**](size-is.md) or [**max\_is**](max-is.md) attribute.

An array is called "varying" when its bounds are determined at compile time, but the range of transmitted elements is determined at runtime. To determine the range of transmitted elements, the array declaration must include a [**length\_is**](length-is.md), [**first\_is**](first-is.md), or [**last\_is**](last-is.md) attribute.

A conformant varying array (also called "open") is an array whose upper bound and range of transmitted elements are determined at runtime. At most, one conformant or conformant varying array can be nested in a C structure and must be the last element of the structure. In contrast, nonconformant varying arrays can occur anywhere in a structure.

## Examples

``` syntax
/* IDL file interface body */ 
#define MAX_INDEX 10 
 
typedef char  ATYPE[MAX_INDEX]; 
typedef short BTYPE[];        // Equivalent to [*]; 
typedef long  CTYPE[*][10];   // [][10] 
typedef float DTYPE[0..10];   // Equivalent to [11] 
typedef float ETYPE[0..(MAX_INDEX)];  
 
typedef struct 
{ 
    unsigned short size; 
    unsigned short length; 
    [size_is(size), length_is(length)] char string[*]; 
} counted_string; 
 
HRESULT MyFunction( 
     [in, out] short * pSize,  
     [in, out, string, size_is(*pSize)] char a[0..*] 
);
```

For more information, see [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers).

## Multidimensional Arrays

The user can declare types that are arrays and then declare arrays of objects of such types. The semantics of *m*-dimensional arrays of *n*-dimensional array types are the same as the semantics of *m*+*n*-dimensional arrays.

For example, the type RECT\_TYPE can be defined as a two-dimensional array and the variable *rect* can be defined as an array of RECT\_TYPE. This is equivalent to the three-dimensional array *equivalent\_rect*:

``` syntax
typedef short int RECT_TYPE[10][20]; 
RECT_TYPE rect[15]; 
short int equivalent_rect[15][10][20];  // ~RECT_TYPE rect[15]
```

Microsoft RPC is C oriented. Following C-language conventions, only the first dimension of a multidimensional array can be determined at runtime. Interoperation with DCE IDL arrays that support other languages is limited to:

-   Multidimensional arrays with constant (compile-time-determined) bounds.
-   Multidimensional arrays with all constant bounds except the first dimension. The upper bound and range of transmitted elements of the first dimension are dependent on runtime.
-   Any one-dimensional arrays with a lower bound of zero.

When the **\[**[**string**](string.md)**\]** attribute is used on multidimensional arrays, the attribute applies to the rightmost array.

## Arrays of Pointers

Reference pointers must point to valid data. The client application must allocate all memory for an **\[**[**in**](in.md)**\]** or **\[** **in,**[**out**](out-idl.md)**\]** array of reference pointers, especially when the array is associated with **\[in\]**, or **\[** **in,out\]**, **\[**[**length\_is**](length-is.md)**\]**, or **\[**[**last\_is**](last-is.md)**\]** values. The client application must also initialize all array elements before the call. Before returning to the client, the server application must verify that all array elements in the transmitted range point to valid storage.

On the server side, the stub allocates storage for all array elements, regardless of the **\[**[**length\_is**](length-is.md)**\]** or **\[**[**last\_is**](last-is.md)**\]** value at the time of the call. This feature can affect the performance of your application.

No restrictions are placed on arrays of unique pointers. On both the client and the server, storage is allocated for null pointers. When pointers are non-null, data is placed in preallocated storage.

An optional pointer declarator can precede the array declarator.

When embedded reference pointers are **\[**[**out**](out-idl.md)**\]**-only parameters, the server-manager code must assign valid values to the array of reference pointers. For example:

``` syntax
typedef [ref] short * ARefPointer;
typedef ARefPointer ArrayOfRef[10];
HRESULT proc1( [out] ArrayOfRef Parameter );
```

The generated stubs allocate the array and assign null values to all pointers embedded in the array.

 

 