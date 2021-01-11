---
description: The InstallAdminPackage action copies the product database to the administrative installation point, which is defined by the TARGETDIR property.
ms.assetid: 9781f14b-0264-4d00-9a83-bd5400c614ec
title: InstallAdminPackage Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallAdminPackage Action

The InstallAdminPackage action copies the product database to the administrative installation point, which is defined by the [**TARGETDIR**](targetdir.md) property.

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages



| Field | Description of action data                                 |
|-------|------------------------------------------------------------|
| \[1\] | Name of install files.                                     |
| \[6\] | Size of database.                                          |
| \[9\] | Identifier of administrative installation–point directory. |



 

## Remarks

The InstallAdminPackage action also updates the summary information of the database and removes any cabinet files located in streams after the database is copied.

 

 



