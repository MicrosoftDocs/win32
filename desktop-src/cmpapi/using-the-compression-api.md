---
description: Many applications need to use lossless data compression and decompression. The Compression API simplifies this by exposing Windows compression algorithms through a public API.
ms.assetid: D603A7DE-D4A1-4515-9702-B03C81504661
title: Using the Compression API
ms.topic: article
ms.date: 05/31/2018
---

# Using the Compression API

Many applications need to use lossless data compression and decompression. The Compression API simplifies this by exposing Windows compression algorithms through a public API. Each compression algorithm has a set of properties that controls its behavior. The Compression API exposes an interface that enables the developer to set or query the values of these properties. All properties for the supported compression algorithms have default values representing commonly used values of these properties. If a property is required for both compression and decompression, the default values will be identical, ensuring identical values are used for compression and decompression.

## Selecting the compression algorithm

After a developer decides that an application needs to compress or decompress data, the next step is to choose a compression algorithm. This may depend upon tests to find the best performing combination of speed, compression ratio, and memory requirement for a particular application. The following list gives a relative comparison of the compression algorithms currently supported by the Compression API. Not every option is available for every compression algorithm, and the comparison is approximate because performance can depend on the input data.

XPRESS (**COMPRESS\_ALGORITHM\_XPRESS**)

-   Very fast with low resource requirements
-   Medium compression ratio
-   High compression and decompression speeds
-   Low memory requirement
-   Supports the **COMPRESS\_INFORMATION\_CLASS\_LEVEL** option available in the [**COMPRESS\_INFORMATION\_CLASS**](/windows/desktop/api/compressapi/ne-compressapi-compress_information_class) enumeration. The default value is **(DWORD)0**. For some data, the value **(DWORD)1** can improve the compression ratio with a slightly slower compression speed.

XPRESS with Huffman encoding (**COMPRESS\_ALGORITHM\_XPRESS\_HUFF**)

-   Compression ratio is higher than **COMPRESS\_ALGORITHM\_XPRESS**
-   Medium compression ratio
-   Medium to high compression and decompression speeds
-   Low memory requirement
-   Supports the **COMPRESS\_INFORMATION\_CLASS\_LEVEL** option in the [**COMPRESS\_INFORMATION\_CLASS**](/windows/desktop/api/compressapi/ne-compressapi-compress_information_class) enumeration. The default value is **(DWORD)0**. For some data, the value **(DWORD)1** can improve the compression ratio with a slightly slower compression speed.

MSZIP (**COMPRESS\_ALGORITHM\_MSZIP**)

-   Uses more resources than **COMPRESS\_ALGORITHM\_XPRESS\_HUFF**
-   Generates a compressed block similar to RFC 1951.
-   Medium to high compression ratio
-   Medium compression speed and high decompression speed
-   Medium memory requirement

LZMS (**COMPRESS\_ALGORITHM\_LZMS**)

-   Good algorithm if the size of the data to be compressed is over 2MB.
-   High compression ratio
-   Low compression speed and high decompression speed
-   Medium to high memory requirement
-   Supports the **COMPRESS\_INFORMATION\_CLASS\_BLOCK\_SIZE** option in the [**COMPRESS\_INFORMATION\_CLASS**](/windows/desktop/api/compressapi/ne-compressapi-compress_information_class) enumeration. A minimum size of 1 MB is suggested to get a better compression ratio.

## Deciding which Compression API mode to use

After a developer selects the compression algorithm, the next decision is which of the two modes of the Compression API to use: buffer mode or block mode. Buffer mode was developed for ease of use and is recommended for most cases.

Buffer mode automatically splits up the input buffer into blocks of a size that is appropriate for the selected compression algorithm. The buffer mode automatically formats and stores the uncompressed buffer size in the compressed buffer. The size of the compressed buffer is not automatically saved, and the application needs to save this for decompression. Do not include the **COMPRESS\_RAW** flag in the *Algorithm* parameter when you call [**CreateCompressor**](/windows/desktop/api/compressapi/nf-compressapi-createcompressor) and [**CreateDecompressor**](/windows/desktop/api/compressapi/nf-compressapi-createdecompressor) to use buffer mode. For a code example of a buffer mode application, see the [Using the Compression API in buffer mode](using-the-compression-api-in-buffer-mode.md) section.

Block mode enables the developer to control the block size, but requires more work be done by the application. When using block mode, the application has to break the input data into appropriately sized pieces when compressing and then put the pieces back together when decompressing. The block mode fails if the size of the input buffer is greater than the internal block size of the compression algorithm. The internal block size is 32KB for the MSZIP and 1GB for the XPRESS compression algorithms. The internal block size for LZMS is configurable up to 64GB with a corresponding increase in memory use. The size of the compressed buffer is not automatically saved, and the application also needs to save this for decompression. The value of *UncompressedBufferSize* parameter of [**Decompress**](/windows/desktop/api/compressapi/nf-compressapi-decompress) must be exactly equal to the original size of the uncompressed data and not just the size of the output buffer. This means your application should save the exact original size of the uncompressed data, as well as the compressed data and compressed size, when using block mode. Include the **COMPRESS\_RAW** flag in the *Algorithm* parameter when you call both [**CreateCompressor**](/windows/desktop/api/compressapi/nf-compressapi-createcompressor) and [**CreateDecompressor**](/windows/desktop/api/compressapi/nf-compressapi-createdecompressor) to use block mode. For a code example of a block mode application, see the [Using the Compression API in block mode](using-the-compression-api-in-block-mode.md) section.

## Custom memory allocation

Buffer and block mode applications have the option to specify a custom memory allocation routine when they call [**CreateCompressor**](/windows/desktop/api/compressapi/nf-compressapi-createcompressor) and [**CreateDecompressor**](/windows/desktop/api/compressapi/nf-compressapi-createdecompressor). The *AllocationRoutines* parameter specifies the [**COMPRESS\_ALLOCATION\_ROUTINES**](/windows/desktop/api/compressapi/ns-compressapi-compress_allocation_routines) structure that contains the memory allocation routine. The application can then set the block size for the compressor using [**SetCompressorInformation**](/windows/desktop/api/compressapi/nf-compressapi-setcompressorinformation). See the [Using the Compression API in block mode](using-the-compression-api-in-block-mode.md) section for an example of a simple customized allocation routine.

 

 



