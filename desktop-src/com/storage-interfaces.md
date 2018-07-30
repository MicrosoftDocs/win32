---
title: Storage Interfaces
description: Storage Interfaces
ms.assetid: bce0fd46-eeba-4a14-be1f-63d16885c28d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storage Interfaces

Control containers must be able to support controls that implement [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage), [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream), or [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit). Optionally, a container can support any other persistence interfaces such as [**IPersistMemory**](https://msdn.microsoft.com/library/aa768210), [**IPersistPropertyBag**](https://msdn.microsoft.com/library/aa768205), and [**IPersistMoniker**](https://msdn.microsoft.com/library/ms775042(v=VS.85).aspx) for those controls that provide support.

Once an ActiveX control container has chosen and initialized a storage interface to use ([**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage), [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream), [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit), etc), that storage interface will remain the primary storage interface for the lifetime of the control, i.e. the control will remain in possession of the storage. This does not preclude the container from saving to other storage interfaces.

ActiveX control containers do not need to support a save as text mechanism, thus using [**IPersistPropertyBag**](https://msdn.microsoft.com/library/aa768205) and the associated container-side interface [**IPropertyBag**](https://msdn.microsoft.com/library/Aa768196(v=VS.85).aspx) are optional.

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 




