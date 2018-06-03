---
title: Additional ReadyBoot Terminology
description: Additional ReadyBoot Terminology
ms.assetid: be7ec03b-025e-49fb-a96f-091c5d5d3fbb
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Additional ReadyBoot Terminology

Additional ReadyBoot terminology necessary for analysis is provided in the table below.



| Term                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EARLINESS (HIT)<br/>   | "Earliness" of a HIT event is defined as the elapsed time between the time a block of data was prefetched into the ReadyBoot cache and a time at which that block is accessed by a read request.<br/>                                                                                                                                                                                                                                                                                                                                                                      |
| EARLINESS (PEND)<br/>  | "Earliness" of a PEND event is defined as the elapsed time between the time at which a block of data is requested by a read and one of the following:<br/> Most common: the time at which that block is prefetched into the ReadyBoot cache and a cache read is initiated<br/> Rare: the time when a timeout is hit, which implies the data did not get prefetched into the cache in time <br/> In case of the timeout, the original read request is forwarded to underlying hard drive and earliness is a total of timeout value + disk read time.<br/> |
| SKIP/SKIPPED READ<br/> | The term "Skipped read" (or a "skip") refers to a disk read that is intentionally not prefetched into or satisfied from the ReadyBoot cache and instead is satisfied from the disk. In Windows Vista the concept of skipped reads does not exist. On Windows 7 and later large read requests may be treated as a Skip and thus satisfied from the disk directly to improve ReadyBoot efficiency.<br/>                                                                                                                                                                      |
| COMPLETE TIME<br/>     | Complete Time for the PEND event is defined as the time when ReadyBoot decides to hold a corresponding read request. Complete Time for other events refer to times of corresponding operation completions. For example, the Complete Time for a MISS even refers to the time when the corresponding read request is completed by the underlying hard drive.)<br/>                                                                                                                                                                                                          |



 

 

 





