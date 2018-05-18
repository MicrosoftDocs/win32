---
title: ReadyBoot Analysis
description: ReadyBoot Analysis
ms.assetid: '24eff7e6-f2e3-460d-9efe-9888d3435904'
---

# ReadyBoot Analysis

ReadyBoot is boot acceleration technology that maintains an in-RAM cache used to service disk reads faster than a slower storage medium such as a disk drive. ReadyBoot reads (prefetches) data into the cache before it is requested. Prefetching optimizes disk access patterns by taking data locality and hard drive's performance characteristics into account. Read requests from system processes, services and user applications are then serviced out of the ReadyBoot RAM cache.

ReadyBoot analysis is a core piece of a comprehensive boot performance analysis. Read requests that are satisfied from the ReadyBoot RAM cache are not reflected as disk reads in the [Disk I/O graphs](disk-i-o.md) and summary tables because those reads do not access the disk. In order to develop a complete picture of the I/O activities performed at boot time, one must consider the I/O information presented in the ReadyBoot graphs and summary tables in addition to the I/O information presented in the Disk I/O graphs and summary tables.

### Contents

[ReadyBoot Quick Start Guide](readyboot-quick-start-guide.md)

[Analyzing ReadyBoot Data](analyzing-readyboot-data.md)

[ReadyBoot Reference](readyboot-reference.md)

 

 




