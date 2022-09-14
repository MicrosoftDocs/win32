---
description: Specifies whether the Mobile Broadband device will automatically connect to a network.
ms.assetid: a2673ac7-6d70-4005-9ac4-cf670eba26ae
title: AutoConnectOnInternet (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AutoConnectOnInternet
api_type: 
- Schema
---

# AutoConnectOnInternet (MBNProfile) Element

The **AutoConnectOnInternet (MBNProfile)** element specifies whether the Mobile Broadband device will automatically connect to a network.

If set to **FALSE**, then the Mobile Broadband service's auto connect logic will not be used if there is any other network connectivity available to the system. If set to **TRUE**, then the Mobile Broadband service will try to automatically connect the device to the network based on the auto connection setting defined in the [**ConnectionMode**](schema-connectionmode-mbnprofile-element.md) element.

**Windows 8 and later:** This element is deprecated. Use the [**WcmSetProperty**](/windows/desktop/api/wcmapi/nf-wcmapi-wcmsetproperty) method with the *Property* parameter set to **wcm\_global\_property\_minimize\_policy** instead.

``` syntax
<xs:element name="AutoConnectOnInternet"
    type="boolean"
 />
```

The **AutoConnectOnInternet** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

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

 

