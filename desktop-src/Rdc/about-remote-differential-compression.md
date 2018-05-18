---
title: About Remote Differential Compression
description: Allows data to be synchronized with a remote source using compression techniques to minimize the amount of data sent across the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1ec21a38-6410-46f1-91f1-6d1eb1cd0694'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-differential-compression'
ms.tgt_platform: multiple
keywords: ["Remote Differential Compression Files , about"]
---

# About Remote Differential Compression

Remote Differential Compression (RDC) allows data to be synchronized with a remote source using compression techniques to minimize the amount of data sent across the network.

RDC is different from patching-oriented differencing mechanisms, such as Binary Delta Compression (BDC), that are designed to operate only on known versions of a single file. BDC requires the server to have copies of all versions of the file, and differences between each pair of versions are precomputed so that they can be distributed efficiently from a server to multiple clients.

RDC makes no assumptions about file similarity or versioning. Because differences between files are computed on the fly, RDC is ideally suited for synchronizing files that are different or have been updated independently.

RDC does not assume that the file data to be synchronized resides in physical files. Therefore, the RDC application is responsible for performing file I/O on behalf of the RDC library.

Because it is transport independent, RDC can be used with RPC, HTTP, or other desired transport mechanisms. The RDC application bears the responsibility for choosing the appropriate transport and performing any client or server authentication that is required to support the transport's security model.

RDC is suitable for applications that move data across a wide area network (WAN) where the data transmission costs outweigh the CPU cost of signature computation. RDC can also be used on faster networks if the amount of data to be transferred is relatively large and the changes to the data are typically small.

## Remote Differential Compression Algorithm Overview

RDC divides a file's data into chunks by computing the local maxima of a fingerprinting function that is computed at every byte position in the file. A *fingerprinting function* is a hash function that can be computed incrementally. For example, if you compute the function F over a range of bytes from the file, B<sub>i</sub>...B<sub>j</sub>, it should then be possible to compute F(B<sub>i+1</sub>...B<sub>j+1</sub>) incrementally by adding the byte B<sub>j+1</sub> and subtracting the byte B<sub>i</sub>. The range of bytes from the file, B<sub>i</sub>...B<sub>j</sub>, is called the *hash window*. The length of this window, in bytes, is called the *hash window size*.

The RDC library's FilterMax signature generator "slides" the hash window across the entire file by adding the byte at the leading edge and subtracting the byte at the trailing edge of the window. Meanwhile, the generator continually examines the sequence of fingerprint function values over a given range of bytes, called the *horizon size*. If a fingerprint function value is a local maximum within the range, its byte position is chosen as a "cut point," or chunk boundary.

After the file has been divided into chunks, the signature generator computes a strong hash value (an MD4 hash), called a signature, for each chunk. The signatures can be used to compare the contents of two arbitrarily different versions of a file.

Because the size of the signature file grows linearly with the size of the original file, comparing very large files can be expensive. This cost is reduced dramatically by applying the RDC algorithm recursively to the signature files. For example, if the original file size is 9 GB, the signature file size would typically be about 81 MB. If the RDC algorithm is applied to the signature file, the resulting second-level signature file size would be about 5.7 MB.

## Remote Differential Compression Application Concepts

When developing an application that uses RDC, it is important to understand the following concepts and terminology.

In a typical RDC scenario, a server and a client have different versions of a file. (The terms client and server refer only to the computers' roles in this scenario, not their operating systems.) The client's copy of the file is called the *seed file*. The server's copy is called the *source file*. The objective of the RDC application is to download the file updates to the client, which uses them to construct a *target file* that combines the updates from the source file with the unchanged contents from the seed file.

The RDC client and server each use the RDC library's FilterMax signature generator to divide their copy of the file into chunks and compute a strong hash, called a signature, for each chunk of file data. Thus, the client has a list of signatures for the seed file, and the server has a list of signatures for the source file. These signature lists can be computed on the fly, or they can be precomputed.

The client initiates the RDC protocol by requesting the source signature list from the server. Then the client compares each source signature against the signatures in its own seed signature list. If a source signature matches a seed signature, the client already has the file data for that signature. If a source signature does not appear in the client's list of seed signatures, the client must request the specified chunk (of file data) from the server.

The result of comparing the two signature lists is a *needs list*, which describes which chunks of file data, from where (seed or source file), are needed to construct the target file on the client computer. Each entry in the needs list is called a *needs block*.

The client iterates through each needs block and copies the specified chunk of the source or seed file data to the target file. Seed file data is copied locally. Source file data is downloaded from the server. The more similar the seed and source files are, the less network bandwidth is required to create the target file.

## Related topics

<dl> <dt>

[Remote Differential Compression](remote-differential-compression.md)
</dt> <dt>

[Optimizing File Replication over Limited-Bandwidth Networks using Remote Differential Compression](http://research.microsoft.com/um/people/gurevich/annotated.md#183)
</dt> </dl>

 

 




