---
Description: 'Note  This interface is no longer supported by the AVI Splitter. Note  It was defined to support certain older hardware decoders that required AVI files to be read directly into hardware memory.'
ms.assetid: '9945bffb-6748-4c7d-ba14-91470cf6c651'
title: IAMDevMemoryControl interface
---

# IAMDevMemoryControl interface

> [!Note]  
> This interface is no longer supported by the AVI Splitter.

 

> [!Note]  
> It was defined to support certain older hardware decoders that required AVI files to be read directly into hardware memory. The interface enables the AVI parser to allocate memory from the downstream filter but still provide its own allocator. There should be no need for any newer devices to support this interface.

 

A device memory control object supports `IAMDevMemoryControl`. This object is aggregated with an [**IMemAllocator**](imemallocator.md) object that is used in the connection. Typically, filters will call the [**IAMDevMemoryAllocator::GetDevMemoryObject**](iamdevmemoryallocator-getdevmemoryobject.md) method to obtain a pointer to this interface.

Implement this interface with the [**IAMDevMemoryAllocator**](iamdevmemoryallocator.md) interface when pins need to have greater control of memory allocation.

Use this interface to synchronize the completion of writing data to a memory allocator, and to get the device ID of the on-board memory allocator.

## Members

The **IAMDevMemoryControl** interface inherits from the [**IUnknown**](com.iunknown) interface. **IAMDevMemoryControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMDevMemoryControl** interface has these methods.



| Method                                                       | Description                                                                                                                                                                    |
|:-------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetDevId**](iamdevmemorycontrol-getdevid.md)             | Retrieves the device ID of the on-board memory allocator.<br/>                                                                                                           |
| [**QueryWriteSync**](iamdevmemorycontrol-querywritesync.md) | Checks if the memory supported by the allocator requires the use of the **WriteSync** method.<br/>                                                                       |
| [**WriteSync**](iamdevmemorycontrol-writesync.md)           | Used to synchronize with the completed write operation by returning when any data being written to the specified allocator region is fully written into the memory.<br/> |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




