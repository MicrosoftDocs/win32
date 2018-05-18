---
title: Components Object
description: Components Object
ms.assetid: '6d779095-12f9-4e00-a25f-0a840f5149fa'
---

# Components Object

The **Components** object represents a collection of components.



|                           |                                    |
|---------------------------|------------------------------------|
| Interfaces                | [**IComponents**](icomponents.md) |
| Outgoing Event Interfaces | None                               |
| CLSID                     | Not applicable                     |



 

## Remarks

Each tune request has a **Components** collection. The collection contains zero or more [Component](component-object.md) objects, each of which describes a stream in the program.

Component information may be filled in when the Guide Store Loader initially creates the tune request, or it may not be known until the program stream is being captured by the hardware and the Transport Information Filter (TIF) has examined the PSI tables. In either case, after a tune request has been submitted, the components collection is updated by the TIF. An application can examine the tune request after submitting it, to discover possible additional information about the program stream.

To get a **Components** object, call the [**ITuneRequest::get\_Components**](itunerequest-get-components.md) method on a tune request. The **Components** object cannot be created with **CoCreateInstance**.

## Related topics

<dl> <dt>

[Components](components.md)
</dt> <dt>

[Tuning Model Objects](tuning-model-objects.md)
</dt> </dl>

 

 




