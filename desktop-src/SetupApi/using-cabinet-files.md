---
description: The setup functions handle cabinets internally. To explicitly enumerate and extract files from a cabinet, you can call the SetupIterateCabinet function.
ms.assetid: 14bd925a-e7fe-48a3-9ed6-4e42ce796290
title: Using Cabinet Files
ms.topic: article
ms.date: 05/31/2018
---

# Using Cabinet Files

The setup functions handle cabinets internally. To explicitly enumerate and extract files from a cabinet, you can call the [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta) function.

The following topic describes the cabinet processing internal to the setup functions and how to use [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta). Also discussed are the notifications sent by **SetupIterateCabinet** and the required format of a cabinet callback routine to process those notifications.

-   [Extracting Files From Cabinets](extracting-files-from-cabinets.md)
-   [Creating a Cabinet Callback Routine](creating-a-cabinet-callback-routine.md)

 

 



