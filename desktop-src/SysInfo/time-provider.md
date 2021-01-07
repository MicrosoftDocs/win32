---
description: The Microsoft Windows operating system provides support for a variety of hardware devices and network time protocols using the time provider architecture.
ms.assetid: 'a7575373-eeda-4f2a-85e5-d1b50994e7ae'
title: Time Provider
ms.topic: article
ms.date: 05/31/2018
---

# Time Provider

The Microsoft Windows operating system provides support for a variety of hardware devices and network time protocols using the *time provider* architecture. Input time providers retrieve accurate time stamps from hardware or the network, and output time providers provide time stamps to other clients on the network.

Time providers are managed by the *time provider manager*. It is responsible for loading, starting, and stopping time providers as directed by the service control manager. This interface makes writing a time provider easier than writing a full service.

-   [Creating a Time Provider](creating-a-time-provider.md)
-   [Registering a Time Provider](registering-a-time-provider.md)
-   [Sample Time Provider](sample-time-provider.md)

## Related topics

<dl> <dt>

[Windows Time Service](https://www.microsoft.com/technet/prodtechnol/windowsserver2003/technologies/security/ws03mngd/26_s3wts.mspx)
</dt> </dl>

 

 



