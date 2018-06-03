---
title: IStoreFolder SetFlags method
description: Adds message state flags for a specified list of messages.
ms.assetid: c679601a-0459-4d1f-ba23-e8e4b2de34f9
keywords:
- SetFlags method Windows Mail (formerly Outlook Express)
- SetFlags method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , SetFlags method
topic_type:
- apiref
api_name:
- IStoreFolder.SetFlags
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IStoreFolder::SetFlags method

Adds message state flags for a specified list of messages.

## Syntax


```C++
HRESULT SetFlags(
  [in]  LPMESSAGEIDLIST pMsgIdList,
  [in]  DWORD           dwState,
  [in]  DWORD           dwStatemask,
  [out] LPDWORD         prgdwNewFlags
);
```



## Parameters

<dl> <dt>

*pMsgIdList* \[in\]
</dt> <dd>

Type: **LPMESSAGEIDLIST**

Specifies the list of messages to add state flags to.

</dd> <dt>

*dwState* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a combination of state flags to add to the messages specified by *pMsgIdList*. For a list of flags, see [**Message State Flags**](oe-message-state-flags.md).

</dd> <dt>

*dwStatemask* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be set equal to *dwState*.

</dd> <dt>

*prgdwNewFlags* \[out\]
</dt> <dd>

Type: **LPDWORD**

Array that receives **DWORD** values that correspond to the new state for each message in the list specified by *pMsgIdList*. Must have a number of elements equal to the number of elements in *pMsgIdList*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                                                                                                                |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Occurs if the value of *pMsgIdList* is **NULL**, or if the **prgdwMsgId** member value of the structure referenced by *pMsgIdList* is **NULL**.<br/> |



 

## Remarks

This method will only add flags. To remove flags, use the [**IStoreFolder::OpenMessage**](oe-istorefolder-openmessage.md) and [**IStoreFolder::CommitStream**](oe-istorefolder-commitstream.md) methods.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





