---
title: Processing Reservations
description: Reservations for portions of the URL namespace are made by the system administrator and placed in the persistent reservation store.
ms.assetid: deab6323-d114-463b-a0e7-acd173149b63
ms.topic: article
ms.date: 05/31/2018
---

# Processing Reservations

Reservations for portions of the URL namespace are made by the system administrator and placed in the persistent reservation store. The root of the URL namespace for HTTP is owned by the system administrator. For all host and port values, the following two reservations are always assumed at the root of the **relativeUri** namespace.



| Namespace reserved                 | Reserved for              |
|------------------------------------|---------------------------|
| https://&lt;host&gt;:&lt;port&gt;/  | LocalSystem Administrator |
| https://&lt;host&gt;:&lt;port&gt;/ | LocalSystem Administrator |



 

These implicit reservations cannot be removed. However, it is possible to delegate explicit root reservations to other users. Reservations such as the following would create such delegations:



| Namespace reserved        | Reserved for |
|---------------------------|--------------|
| `https://+:80/`           | UserA, UserC |
| `https://adatum.com:443/` | UserB        |



 

If these delegated reservations are removed by the system administrator, ownership of the namespace reverts to the implicit reservation for the corresponding host and port values.

 

 




