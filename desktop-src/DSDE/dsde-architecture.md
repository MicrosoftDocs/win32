---
Description: 'The DSDE utility takes input from either the command line or a DSML request file. It processes inputs and sends requests to the LDAP server or DSML Services for Windows server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '6ccdbc79-7ad3-441f-81ef-ef5a478f80d3'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
title: DSDE Architecture
---

# DSDE Architecture

The DSDE utility takes input from either the command line or a DSML request file. It processes inputs and sends requests to the LDAP server or DSML Services for Windows server. It receives the server response, processes the response, and returns results to the user.

DSDE operates either in import or export mode. In import mode, DSDE reads the contents of a DSML V2 request file to modify the contents of the directory. In export mode, DSDE reads the contents of the directory and outputs data to a DSML V2 data file or to the console window. DSDE can operate in only one mode at a time.

 

 



