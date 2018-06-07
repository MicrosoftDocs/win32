---
Description: The DestroyHandoffTable function destroys a handoff table created with CreateHandoffTable.
ms.assetid: 01ae9899-4f7c-4706-a2ce-9f55b112351d
title: DestroyHandoffTable function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DestroyHandoffTable function

The **DestroyHandoffTable** function destroys a handoff table created with **CreateHandoffTable**.

## Syntax


```C++
VOID WINAPI DestroyHandoffTable(
  _In_ LPHANDOFFTABLE hTable
);
```



## Parameters

<dl> <dt>

*hTable* \[in\]
</dt> <dd>

Handle to the destroyed handoff table.

</dd> </dl>

## Return value

None.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




