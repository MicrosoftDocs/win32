---
title: The ProviderSpecific Buffer
description: The ProviderSpecific buffer provides applications that have special QOS needs with a mechanism that enables fine-grained tuning of required QOS parameters.
ms.assetid: 98907187-ad29-4b2c-804c-594fa5ef7401
keywords:
- ProviderSpecific buffer QOS
- Quality of Service QOS , described, ProviderSpecific buffer
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The ProviderSpecific Buffer

The ProviderSpecific buffer provides applications that have special QOS needs with a mechanism that enables fine-grained tuning of required QOS parameters. The ProviderSpecific buffer is of type [**WSABUF**](https://msdn.microsoft.com/library/windows/desktop/ms741542) as defined by Windows Sockets 2 and is a member of the [**QOS**](/windows/win32/Winsock2/ns-winsock2-_qualityofservice?branch=master) structure.

The standard mechanisms by which Windows 2000 QOS enables service quality provisioning fulfills QOS requirements for the majority of applications. In some cases, however, service quality parameters not available with standard QOS mechanisms may need to be implemented. The ProviderSpecific buffer interface is provided for those situations.

The ProviderSpecific buffer specifically includes a length field and a pointer to a buffer, which may contain one or more QOS objects. The format of each object is as follows:

-   Each object includes a type field, which specifically identifies the object, followed by:
-   A length field, which contains the length of the object inclusive of the header, followed by:
-   The object data itself.

The end of a list of QOS objects in a WSABUF buffer is indicated by a QOS\_OBJECT\_END\_OF\_LIST object, as defined in the Qos.h header file.

See [QOS Objects](qos-objects.md) for more information.

 

 




