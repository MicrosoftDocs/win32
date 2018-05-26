---
Description: To create custom extensions or to encode a complex extension, you can write your own extension handlers that export custom interfaces.
ms.assetid: a33ac417-b5f9-4ad7-a26e-13cdb1e4ac1b
title: Writing Custom Extension Handlers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Writing Custom Extension Handlers

To create custom extensions or to encode a complex extension, you can write your own extension handlers that export custom interfaces. Microsoft Certificate Services ships with the following interfaces which can be used to encode various types of extension data: [**ICertEncodeAltName**](/windows/win32/Certenc/nn-certenc-icertencodealtname?branch=master), [**ICertEncodeBitString**](/windows/win32/Certenc/nn-certenc-icertencodebitstring?branch=master), [**ICertEncodeCRLDistInfo**](/windows/win32/Certenc/nn-certenc-icertencodecrldistinfo?branch=master), [**ICertEncodeDateArray**](/windows/win32/Certenc/nn-certenc-icertencodedatearray?branch=master), [**ICertEncodeLongArray**](/windows/win32/Certenc/nn-certenc-icertencodelongarray?branch=master), and [**ICertEncodeStringArray**](/windows/win32/Certenc/nn-certenc-icertencodestringarray?branch=master). These interfaces are contained in Certenc.dll. Additionally, the type information for these interfaces is contained in Certencl.dll, which is contained in the Platform Software Development Kit (SDK).

For more information about extension handlers, see [Extension Handlers](extension-handlers.md).

 

 



