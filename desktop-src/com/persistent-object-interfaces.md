---
title: Persistent Object Interfaces
description: A persistent object implements one or more persistent object interfaces.
ms.assetid: '8c8e44e4-f564-4af5-9a8a-ac6883862cae'
---

# Persistent Object Interfaces

A persistent object implements one or more *persistent object interfaces*. Clients use persistent object interfaces to tell those objects when and where to store their state. All persistent object interfaces are derived from [**IPersist**](ipersist.md), so any object that implements any persistent object interface also implements **IPersist**.

The following persistent object interfaces are currently defined:

-   [**IPersistStream**](ipersiststream.md)
-   [**IPersistStreamInit**](ipersiststreaminit.md)
-   [**IPersistStorage**](ipersiststorage.md)
-   [**IPersistFile**](ipersistfile.md)
-   [**IPersistMoniker**](_inet_IPersistMoniker_Interface_cpp)
-   [IPersistMemory](http://go.microsoft.com/fwlink/p/?linkid=103818)
-   [IPersistPropertyBag](http://go.microsoft.com/fwlink/p/?linkid=103820)

Implementers choose which persistent object interfaces an object supports depending on how the object is to be used. By not supporting any persistent object interfaces, the implementer is effectively saying, "This object's state cannot be persistently stored." By supporting one or more persistent object interfaces, the implementer is effectively saying, "This object's state can be persistently stored in one or more data store mediums."

For example, the following table lists several object types that allow support for different persistent object interfaces.



| Category                            | Persistent object interfaces typically supported                                                                                                                                                         |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Monikers<br/>                 | [**IPersistStream**](ipersiststream.md)<br/>                                                                                                                                                      |
| OLE embeddable objects<br/>   | [**IPersistStorage**](ipersiststorage.md), [**IPersistFile**](ipersistfile.md)<br/>                                                                                                              |
| ActiveX controls<br/>         | [**IPersistStreamInit**](ipersiststreaminit.md), [**IPersistStorage**](ipersiststorage.md), IPersistMemory, IPersistPropertyBag, [**IPersistMoniker**](_inet_IPersistMoniker_Interface_cpp)<br/> |
| ActiveX document objects<br/> | [**IPersistStorage**](ipersiststorage.md), [**IPersistFile**](ipersistfile.md)<br/>                                                                                                              |



 

Client implementers can also choose which persistent object interfaces the client can use. The interfaces a client uses is usually determined by where the client can store its own data. A client that can store its data only in a flat file will probably use only [**IPersistStreamInit**](ipersiststreaminit.md), [**IPersistMoniker**](_inet_IPersistMoniker_Interface_cpp), and IPersistPropertyBag. (**IPersistStreamInit** can replace [**IPersistStream**](ipersiststream.md) in most applications, because it contains that definition and adds an initialization method.) A client that can save its data to a structured storage file will, in addition, use [**IPersistStorage**](ipersiststorage.md).

## Related topics

<dl> <dt>

[Initializing Persistent Objects](initializing-persistent-objects.md)
</dt> </dl>

 

 





