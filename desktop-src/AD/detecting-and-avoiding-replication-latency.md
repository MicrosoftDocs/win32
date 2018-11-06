---
title: Detecting and Avoiding Replication Latency
description: Replication latency is a fact of life in a loosely coupled distributed system.
ms.assetid: ea65759b-2bfa-4859-8d2a-5949bbb9adef
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Detecting and Avoiding Replication Latency

Replication latency is a fact of life in a loosely coupled distributed system. Applications must accommodate this. The best way to accommodate replication latency is to design applications to minimize the effects. The ideal directory-enabled application:

-   Is insensitive to version skew.
-   Does not depend on relationships among multiple objects.
-   Has no intra- or inter-object consistency requirements.

Applications and services that fit this profile need not be concerned with replication latency. Other applications must be designed with replication latency in mind. The key to success in designing such an application is awareness of the replication process. Steps taken at design time to reduce inter-object dependencies and minimize partial update windows will pay large dividends at run time. Approaches to dealing with replication latency are divided into two classes—avoidance strategies that reduce the impact of latency and detection strategies that allow an application to detect latency-induced states.

 

 




