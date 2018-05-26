---
Description: The SPFILENOTIFY\_NEEDNEWCABINET notification is sent by SetupIterateCabinet to indicate that the current file continues in another cabinet.
ms.assetid: 01207429-11fb-4e2c-89ba-54321992e953
title: SPFILENOTIFY\_NEEDNEWCABINET message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_NEEDNEWCABINET message

The **SPFILENOTIFY\_NEEDNEWCABINET** notification is sent by [**SetupIterateCabinet**](/windows/win32/Setupapi/nf-setupapi-setupiteratecabineta?branch=master) to indicate that the current file continues in another cabinet. Your callback routine can then call [**SetupPromptForDisk**](/windows/win32/Setupapi/nf-setupapi-setuppromptfordiska?branch=master), or create its own dialog box to prompt the user to insert the next disk.


```C++
SPFILENOTIFY_NEEDNEWCABINET
  Param1 = (UINT) CabinetInfo;
  Param2 = (UINT) NewPath;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**CABINET\_INFO**](/windows/win32/Setupapi/ns-setupapi-_cabinet_info_a?branch=master) structure that contains information about the cabinet and the file to be extracted.

</dd> <dt>

*Param2* 
</dt> <dd>

If the callback returns NO\_ERROR, this parameter is a pointer to a null-terminated string. If the string is not empty, it specifies a new path to the cabinet.

</dd> </dl>

## Return value

Your routine should return one of the following values.



| Return code                                                                                 | Description                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NO\_ERROR**</dt> </dl>    | No error was encountered, continue processing the cabinet.<br/>                                                                                                                                                                        |
| <dl> <dt>**ERROR\_*XXX***</dt> </dl> | An error of the specified type occurred. The [**SetupIterateCabinet**](/windows/win32/Setupapi/nf-setupapi-setupiteratecabineta?branch=master) function will return **FALSE**, and the specified error code will be returned by a call to [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).<br/> |



 

> [!Note]  
> There is no default cabinet callback routine; thus, you must supply a callback routine to handle the notifications sent by [**SetupIterateCabinet**](/windows/win32/Setupapi/nf-setupapi-setupiteratecabineta?branch=master).

 

## Remarks

If the callback routine returns NO\_ERROR, [**SetupIterateCabinet**](/windows/win32/Setupapi/nf-setupapi-setupiteratecabineta?branch=master) checks the buffer pointed to by *Param2*. If the buffer is not empty, then it contains a new source path. If the buffer is empty, the source path is assumed to be unchanged.

Your callback function should ensure that the cabinet is accessible before it returns, calling the [**SetupPromptForDisk**](/windows/win32/Setupapi/nf-setupapi-setuppromptfordiska?branch=master) function, if new media needs to be inserted.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Setupapi.h</dt> </dl> |



## See also

<dl> <dt>

[Overview](overview.md)
</dt> <dt>

[Notifications](notifications.md)
</dt> <dt>

[**CABINET\_INFO**](/windows/win32/Setupapi/ns-setupapi-_cabinet_info_a?branch=master)
</dt> <dt>

[**SetupIterateCabinet**](/windows/win32/Setupapi/nf-setupapi-setupiteratecabineta?branch=master)
</dt> </dl>

 

 




