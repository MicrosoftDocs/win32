---
description: Represents information about a source code file.
MS-HAID: vspixengine.SourceFileInfo
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: SourceFileInfo structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: A5222610-36ED-4F3B-BD95-A4F8611CC557
api_name: 
 - SourceFileInfo
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.sourcefileinfo"></span>SourceFileInfo structure

Represents information about a source code file.

## Syntax


```C++
} SourceFileInfo;
```

## Members

**fileName**  
A COM string comtaining the filepath of the associated source file.

**checksumByteCount**  
The number of bytes in the checksum. When checkSumAlgorithm is equal to CHECKSUMALGORITHM::md5, checkSumByteCount is 16. When checkSumAlgorithm is equal to CHECKSUMALGORITHM::sha1, checkSumByteCount is 20.

**checkSumAlgorithm**  
Specifies the algorithm used to generate the checksum of the file. Supported algorithms are MD5 and SHA1. For more information, see the CHECKSUMALGORITHM enum.

**checkSumFirstPart**  
The first 8 byte portion of the checksum.

**checkSumSecondPart**  
The second 8 byte portion of the checksum.

**checkSumThirdPart**  
The third 8 byte portion of the checksum.

**checkSumFourthPart**  
The fourth 8 byte portion of the checksum.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



