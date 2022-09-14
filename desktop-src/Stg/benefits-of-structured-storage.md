---
title: Benefits of Structured Storage
description: COM provides a set of services collectively called structured storage.
ms.assetid: d05d2dbc-d1d2-4ef8-a773-5337e2746da3
keywords:
- Structured Storage Strctd Stg , benefits
ms.topic: article
ms.date: 05/31/2018
---

# Benefits of Structured Storage

COM provides a set of services collectively called structured storage. Among the benefits of these services is the reduction of performance penalties and overhead associated with storing separate objects in a flat file. Instead of a flat file, COM stores the separate objects in a single, structured file consisting of two main elements: storage objects and stream objects. Together, they function like a file system within a file.

Structured storage solves performance problems by eliminating the need to totally rewrite a file to storage whenever a new object is added to a compound file, or an existing object increases in size. The new data is written to the next available location in permanent storage, and the storage object updates the table of pointers it maintains to track the locations of its storage objects and stream objects. At the same time, structured storage enables end users to interact and manage a compound file as if it were a single file rather than a nested hierarchy of separate objects.

Structured storage also has other benefits:

-   **Incremental access**. If a user needs access to an object within a compound file, the user can load and save only that object, rather than the entire file.
-   **Multiple use**. More than one end user or application can concurrently read and write information in the same compound file.
-   **Transaction processing**. Users can read or write to COM compound files in transacted mode, where changes made to the file are buffered and can subsequently either be committed to the file or reversed.
-   **Low-memory saves**. Structured storage provides facilities for saving files in low-memory situations.

 

 




