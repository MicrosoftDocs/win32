---
title: Compound File Optimization
description: Asynchronous storage enables applications to precisely layout compound files so that data is available in the order in which applications will require it.
ms.assetid: 0737c5b2-09f6-4993-bb42-f2a684e5a136
keywords:
- Compound File Optimization
ms.topic: article
ms.date: 05/31/2018
---

# Compound File Optimization

Asynchronous storage enables applications to precisely layout compound files so that data is available in the order in which applications will require it. If an application requires only part of its data to display a first page of information, this data can be placed at the beginning of the file, even if it logically resides at the end of a stream. Data from different streams can be interleaved. Audio and video data, for example, can be interleaved so that subsequent read operations retrieve both simultaneously, a requirement for multimedia applications.

[**IStorage::CopyTo**](/windows/desktop/api/Objidl/nf-objidl-istorage-copyto) can be used to layout a docfile, thus improving performance in most scenarios.

 

 




