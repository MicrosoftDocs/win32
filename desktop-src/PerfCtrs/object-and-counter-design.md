---
description: A performance object is an entity for which performance data is available.
ms.assetid: 97b9c9ec-e758-4928-b3fa-90d220bca5fb
title: Object and Counter Design
ms.topic: article
ms.date: 05/31/2018
---

# Object and Counter Design

A performance object is an entity for which performance data is available. Performance counters define the type of data that is available for a performance object. An application can provide information for multiple performance objects. Performance objects can contain either single instance counters or multiple instance counters. A single instance object returns a single set of counter values.

A multiple instance object returns an instance of the object for each occurrence of the object that the application controls. For example, a SCSI application could define a drive object with two counters, such as Bytes Read and Bytes Written. When the consumer queries the object, the performance DLL returns an instance of the object for each drive that the application controls.

After deciding if your object supports a single instance or multiple instances, you need to decide on the type of counters that you want the object to provide. For example, you can provide counter values that are displayed as raw values, as rates, or as percentages.

For a list of predefined counter types that you should choose from, see the Counter Types section of the [Windows Server 2003 Deployment Kit](/previous-versions/windows/it-pro/windows-server-2003/cc776490(v=ws.10)). Depending on the counter type, you may simply provide the raw data, or you may also have to provide time and frequency information and additional counter data used by the consumer to calculate a displayable value.

The method you use to collect the data can be as simple as incrementing a counter each time a particular routine in the application is called, or it can involve time-consuming calculations. Counters and timers should increment and never be cleared. Counters can wrap, as long as they do not wrap twice between being sampled by the consumer. Your application can collect and store data during its normal execution, as long as it does not affect its performance.

For some types of data, it may be more efficient or appropriate to collect the data on demand. In this situation, the performance DLL must communicate to the application that the data has been requested. For data that is expensive to collect (in terms of processor time or memory usage), consider collecting data only when the consumer requests **Costly** data. This allows a consumer to routinely request data for all counters that are not costly. The data can be requested only when needed. The Performance tool does not collect **Costly** data.

 

 
