---
title: IGatherNotify Init (Deprecated) method
description: This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search ISearchPersistentItemsChangedSink API in the Windows SDK. | IGatherNotify Init (Deprecated) method
ms.assetid: 6a5f89eb-10f4-4262-89bf-b47e345f12eb
keywords:
- Init (Deprecated) method Legacy Windows Environment Features
- Init (Deprecated) method Legacy Windows Environment Features , IGatherNotify interface
- IGatherNotify interface Legacy Windows Environment Features , Init (Deprecated) method
topic_type:
- apiref
api_name:
- IGatherNotify.Init (Deprecated)
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IGatherNotify::Init (Deprecated) method

\[**Init** may be altered or unavailable in subsequent versions of the operating system or product.\]

This Windows Desktop Search interface topic is deprecated and is superseded by the Windows Search [**ISearchPersistentItemsChangedSink**](/windows/desktop/api/searchapi/nn-searchapi-isearchpersistentitemschangedsink) API in the Windows SDK.

Initializes the Gatherer interface. Also specifies the index to notify and the application store to monitor.

## Syntax


```C++
void Init (Deprecated)(
  [in] BSTR    bstrApplication,
  [in] BSTR    bstrProject,
  [in] variant varScopesBstrArray
);
```



## Parameters

<dl> <dt>

*bstrApplication* \[in\]
</dt> <dd>

Type: **BSTR**

A string that specifies the target application.

</dd> <dt>

*bstrProject* \[in\]
</dt> <dd>

Type: **BSTR**

A string that specifies the name of the indexer to pass gatherer information to.

</dd> <dt>

*varScopesBstrArray* \[in\]
</dt> <dd>

Type: **variant**

Optional parameter, that enables you to pass an array of scopes to be initialized.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Initialize with application="RSApp", Project="MyIndex".

 

 
