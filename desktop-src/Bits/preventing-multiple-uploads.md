---
title: Preventing Multiple Uploads
description: When you upload a file, BITS creates a session ID that identifies the upload session to both the BITS client and BITS server.
ms.assetid: 97283f8e-d2fa-4383-9b92-a05f46680443
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Multiple Uploads

When you upload a file, BITS creates a session ID that identifies the upload session to both the BITS client and BITS server. If the connection between the BITS client and server is broken while BITS is uploading a file, the client will use the session ID to try to resume the upload.

If the BITS client connects to the same server as before, the server will recognize the session ID and the upload will resume from the point of interruption. However, if the client connects to a different server, the client must start the upload from the beginning because the new server does not have the session context or the previously uploaded data. BITS may connect to a different server when the BITS server is hosted on a web farm and the BITS IIS extension property, [BITSHostId](bits-iis-extension-properties.md), is not set. The BITSHostId property prevents restarts by forcing the BITS client to connect to the previous server's unique address instead of the shared server address.

The BITS server will attempt to send the upload file only once to the server application, but it is possible that the file may be sent more than one time. This can occur, for example, if the BITS server sends the file to the server application and then terminates while waiting for the reply from the server application. The BITS client will receive an error code from the HTTP layer, and retry the upload after a delay. If the server stays offline for longer than the [BITSHostIdFallbackTimeout](bits-iis-extension-properties.md) timeout, then the client will eventually send the request to the shared server address again; a different BITS server will receive the file and deliver it again to the server application.

A similar case can occur even with a single front-end server. For example, when the client has uploaded the entire file to the server, the final block causes the server to forward the file to the server application. If the BITS server or the server application terminate after the file is processed but before the acknowledgment is sent to the client, then the client will receive an error code and retry later. When the client retries, the BITS server will see that the final block has been uploaded, and it will again forward the file to the server application. If receiving the upload file multiple times is an issue for your server application, you should consider including a transaction identifier in the data.

 

 




