---
title: Checksums and Object Counts
description: Checksums and object counts are detection strategies that allow an application to detect a partial update state.
ms.assetid: 14829a74-c186-4250-beac-036c5ecc5913
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Checksums and Object Counts

Checksums and object counts are detection strategies that allow an application to detect a partial update state. Checksums can also be used to detect inconsistencies introduced by collision resolution. Both checksums and object counts require a place to store the value used for verifying a checksum or object count. This can be on a "master" object chosen from among those involved in the application-specific relationship or on a parent object under which the related objects are stored.

For checksums, applications reading the related objects verify the checksum by calculating a local result and comparing it with the stored value. If the values do not match, the replica is in a partial update state and the objects cannot be used.

For object counts, applications count the related objects (typically children of a single parent) and compare the count with the stored value. If the counts do not match, the replica is in a partial update state and the objects cannot be used.

Some important considerations:

-   For the checksum approach to work, the one or more attributes used in computing the checksum must be updated. The algorithm used to compute the checksum must reliably reflect differences in input. If many different inputs product the same checksum, the algorithm will not reliably detect partial updates. "Salting" the input with values like the **objectGUID** of the source computer and the date and time of the update is also helpful.
-   Object counts work best when used with new sets of objects, or in combination with consistency GUIDs (see the next section for more information). The application performing the update must either know, in advance, the number of objects that will be in the container when the update is completed or use some other means of marking the container invalid while the update proceeds (for example, setting the count to zero). After completing the update the source application marks the container with the count of objects contained.

 

 




