---
title: Data (ComputerInformation) Element
description: Identifies a property of the computer that ran the package.
ms.assetid: 0faec17e-702a-4a1c-971d-c5ae69e5801f
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

# Data (ComputerInformation) Element

Identifies a property of the computer that ran the package.

``` syntax
<xs:element name="Data"
    type="dcmRR:Data"
 />
```

The **Data** element is defined by the [**ComputerInformation**](report-computerinformation-complextype.md) complex type.

## Remarks

The [**ComputerInformation (Header)**](report-computerinformation-header-element.md) node will contain three child **Data** elements that identify the properties of the computer. For a list of the properties, see the [**ComputerInformation**](report-computerinformation-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**ComputerInformation (Header)**](report-computerinformation-header-element.md)
</dt> </dl>

 

 





