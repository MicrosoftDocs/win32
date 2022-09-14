---
description: The LockIt class is an internal class that locks and unlocks the DMO.
ms.assetid: f516ce22-17ad-488e-a768-3f3849c56087
title: IMediaObjectImpl::LockIt Class (Dmoimpl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMediaObjectImpl::LockIt Class

The `LockIt` class is an internal class that locks and unlocks the DMO.

``` syntax
LockIt(
    _DERIVED_ *p
);
```

## Parameters

<dl> <dt>

<span id="p"></span><span id="P"></span>*p*
</dt> <dd>

Pointer to the derived object.

</dd> </dl>

## Remarks

The `LockIt` constructor locks the DMO, and the destructor unlocks the DMO. To lock the object from inside your derived class, declare a local variable of type `LockIt`. The DMO is locked while the `LockIt` object remains in scope:


```C++
void SomeMethod()
{
    // The DMO is not locked.
    {
        LockIt dmoLock(this); // Locks the DMO.
        /* ... */
    } 
    // dmoLock goes out of scope, DMO is unlocked.
}
```



The methods in **IMediaObjectImpl** automatically lock the DMO.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dmoimpl.h</dt> </dl>                                                                     |
| Library<br/> | <dl> <dt>Dmoguids.lib; </dt> <dt>Msdmo.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaObjectImpl Class Template**](imediaobjectimpl-class-template.md)
</dt> </dl>

 

 




