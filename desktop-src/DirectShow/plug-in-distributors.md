---
Description: Plug-in Distributors
ms.assetid: 80ff713d-f704-40d3-9317-cbf33d932207
title: Plug-in Distributors
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Plug-in Distributors

Plug-in distributors (PIDs) are a way to extend the functionality of the filter graph manager. A plug-in distributor is a COM object that the filter graph manager aggregates at run time. Applications obtain access to the PID through the filter graph manager.

When the filter graph manager is queried for an interface that it does not support, it searches the registry for a key with the following form:


```C++
HKEY_CLASSES_ROOT\Interface\IID\Distributor
```



`IID` is a string containing the interface identifier. If the registry entry exists, the value of the entry defines the class identifier (CLSID) of a PID that supports the interface. The filter graph manager aggregates the PID and returns an interface pointer, thereby acting as the outer **IUnknown** for the PID. When the application calls methods on the interface, it is actually calling them on the PID. However, the existence of the PID is transparent to the application.

The term *distributor* stems from the fact that a PID can query its outer **IUnknown** pointer for interfaces on the filter graph manager. By calling the [**IFilterGraph::EnumFilters**](/windows/win32/Strmif/nf-strmif-ifiltergraph-enumfilters?branch=master) method, the PID can enumerate the filters in the graph and distribute method calls to those filters. In this way, a PID can serve as a single control point for the application to call methods on filters.

When the filter graph manager aggregates a PID, it queries the PID for the [**IDistributorNotify**](/windows/win32/Strmif/nn-strmif-idistributornotify?branch=master) interface. If the PID supports this interface, the filter graph manager uses it to notify the PID about changes in the graph:

-   When the filter graph switches between run, paused, and stopped states, it calls [**IDistributorNotify::Run**](/windows/win32/Strmif/nf-strmif-idistributornotify-run?branch=master), [**IDistributorNotify::Pause**](/windows/win32/Strmif/nf-strmif-idistributornotify-pause?branch=master), or [**IDistributorNotify::Stop**](/windows/win32/Strmif/nf-strmif-idistributornotify-stop?branch=master).
-   When a reference clock is set, the filter graph manager calls [**IDistributorNotify::SetSyncSource**](/windows/win32/Strmif/nf-strmif-idistributornotify-setsyncsource?branch=master).
-   When filters are added or removed, or pin connections are changed, the filter graph manager calls [**IDistributorNotify::NotifyGraphChange**](/windows/win32/Strmif/nf-strmif-idistributornotify-notifygraphchange?branch=master).

To implement a custom PID, create a COM object that supports aggregation. It must support an interface that the filter graph manager does not already support. Optionally, it can support the **IDistributorNotify** interface.

If the PID obtains any interface pointers from the filter graph manager, it should release them immediately. Otherwise, it might create a circular reference count, which could prevent the filter graph manager from being destroyed. Holding a reference count on the filter graph manager is unnecessary in any case, because the filter graph manager controls the PID's lifetime.

Because a PID is designed specifically for aggregation by the filter graph manager, you might want to enforce this in the PID's constructor method. Check whether the outer **IUnknown** pointer is **NULL**, and if so, return the error code VFW\_E\_NEED\_OWNER. (See [Error and Success Codes](error-and-success-codes.md).) Also, to prevent other objects from aggregating the PID, you can query the outer **IUnknown** pointer for the [**IGraphBuilder**](/windows/win32/Strmif/nn-strmif-igraphbuilder?branch=master) interface. Return an error code if the object does not expose **IGraphBuilder**.

 

 



