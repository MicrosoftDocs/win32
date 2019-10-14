---
title: UseWinLogonCredentials (EapType) Element
description: Controls use of the winlogin credentials.
ms.assetid: 8ebd87ce-7d2b-4305-b50c-239bb9c7af75
keywords:
- UseWinLogonCredentials element EAPHost
topic_type:
- apiref
api_name:
- UseWinLogonCredentials
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# UseWinLogonCredentials (EapType) Element

The **UseWinLogonCredentials (EapType)** element controls use of the winlogin credentials.

``` syntax
<xs:element name="UseWinLogonCredentials"
    type="boolean"
 />
```

The **UseWinLogonCredentials** element is defined by the [**EapType**](mschapv2connectionpropertiesv1schema-eaptype-element.md) element.

## Remarks

If TRUE, then EAP MS-CHAPv2 obtains credentials from winlogon. If FALSE, then EAP MS-CHAPv2 obtains credentials from the user. The **UseWinLogonCredentials (EapType)** element is optional.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**EapType**](mschapv2connectionpropertiesv1schema-eaptype-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**EapType**](mschapv2connectionpropertiesv1schema-eaptype-element.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mschapv2connectionpropertiesv1 Schema](mschapv2connectionpropertiesv1schema-schema.md)
</dt> </dl>

 

 





