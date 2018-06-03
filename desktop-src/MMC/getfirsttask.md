---
title: MMCCtrl.GetFirstTask method
description: The GetFirstTask method returns an MMCTask object that represents the first task in the set of tasks to be displayed on the taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e49350d7-20f0-4546-89fb-80b0124e6986
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetFirstTask method MMC
- GetFirstTask method MMC , MMCCtrl class
- MMCCtrl class MMC , GetFirstTask method
topic_type:
- apiref
api_name:
- MMCCtrl.GetFirstTask
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCCtrl.GetFirstTask method

The **GetFirstTask** method returns an **MMCTask** object that represents the first task in the set of tasks to be displayed on the taskpad.

## Syntax


```VB
MMCCtrl.GetFirstTask( _
  ByVal szGroupText _
)
```



## Parameters

<dl> <dt>

*szGroupText* \[in\]
</dt> <dd>

A string that contains the group name that identifies the taskpad. The group name is the string that follows the hash (\#) in the string passed in the *ppViewType* parameter when MMC called [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) to display the taskpad. If no group name was specified, *szGroupText* is an empty string.

Be aware that the group name is stored in the hash property of the location object of the taskpad's HTML page. See the following example.

</dd> </dl>

## Return value

An **MMCTask** object that represents the first task to be placed on the taskpad. If there are no tasks for the taskpad, **NULL** is returned.

## Examples

The following code example gets the first task by calling the **GetFirstTask** method on an MMCCtrl control with an ID of taskctrl:


```VB
var hash = location.hash;
if (hash != "") {
    hash = hash.substr(1);
}
 
// get first task
var task = taskctrl.GetFirstTask (hash);
```



## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





