---
Description: 'Retrieves the number of tablets attached to the system.'
ms.assetid: 'b2027336-611b-4d17-8943-f16770effaf8'
title: 'ITabletManager::GetTabletCount method'
---

# ITabletManager::GetTabletCount method

Retrieves the number of tablets attached to the system.

## Syntax


```C++
HRESULT GetTabletCount(
  [out] ULONG *pcTablets
);
```



## Parameters

<dl> <dt>

*pcTablets* \[out\]
</dt> <dd>

The number of tablets attached to the system.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletManager Interface**](itabletmanager.md)
</dt> </dl>

 

 




