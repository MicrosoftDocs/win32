---
Description: The Add method adds the attribute at the specified index.
ms.assetid: 5b74c177-bf5c-4547-bebb-034a9a10be13
title: ITAttributeList::Add method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITAttributeList::Add method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Add** method adds the attribute at the specified index.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of the attribute to add.

</dd> <dt>

*pAttribute* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the value of the attribute to add.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *Index* or *pAttribute* parameter is not valid.<br/>  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The application must use [**SysAllocString**](https://msdn.microsoft.com/en-us/library/ms221458(v=VS.71).aspx) to allocate memory for the *pAttribute* parameter and use [**SysFreeString**](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx) to free the memory when the variable is no longer needed.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITAttributeList**](itattributelist.md)
</dt> </dl>

 

 




