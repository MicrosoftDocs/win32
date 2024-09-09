---
title: Handles and objects
description: An object is a data structure that represents a system resource, such as a file, thread, or graphic image.
ms.assetid: '26aaad09-c1e1-46e8-9cd3-7d795a10d900'
ms.topic: article
ms.date: 11/09/2021
---

# Handles and objects

An *object* is a data structure that represents a system resource, such as a file, thread, or graphic image. Your application can't directly access object data, nor the system resource that an object represents. Instead, your application must obtain an object *handle*, which it can use to examine or modify the system resource. Each handle has an entry in an internally maintained table. Those entries contain the addresses of the resources, and the means to identify the resource type.

* [About handles and objects](about-handles-and-objects.md)
* [Object categories](object-categories.md)
* [Handle and object reference](handle-and-object-reference.md)
