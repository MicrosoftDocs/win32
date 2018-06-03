---
title: Enumerating Application Directory Partitions in a Forest
description: Like domain partitions, every application directory partition is represented by a crossRef object in the Partitions container of the configuration partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dd1ff72d-ed19-4e8c-a401-a5b1b3d577e8
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Enumerating Application Directory Partitions in a Forest AD
- Application Directory Partitions AD , Enumerating in a Forest
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Application Directory Partitions in a Forest

Like domain partitions, every application directory partition is represented by a [**crossRef**](https://msdn.microsoft.com/library/ms681007) object in the Partitions container of the configuration partition. Each **crossRef** object stores data about its corresponding partition.

A [**crossRef**](https://msdn.microsoft.com/library/ms681007) object that represents a domain partition is distinguished from a **crossRef** object that represents an application directory partition by the contents of the [**systemFlags**](https://msdn.microsoft.com/library/ms680022) attribute. The **crossRef** object that represents a domain partition will have both the [**ADS\_SYSTEMFLAG\_CR\_NTDS\_NC**](https://msdn.microsoft.com/library/aa772297) and **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flags set in the **systemFlags** attribute. The **crossRef** object that represents an application directory partition will have the **ADS\_SYSTEMFLAG\_CR\_NTDS\_NC** flag set and the **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flag will not be set in the **systemFlags** attribute.

The [**crossRef**](https://msdn.microsoft.com/library/ms681007) objects that represent the Schema and Configuration partitions will also have the have [**ADS\_SYSTEMFLAG\_CR\_NTDS\_NC**](https://msdn.microsoft.com/library/aa772297) flag set and the **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flag will not be set in the [**systemFlags**](https://msdn.microsoft.com/library/ms680022) attribute. This requires that these two **crossRef** objects be distinguished by the contents of the [**nCName**](https://msdn.microsoft.com/library/ms678699) attribute. The **nCName** attribute for the **crossRef** object that represents the Schema container will be identical to the **schemaNamingContext** attribute of the RootDSE object. Similarly, the **nCName** attribute for the **crossRef** object that represents the Configuration container will be identical to the **configurationNamingContext** attribute of the RootDSE object.

**To identify all application directory partitions in a forest, perform the following steps**

1.  In the Partitions container of the configuration partition, search for or enumerate all [**crossRef**](https://msdn.microsoft.com/library/ms681007) objects.
2.  If a [**crossRef**](https://msdn.microsoft.com/library/ms681007) object does not have the [**ADS\_SYSTEMFLAG\_CR\_NTDS\_NC**](https://msdn.microsoft.com/library/aa772297) flag set or has the **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flag set in the [**systemFlags**](https://msdn.microsoft.com/library/ms680022) attribute value, exclude the object from the result set.
3.  Exclude the Schema partition from the result set by comparing the [**nCName**](https://msdn.microsoft.com/library/ms678699) attribute of the [**crossRef**](https://msdn.microsoft.com/library/ms681007) object to the **schemaNamingContext** attribute of the RootDSE object.
4.  Exclude the Configuration partition from the result set by comparing the [**nCName**](https://msdn.microsoft.com/library/ms678699) attribute of the [**crossRef**](https://msdn.microsoft.com/library/ms681007) object to the **configurationNamingContext** attribute of the RootDSE object.
5.  The remaining [**crossRef**](https://msdn.microsoft.com/library/ms681007) objects in the result set all represent application directory partitions.

 

 




