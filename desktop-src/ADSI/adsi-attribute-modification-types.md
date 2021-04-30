---
title: ADSI Attribute Modification Types (Iads.h)
description: Used with the dwControlCode member of ADS\_ATTR\_INFO structure to specify the type of operation to be performed when an attribute is modified with the IDirectoryObject SetObjectAttributes method.
ms.assetid: e9a454c8-e067-4730-97f4-85c4f5889e05
ms.tgt_platform: multiple
keywords:
- attribute modification types ADSI
topic_type:
- apiref
api_name:
- ADS_ATTR_CLEAR
- ADS_ATTR_UPDATE
- ADS_ATTR_APPEND
- ADS_ATTR_DELETE
api_location:
- Iads.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ADSI Attribute Modification Types

The following constants are used with the **dwControlCode** member of [**ADS\_ATTR\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_attr_info) structure to specify the type of operation to be performed when an attribute is modified with the [**IDirectoryObject::SetObjectAttributes**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-setobjectattributes) method. For more information about using these values, see [Modifying Attributes with ADSI](modifying-attributes-with-adsi.md).

<dl> <dt>

<span id="ADS_ATTR_CLEAR"></span><span id="ads_attr_clear"></span>**ADS\_ATTR\_CLEAR**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Causes all attribute values to be removed from an object.


</dt> </dl> </dd> <dt>

<span id="ADS_ATTR_UPDATE"></span><span id="ads_attr_update"></span>**ADS\_ATTR\_UPDATE**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Causes the specified attribute values to be updated.


</dt> </dl> </dd> <dt>

<span id="ADS_ATTR_APPEND"></span><span id="ads_attr_append"></span>**ADS\_ATTR\_APPEND**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



Causes the specified attribute values to be appended to the existing attribute values.


</dt> </dl> </dd> <dt>

<span id="ADS_ATTR_DELETE"></span><span id="ads_attr_delete"></span>**ADS\_ATTR\_DELETE**
</dt> <dd> <dl> <dt>

4
</dt> <dt>



Causes the specified attribute values to be removed from an object.


</dt> </dl> </dd> </dl>

## Remarks

These constants are intended to be used with the [**ADS\_ATTR\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_attr_info) structure in the [**IDirectoryObject::SetObjectAttributes**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-setobjectattributes) method. These constants should not be confused with members of the [**ADS\_PROPERTY\_OPERATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_property_operation_enum) enumeration, which are intended to be used with the [**IADs::PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) method.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                    |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl> |



## See also

<dl> <dt>

[**ADS\_ATTR\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_attr_info)
</dt> <dt>

[**IDirectoryObject::SetObjectAttributes**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-setobjectattributes)
</dt> <dt>

[Modifying Attributes with ADSI](modifying-attributes-with-adsi.md)
</dt> </dl>

 

 





