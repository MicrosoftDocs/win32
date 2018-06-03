---
title: IIS Extensible Node Types
description: The Internet Information Services (IIS) snap-in allows extensions for the following node types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5cd0294d-f58d-4ca3-bcb0-84064ff11413
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IIS Extensible Node Types

The Internet Information Services (IIS) snap-in allows extensions for the following node types.



| Node type       | Node type GUID                         |
|-----------------|----------------------------------------|
| Child node      | {A841B6C8-7577-11D0-BB1F-00A0C922E79C} |
| File node       | {A841B6C9-7577-11D0-BB1F-00A0C922E79C} |
| Instance node   | {A841B6C7-7577-11D0-BB1F-00A0C922E79C} |
| IIS Static node | {A841B6C3-7577-11D0-BB1F-00A0C922E79C} |
| Machine node    | {A841B6C4-7577-11D0-BB1F-00A0C922E79C} |



 

## Remarks

"Child" nodes are virtual directories. Also, the globally unique identifiers (**GUID**s) for virtual directories and instances do not distinguish between FTP and WWW. Use the **ISM\_SNAPIN\_SERVICE** clipboard format to distinguish between FTP and WWW.

 

 




