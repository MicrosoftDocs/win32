---
title: Asynchronous Storage
description: Asynchronous storage enhances the COM structured storage specification to support asynchronous download of storage objects on high-latency, slow-link networks such as the Internet.
ms.assetid: 12b97059-2c8c-4712-8a76-03c3ce7094a0
keywords:
- Structured Storage Strctd Stg , asynchronous storage
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Storage

Asynchronous storage enhances the COM structured storage specification to support asynchronous download of storage objects on high-latency, slow-link networks such as the Internet. Asynchronous storage enables both new and legacy applications that use compound files to efficiently render their content when accessed by means of existing Internet protocols. A single request to a World Wide Web server triggers the download of nested objects contained within a Web page, eliminating the need to separately request each object. An asynchronous download and access mechanism enables an application to render the first page of data before all the data has been received. The exact order in which elements of a page become available can be specified by the Web publisher and is not dependent on random factors of network topology and server availability.

Asynchronous storage works together with asynchronous monikers to provide complete asynchronous binding behavior. For more information about asynchronous monikers, see the Microsoft ActiveX software development kit. A protocol-specific asynchronous moniker triggers the binding operation and sets up the required components. In the Internet case, this moniker would be one that can parse a URL to bind to an object or storage. If the target of the binding operation is a persistent object, the call to [**IMoniker::BindToStorage**](/windows/win32/api/objidl/nf-objidl-imoniker-bindtostorage) returns an asynchronous storage object.

> [!Note]  
> The current version of Microsoft URL monikers does not support asynchronous storage.

 

An asynchronous moniker client requests asynchronous binding by implementing a bind-status callback object and registering it with the bind context. The bind-status callback object exposes the [**IBindStatusCallback**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775060(v=vs.85)) interface, which enables the client to specify binding preferences and to receive progress and global data-availability notifications during the course of a binding operation. The asynchronous compound file implementation provides a connection point for [**IProgressNotify**](/windows/win32/api/objidl/nn-objidl-iprogressnotify), which clients can use to receive specific availability notifications on individual streams.

 

 