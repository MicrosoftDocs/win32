---
description: This section details the binary version of the DirectX (.x) file format as introduced with the release of DirectX 3.0.
ms.assetid: d1b6698f-72bd-40a4-a501-c2093cd940f6
title: Binary Encoding
ms.topic: article
ms.date: 05/31/2018
---

# Binary Encoding

This section details the binary version of the DirectX (.x) file format as introduced with the release of DirectX 3.0.

The binary format is a tokenized representation of the text format. Tokens can be stand-alone or accompanied by primitive data records. Stand-alone tokens give grammatical structure, and record-bearing tokens supply the necessary data.

Note that all data is stored in little-endian format. A valid binary data stream consists of a header followed by templates and/or data objects.

This section discusses the following components of the binary file format and provides an example template and binary data object.

-   [Header](header.md)
-   [Tokens](tokens.md)
-   [Token Records](token-records.md)
-   [Templates](dx9-graphics-reference-x-file-binaryencoding-templates.md)
-   [Data](dx9-graphics-reference-x-file-binaryencoding-data.md)
-   [Examples](examples.md)

## Related topics

<dl> <dt>

[X File Format Reference](dx9-graphics-reference-x-file-format.md)
</dt> </dl>

 

 



