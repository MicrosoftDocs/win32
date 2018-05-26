---
title: Modifying Attributes with ADSI
description: To modify attribute values, ADSI provides the IADs.Put and IADs.PutEx methods. These methods modify the data on the client-side cache. The IADs.SetInfo method must be called to commit the changes to the directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: cbb5c313-3b9d-4943-bd16-6e4489abe804
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Modifying Attributes with ADSI
- Attributes ADSI , Modifying
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Modifying Attributes with ADSI

To modify attribute values, ADSI provides the [**IADs.Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) and [**IADs.PutEx**](/windows/win32/Iads/nf-iads-iads-putex?branch=master) methods. These methods modify the data on the client-side cache. The [**IADs.SetInfo**](/windows/win32/Iads/nf-iads-iads-setinfo?branch=master) method must be called to commit the changes to the directory.

> [!Note]  
> When multiple attribute changes are committed in a single call to [**IADs.SetInfo**](/windows/win32/Iads/nf-iads-iads-setinfo?branch=master), if any single attribute cannot be modified, none of the attributes will be modified. For example, if you modify the [**sn**](https://msdn.microsoft.com/library/ms679872) and [**givenName**](https://msdn.microsoft.com/library/ms675719) attributes and clear the [**telephoneNumber**](https://msdn.microsoft.com/library/ms680027) attribute of a user object without any subsequent calls to the **SetInfo** method, the changes are entered when you call **SetInfo**. If one or more of the modifications are not allowed and therefore cannot be performed, then none of the collective modifications made to the attributes are entered during the call to **SetInfo**.

 

The [**IADs.Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) method takes an attribute name and a variant parameter. Use this method to set attributes that contain both single and multiple values.

The [**IADs.PutEx**](/windows/win32/Iads/nf-iads-iads-putex?branch=master) method provides control over operations on multi-valued attributes. You can append, delete, update, and clear existing values. The **IADs.PutEx** method always expects a variant array of attribute values. However, you can use this method to set an attribute with a single value as well.

The [**IADs.PutEx**](/windows/win32/Iads/nf-iads-iads-putex?branch=master) method uses the operations specified by the [**ADS\_PROPERTY\_OPERATION\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0027?branch=master) enumeration.

 

 




