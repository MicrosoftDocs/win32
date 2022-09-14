---
description: You can model a class provider as a push or pull provider, which specifies how a provider expects to interact with WMI.
ms.assetid: d1852784-8440-4b8a-9cdd-896e51cdee98
ms.tgt_platform: multiple
title: Determining Push or Pull Status
ms.topic: article
ms.date: 05/31/2018
---

# Determining Push or Pull Status

You can model a class provider as a push or pull provider, which specifies how a provider expects to interact with WMI. Pull providers receive a request from WMI and satisfy the request either by generating the data dynamically or retrieving it from a local cache. Pull providers also must implement a large number of interfaces.

A pull provider generates class definitions dynamically. Typically, the data managed by a pull provider changes frequently, requiring the provider to either generate the class dynamically or retrieve the class from a local cache whenever an application issues a request. A pull provider must implement its own data retrieval, cache, and event notification mechanisms. Because most providers are pull providers, the documentation in this file assumes you are building a pull provider unless explicitly stated otherwise.

In contrast, WMI uses data in the WMI repository to handle all application requests for push providers. Push providers also use fewer interface methods, and thus are easier to implement. A push provider uses the WMI repository as a storage area for information on the managed object, and updates that information only during initialization. For example, the WDM class provider included in the WMI section of the Microsoft Windows Software Development Kit (SDK) is modeled as a push provider.

By using the WMI repository as a storage area, a push provider gains the following benefits over a pull provider:

-   The provider does not need to implement a local cache to store data.
-   The provider does not need to support data retrieval; instead, the provider can rely on WMI to provide retrieval support.
-   When an application requests data supplied by the provider, WMI fulfills that request.
-   The provider can also rely on WMI to support event notification.

However, because a push provider updates only during initialization, any changes to a class may not be reflected in the WMI repository for some time. Therefore, the push provider model works best with classes that change little or else are completely static.

 

 



