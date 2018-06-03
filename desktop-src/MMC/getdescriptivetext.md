---
title: MMCCtrl.GetDescriptiveText method
description: The GetDescriptiveText method returns the taskpad's description.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c4ee273-10a1-4fa5-afc9-3213a9494376
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetDescriptiveText method MMC
- GetDescriptiveText method MMC , MMCCtrl class
- MMCCtrl class MMC , GetDescriptiveText method
topic_type:
- apiref
api_name:
- MMCCtrl.GetDescriptiveText
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCCtrl.GetDescriptiveText method

The **GetDescriptiveText** method returns the taskpad's description.

## Syntax


```VB
MMCCtrl.GetDescriptiveText( _
  ByVal szGroupText _
)
```



## Parameters

<dl> <dt>

*szGroupText* \[in\]
</dt> <dd>

A string that contains the group name that identifies the taskpad. The group name is the string that follows the hash (\#) in the string passed in the *ppViewType* parameter when MMC called **IComponent::GetResultViewType** to display the taskpad. If no group name was specified, *szGroupText* is an empty string.

Be aware that the group name is stored in the hash property of the location object of the taskpad's HTML page.

</dd> </dl>

## Return value

String that contains the taskpad's description.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| Header<br/>          | <dl> <dt>Mmc.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





