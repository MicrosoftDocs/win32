---
description: The CIMType qualifier contains text describing the type of a property.
ms.assetid: ae65d4c7-2150-489b-a368-fb38c0d1b3be
ms.tgt_platform: multiple
title: CIMType Qualifier
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIMType
api_type: 
- NA
api_location: 
---

# CIMType Qualifier

The **CIMType** qualifier contains text describing the type of a property.

This text can be the MOF type such as "string" and "sint32" or the CIM type such as "CIM\_STRING" and "CIM\_SINT32". There is a one-to-one correspondence between the **CIMType** qualifier and the type of the property used in the *pvtType* parameter of the [**IWbemClassObject::Get**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-get) method.

The two exceptions are:

-   [*Reference properties*](gloss-r.md), which have the type **CIM\_REFERENCE**, that contains the "REF:classname" value. The classname value describes the class type of the reference property.
-   Embedded object properties, which have the **CIM\_OBJECT** type.

Please note, however, that the **CIMType** qualifier can and should be used to type a reference property more exactly. For example, if the property always refers to instances of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class, its **CIMType** qualifier should be set to:


```mof
"ref:Win32_LogicalDisk"
```



By default, the **CIMType** qualifier of a reference property has the type **ref**.

As with reference properties, the **CIMType** qualifier should used to type an embedded object property more exactly with the following syntax:


```mof
"object:EmbedClass"
```



Because WMI allows more types than can be expressed by standard constants with the VT\_ prefix, the **CIMType** qualifier can help interpret type values. The **CIMType** qualifier is added automatically. For more information, see [MOF Data Types](mof-data-types.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**Standard WMI Qualifiers**](standard-wmi-qualifiers.md)
</dt> <dt>

[WMI Qualifiers](wmi-qualifiers.md)
</dt> <dt>

[Adding a Qualifier](adding-a-qualifier.md)
</dt> </dl>

 

