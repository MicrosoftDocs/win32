---
title: Anti-Monikers
description: OLE provides an implementation of a special type of moniker called an anti-moniker.
ms.assetid: 3b52d3bd-8375-4463-a0e3-5117fa96a1c1
ms.topic: article
ms.date: 05/31/2018
---

# Anti-Monikers

OLE provides an implementation of a special type of moniker called an *anti-moniker*. You use this moniker in the creation of new moniker classes. You use it as the inverse of the moniker that it is composed onto, effectively canceling that moniker, in much the same way that the ".." operator moves up a directory level in a file system command.

It is necessary to have an anti-moniker available, because once a composite moniker is created, it is not possible to delete parts of the moniker if, for example, an object moves. Instead, you use an anti-moniker to remove one or more entries from a composite moniker.

Anti-monikers are a moniker class explicitly intended for use as an inverse. COM defines the named [**CreateAntiMoniker**](/windows/desktop/api/Objbase/nf-objbase-createantimoniker) function, which returns an anti-moniker. You generally use this function to implement the [**IMoniker::Inverse**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-inverse) method.

An anti-moniker is only an inverse for those types of monikers that are implemented to treat anti-monikers as an inverse. For example, if you want to remove the last piece of a composite moniker, you should not create an anti-moniker and compose it to the end of the composite. You cannot be sure that the last piece of the composite considers an anti-moniker to be its inverse. Instead, you should call [**IMoniker::Enum**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-enum) on the composite moniker, specifying **FALSE** as the first parameter. This creates an enumerator that returns the component monikers in reverse order. Use the enumerator to retrieve the last piece of the composite, and call [**Inverse**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-inverse) on that moniker. The moniker returned by **Inverse** is what you need to remove the last piece of the composite.

## Related topics

<dl> <dt>

[Class Monikers](class-monikers.md)
</dt> <dt>

[Composite Monikers](composite-monikers.md)
</dt> <dt>

[File Monikers](file-monikers.md)
</dt> <dt>

[Item Monikers](item-monikers.md)
</dt> <dt>

[Pointer Monikers](pointer-monikers.md)
</dt> </dl>

 

 




