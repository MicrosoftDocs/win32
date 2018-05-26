---
title: Data (PackageInformation) Element
description: Identifies a property of a troubleshooter in the package.
ms.assetid: 3e7b9a98-01b9-4854-bae8-ef89fa52126d
keywords:
- Data element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Data
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Data (PackageInformation) Element

Identifies a property of a troubleshooter in the package.

``` syntax
<xs:element name="Data"
    type="dcmRR:Data"
 />
```

The **Data** element is defined by the [**PackageInformation**](report-packageinformation-complextype.md) complex type.

## Remarks

The [**PackageInformation (Header)**](report-packageinformation-header-element.md) node will contain three child **Data** elements that identify the properties of the troubleshooter. For a list of the properties, see the [**PackageInformation**](report-packageinformation-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**PackageInformation (Header)**](report-packageinformation-header-element.md)
</dt> </dl>

 

 





