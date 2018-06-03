---
title: MMCCtrl.GetBackground method
description: The GetBackground method returns the MMCDisplayObject object used for the background image.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3274b3ae-f60f-4713-87f6-23102271e4d6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetBackground method MMC
- GetBackground method MMC , MMCCtrl class
- MMCCtrl class MMC , GetBackground method
topic_type:
- apiref
api_name:
- MMCCtrl.GetBackground
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCCtrl.GetBackground method

The **GetBackground** method returns the **MMCDisplayObject** object used for the background image.

## Syntax


```VB
MMCCtrl.GetBackground( _
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

An **MMCDisplayObject** object that contains the display information for the taskpad's background image.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





