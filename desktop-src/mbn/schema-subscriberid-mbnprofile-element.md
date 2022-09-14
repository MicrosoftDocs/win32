---
description: Identifies the unique identifier of the profile.
ms.assetid: 7572ef4f-ce7a-4595-a5ad-ade96e36d7d7
title: SubscriberID (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SubscriberID
api_type: 
- Schema
---

# SubscriberID (MBNProfile) Element

The **SubscriberID (MBNProfile)** element identifies the unique identifier of the profile.

For a GSM network this should contain the IMSI (International Mobile Subscriber Identity) of the SIM and for CDMA devices it should contain the MIN (Mobile Identification Number) of the device.

The element is is a numeric string with a maximum length 15 digits.

The element is required.

``` syntax
<xs:element name="SubscriberID"
    type="subscriberIdType"
 />
```

The **SubscriberID** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> </dl>

 

 




