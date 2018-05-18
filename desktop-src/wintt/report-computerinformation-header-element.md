---
title: ComputerInformation (Header) Element
description: Identifies the computer on which the troubleshooting package ran.
ms.assetid: '9dc12622-f1a9-4379-ba1d-0274507ce579'
keywords: ["ComputerInformation element Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- ComputerInformation
api_type:
- Schema
---

# ComputerInformation (Header) Element

Identifies the computer on which the troubleshooting package ran.

``` syntax
<xs:element name="ComputerInformation"
    type="dcmRR:ComputerInformation"
 />
```

The **ComputerInformation** element is defined by the [**Header**](report-header-complextype.md) complex type.

## Remarks

The children of this node are [**Data (ComputerInformation)**](https://msdn.microsoft.com/library/windows/desktop/ee692408) elements that specify the version and architecture of the operating system, and whether the client is a server or client SKU.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**Header (ResultReport)**](report-header-resultreport-element.md)
</dt> </dl>

 

 





