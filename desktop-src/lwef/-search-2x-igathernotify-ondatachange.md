---
title: IGatherNotify OnDataChange (Deprecated) method
description: This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search ISearchPersistentItemsChangedSink API in the Windows SDK. | IGatherNotify OnDataChange (Deprecated) method
ms.assetid: 0cbfa6b7-44f0-41f0-93a3-d5941b5822de
keywords:
- OnDataChange (Deprecated) method Legacy Windows Environment Features
- OnDataChange (Deprecated) method Legacy Windows Environment Features , IGatherNotify interface
- IGatherNotify interface Legacy Windows Environment Features , OnDataChange (Deprecated) method
topic_type:
- apiref
api_name:
- IGatherNotify.OnDataChange (Deprecated)
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IGatherNotify::OnDataChange (Deprecated) method

\[**OnDataChange** may be altered or unavailable in subsequent versions of the operating system or product.\]

This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search [**ISearchPersistentItemsChangedSink**](/windows/desktop/api/searchapi/nn-searchapi-isearchpersistentitemschangedsink) API in the Windows SDK.

This method notifies the indexer of data that has changed. When it sends the notification to the indexer, it includes the type of change, physical address, and logical address.

## Syntax


```C++
void OnDataChange (Deprecated)(
  [in] long eChangeAdvise,
  [in] BSTR bstrPhysicalAddress,
  [in] BSTR bstrLogicalAddress
);
```



## Parameters

<dl> <dt>

*eChangeAdvise* \[in\]
</dt> <dd>

Type: **long**

An enumerated value that specifies the type of change.

</dd> <dt>

*bstrPhysicalAddress* \[in\]
</dt> <dd>

Type: **BSTR**

The physical address of the item that changed.

</dd> <dt>

*bstrLogicalAddress* \[in\]
</dt> <dd>

Type: **BSTR**

The logical address of the item that changed.

</dd> </dl>

## Return value

This method does not return a value.

 

 
