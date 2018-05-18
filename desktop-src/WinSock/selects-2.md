---
Description: 'In the original Berkeley Software Distribution (BSD) socket interface the select function was the standard (and only) means to obtain network event indications.'
ms.assetid: 'f7f42b03-1f89-4801-abf0-396ff8b61cae'
title: Selects
---

# Selects

In the original Berkeley Software Distribution (BSD) socket interface the [**select**](select-2.md) function was the standard (and only) means to obtain network event indications. For each socket, information on read, write, or error status can be polled or waited on. See [**WSPSelect**](wspselect-2.md) for more information. Note that network event FD\_QOS cannot be obtained by this approach.

 

 



