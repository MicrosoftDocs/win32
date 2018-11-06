---
title: Using Serialization Services
description: MIDL generates a serialization stub for the procedure with the attributes \ encode\ and \ decode\ .
ms.assetid: b1fce133-32e3-4b5e-9f9d-ffbe60e9d9cd
keywords:
- Remote Procedure Call RPC , tasks, using serialization services
ms.topic: article
ms.date: 05/31/2018
---

# Using Serialization Services

MIDL generates a serialization stub for the procedure with the attributes \[[**encode**](https://msdn.microsoft.com/library/windows/desktop/aa366812)\] and \[[**decode**](https://msdn.microsoft.com/library/windows/desktop/aa366784)\]. When you call this routine, you execute a serialization call instead of a remote call. The procedure arguments are marshaled to or unmarshaled from a buffer in the usual way. You then have complete control of the buffers.

In contrast, when your program performs type serialization (a type is labeled with serialization attributes), MIDL generates routines to size, encode, and decode objects of that type. To serialize data, you must call these routines in the appropriate way. Type serialization is a Microsoft extension and, as such, is not available when you compile in DCE-compatibility ([**/osf**](https://msdn.microsoft.com/library/windows/desktop/aa367357)) mode. By using the \[[**encode**](https://msdn.microsoft.com/library/windows/desktop/aa366812)\] and \[[**decode**](https://msdn.microsoft.com/library/windows/desktop/aa366784)\] attributes as interface attributes, RPC applies encoding to all the types and routines defined in the IDL file.

You must supply adequately aligned buffers when using serialization services. The beginning of the buffer must be aligned at an address that is a multiple of 8, or 8-byte aligned. For procedure serialization, each procedure call must marshal into or unmarshal from a buffer position that is 8-byte aligned. For type serialization, sizing, encoding, and decoding must start at a position that is 8-byte aligned.

One way for your application to ensure that its buffers are aligned is to write the [**midl\_user\_allocate**](https://msdn.microsoft.com/library/windows/desktop/aa367095) function such that it creates aligned buffers. The following code sample demonstrates how this can be done.


```C++
#include <windows.h>

#define ALIGN_TO8(p)   (char *)((unsigned long)((char *)p + 7) & ~7)

void __RPC_FAR *__RPC_USER  MIDL_user_allocate(size_t sizeInBytes)
{
    unsigned char *pcAllocated;
    unsigned char *pcUserPtr;

    pcAllocated = (unsigned char *) malloc( sizeInBytes + 15 );
    pcUserPtr =  ALIGN_TO8( pcAllocated );
    if ( pcUserPtr == pcAllocated )
        pcUserPtr = pcAllocated + 8;

    *(pcUserPtr - 1) = pcUserPtr - pcAllocated;

    return( pcUserPtr );
}
```



The following example shows the corresponding [**midl\_user\_free**](https://msdn.microsoft.com/library/windows/desktop/aa367096) function.


```C++
void __RPC_USER  MIDL_user_free(void __RPC_FAR *f)
{
    unsigned char * pcAllocated;
    unsigned char * pcUserPtr;

    pcUserPtr = (unsigned char *) f;
    pcAllocated = pcUserPtr - *(pcUserPtr - 1);

    free( pcAllocated );
}
```



 

 




