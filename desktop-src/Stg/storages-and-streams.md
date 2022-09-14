---
title: Storages and Streams
description: A storage object is analogous to a file system directory.
ms.assetid: 57b2a66d-e912-4879-b778-75f8461d211f
ms.topic: article
ms.date: 05/31/2018
---

# Storages and Streams

A storage object is analogous to a file system directory. Just as a directory can contain other directories and files, a storage object can contain other storage objects and stream objects. Also like a directory, a storage object tracks the locations and sizes of the storage objects and stream objects nested beneath it.

A stream object is analogous to the traditional notion of a file. Like a file, a stream contains data stored as a consecutive sequence of bytes.

A COM compound file consists of a root storage object containing at least one stream object representing its native data along with one or more storage objects corresponding to its linked and embedded objects. The root storage object maps to a file name in whatever file system it happens to reside. Each of the objects inside the document also is represented by a storage object containing one or more stream objects, and perhaps also containing one or more storage objects. In this way, a document can consist of an unlimited number of nested objects. For more information, see [Compound Files](compound-files.md).

 

 




