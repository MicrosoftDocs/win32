---
title: Modifying Attributes with ADSI
description: To modify attribute values, ADSI provides the IADs.Put and IADs.PutEx methods. These methods modify the data on the client-side cache. The IADs.SetInfo method must be called to commit the changes to the directory.
ms.assetid: cbb5c313-3b9d-4943-bd16-6e4489abe804
ms.tgt_platform: multiple
keywords:
- Modifying Attributes with ADSI
- Attributes ADSI , Modifying
ms.topic: article
ms.date: 05/31/2018
---

# Modifying Attributes with ADSI

To modify attribute values, ADSI provides the [**IADs.Put**](/windows/desktop/api/Iads/nf-iads-iads-put) and [**IADs.PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) methods. These methods modify the data on the client-side cache. The [**IADs.SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) method must be called to commit the changes to the directory.

> [!Note]  
> When multiple attribute changes are committed in a single call to [**IADs.SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo), if any single attribute cannot be modified, none of the attributes will be modified. For example, if you modify the [**sn**](/windows/desktop/ADSchema/a-sn) and [**givenName**](/windows/desktop/ADSchema/a-givenname) attributes and clear the [**telephoneNumber**](/windows/desktop/ADSchema/a-telephonenumber) attribute of a user object without any subsequent calls to the **SetInfo** method, the changes are entered when you call **SetInfo**. If one or more of the modifications are not allowed and therefore cannot be performed, then none of the collective modifications made to the attributes are entered during the call to **SetInfo**.

 

The [**IADs.Put**](/windows/desktop/api/Iads/nf-iads-iads-put) method takes an attribute name and a variant parameter. Use this method to set attributes that contain both single and multiple values.

The [**IADs.PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) method provides control over operations on multi-valued attributes. You can append, delete, update, and clear existing values. The **IADs.PutEx** method always expects a variant array of attribute values. However, you can use this method to set an attribute with a single value as well.

The [**IADs.PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) method uses the operations specified by the [**ADS\_PROPERTY\_OPERATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_property_operation_enum) enumeration.

 

 