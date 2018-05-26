---
Description: The SPFILENOTIFY\_FILEOPDELAYED notification is sent by SetupInstallFileEx or SetupCommitFileQueue to a callback routine when a file operation was delayed because the file was in use. The operation will be processed the next time the system is rebooted.
ms.assetid: a0b38e2b-2390-49e5-b288-77c31636e696
title: SPFILENOTIFY\_FILEOPDELAYED message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_FILEOPDELAYED message

The **SPFILENOTIFY\_FILEOPDELAYED** notification is sent by [**SetupInstallFileEx**](/windows/win32/Setupapi/nf-setupapi-setupinstallfileexa?branch=master) or [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) to a callback routine when a file operation was delayed because the file was in use. The operation will be processed the next time the system is rebooted.


```C++
SPFILENOTIFY_FILEOPDELAYED
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure.

If the delayed operation is a file copy operation, the [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure contains the following information.



| FILEPATHS member | Value                                |
|------------------|--------------------------------------|
| **Win32Error**   | NO\_ERROR                            |
| **Flags**        | FILEOP\_COPY                         |
| **Source**       | Full path of the temporary file.     |
| **Target**       | Full path of the actual target file. |



 

This temporary file will be copied to the target directory when the system is rebooted. The setup functions automatically generate a path for the temporary file.

If the delayed operation is a file delete operation, the [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure contains the following information.



| FILEPATHS member | Value                                |
|------------------|--------------------------------------|
| **Win32Error**   | NO\_ERROR                            |
| **Flags**        | FILEOP\_DELETE                       |
| **Source**       | NULL                                 |
| **Target**       | Full path of the file to be deleted. |



 

</dd> <dt>

*Param2* 
</dt> <dd>

Is not used.

</dd> </dl>

## Return value

The return value is ignored.

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

[**SetupInstallFile**](/windows/win32/Setupapi/nf-setupapi-setupinstallfilea?branch=master)
</dt> <dt>

[**SetupInstallFileEx**](/windows/win32/Setupapi/nf-setupapi-setupinstallfileexa?branch=master)
</dt> <dt>

[**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master)
</dt> </dl>

 

 




