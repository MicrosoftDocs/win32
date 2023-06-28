---
title: Handler Architecture
description: Handler Architecture
ms.assetid: 93839b82-09cb-41af-ac0e-a8e9448bf04b
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Handler Architecture

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The internal function of a file or stream handler is defined by the handler itself. To an application, a file handler typically appears as a module to read and write AVI files. Similarly, a stream handler appears as a module to read and write a specific type of data stream. The consistent stream interface makes the source and destination of the stream unimportant to the application that uses the handler.

A file handler provides access to a data source consisting of one or more data streams. File handlers typically provide access to disk files containing one or more data streams, and the internal functions of the file handler read and write the multimedia data. However, file handlers can work with any data source, such as a digital transmission channel containing several intermingled data streams.

In contrast, a stream handler processes one type of data and appears as a data stream to an application. A stream handler can provide data that it manufactures, or it can retrieve data from a file or an external source. It supplies its data in a format that your application can use.

 

 




