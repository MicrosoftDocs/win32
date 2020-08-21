---
title: Persistent Object Interfaces (COM)
description: A persistent object implements one or more persistent object interfaces.
ms.assetid: 8c8e44e4-f564-4af5-9a8a-ac6883862cae
ms.topic: article
ms.date: 05/31/2018
---

# Persistent Object Interfaces

A persistent object implements one or more *persistent object interfaces*. Clients use persistent object interfaces to tell those objects when and where to store their state. All persistent object interfaces are derived from [**IPersist**](/windows/desktop/api/ObjIdl/nn-objidl-ipersist), so any object that implements any persistent object interface also implements **IPersist**.

The following persistent object interfaces are currently defined:

-   [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream)
-   [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit)
-   [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage)
-   [**IPersistFile**](/windows/desktop/api/ObjIdl/nn-objidl-ipersistfile)
-   [**IPersistMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775042(v=vs.85))
-   [IPersistMemory](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768210(v=vs.85))
-   [IPersistPropertyBag](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768210(v=vs.85))

Implementers choose which persistent object interfaces an object supports depending on how the object is to be used. By not supporting any persistent object interfaces, the implementer is effectively saying, "This object's state cannot be persistently stored." By supporting one or more persistent object interfaces, the implementer is effectively saying, "This object's state can be persistently stored in one or more data store mediums."

For example, the following table lists several object types that allow support for different persistent object interfaces.



| Category                            | Persistent object interfaces typically supported                                                                                                                                                         |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Monikers<br/>                 | [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream)<br/>                                                                                                                                                      |
| OLE embeddable objects<br/>   | [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage), [**IPersistFile**](/windows/desktop/api/ObjIdl/nn-objidl-ipersistfile)<br/>                                                                                                              |
| ActiveX controls<br/>         | [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit), [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage), IPersistMemory, IPersistPropertyBag, [**IPersistMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775042(v=vs.85))<br/> |
| ActiveX document objects<br/> | [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage), [**IPersistFile**](/windows/desktop/api/ObjIdl/nn-objidl-ipersistfile)<br/>                                                                                                              |



 

Client implementers can also choose which persistent object interfaces the client can use. The interfaces a client uses is usually determined by where the client can store its own data. A client that can store its data only in a flat file will probably use only [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit), [**IPersistMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775042(v=vs.85)), and IPersistPropertyBag. (**IPersistStreamInit** can replace [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream) in most applications, because it contains that definition and adds an initialization method.) A client that can save its data to a structured storage file will, in addition, use [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage).

## Related topics

<dl> <dt>

[Initializing Persistent Objects](initializing-persistent-objects.md)
</dt> </dl>

 

