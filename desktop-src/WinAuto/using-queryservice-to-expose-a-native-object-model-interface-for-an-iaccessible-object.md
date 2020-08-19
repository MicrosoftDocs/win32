---
title: Use QueryService to retrieve a native interface for an IAccessible object
description: Server developers can use this technique to expose a pointer to a custom document node for an IAccessible object. This assumes that you already expose IAccessible objects. This technique allows clients to get a custom object from an IAccessible object.
ms.assetid: aaa0e840-f8c2-4f3d-9d97-1910f00c1041
ms.topic: article
ms.date: 05/31/2018
---

# Use QueryService to retrieve a native interface for an IAccessible object

Server developers can use this technique to expose a pointer to a custom document node for an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object. This assumes that you already expose **IAccessible** objects. This technique allows clients to get a custom object from an **IAccessible** object.

**To expose a native object model for an IAccessible (servers)**

1.  Add support for the **IServiceProvider** interface on your [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object.
2.  Define a GUID that represents the functionality of obtaining the custom interface from an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) objects. This is called a service ID. You can use GUIDGEN.EXE to generate a service ID, or reuse the interface ID if you have a custom interface.
3.  Implement the **IServiceProvider::QueryService** method so that it returns a pointer to the custom interface when called with the service ID defined earlier in this procedure. **QueryService** should return **NULL** for all other service ID values.
4.  Publish the service ID so that clients can use it.

Clients can use this functionality to obtain a pointer to the custom object from an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object.

**To obtain a pointer to a custom object from an IAccessible (clients)**

1.  Call [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q))(IID\_IServiceProvider) on an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer to obtain an **IServiceProvider** interface pointer.
2.  Call **IServiceProvider::QueryService** with the published service ID to obtain a pointer to the custom object for the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible).
3.  Release the **IServiceProvider** interface if it is no longer needed.

To be usable across processes, servers might need to register the returned interface with Component Object Model (COM).

This technique is used by Microsoft Internet Explorer 4.0 and later. It allows clients to obtain an **IHTMLElement2** interface pointer that corresponds to an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object.

 

 