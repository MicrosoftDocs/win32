---
title: D1103 Leaked Handle
ms.assetid: 9bb08cd6-104a-4168-b14e-3caec1679388
description: 
keywords:
- D1103 Leaked Handle Direct2D
topic_type:
- apiref
api_name:
- D1103 Leaked Handle
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D1103: Leaked Handle

An interface \[*interface*\] was created but not released.

## Placeholders

<dl> <dt>

<span id="interface"></span><span id="INTERFACE"></span>*interface*
</dt> <dd>

The address of the interface.

</dd> </dl> 

|             |       |
|-------------|-------|
| Error Level | Error |



 

## Possible Causes

Invalid resource usage. An application fails to release an interface when it is no longer in use.

 

 




