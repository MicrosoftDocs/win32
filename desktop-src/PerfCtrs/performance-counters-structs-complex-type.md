---
Description: Defines a list of structures that contain counter values.
ms.assetid: 6f6b33ed-6440-456c-8379-61a37798c95f
title: structs Complex Type
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# structs Complex Type

Defines a list of structures that contain counter values.

``` syntax
<xs:complexType name="structs">
    <xs:choice
        minOccurs="1"
        maxOccurs="unbounded"
    >
        <xs:element name="struct"
            type="man:struct"
         />
    </xs:choice>
</xs:complexType>
```

## Child elements



| Element    | Type                                                           | Description                                                      |
|------------|----------------------------------------------------------------|------------------------------------------------------------------|
| **struct** | [**man:struct**](performance-counters-struct-complex-type.md) | The name of a structure that contains counter values.<br/> |



## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




