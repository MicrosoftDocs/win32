---
title: Performance guidelines
description: Guidelines for developing applications that perform well in a Remote Desktop Services environment.
ms.assetid: 50f0c1f6-8046-4ceb-b2c4-6fc1ae86fd73
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Performance guidelines

The following sections provide guidelines for developing applications that perform well in a Remote Desktop Services environment.

## In this section

<dl> <dt>

[Graphic effects](graphic-effects.md)
</dt> <dd>

A list of features that should be disabled when running as a remote session in a Remote Desktop Services environment.

</dd> <dt>

[Guidelines for background tasks in Remote Desktop Services](background-tasks.md)
</dt> <dd>

To maximize CPU availability for all users, either disable background tasks when running in a Remote Desktop Services environment or create efficient background tasks that are not resource-intensive.

</dd> <dt>

[Thread usage](thread-usage.md)
</dt> <dd>

You should tune and balance application thread usage for a multiuser, multiprocessor Remote Desktop Services environment.

</dd> <dt>

[Detecting the Remote Desktop Services environment](detecting-the-terminal-services-environment.md)
</dt> <dd>

To optimize performance, it is good practice for applications to detect whether they are running in a Remote Desktop Services client session.

</dd> </dl>

Check your application for memory leaks and resolve any problems. Of course this is good advice for any application, but in a Remote Desktop Services environment, an application can be run multiple times by multiple users, thus rapidly magnifying the effect of a memory leak.

Animations, large images, audio, and other bandwidth-intensive services must be configurable. When these services are not the primary function, they can be off by default for remote sessions, but enabled when a session is running locally or over a high bandwidth connection. If the purpose of an application is to provide high bandwidth services, such as streaming video broadcasts, the service does not have to be off by default.

 

 




