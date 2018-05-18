---
title: Obtaining an Object Identifier from Microsoft
description: To extend the Active Directory schema successfully you can obtain a root OID from a script available at http //go.microsoft.com/fwlink/p/ linkid 100725.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '9ed2dd0a-620d-4856-a8a1-2d2a4468fd4c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Obtaining an Object Identifier from Microsoft"]
---

# Obtaining an Object Identifier from Microsoft

To extend the Active Directory schema successfully you can obtain a root OID from a script available at <http://go.microsoft.com/fwlink/p/?linkid=100725>. The OIDs generated from the script are unique; they are mapped from a unique GUID. Please read the best practices carefully as poorly handled OIDs can result in data loss.

> [!Note]  
> For instructions on obtaining a link-Id from Microsoft, please visit the [Linked Attributes](linked-attributes.md) topic.

 

## After You Have Obtained a Base OID

Once you have a base OID, be careful when deciding how the OIDs should be divided into categories, because these OIDs are contained in the prefix table and are part of the DC replication data. It is recommended that no more than two OID categories be created.

You can create subsequent OIDs for new schema classes and attributes by appending digits to the OID in the form of OID.X, where X may be any number that you choose. A common schema extension generally uses the following structure:

If your assigned base OID was 1.2.840.113556.1.8000.999999, you might create categories as follows.



| OID base value                            | Description                                                                                                                                                                                        |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.2.840.113556.1.8000.999999.1<br/> | Application Classes<br/> The first class would have the OID 1.2.840.113556.1.8000.999999.1.1, the second class would have the OID 1.2.840.113556.1.8000.999999.1.2, and so on.<br/>    |
| 1.2.840.113556.1.8000.999999.2<br/> | Application Attributes<br/> The first attribute's OID would be 1.2.840.113556.1.8000.999999.2.1, the second attribute's OID would be 1.2.840.113556.1.8000.999999.2.2, and so on.<br/> |



 

 

 





