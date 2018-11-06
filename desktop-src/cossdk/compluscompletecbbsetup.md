---
Description: Completes a catalog migration on the destination computer.
ms.assetid: 868634ee-98b4-4f08-90b9-9af26fef44bc
title: ComPlusCompleteCbbSetup function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ComPlusCompleteCbbSetup
api_type: 
- NA
api_location: 
---

# ComPlusCompleteCbbSetup function

Completes a catalog migration on the destination computer.

## Syntax


```C++
HRESULT CALLBACK ComPlusCompleteCbbSetup(
  _In_ IUnknown *pUnk,
  _In_ HANDLE   hSetupLogFile
);
```



## Parameters

<dl> <dt>

*pUnk* \[in\]
</dt> <dd>

A pointer to the setup migration context.

</dd> <dt>

*hSetupLogFile* \[in\]
</dt> <dd>

A handle to the log file for Comsetup.dll to write to when completing the migration.

</dd> </dl>

## Return value

This method can return the standard return values E\_INVALIDARG, E\_OUTOFMEMORY, E\_UNEXPECTED, and S\_OK.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




