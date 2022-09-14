---
description: To create custom extensions or to encode a complex extension, you can write your own extension handlers that export custom interfaces.
ms.assetid: a33ac417-b5f9-4ad7-a26e-13cdb1e4ac1b
title: Writing Custom Extension Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Writing Custom Extension Handlers

To create custom extensions or to encode a complex extension, you can write your own extension handlers that export custom interfaces. Microsoft Certificate Services ships with the following interfaces which can be used to encode various types of extension data: [**ICertEncodeAltName**](/windows/desktop/api/Certenc/nn-certenc-icertencodealtname), [**ICertEncodeBitString**](/windows/desktop/api/Certenc/nn-certenc-icertencodebitstring), [**ICertEncodeCRLDistInfo**](/windows/desktop/api/Certenc/nn-certenc-icertencodecrldistinfo), [**ICertEncodeDateArray**](/windows/desktop/api/Certenc/nn-certenc-icertencodedatearray), [**ICertEncodeLongArray**](/windows/desktop/api/Certenc/nn-certenc-icertencodelongarray), and [**ICertEncodeStringArray**](/windows/desktop/api/Certenc/nn-certenc-icertencodestringarray). These interfaces are contained in Certenc.dll. Additionally, the type information for these interfaces is contained in Certencl.dll, which is contained in the Platform Software Development Kit (SDK).

For more information about extension handlers, see [Extension Handlers](extension-handlers.md).

 

 



