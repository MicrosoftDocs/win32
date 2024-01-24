---
description: This section examines a portion of a sample application that operates over the network very slowly. Throughout this section, modifications are made to the initial code to improve its performance.
ms.assetid: 29b96540-1b45-46b7-871a-e728aa50ad24
title: Improving a Slow Application
ms.topic: article
ms.date: 05/31/2018
---

# Improving a Slow Application

This section examines a portion of a sample application that operates over the network very slowly. Throughout this section, modifications are made to the initial code to improve its performance.

The mock sample is the updated portion for a game called Life. The application is written such that the client performs the calculations for the updates and sends them to the server. The server then displays the resulting Life field. The output from the client is a stream of bytes, grouped in threes (triplets), each triplet representing one cell update. The bytes in the triplet represent the row, column, and value, respectively, for the cell.

This sample begins as an intentionally poor performing application, which provides the baseline from which performance improvements can be illustrated. From there, the code is improved three times to address various issues that affect performance. These samples should be read in order, as each iteration improves on the previous version.

The baseline code, and the revisions that improve that code, are the following:

-   [The Baseline Version: A Very Poor Performing Application](the-baseline-version-a-very-poor-performing-application-2.md)
-   [Revision 1: Cleaning up the Obvious](revision-1-cleaning-up-the-obvious-2.md)
-   [Revision 2: Redesigning for Fewer Connects](revision-2-redesigning-for-fewer-connects-2.md)
-   [Revision 3: Compressed Block Send](revision-3-compressed-block-send-2.md)
-   [Future Improvements](future-improvements-2.md)

> [!WARNING]
> The first few examples of the application provide intentionally poor performance, in order to illustrate performance improvements possible with changes to code. Do not use these code samples in your application; they are for illustration purposes only.

 

## Related topics

<dl> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> </dl>

 

 



