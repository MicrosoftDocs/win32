---
title: IGatherNotify AddScope (Deprecated) method
description: This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search ISearchPersistentItemsChangedSink API in the Windows SDK. | IGatherNotify AddScope (Deprecated) method
ms.assetid: 3b250818-1876-40b2-9a85-91f2bf6f52ec
keywords:
- AddScope (Deprecated) method Legacy Windows Environment Features
- AddScope (Deprecated) method Legacy Windows Environment Features , IGatherNotify interface
- IGatherNotify interface Legacy Windows Environment Features , AddScope (Deprecated) method
topic_type:
- apiref
api_name:
- IGatherNotify.AddScope (Deprecated)
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IGatherNotify::AddScope (Deprecated) method

\[**AddScope** may be altered or unavailable in subsequent versions of the operating system or product.\]

This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search [**ISearchPersistentItemsChangedSink**](/windows/desktop/api/searchapi/nn-searchapi-isearchpersistentitemschangedsink) API in the Windows SDK.

Adds the start page or URL you are monitoring. This initiates an incremental crawl when you connect, and then assumes all further URL changes are by notification.

## Syntax


```C++
void AddScope (Deprecated)(
  [in] BSTR bstrScope
);
```



## Parameters

<dl> <dt>

*bstrScope* \[in\]
</dt> <dd>

Type: **BSTR**

A string that specifies the start page or URLthat you are monitoring.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Calling this method starts an incremental crawl when connected to the store. Thereafter, it is assumed that all URL changes are by notification after the initial update.

 

 
