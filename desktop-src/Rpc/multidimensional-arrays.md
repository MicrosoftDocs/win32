---
title: Multidimensional Arrays
description: Array attributes can also be used with multidimensional arrays.
ms.assetid: a01b904c-fbe8-4af4-8393-6864f7ef7364
ms.topic: article
ms.date: 05/31/2018
---

# Multidimensional Arrays

Array attributes can also be used with multidimensional arrays. However, be careful to ensure that every dimension of the array has a corresponding attribute. For example:

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(2.0)
]
interface multiarray
{
  void arr2d( [in] short        d1size,
              [in] short        d2len,
              [in, size_is( d1size, ), length_is ( , d2len) ] long array2d[*][30] ) ;
}
```

The preceding array is a conformant array (of size d1size ) of 30 element arrays (with d2len elements shipped for each). The comma in the parentheses of the \[[**size\_is**](/windows/desktop/Midl/size-is)\] attribute specifies that value in d1size is applied to the first dimension of the array. Likewise, the command in the parentheses of the \[[**length\_is**](/windows/desktop/Midl/length-is)\] attribute indicates that the value in d2len is applied to the second dimension of the array.

The MIDL 2.0 compiler provides two methods for marshaling parameters: mixed-mode (/**Os**) and fully-interpreted (/**Oif** or /**Oicf**). By default, the MIDL compiler compiles interfaces in mixed mode. You do not need to explicitly specify the [**/Os**](/windows/desktop/Midl/-os) switch to get mixed-mode marshaling.

The fully-interpreted method marshals data completely offline. This reduces the size of the stub code considerably, but it also results in decreased performance. In mixed-mode marshaling, the stubs marshals some parameters online. While this results in a larger stub size, it also offers increased performance.

> [!Caution]  
> Exercise caution when compiling IDL files in this mode. Using multidimensional arrays in mixed mode can result in parameters that are not marshaled correctly. The [**/Oicf**](/windows/desktop/Midl/-oi) command line switch is recommended when your interface defines parameters that are multidimensional arrays.

 

The \[[**string**](/windows/desktop/Midl/string)\] attribute can also be used with multidimensional arrays. The attribute applies to the least significant dimension, such as a conformant array of strings. You can also use multidimensional pointer attributes. For example:

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(2.0)
]
interface multiarray
{
  void arr2d([in] short  d1len,
             [in] short  d2len,
             [in] size_is(d1len, d2len) ] long  ** ptr2d) ;
}
```

In the preceding example, the variable ptr2d is a pointer to a d1len-sized block of pointers, each of which points to d2len pointers to **long**.

Multidimensional arrays are not equivalent to arrays of pointers. A multidimensional array is a single, large block of data in memory. An array of pointers only contains a block of pointers in the array. The data that the pointers point to can be anywhere in memory. Also, ANSI C syntax allows only the most significant (leftmost) array dimension to be unspecified in a multidimensional array. Therefore, the following is a valid statement:

`long a1[] [20]`

Compare this to the following invalid statement:

`long a1[20] []`

 

 