---
title: IRangeList Save method
description: Returns a copy of the internal message range list representation that can be loaded later by using the IRangeList Load method.
ms.assetid: 'd63bb393-3fc1-4cd3-a75c-e765a6c7a212'
keywords: ["Save method Windows Mail (formerly Outlook Express)", "Save method Windows Mail (formerly Outlook Express) , IRangeList interface", "IRangeList interface Windows Mail (formerly Outlook Express) , Save method"]
topic_type:
- apiref
api_name:
- IRangeList.Save
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRangeList::Save method

\[**IRangeList::Save** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a copy of the internal message range list representation that can be loaded later by using the [**IRangeList::Load**](oe-irangelist-load.md) method.

## Syntax


```C++
HRESULT Save(
  [out] byte  **ppbDestination,
  [out] ULONG *pulSizeOfDestination
);
```



## Parameters

<dl> <dt>

*ppbDestination* \[out\]
</dt> <dd>

Type: **byte\*\***

Receives the address of a pointer to a copy of the internal range list.

</dd> <dt>

*pulSizeOfDestination* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the size (in bytes) of the data pointed to by *ppbDestination*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

Failure to allocate memory is typically the reason for failure.

> \[!Caution\]  
> The internal range list representation is not suitable for network transmittal.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





