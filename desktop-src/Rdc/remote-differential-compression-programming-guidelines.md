---
title: Remote Differential Compression Programming Guidelines
description: This section provides guidelines for developing Remote Differential Compression (RDC) applications that perform well.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ebc72c88-14b3-4029-90b2-44ced69e0193'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-differential-compression'
ms.tgt_platform: multiple
keywords: ["Remote Differential Compression Files , programming guidelines"]
---

# Remote Differential Compression Programming Guidelines

This section provides guidelines for developing Remote Differential Compression (RDC) applications that perform well.

## Choosing an Appropriate Recursion Depth

Initially, your application can use the default recursion depth value returned by the [**IRdcLibrary::ComputeDefaultRecursionDepth**](irdclibrary-computedefaultrecursiondepth.md) method. The range of values that RDC supports is from 1 to 8. The maximum value is sufficient to accommodate files that are many terabytes in size. However, your application should also check the sizes of the generated signature files for each level. If they are very small at the computed recursion depth, it might make sense to choose a lower default recursion depth to transfer a particular file. There is a trade-off between the number of bytes sent over the wire and the number of round trips. For example, if the signature file size is 16 KB at level 2, 1 KB at level 3, and 81 bytes at level 4, certainly you should skip level 4 because level 3 is only 1 KB, and possibly skip level 3 as well. The optimal solution depends on the available bandwidth and the cost of an extra round trip.

## Choosing the Comparator Buffer Size

The comparator buffer size is set by passing the desired value in the *comparatorBufferSize* parameter of the [**IRdcLibrary::CreateComparator**](irdclibrary-createcomparator.md) method. The supported range of values is from MSRDC\_MINIMUM\_COMPAREBUFFER to MSRDC\_MAXIMUM\_COMPAREBUFFER. For best performance, this value should be greater than or equal to the size, in bytes, of the source signature file. This is because each time a portion of the signature data is read in from the source signature file, the entire seed signature file is read in from disk.

## Choosing the Horizon Size and Hash Window Size

The horizon and hash window sizes are set by calling the [**IRdcGeneratorFilterMaxParameters::SetHorizonSize**](irdcgeneratorfiltermaxparameters-sethorizonsize.md) and [**IRdcGeneratorFilterMaxParameters::SetHashWindowSize**](irdcgeneratorfiltermaxparameters-sethashwindowsize.md) methods on the generator parameter structure that was created by the [**IRdcLibrary::CreateGeneratorParameters**](irdclibrary-creategeneratorparameters.md) method. Most applications should use the default values for these parameters. However, you may want to experiment with larger values to see how they affect performance. If you change these parameters, you must do so before calling the [**IRdcLibrary::CreateGenerator**](irdclibrary-creategenerator.md) method. After a signature generator is created, its parameter values cannot be changed.

## Caching Signature Files

For better performance, your application may cache signature files and have some way to ensure that they are regenerated when the corresponding source or seed files have changed. There is no single best way to detect file changes; you will need to determine what is best for your application. Some of the techniques that can be used include:

-   Monitoring the USN change journal for the volume where the files reside.
-   Checking for changes to the last-write time for each file.

## Other Guidelines For RDC Applications

When you are developing RDC applications, follow these guidelines:

-   Don't automatically use RDC for every file. For better performance, you might want to set a minimum file size, such as 16 KB.
-   For better performance, the client portion of your application should download chunks of source file data from the server in batches rather than one at a time. This data can also be compressed using a traditional data compression library.
-   Consider using a multithreaded RDC application to sync multiple files in parallel between client and server or using other methods of pipelining downloads to address networks with high latency and low bandwidth.
-   When debugging your RDC application, you may want to examine the contents of the signature files. To print out the signatures and the parameters used to generate them, call the [**IRdcSignatureReader::ReadHeader**](irdcsignaturereader-readheader.md) and [**IRdcSignatureReader::ReadSignatures**](irdcsignaturereader-readsignatures.md) methods.
-   Your application should check the RDC library versions on the client and server to make sure they are compatible. To do this, call the [**IRdcLibrary::GetRDCVersion**](irdclibrary-getrdcversion.md) method.

 

 




