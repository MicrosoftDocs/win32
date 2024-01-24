---
title: Windows Event Collector Constants (Evcoll.h)
description: The Windows Event Collector SDK contains the following constants.
ms.assetid: 2ba862f9-6849-43b3-8914-e18ede1d63c0
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- EC_VARIANT_TYPE_MASK
- EC_VARIANT_TYPE_ARRAY
- EC_READ_ACCESS
- EC_WRITE_ACCESS
- EC_OPEN_ALWAYS
- EC_CREATE_NEW
- EC_OPEN_EXISTING
api_location:
- Evcoll.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Event Collector Constants

The Windows Event Collector SDK contains the following constants.

<dl> <dt>

<span id="EC_VARIANT_TYPE_MASK"></span><span id="ec_variant_type_mask"></span>**EC\_VARIANT\_TYPE\_MASK**
</dt> <dd> <dl> <dt>

0x7f
</dt> <dt>



Used to mask out the array bit from the **Type** property of an [**EC\_VARIANT**](/windows/desktop/api/Evcoll/ns-evcoll-ec_variant) to extract the type of the variant value.


</dt> </dl> </dd> <dt>

<span id="EC_VARIANT_TYPE_ARRAY"></span><span id="ec_variant_type_array"></span>**EC\_VARIANT\_TYPE\_ARRAY**
</dt> <dd> <dl> <dt>

128 (0x80)
</dt> <dt>



When this bit is set in the **Type** property of an [**EC\_VARIANT**](/windows/desktop/api/Evcoll/ns-evcoll-ec_variant), the variant contains a pointer to an array of values, rather than the value itself.


</dt> </dl> </dd> <dt>

<span id="EC_READ_ACCESS"></span><span id="ec_read_access"></span>**EC\_READ\_ACCESS**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Read access control permission that allows information to be read from the event collector.


</dt> </dl> </dd> <dt>

<span id="EC_WRITE_ACCESS"></span><span id="ec_write_access"></span>**EC\_WRITE\_ACCESS**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Write access control permission that allows information to be written to the event collector.


</dt> </dl> </dd> <dt>

<span id="EC_OPEN_ALWAYS"></span><span id="ec_open_always"></span>**EC\_OPEN\_ALWAYS**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Opens an existing subscription or creates the subscription if it does not exist. Used by the [**EcOpenSubscription**](/windows/desktop/api/Evcoll/nf-evcoll-ecopensubscription) method.


</dt> </dl> </dd> <dt>

<span id="EC_CREATE_NEW"></span><span id="ec_create_new"></span>**EC\_CREATE\_NEW**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



A flag passed to the [**EcOpenSubscription**](/windows/desktop/api/Evcoll/nf-evcoll-ecopensubscription) function specifying that a new subscription should be created.


</dt> </dl> </dd> <dt>

<span id="EC_OPEN_EXISTING"></span><span id="ec_open_existing"></span>**EC\_OPEN\_EXISTING**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



A flag passed to the [**EcOpenSubscription**](/windows/desktop/api/Evcoll/nf-evcoll-ecopensubscription) function specifying that an existing subscription should be opened.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Evcoll.h</dt> </dl> |



 

 





