---
title: processTokenSidType Simple Type
description: Defines the possible values for the ProcessTokenSidType (principalType) element.
ms.assetid: 9db3e113-c525-4cbf-88c2-be256d641e92
keywords:
- processTokenSidType simple type Task Scheduler
topic_type:
- apiref
api_name:
- processTokenSidType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# processTokenSidType Simple Type

Defines the possible values for the [**ProcessTokenSidType (principalType)**](taskschedulerschema-processtokensidtype-principaltype-element.md) element.

``` syntax
<xs:simpleType name="processTokenSidType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="None"
         />
        <xs:enumeration
            value="Unrestricted"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **processTokenSidType** simple type defines the following values.



| Value        | Description                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| None         | Tasks are run in a process that does not contain a process token SID (no changes will be made to the process token groups list).<br/> |
| Unrestricted | A task SID will be derived from the full task path and will be added to the process token groups list.<br/>                           |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





