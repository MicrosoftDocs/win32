---
description: 'Clusters may be referred to from two different perspectives: within the file and on the volume.'
ms.assetid: 8e999524-4fe9-49b0-8b59-081fa7a42c72
title: Clusters and Extents
ms.topic: article
ms.date: 05/31/2018
---

# Clusters and Extents

Clusters may be referred to from two different perspectives: within the file and on the volume. Any cluster in a file has a *virtual cluster number* (VCN), which is its relative offset from the beginning of the file. For example, a seek to twice the size of a cluster, followed by a read, will return data beginning at the third VCN. A *logical cluster number* (LCN) describes the offset of a cluster from some arbitrary point within the volume. LCNs should be treated only as ordinal, or relative, numbers. There is no guaranteed mapping of logical clusters to physical hard disk drive sectors.

An *extent* is a run of contiguous clusters. For example, suppose a file consisting of 30 clusters is recorded in two extents. The first extent might consist of five contiguous clusters, the other of the remaining 25 clusters.

There is no guarantee of any relationship on the disk of any extent to any other extent. For example, the first extent may be at a higher LCN than a subsequent extent.

 

 



