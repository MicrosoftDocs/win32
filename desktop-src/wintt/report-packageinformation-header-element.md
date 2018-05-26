---
title: PackageInformation (Header) Element
description: Identifies a troubleshooter within the troubleshooting package.
ms.assetid: 5a68dc4a-188d-4843-8592-83d7ae7fc89b
keywords:
- PackageInformation element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- PackageInformation
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PackageInformation (Header) Element

Identifies a troubleshooter within the troubleshooting package.

``` syntax
<xs:element name="PackageInformation"
    type="dcmRR:PackageInformation"
 />
```

The **PackageInformation** element is defined by the [**Header**](report-header-complextype.md) complex type.

## Remarks

This node will contain three child **Data** elements that identify the properties of the troubleshooter. For a list of the properties, see the [**PackageInformation**](report-packageinformation-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**Header (ResultReport)**](report-header-resultreport-element.md)
</dt> </dl>

 

 





