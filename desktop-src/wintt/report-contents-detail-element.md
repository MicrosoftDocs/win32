---
title: Contents (Detail) Element
description: The contents of a custom detail.
ms.assetid: 32f785c8-daf5-482a-9ca8-a1533d43762e
keywords:
- Contents element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Contents
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Contents (Detail) Element

The contents of a custom detail.

``` syntax
<xs:element name="Contents"
    type=" dcmRR:Contents"
 />
```

The **Contents** element is defined by the [**Detail**](report-detail-complextype.md) complex type.

## Remarks

The body of this node contains an XML fragment if the caller to the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet used the -Xml parameter; otherwise, the body contains a child [**Data (Contents)**](report-data-contents-element.md) node that identifies the file that contains the custom detail (if the caller used the -File parameter). For details on the **Data** element, see the [**Contents**](report-contents-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**Detail (DetailedInformation)**](https://msdn.microsoft.com/library/windows/desktop/ee692419)
</dt> </dl>

 

 





