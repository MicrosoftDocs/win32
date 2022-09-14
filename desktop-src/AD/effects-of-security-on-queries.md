---
title: Effects of Security on Searching
description: Security is an implicit filter when performing searches, enumerating containers, or reading properties.
ms.assetid: 4a027069-8c3d-4a95-a04b-c9c59200a9ed
ms.tgt_platform: multiple
keywords:
- effects of security on searching Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Effects of Security on Searching

Security is an implicit filter when performing searches, enumerating containers, or reading properties.

ADSI can return NO\_SUCH\_PROPERTY or NO\_SUCH\_OBJECT errors even when the object exists if you do not have access to read attributes on the object.

For example, a caller may be able to enumerate the child objects in a container because the caller has LIST\_CONTENTS rights on the container. But the same caller may not be able to access the enumerated objects if the caller does not have read access to the child objects. In this case, a query for a child object may return NO\_SUCH\_OBJECT even though the caller successfully enumerated the object.

If the caller does not have sufficient rights, the following return codes may be returned:

E\_ADS\_INVALID\_DOMAIN\_OBJECT

E\_ADS\_PROPERTY\_NOT\_SUPPORTED

E\_ADS\_PROPERTY\_NOT\_FOUND

 

 




