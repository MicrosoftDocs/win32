---
title: MMCCtrl.GetListPadInfo method
description: The GetListPadInfo method returns an MMCListPadInfo object that represents list pad information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '59bf5d87-c1c1-46a3-9770-2ae819dda18b'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["GetListPadInfo method MMC", "GetListPadInfo method MMC , MMCCtrl class", "MMCCtrl class MMC , GetListPadInfo method"]
topic_type:
- apiref
api_name:
- MMCCtrl.GetListPadInfo
api_location:
- Cic.dll
api_type:
- COM
---

# MMCCtrl.GetListPadInfo method

The **GetListPadInfo** method returns an **MMCListPadInfo** object that represents list pad information. An **MMCListPadInfo** object represents labels and a button for the **ListPad** control to be added to the taskpad page. This method should be used on list view taskpads only.

## Syntax


```VB
MMCCtrl.GetListPadInfo( _
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

An **MMCListPadInfo** object that represents list view labels and a button to be placed on a list view taskpad.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| Header<br/>          | <dl> <dt>Mmc.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





