---
title: Storage Interfaces
description: Storage Interfaces
ms.assetid: 'bce0fd46-eeba-4a14-be1f-63d16885c28d'
---

# Storage Interfaces

Control containers must be able to support controls that implement [**IPersistStorage**](ipersiststorage.md), [**IPersistStream**](ipersiststream.md), or [**IPersistStreamInit**](ipersiststreaminit.md). Optionally, a container can support any other persistence interfaces such as [**IPersistMemory**](https://msdn.microsoft.com/library/aa768210), [**IPersistPropertyBag**](https://msdn.microsoft.com/library/aa768205), and [**IPersistMoniker**](_inet_IPersistMoniker_Interface_cpp) for those controls that provide support.

Once an ActiveX control container has chosen and initialized a storage interface to use ([**IPersistStorage**](ipersiststorage.md), [**IPersistStream**](ipersiststream.md), [**IPersistStreamInit**](ipersiststreaminit.md), etc), that storage interface will remain the primary storage interface for the lifetime of the control, i.e. the control will remain in possession of the storage. This does not preclude the container from saving to other storage interfaces.

ActiveX control containers do not need to support a save as text mechanism, thus using [**IPersistPropertyBag**](https://msdn.microsoft.com/library/aa768205) and the associated container-side interface [**IPropertyBag**](_inet_IPropertyBag_Interface_cpp) are optional.

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 




