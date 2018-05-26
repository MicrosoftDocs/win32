---
title: Media-Type Negotiation
description: Many application-layer Internet protocols are based on the exchange of messages in a simple, flexible format called Multipurpose Internet Mail Extensions (MIME).
ms.assetid: 7a2c9d8f-639a-4865-a62b-63330175f5f0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Media-Type Negotiation

Many application-layer Internet protocols are based on the exchange of messages in a simple, flexible format called Multipurpose Internet Mail Extensions (MIME). Although MIME originated as a standard for exchanging electronic mail messages, it is used today by a wide variety of applications to specify mutually understood data formats as MIME, or media, types. The process is called *media-type negotiation*.

Media types are simple strings that denote a type and subtype (such as "text/plain" or "text/HTML"). They are used to label data or qualify a request. A Web browser, for example, as part of an HTTP request-for-data or request-for-info, specifies that it is requesting "image/gif" or "image/jpeg" Media Types, to which a web server responds by returning the appropriate media type and, if the call was a request-for-data, the data itself in the requested format.

Media-type negotiation is often similar to how existing desktop applications negotiate with the system clipboard to determine which data format to paste when a user chooses Edit/Paste or queries for formats when receiving an [**IDataObject**](/windows/win32/ObjIdl/nn-objidl-idataobject?branch=master) pointer during a drag-and-drop operation. The subtle difference in HTTP media-type negotiation is that the client does not know ahead of time which formats the server has available. Therefore, the client specifies up-front the media types it supports, in order of greatest fidelity, and the server responds with the best available format.

URL monikers support media-type negotiation as a way for Internet clients and servers to agree upon formats to be used when downloading data in [**BindToStorage**](/windows/win32/ObjIdl/nf-objidl-imoniker-bindtostorage?branch=master) operations. To support media-type negotiation, a client implements the [**IEnumFORMATETC**](/windows/win32/ObjIdl/nn-objidl-ienumformatetc?branch=master) interface and calls the [**RegisterFormatEnumerator**](_inet_RegisterFormatEnumerator_Function_cpp) function to register it with the bind context. The format enumerator lists the formats the client can accept. A URL moniker translates these formats into media types when binding to HTTP URLs.

The possible media types requested by the client are represented to URL monikers through [**FORMATETC**](/windows/win32/ObjIdl/ns-objidl-tagformatetc?branch=master) structures available from the [**IEnumFORMATETC**](/windows/win32/ObjIdl/nn-objidl-ienumformatetc?branch=master) enumerator registered by the caller on the bind context: Each **FORMATETC** specifies a clipboard format identifying the media type. For example, the following code fragment specifies that the media type is PostScript.

``` syntax
FORMATETC fmtetc;
fmtetc.cfFormat = RegisterClipboardFormat(CF_MIME_POSTSCRIPT);
. . .
```

A client can set the clipboard format to the special media type CF\_NULL to indicate that the default media type of the resource pointed to by the URL should be retrieved. This format is usually the last one in which the client is interested. When no enumerator is registered with the bind context, a URL moniker works as if an enumerator containing a single [**FORMATETC**](/windows/win32/ObjIdl/ns-objidl-tagformatetc?branch=master) with **cfFormat**=CF\_NULL is available, automatically downloading the default media-type.

Whatever media type is to be used, the client is notified of the choice by means of the *pformatetc* argument on its [**IBindStatusCallback::OnDataAvailable**](_inet_IBindStatusCallback_OnDataAvailable_Method) method. The callback occurs within the context of the client's call to [**BindToStorage**](/windows/win32/ObjIdl/nf-objidl-imoniker-bindtostorage?branch=master).

> [!Note]  
> If received content is of an unrecognized media-type, the client automatically calls [**RegisterMediaTypes**](_inet_RegisterMediaTypes_Function_cpp) to register the new type.

 

## Related topics

<dl> <dt>

[URL Monikers](url-monikers.md)
</dt> </dl>

 

 




