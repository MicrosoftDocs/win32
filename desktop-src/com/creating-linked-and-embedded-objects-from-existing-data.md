---
title: Creating Linked and Embedded Objects from Existing Data
description: Creating Linked and Embedded Objects from Existing Data
ms.assetid: 76848b7e-6068-4bac-9793-304f813096f0
ms.topic: article
ms.date: 05/31/2018
---

# Creating Linked and Embedded Objects from Existing Data

A user typically assembles a compound document by using either the clipboard or drag and drop to copy a data object from its server application to the user's container application. With applications that support OLE, the user can initiate the transfer from either the server or the container. For example, the server can copy data to the clipboard in the server application, then switch to the container application and choose Paste Special/Embedded Object or an equivalent menu command to create a new embedded object from the selected data. Or, the user can drag the data from one application to the other. The process is similar for creating a linked object.

> [!Note]  
> An application that functions as both OLE server and container can use a selection of its own data to create an embedded or linked object at a new location within the same document.

 

Data transfer between OLE server and container applications is built on uniform data transfer, as described in [Data Transfer](data-transfer.md). OLE servers and object handlers implement [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) in order to make their data available for transfers using either the clipboard or drag and drop. OLE objects support all the usual clipboard formats. In addition, they support six clipboard formats that support the creation of linked and embedded objects from a selected data object.

OLE clipboard formats describe data objects that, upon being dropped or pasted in OLE containers, are to become embedded or linked compound-document objects. The data object presents these formats to container applications in order of their fidelity as descriptions of the data. In other words, the object presents first the format that best represents it, followed by the next best format, and so on. This intentional ordering encourages a container application to use the best possible format.

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> <dt>

[Data Transfer](data-transfer.md)
</dt> </dl>

 

 




