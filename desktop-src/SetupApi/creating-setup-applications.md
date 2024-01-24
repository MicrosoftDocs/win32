---
description: After you create an INF file, you will typically write the source code for your setup application. You call the setup functions from your setup application to perform many installation operations.
ms.assetid: 9f444564-d3a4-4b3c-8849-b56cd610356c
title: Creating Setup Applications
ms.topic: article
ms.date: 05/31/2018
---

# Creating Setup Applications

After you create an INF file, you will typically write the source code for your setup application. You call the setup functions from your setup application to perform many installation operations.

The following steps cover one way to use the setup functions to create a setup application. You can use this example as a starting point, or develop your own installation algorithm.

**Initialization**

-   [Open the INF and, if appropriate, append other INF files.](opening-the-inf-file.md)
-   [Extract file information from the INF file.](extracting-file-information-from-the-inf-file.md)
-   [Gather setup information from the user.](gathering-setup-information-from-the-user.md)
-   [Create a queue.](creating-a-queue-and-queuing-file-operations.md)

**Install files**

-   [Commit the queue, specifying a callback routine.](committing-the-queue.md)
-   [Update registry information.](updating-registry-information.md)

**Clean up**

-   [Close the file queue and INF.](closing-the-file-queue-and-inf-file.md)
-   [Release any other system resources and end the program.](releasing-other-system-resources.md)

 

 



