---
title: Reliability of Extended Error Information
description: Extended error information is not reliable.
ms.assetid: d4735a7b-ede0-4230-b10a-bf9772aca6a6
ms.topic: article
ms.date: 05/31/2018
---

# Reliability of Extended Error Information

Extended error information is not reliable. Extended error information cannot be used for building code logic. It is appropriate to check for the presence of extended error information, and if there, to dump, save, or log that information. But do not rely on the information or its contents.

The following reasons explain why extended error information is not reliable:

-   The sequence and contents of the extended error records depends on the internal architecture of the system, which is subject to change. A certain operation may go through NPFS on current systems, but tomorrow could go through TCP. These different components generate very different error codes, and code checks therefore are inherently unreliable and not recommended.
-   The propagation of extended error information can be disabled, as explained previously. If detection code is included, the application will likely stop working in certain environments.
-   The propagation of extended error information is performed in a best effort manner. Propagation or generation of extended error information can fail if there isn't enough memory on the computer to process or propagate the chain. Under such circumstances, the chain will be dropped. Some protocols have limited lengths for fault packets since they usually don't include much information. If the length of the chain exceeds the allowed length of the packet, the RPC run time begins dropping information from the chain in an attempt to fit the chain into the packet. The run time first drops records, starting from the penultimate record, going backwards, until only the first and last records remain. If the chain still doesn't fit into a packet, the run time drops string parameters and computer names. If a string parameter is dropped, the type of the parameter is set to none. If a record is dropped, the EEInfoNextRecordsMissing flag is set in the next record, and EEInfoPreviousRecordsMissing is set in the previous record.

 

 




