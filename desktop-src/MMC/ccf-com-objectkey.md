---
title: CCF\_COM\_OBJECTKEY clipboard format
description: The CCF\_COM\_OBJECTKEY clipboard format returns the object key (CLSID, GUID, or IID) for the selected node. Object keys are defined for the Application, Component, and Interface node types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8e138969-6aa8-41c6-ab7a-e80ced91a873
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_COM_OBJECTKEY clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_COM_OBJECTKEY
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCF\_COM\_OBJECTKEY clipboard format

The **CCF\_COM\_OBJECTKEY** clipboard format returns the object key (CLSID, GUID, or IID) for the selected node. Object keys are defined for the Application, Component, and Interface node types.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string. If an object key is not defined for the selected node, an empty string, L"", is the returned data.

 

 




