---
description: Shuts down the user name resolution thread.
ms.assetid: 6c4544b9-81e7-4a72-aa00-70011e5cd85a
title: DiskQuotaControl.ShutdownNameResolution method (Dskquota.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.ShutdownNameResolution
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.ShutdownNameResolution method

Shuts down the user name resolution thread.

## Syntax


```JScript
DiskQuotaControl.ShutdownNameResolution()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The security identifier (SID) name resolver translates SID to user names on a background thread. This thread is shut down automatically when the associated quota control object is destroyed. However, there are some cases when the thread is no longer needed, but the object is not yet ready to be destroyed. A typical example is when no further processing is taking place, but clients are still holding references to the object. The **ShutdownNameResolution** method allows you to terminate the resolver thread and free the associated resources without destroying the quota control object.

> [!Note]  
> When you shut down the resolver thread, asynchronous name resolution immediately stops. If calls are subsequently made to methods such as [**AddUser**](diskquotacontrol-adduser.md) or [**FindUser**](diskquotacontrol-finduser.md), the quota object might re-create the resolver thread.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Dskquota.h</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> </dl>

 

 




