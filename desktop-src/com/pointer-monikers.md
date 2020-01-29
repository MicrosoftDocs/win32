---
title: Pointer Monikers
description: A pointer moniker identifies an object that can exist only in the active or running state. This differs from other classes of monikers, which identify objects that can exist in either the passive or the active state.
ms.assetid: 9895f03d-7110-41c1-a934-87010f9ad380
ms.topic: article
ms.date: 05/31/2018
---

# Pointer Monikers

A *pointer moniker* identifies an object that can exist only in the active or running state. This differs from other classes of monikers, which identify objects that can exist in either the passive or the active state.

Suppose, for example, an application has an object that has no persistent representation. Normally, if a client of your application needs access to that object, you could simply pass the client a pointer to the object. However, suppose your client is expecting a moniker. The object cannot be identified with a file moniker, because it isn't stored in a file, nor with an item moniker, because it isn't contained in another object.

Instead, your application can create a pointer moniker, which is a moniker that simply contains a pointer internally, and pass that to the client. The client can treat this moniker like any other. However, when the client calls [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) on the pointer moniker, the moniker code does not check the running object table (ROT) or load anything from storage. Instead, the moniker code simply calls [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) on the pointer stored inside the moniker.

Pointer monikers allow objects that exist only in the active or running state to participate in moniker operations and be used by moniker clients. One important difference between pointer monikers and other classes of monikers is that pointer monikers cannot be saved to persistent storage. If you do, calling the [**IMoniker::Save**](/windows/desktop/api/ObjIdl/nf-objidl-ipersiststream-save) method returns an error. This means that pointer monikers are useful only in specialized situations. You can use the [**CreatePointerMoniker**](/windows/desktop/api/Objbase/nf-objbase-createpointermoniker) function if you need to use a pointer moniker.

## Related topics

<dl> <dt>

[Anti-Monikers](anti-monikers.md)
</dt> <dt>

[Class Monikers](class-monikers.md)
</dt> <dt>

[Composite Monikers](composite-monikers.md)
</dt> <dt>

[File Monikers](file-monikers.md)
</dt> <dt>

[Item Monikers](item-monikers.md)
</dt> </dl>

 

 




