---
title: The OLE Component Object Model
description: The OLE Component Object Model
ms.assetid: f3200d81-c2fa-4cc7-bf85-54f6c753a529
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The OLE Component Object Model

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The objects used by the AVIFile library are all part of the OLE Component Object Model. Primarily, this means they share certain methods that make them easier to work with, and the values they return are common to most OLE interface methods.

The OLE Component Object Model of the file and stream handlers uses the OLE **IClassFactory** interface to create instances of their object class. As component objects, they implement the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface, which consists of the [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(refiid_void)), [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release), and [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) methods. The **IUnknown** interface lets an application obtain pointers to other interfaces supported by the same object.

You can determine if an object supports a specific interface by using the **QueryInterface** method. If an object supports a specified interface, **QueryInterface** returns a pointer to that interface.

You can increment and decrement the reference count associated with an object by using the [**AddRef**](/previous-versions//dd757100(v=vs.85)) and [**Release**](/previous-versions//dd757102(v=vs.85)) methods. The reference count lets multiple clients access an object. When an object is used by the first application, its reference count is set to 1. Applications subsequently use the **AddRef** method to increment the count to let the object keep track of the number of times it is accessed.

When an application is done using an object, it calls the **Release** method to decrement the reference count. When the reference count is zero, the object is no longer needed and **Release** frees any resources it uses and destroys the object. Because an object uses internal resources transparent to the application, the object is responsible for freeing them. For example, a file handler might need to close open disk files and free buffer memory when released.

Most OLE interface methods return result handles that are defined by using the **HRESULT** data type. This data type is made of a severity code, contextual information, a facility code, and a status code. A return result handle that indicates success has the value zero. A nonzero value indicates failure and the status code member of the return result handle provides a basis for additional interpretation. For additional information about OLE return result handles, see the *OLE Programmer's Reference*.

 

 