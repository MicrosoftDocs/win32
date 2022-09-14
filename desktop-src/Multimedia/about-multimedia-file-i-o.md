---
title: About Multimedia File I/O
description: About Multimedia File I/O
ms.assetid: d72ba20c-0085-4d5c-9fc6-b9024b575027
keywords:
- Windows multimedia,file I/O
- multimedia,file I/O
- multimedia input,file I/O
- multimedia file I/O,about
- file I/O,about
- input and output (I/O),about
- I/O (input and output),about
- basic I/O
- resource interchange file format (RIFF)
- RIFF (resource interchange file format)
- RIFF I/O
ms.topic: article
ms.date: 05/31/2018
---

# About Multimedia File I/O

Most multimedia applications require file input and output (I/O) — that is, the ability to create, read, and write disk files. Multimedia file I/O services provide buffered and unbuffered file I/O and support for RIFF files. The services are extensible with custom I/O procedures that can be shared among applications.

Most applications need only the basic file I/O services and the RIFF file I/O services. Applications sensitive to file I/O performance, such as applications that stream data from compact disc in real time, can optimize performance by using services to directly access the file I/O buffer. Applications that access custom storage systems, such as file archives and databases, can provide their own I/O procedure that reads and writes elements of the storage system.

 

 




