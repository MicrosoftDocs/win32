---
title: MetaPackageInformation (Header) Element
description: Identifies the troubleshooting package.
ms.assetid: '0a83cfde-3626-4298-a5d7-de7aee62b41c'
keywords: ["MetaPackageInformation element Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- MetaPackageInformation
api_type:
- Schema
---

# MetaPackageInformation (Header) Element

Identifies the troubleshooting package.

``` syntax
<xs:element name="MetaPackageInformation"
    type="dcmRR:PackageInformation"
 />
```

The **MetaPackageInformation** element is defined by the [**Header**](report-header-complextype.md) complex type.

## Remarks

This node will contain three child **Data** elements that identify the properties of the troubleshooting package. For a list of the properties, see the [**PackageInformation**](report-packageinformation-complextype.md) complex type.

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

 

 





