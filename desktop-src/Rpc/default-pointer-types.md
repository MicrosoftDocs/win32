---
title: Default Pointer Types
description: Pointers are not required to have an explicit attribute description. When an explicit attribute is not provided, the MIDL Compiler uses a default pointer attribute.
ms.assetid: b90619c3-70b4-44f0-ba37-293595281031
ms.topic: article
ms.date: 05/31/2018
---

# Default Pointer Types

Pointers are not required to have an explicit attribute description. When an explicit attribute is not provided, the MIDL Compiler uses a default pointer attribute.

The default cases for unattributed pointers are the following:

-   Top-level pointers that appear in parameter lists default to \[[**ref**](/windows/desktop/Midl/ref)\] pointers.
-   All other pointers default to the type specified by the \[[**pointer\_default**](/windows/desktop/Midl/pointer-default)\] attribute. When no \[**pointer\_default**\] attribute is supplied, these pointers default to the \[ [**unique**](/windows/desktop/Midl/unique) \] attribute when the MIDL compiler is in [Microsoft Extensions](microsoft-rpc-binding-handle-extensions.md) mode or the \[[**ptr**](/windows/desktop/Midl/ptr)\] attribute when the MIDL compiler is in DCE-compatible mode.

When a remote procedure returns a pointer, the return value must be a \[ [**unique**](/windows/desktop/Midl/unique) \] or full (\[ [**ptr**](/windows/desktop/Midl/ptr) \]) pointer.

``` syntax
/* IDL file compiled without /osf */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(1.0),
  pointer_default(ptr)
]
interface MyInterface
{
    typedef long *PLONG;
  
    struct MyCircularList {
        struct MyCircularList *pRight;
        struct MyCircularList *pLeft;
        long Data;
    };

    void Foo1( [in] PLONG p );                   // p is ref
 
    void Foo2( [in] struct MyCircularList *p );  // p is ref, p->pRight and p->pLeft is ptr

    struct MyCircularList *Foo3( void );         // returned pointer is ptr.    
}

[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea46),
  version(1.0)
]
interface MyInterface2
{
    struct MySingleList
       {
       struct MySingleList *pNext;
       long Data;
       };
    void Foo4( [in] struct MySingleList *p );  // p is ref, p->pNext is unique

    struct MySingleList *Foo5( void );         // returned pointer is unique.    
}
```

### Remarks

To ensure unambiguous pointer-attribute behavior, always use explicit pointer attributes when defining a pointer.

It is recommended that **\[**ptr**\]** is used only when pointer aliasing is required.

 

 