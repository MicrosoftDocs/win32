---
title: Enumerating Application Directory Partitions in a Forest
description: Like domain partitions, every application directory partition is represented by a crossRef object in the Partitions container of the configuration partition.
ms.assetid: dd1ff72d-ed19-4e8c-a401-a5b1b3d577e8
ms.tgt_platform: multiple
keywords:
- Enumerating Application Directory Partitions in a Forest AD
- Application Directory Partitions AD , Enumerating in a Forest
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Application Directory Partitions in a Forest

Like domain partitions, every application directory partition is represented by a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object in the Partitions container of the configuration partition. Each **crossRef** object stores data about its corresponding partition.

A [**crossRef**](/windows/desktop/ADSchema/c-crossref) object that represents a domain partition is distinguished from a **crossRef** object that represents an application directory partition by the contents of the [**systemFlags**](/windows/desktop/ADSchema/a-systemflags) attribute. The **crossRef** object that represents a domain partition will have both the [**ADS\_SYSTEMFLAG\_CR\_NTDS\_NC**](/windows/win32/api/iads/ne-iads-ads_systemflag_enum) and **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flags set in the **systemFlags** attribute. The **crossRef** object that represents an application directory partition will have the **ADS\_SYSTEMFLAG\_CR\_NTDS\_NC** flag set and the **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flag will not be set in the **systemFlags** attribute.

The [**crossRef**](/windows/desktop/ADSchema/c-crossref) objects that represent the Schema and Configuration partitions will also have the have [**ADS\_SYSTEMFLAG\_CR\_NTDS\_NC**](/windows/win32/api/iads/ne-iads-ads_systemflag_enum) flag set and the **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flag will not be set in the [**systemFlags**](/windows/desktop/ADSchema/a-systemflags) attribute. This requires that these two **crossRef** objects be distinguished by the contents of the [**nCName**](/windows/desktop/ADSchema/a-ncname) attribute. The **nCName** attribute for the **crossRef** object that represents the Schema container will be identical to the **schemaNamingContext** attribute of the RootDSE object. Similarly, the **nCName** attribute for the **crossRef** object that represents the Configuration container will be identical to the **configurationNamingContext** attribute of the RootDSE object.

**To identify all application directory partitions in a forest, perform the following steps**

1.  In the Partitions container of the configuration partition, search for or enumerate all [**crossRef**](/windows/desktop/ADSchema/c-crossref) objects.
2.  If a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object does not have the [**ADS\_SYSTEMFLAG\_CR\_NTDS\_NC**](/windows/win32/api/iads/ne-iads-ads_systemflag_enum) flag set or has the **ADS\_SYSTEMFLAG\_CR\_NTDS\_DOMAIN** flag set in the [**systemFlags**](/windows/desktop/ADSchema/a-systemflags) attribute value, exclude the object from the result set.
3.  Exclude the Schema partition from the result set by comparing the [**nCName**](/windows/desktop/ADSchema/a-ncname) attribute of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object to the **schemaNamingContext** attribute of the RootDSE object.
4.  Exclude the Configuration partition from the result set by comparing the [**nCName**](/windows/desktop/ADSchema/a-ncname) attribute of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object to the **configurationNamingContext** attribute of the RootDSE object.
5.  The remaining [**crossRef**](/windows/desktop/ADSchema/c-crossref) objects in the result set all represent application directory partitions.

 

 