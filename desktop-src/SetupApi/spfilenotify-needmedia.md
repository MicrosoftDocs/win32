---
Description: The SPFILENOTIFY\_NEEDMEDIA notification is sent to the callback routine when new media or a new cabinet file is required.
ms.assetid: 6a7947de-1bb3-46e0-9334-405684e58e98
title: SPFILENOTIFY\_NEEDMEDIA message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_NEEDMEDIA message

The **SPFILENOTIFY\_NEEDMEDIA** notification is sent to the callback routine when new media or a new cabinet file is required.


```C++
SPFILENOTIFY_NEEDMEDIA
  Param1 = (UINT) SourceMediaInfo;
  Param2 = (UINT) NewPathInfo;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**SOURCE\_MEDIA**](/windows/win32/Setupapi/ns-setupapi-_source_media_a?branch=master) structure.

</dd> <dt>

*Param2* 
</dt> <dd>

Pointer to a character array to store new path information supplied by the user. The buffer size is a **TCHAR** array of MAX\_PATH elements. The path information returned by your setup application should not exceed this size.

</dd> </dl>

## Return value

The callback routine should return one of the following.



| Return code                                                                                    | Description                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**FILEOP\_NEWPATH**</dt> </dl> | The media is present and the requested file is available at the path specified in the buffer pointed to by *Param2*.<br/>                                                                                         |
| <dl> <dt>**FILEOP\_SKIP**</dt> </dl>    | Skip the requested file<br/>                                                                                                                                                                                      |
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl>   | Abort queue processing. The [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) function returns **FALSE**. GetLastError returns extended error information, such as ERROR\_CANCELLED if the user canceled.<br/> |
| <dl> <dt>**FILEOP-DOIT**</dt> </dl>     | The media is available.<br/>                                                                                                                                                                                      |



 

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

[**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master)
</dt> <dt>

[**SetupDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupdefaultqueuecallbacka?branch=master)
</dt> <dt>

[**SOURCE\_MEDIA**](/windows/win32/Setupapi/ns-setupapi-_source_media_a?branch=master)
</dt> </dl>

 

 




