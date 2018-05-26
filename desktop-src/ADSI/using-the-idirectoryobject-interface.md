---
title: Using the IDirectoryObject Interface
description: When you create an ADSI client in C or C++ that uses early binding, you will have a wider variety of ADSI data types available to use for your client if it calls the IDirectoryObject interface instead of the IADs interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d2c706ed-a341-4c49-91da-70230192f055
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- IDirectoryObject ADSI , using
- ADSI ADSI , using,using the IDirectoryObject interface
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using the IDirectoryObject Interface

When you create an ADSI client in C or C++ that uses early binding, you will have a wider variety of ADSI data types available to use for your client if it calls the [**IDirectoryObject**](/windows/win32/Iads/nn-iads-idirectoryobject?branch=master) interface instead of the [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master) interface. The **IDirectoryObject** interface provides methods to support a subset of an object's maintenance properties and to access its attributes. The following figure shows the relationships among the data structures.

![idirectoryobject interface data structures](images/ds2dso.png)

In the preceding figure, the structure [**ADS\_OBJECT\_INFO**](/windows/win32/Iads/ns-iads-_ads_object_info?branch=master) defines properties that identify the object by distinguished name, relative distinguished name, by container (ParentDN), by object type (ClassDN), and by schema definition (SchemaDN). The attribute descriptor [**ADS\_ATTR\_INFO**](/windows/win32/Iads/ns-iads-_ads_attr_info?branch=master) consists of a name, data type, an array of data values shown in [**ADSVALUE**](/windows/win32/Iads/ns-iads-_adsvalue?branch=master), and a flag that directs the underlying directory service to perform certain operations on the attributes detailed in [ADS\_ATTR\_\* constants](adsi-constants.md). The data types for these attributes include the ADSI extended syntax types, detailed in [**ADSTYPEENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0001?branch=master).

 

 




