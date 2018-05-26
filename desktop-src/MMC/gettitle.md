---
title: MMCCtrl.GetTitle method
description: The GetTitle method returns the string to be used for the taskpads title.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 65a9faa8-b2ec-42a3-9521-d991aedf0ace
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetTitle method MMC
- GetTitle method MMC , MMCCtrl class
- MMCCtrl class MMC , GetTitle method
topic_type:
- apiref
api_name:
- MMCCtrl.GetTitle
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCCtrl.GetTitle method

The **GetTitle** method returns the string to be used for the taskpad's title.

## Syntax


```VB
MMCCtrl.GetTitle( _
  ByVal szGroupText _
)
```



## Parameters

<dl> <dt>

*szGroupText* \[in\]
</dt> <dd>

A string that contains the group name that identifies the taskpad. The group name is the string that follows the hash (\#) in the string passed in the *ppViewType* parameter when MMC called [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) to display the taskpad. If no group name was specified, *szGroupText* is an empty string.

Be aware that the group name is stored in the hash property of the location object of the taskpad's HTML page. See the following example.

</dd> </dl>

## Return value

String that contains the taskpad title.

## Examples

The following code example gets the title string by calling the **GetTitle** method on an MMCCtrl control with an ID of taskctrl:


```VB
var mszTaskpadTitle;
var hash = location.hash;
if (hash != "") {
    hash = hash.substr(1);
}
 
// get taskpad title
mszTaskpadTitle = taskctrl.GetTitle (hash);
```



## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





