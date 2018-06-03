---
title: What is a Directory Service
description: A directory is similar to a database, but typically contains more descriptive, attribute-based data; that is, data read more often than it is written.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7a1693e9-1afb-44f3-b9f2-d9e54701fe6a
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What is a Directory Service?

A directory is similar to a database, but typically contains more descriptive, attribute-based data; that is, data read more often than it is written. Also, a directory contains data that is concise and strictly relevant to an entry. By contrast, a database contains large amounts of data for each entry that may, or may not, be directly relevant to the entry. For this reason, a directory does not usually implement the transaction or roll-back schemes that regular databases require. If they are permitted at all, directory updates are typically simple all-or-nothing changes. Directories are tuned to respond quickly to high-volume lookup or search operations.

A lookup is an operation that targets a specific, unique entry, such as a domain name. A search is an operation that targets data common to multiple entries, such as the data collected, by an Internet search engine, about a topic.

Directories may replicate data widely to increase availability and reliability, and thus reduce response time. When directory data is replicated, temporary inconsistencies between the replicas may be acceptable — as long as all the replicas are updated eventually — depending on the particular role of the directory. These applications can be defined only by the specific directory design and are irrelevant to the deployment of LDAP.

There are many methods used to provide a directory service. Different methods allow various types of data to be stored in a directory, require the data to be referenced, queried, updated, protected, and so on. Some directory services are local, providing service to a restricted context, for example, the finger service on a single computer. Other services are global, providing service to a much broader context, for example, the entire Internet. Global services are usually distributed, meaning that the data they contain is shared across many computers which cooperate to provide the directory service. Typically, a global service defines a uniform namespace, which gives the same view of the data regardless of where the computer is in relation to the data.

 

 




