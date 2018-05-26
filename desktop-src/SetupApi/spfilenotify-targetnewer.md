---
Description: The SPFILENOTIFY\_TARGETNEWER notification is sent to the callback routine if the file to be copied was queued with the SP\_COPY\_NEWER or SP\_COPY\_FORCE\_NEWER flags specified and a newer version of the file already exists in the target directory.
ms.assetid: 93bcd610-f75d-4900-841c-f67946af5c4a
title: SPFILENOTIFY\_TARGETNEWER message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_TARGETNEWER message

The **SPFILENOTIFY\_TARGETNEWER** notification is sent to the callback routine if the file to be copied was queued with the SP\_COPY\_NEWER or SP\_COPY\_FORCE\_NEWER flags specified and a newer version of the file already exists in the target directory. It can be sent to the callback routine alone or ORed together with [**SPFILENOTIFY\_LANGMISMATCH**](spfilenotify-langmismatch.md) and/or [**SPFILENOTIFY\_TARGETEXISTS**](spfilenotify-targetexists.md).


```C++
SPFILENOTIFY_TARGETNEWER
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure that contains information about the paths for source and target files.

</dd> <dt>

*Param2* 
</dt> <dd>

This parameter is not used unless this notification is combined, by using the OR operator, with [**SPFILENOTIFY\_LANGMISMATCH**](spfilenotify-langmismatch.md).

</dd> </dl>

## Return value

The callback routine should return one of the following values.



| Return code                                                                          | Description                                            |
|--------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | Overwrite the file in the target directory.<br/> |
| <dl> <dt>**FALSE**</dt> </dl> | Skip the current copy operation.<br/>            |



 

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

[**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master)
</dt> <dt>

[**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master)
</dt> <dt>

[**SetupDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupdefaultqueuecallbacka?branch=master)
</dt> <dt>

[**SetupInstallFile**](/windows/win32/Setupapi/nf-setupapi-setupinstallfilea?branch=master)
</dt> <dt>

[**SetupInstallFileEx**](/windows/win32/Setupapi/nf-setupapi-setupinstallfileexa?branch=master)
</dt> <dt>

[**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master)
</dt> </dl>

 

 




