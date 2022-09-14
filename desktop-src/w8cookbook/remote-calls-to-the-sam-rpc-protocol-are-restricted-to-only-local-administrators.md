---
title: Remote calls to the SAM RPC protocol are restricted to only local administrators
description: The SAM RPC protocol is being restricted. This means that only members of the local Administrator group can make remote calls against methods in this protocol. Active Directory domain controller behavior is unaffected.
ms.assetid: 816BFB8C-A8EE-44F4-864D-748AF8BCF1F8
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Remote calls to the SAM RPC protocol are restricted to only local administrators

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The SAM RPC protocol is being restricted. This means that only members of the local Administrator group can make remote calls against methods in this protocol. Active Directory domain controller behavior is unaffected.

## Mitigations

Ensure that the right users are set as administrators on the PC. The ACL used for the access check is configurable via group policy.

 

 




