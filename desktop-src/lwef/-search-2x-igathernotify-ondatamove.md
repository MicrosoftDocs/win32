---
title: IGatherNotify OnDataMove (Deprecated) method
description: This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search ISearchPersistentItemsChangedSink API in the Windows SDK. | IGatherNotify OnDataMove (Deprecated) method
ms.assetid: cc223d0f-6508-4e38-b365-c60660db5324
keywords:
- OnDataMove (Deprecated) method Legacy Windows Environment Features
- OnDataMove (Deprecated) method Legacy Windows Environment Features , IGatherNotify interface
- IGatherNotify interface Legacy Windows Environment Features , OnDataMove (Deprecated) method
topic_type:
- apiref
api_name:
- IGatherNotify.OnDataMove (Deprecated)
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IGatherNotify::OnDataMove (Deprecated) method

\[**OnDataMove** may be altered or unavailable in subsequent versions of the operating system or product.\]

This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search [**ISearchPersistentItemsChangedSink**](/windows/desktop/api/searchapi/nn-searchapi-isearchpersistentitemschangedsink) API in the Windows SDK.

This method notifies the indexer of data that has been moved. When it sends the notification to the indexer, it includes the old address, new address, and logical address.

## Syntax


```C++
void OnDataMove (Deprecated)(
  [in] long eChangeAdviseSemantics,
  [in] BSTR bstrOldAddress,
  [in] BSTR bstrNewAddress,
  [in] BSTR bstrLogicalAddress
);
```



## Parameters

<dl> <dt>

*eChangeAdviseSemantics* \[in\]
</dt> <dd>

Type: **long**

An enumerated parameter that describes the type of move that occurred.

</dd> <dt>

*bstrOldAddress* \[in\]
</dt> <dd>

Type: **BSTR**

The old address of the item that moved. For normal files,*eChangeAdviseSematics* is **NULL**. For a folder or directory, set*eChangeAdviseSematics*to GTHR\_CA\_SEMANTICS\_DIRECTORY.

</dd> <dt>

*bstrNewAddress* \[in\]
</dt> <dd>

Type: **BSTR**

The new address of the item that moved.

</dd> <dt>

*bstrLogicalAddress* \[in\]
</dt> <dd>

Type: **BSTR**

The logical address of the item that moved.

</dd> </dl>

## Return value

This method does not return a value.

 

 
