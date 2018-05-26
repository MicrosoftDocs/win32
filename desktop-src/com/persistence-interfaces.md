---
title: Persistence Interfaces
description: Persistence Interfaces
ms.assetid: a93582b3-bdbf-430d-b4a6-c0df7bc35dc0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Persistence Interfaces

Objects that have a persistent state of any kind must implement at least one IPersist\* interface, and preferably multiple interfaces, in order to provide the container with the most flexible choice of how it wishes to save a control's state.

If a control has any persistent state whatsoever, it must, as a minimum, implement either [**IPersistStream**](/windows/win32/ObjIdl/nn-objidl-ipersiststream?branch=master) or [**IPersistStreamInit**](/windows/win32/OCIdl/nn-ocidl-ipersiststreaminit?branch=master) (the two are mutually exclusive and shouldn't be implemented together for the most part). The latter is used when a control wishes to know when it is created new as opposed to reloaded from an existing persistent state (**IPersistStream** does not have the created new capability). The existence of either interface indicates that the control can save and load its persistent state into a stream, that is, an instance of [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034).

Beyond these two stream-based interfaces, the IPersist\* interfaces listed in the following table can be optionally provided in order to support persistence to locations other than an expandable [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034).

A set of component categories is identified to cover the support for persistency interfaces see [Component Categories](component-categories.md).



| Interface                                                              | Usage                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPersistMemory**](https://msdn.microsoft.com/library/aa768210)<br/>           | The object can save and load its state into a fixed-length sequential byte array (in memory).<br/>                                                                                                                                                                                                                                                    |
| [**IPersistStorage**](/windows/win32/ObjIdl/nn-objidl-ipersiststorage?branch=master)<br/>                  | The object can save and load its state into an [**IStorage**](https://msdn.microsoft.com/library/windows/desktop/aa380015) instance. Controls that wish to be marked Insertable as other compound document objects (for insertion into non-control aware containers) must support this interface.<br/>                                                                                               |
| [**IPersistPropertyBag**](https://msdn.microsoft.com/library/aa768205)<br/> | The object can save and load its state as individual properties written to IPropertyBag which the container implements. This is used for Save As Text functionality in some containers.<br/>                                                                                                                                                          |
| [**IPersistMoniker**](_inet_IPersistMoniker_Interface_cpp)<br/>  | The object can save and load its state to a location named by a moniker. The control calls [**IMoniker::BindToStorage**](/windows/win32/ObjIdl/nf-objidl-imoniker-bindtostorage?branch=master) to retrieve the storage interface it requires, such as [**IStorage**](https://msdn.microsoft.com/library/windows/desktop/aa380015), [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034), [**ILockBytes**](https://msdn.microsoft.com/library/windows/desktop/aa379238), [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master), etc.<br/> |



 

While support for [**IPersistPropertyBag**](https://msdn.microsoft.com/library/aa768205) is optional, it is strongly recommended as an optimization for containers with Save As Text features, such as Visual Basic.

With the exception of [**IPersistStream::GetSizeMax**](/windows/win32/ObjIdl/nf-objidl-ipersiststream-getsizemax?branch=master), [**IPersistStreamInit::GetSizeMax**](/windows/win32/OCIdl/nf-ocidl-ipersiststreaminit-getsizemax?branch=master), and [**IPersistMemory::GetSizeMax**](_inet_IPersistMemory_GetSizeMax_Method), all methods of each interface must be fully implemented.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 





