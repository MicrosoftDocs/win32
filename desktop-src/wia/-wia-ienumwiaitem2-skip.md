---
description: Skips the specified number of items during an enumeration of available IWiaItem2 objects.
ms.assetid: 7a5e9e1c-1e6e-4de0-9499-bf89e35c19aa
title: IEnumWiaItem2::Skip method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumWiaItem2.Skip
api_type: 
- COM
api_location: 
- Wia.h
---

# IEnumWiaItem2::Skip method

Skips the specified number of items during an enumeration of available [**IWiaItem2**](-wia-iwiaitem2.md) objects.

## Syntax


```C++
HRESULT Skip(
  [in] ULONG cElt
);
```



## Parameters

<dl> <dt>

*cElt* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the number of items to skip.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




