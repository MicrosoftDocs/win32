---
title: Eap Element
description: Captures the method type selected and method-specific configuration.
ms.assetid: 4adef133-1d18-444a-baa3-5419b8cbe298
keywords:
- Eap element EAPHost
topic_type:
- apiref
api_name:
- Eap
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Eap Element

The **Eap** element captures the method type selected and method-specific configuration.

``` syntax
<xs:element name="Eap"
    type="BaseEapParameters"
 />
```

## Remarks

The method can define the constituent elements inside the **Eap** element. The method also performs schema validation on the elements in **Eap**.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[baseeapuserpropertiesv1 Schema](baseeapuserpropertiesv1schema-schema.md)
</dt> </dl>

 

 





