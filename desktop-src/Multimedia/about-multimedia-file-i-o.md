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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Multimedia File I/O

\[The feature associated with this page, [Multimedia File I/O](/windows/win32/multimedia/multimedia-file-i-o), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **Multimedia File I/O**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Most multimedia applications require file input and output (I/O) — that is, the ability to create, read, and write disk files. Multimedia file I/O services provide buffered and unbuffered file I/O and support for RIFF files. The services are extensible with custom I/O procedures that can be shared among applications.

Most applications need only the basic file I/O services and the RIFF file I/O services. Applications sensitive to file I/O performance, such as applications that stream data from compact disc in real time, can optimize performance by using services to directly access the file I/O buffer. Applications that access custom storage systems, such as file archives and databases, can provide their own I/O procedure that reads and writes elements of the storage system.

 

 




