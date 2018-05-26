---
title: Client Security During an Asynchronous Call
description: Client Security During an Asynchronous Call
ms.assetid: 26d1f2c2-cb08-49f1-8beb-b99b029f0d8c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Security During an Asynchronous Call

The proxy manager created by MIDL for objects that use standard marshaling implements the [**IClientSecurity**](/windows/win32/ObjIdl/nn-objidl-iclientsecurity?branch=master) interface. Clients can manage the security of marshaled calls by querying for **IClientSecurity** on the call object and obtaining or changing security settings.

## Related topics

<dl> <dt>

[Making an Asynchronous Call](making-an-asynchronous-call.md)
</dt> </dl>

 

 




