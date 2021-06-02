---
description: Future improvements to example Winsock application code.
ms.assetid: 317baa53-6bc8-42bd-8f56-480cab29ae6b
title: Future Improvements
ms.topic: article
ms.date: 05/31/2018
---

# Future Improvements

There are several improvements that can be made to this application, such as:

-   A single, persistent connection could be created by the application. Appropriate error handling would have to be added. This would reduce the overhead associated with connection startup and teardown.
-   The reply code on the server could be optimized to consolidate replies, reducing the number of packets sent from the server.
-   Improvements in the protocol could be made. For example, an update bitmask could be used to signify which cells are to be updated, and only that cell data sent.
-   Updates could be overlapped using different threads, so that the network is not idle while the **ComputeNext** function is running.

## Related topics

<dl> <dt>

[Improving a Slow Application](improving-a-slow-application-2.md)
</dt> <dt>

[The Baseline Version: A Very Poor Performing Application](the-baseline-version-a-very-poor-performing-application-2.md)
</dt> <dt>

[Revision 1: Cleaning up the Obvious](revision-1-cleaning-up-the-obvious-2.md)
</dt> <dt>

[Revision 2: Redesigning for Fewer Connects](revision-2-redesigning-for-fewer-connects-2.md)
</dt> <dt>

[Revision 3: Compressed Block Send](revision-3-compressed-block-send-2.md)
</dt> </dl>

 

 



