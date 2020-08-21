---
title: Compound Documents
description: OLE compound documents enable users working within a single application to manipulate data written in various formats and derived from multiple sources.
ms.assetid: d17dc0dd-3115-4830-8c6b-694a8d1accaa
ms.topic: article
ms.date: 05/31/2018
---

# Compound Documents

OLE compound documents enable users working within a single application to manipulate data written in various formats and derived from multiple sources. For example, a user might insert into a word processing document a graph created in a second application and a sound object created in a third application. Activating the graph causes the second application to load its user interface, or at least that part containing tools necessary to edit the object. Activating the sound object causes the third application to play it. In both cases, a user is able to manipulate data from external sources from within the context of a single document.

OLE compound document technology rests on a foundation consisting of COM, structured storage, and uniform data transfer. As summarized below, each of these core technologies plays a critical role in OLE compound documents:

<dl> <dt>

<span id="COM"></span><span id="com"></span>COM
</dt> <dd>

A compound document object is essentially a COM object that can be embedded in, or linked to, an existing document. As a COM object, a compound document object exposes the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface, through which clients can obtain pointers to its other interfaces, including several, such as [**IOleObject**](/windows/desktop/api/OleIdl/nn-oleidl-ioleobject), [**IOleLink**](/windows/desktop/api/OleIdl/nn-oleidl-iolelink), and [**IViewObject2**](/windows/desktop/api/OleIdl/nn-oleidl-iviewobject2), that provide special features unique to compound document objects.

</dd> <dt>

<span id="Structured_Storage"></span><span id="structured_storage"></span><span id="STRUCTURED_STORAGE"></span>Structured Storage
</dt> <dd>

A compound document object must implement the [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage) or, optionally, [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream) interfaces to manage its own storage. A container used to create compound documents must supply the [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) interface, through which objects store and retrieve data. Containers almost always provide instances of **IStorage** obtained from OLE's Compound Files implementation. Containers must also use an object's **IPersistStorage** and/or **IPersistStream** interfaces.

</dd> <dt>

<span id="Uniform_Data_Transfer"></span><span id="uniform_data_transfer"></span><span id="UNIFORM_DATA_TRANSFER"></span>Uniform Data Transfer
</dt> <dd>

Applications that support compound documents must implement [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) because embedded objects and linked objects begin as data that has been transferred using special OLE clipboard formats, rather than standard Microsoft Windows clipboard formats. In other words, formatting data as an embedded or linked object is simply one more option provided by OLE's uniform data transfer model.

</dd> </dl>

OLE's compound document technology benefits both software developers and users alike. Instead of feeling obligated to cram every conceivable feature into a single application, software developers are now free, if they like, to develop smaller, more focused applications that rely on other applications to supply additional features. In cases where a software developer decides to provide an application with capabilities beyond its core features, the developer can implement these additional services as separate DLLs, which are loaded into memory only when their services are required. Users benefit from smaller, faster, more capable software that they can mix and match as needed, manipulating all required components from within a single master document.

For more information, see the following topics:

-   [Containers and Servers](containers-and-servers.md)
-   [Linking and Embedding](linking-and-embedding.md)
-   [Object Handlers](object-handlers.md)
-   [In-Process Servers](in-process-servers.md)
-   [Linked Objects and Monikers](linked-objects-and-monikers.md)
-   [Notifications](notifications.md)
-   [Compound Document Interfaces](compound-document-interfaces.md)
-   [Object States](object-states.md)
-   [Implementing In-Place Activation](implementing-in-place-activation.md)
-   [Creating Linked and Embedded Objects from Existing Data](creating-linked-and-embedded-objects-from-existing-data.md)
-   [View Caching](view-caching.md)

## Related topics

<dl> <dt>

[Data Transfer](data-transfer.md)
</dt> <dt>

[Structured Storage](/windows/desktop/Stg/structured-storage-start-page)
</dt> </dl>

 

 