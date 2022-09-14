---
title: Extended Error Information for the User
description: If extended error information is available, the components participating in the creation of the extended error information must make it easy to find the problem.
ms.assetid: 10c54f53-f449-4e7d-ba84-7b000beaee22
ms.topic: article
ms.date: 05/31/2018
---

# Extended Error Information for the User

If extended error information is available, the components participating in the creation of the extended error information must make it easy to find the problem. The first step is to review the last extended error record, and determine on which computer and which process the problem originated. This is often the cause of the RPC\_S\_\* error. Find the detection location, and determine what the parameters for this detection location mean. Usually they indicate a failure of a function call or particular check. From there, determine why the function or check fails, and take corrective action.

The records before the last record indicate the path by which the error arrived, and generally serve as a sanity check rather than an aide in the troubleshooting process.

 

 




