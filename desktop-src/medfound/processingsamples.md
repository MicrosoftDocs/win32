---
description: Processing Codec DMO Input and Output
ms.assetid: fab6244e-a20e-4395-a82c-0905e3225516
title: Processing Codec DMO Input and Output
ms.topic: article
ms.date: 05/31/2018
---

# Processing Codec DMO Input and Output

When you have configured the input type and output type for a DMO, you can begin processing data samples. You pass samples to the DMO for processing using the **IMediaObject::ProcessInput** method, and then retrieve the processed sample by calling **IMediaObject::ProcessOutput**. You should set accurate time stamps and durations for all input samples passed. Time stamps are not strictly required but help maintain audio/video synchronization. If you do not have the time stamps for your samples it is better to leave them out than to use uncertain values.

## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> </dl>

 

 



