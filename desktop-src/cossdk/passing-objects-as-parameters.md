---
description: Passing Objects as Parameters
ms.assetid: 174847c8-4545-4f61-ae13-42bdec1405e7
title: Passing Objects as Parameters
ms.topic: article
ms.date: 05/31/2018
---

# Passing Objects as Parameters

The COM+ queued components service does not enable queuing for every existing COM component. There are restrictions on the types of methods that can be queued. Because of messaging constraints, methods must adhere to the following rules:

-   They must contain input parameters only.
-   They must return no application-specific result.

Additionally, there are restrictions on the types of input parameters that can be passed to a queued component. At run time, the queued components service packages the arguments at the client and passes them to the server component by using [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)). Simple types, such as integers and Booleans, can be marshaled easily—more complex types cannot be marshaled without help.

In the case of passing an object through a queued component's method call as a parameter, the client passes the object to the recorder. The recorder marshals the object into a Message Queuing message and passes it to the listener. After the listener picks up the message and passes it to the player, the player must reinstantiate the object to dispatch it to the method call specified by the client. Based on the lifetimes of the client and server in a queued environment, the implication is that these objects must be able to marshal by value. Because COM+ does not provide pass-by-value semantics for standard COM objects, the recorder and player need help from the component to marshal and unmarshal the object.

Object references that support [**IPersistStream**](/windows/desktop/api/objidl/nn-objidl-ipersiststream) can be used as parameters to method calls on queued components. The object cannot make assumptions about when it will be reinstantiated. For example, the server may be unavailable or the server component may not be started until later in the day. Objects that do not support **IPersistStream** will return an error.

## Visual Basic Persistable Objects

Microsoft Visual Basic 6 allows persistable objects to be created. These objects support [**IPersistStream**](/windows/desktop/api/objidl/nn-objidl-ipersiststream) and can be passed as parameters to queued component method calls. Before a Visual Basic object can be passed to a queued component, the persistable object must be initialized. This can be done in one of the following two ways:

-   If the application creating the persistable object is written in Visual Basic, the Visual Basic runtime handles the object initialization automatically.
-   If the application that creates the Visual Basic persistable object is written in a language other than Visual Basic, such as Microsoft Visual C++, the application must explicitly initialize the component by either querying for the persistable object's [**IPersistStream**](/windows/desktop/api/objidl/nn-objidl-ipersiststream) interface or calling the [**IPersistStreamInit::InitNew**](/windows/desktop/api/ocidl/nf-ocidl-ipersiststreaminit-initnew), or [**IPersistStream::Load**](/windows/desktop/api/objidl/nf-objidl-ipersiststream-load) method.

## ADO Recordsets and OLE DB Rowsets

Passing ADO **Recordset** or OLE DB rowset objects between components allows one component to process the results of queries executed by another component. This is helpful when deploying an application across multiple computers. **Recordset** and rowset objects can be passed as method parameters to queued components, with the following restrictions:

-   Server-side **Recordset** objects cannot be marshaled using [**IPersistStream**](/windows/desktop/api/objidl/nn-objidl-ipersiststream). Only client-side **Recordset** objects can be passed as parameters to a queued component method call.
-   If you work directly with OLE DB, the OLE DB rowset must be defined as a client-side rowset.

 

 
