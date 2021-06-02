---
description: Makes an unsigned catalog file, which contains the hashes of a set of files along with associated attributes of each file in the set. A catalog file allows the user to sign one file (the catalog) instead of signing numerous individual files.
ms.assetid: 0a6ce2cd-db1f-4b47-990c-36fa87c28a60
title: Using MakeCat
ms.topic: article
ms.date: 05/31/2018
---

# Using MakeCat

The [MakeCat](makecat.md) tool makes an unsigned catalog file, which contains the [*hashes*](../secgloss/h-gly.md) of a set of files along with associated attributes of each file in the set. A catalog file allows the user to sign one file (the catalog) instead of signing numerous individual files.

After the unsigned catalog file is signed and transmitted, the receiver can compare the hashes of the original files to the hashes contained within the catalog file and verify that the files are free of tampering.

Prior to using the [MakeCat](makecat.md) tool, the user must prepare a Catalog Definition File (.cdf), by using any text editor. The .cdf file contains the list of files and the attributes of the files to be cataloged (the specifications are listed below). The MakeCat tool scans the .cdf file, verifies the list of attributes of each listed file, adds the listed attributes to the catalog itself, hashes each of the listed files, and stores the hashes of each file into the catalog file. Each file has its hash and attributes stored separately within the catalog. This catalog file can then be signed and transmitted. The receiver can subsequently compare the hash of each file within the catalog with the hash of the original files to prove that the original content is free of tampering. MakeCat does not modify the .cdf file.

The following examples use [MakeCat](makecat.md) commands.

-   Generate a catalog file from the file Good.cdf.

    **MakeCat -v good.cdf**

A file, Good.cdf, produces a catalog file, Good.cat, by parsing the files UnsignedPE.exe, UnsignedDOS.exe, Unsigned.cab, Unsigned.Class, and SignedPE.exe. The parsed files, along with Good.cdf and the newly generated Good.cat, are all in the same directory.

``` syntax
[CatalogHeader]
Name=Good.cat
ResultDir=.\
PublicVersion=0x00000001
EncodingType=
CATATTR1=0x10010001:Movie1:FirstMovie
CATATTR2=0x10010001:Movie2:SecondMovie
CATATTR3=0x10010001:Movie3:ThirdMovie

[CatalogFiles]
UnsignedPE=.\UnsignedPE.EXE
UnsignedDOS=.\UnsignedDOS.EXE
<HASH>UnsignedCAB=.\Unsigned.CAB
UnsignedClass=.\Unsigned.Class
SignedPE=.\SignedPE.EXE
```

> [!Note]  
> The last entry in the .cdf file must always have an explicit newline character at the end of the line.

 

 

 
