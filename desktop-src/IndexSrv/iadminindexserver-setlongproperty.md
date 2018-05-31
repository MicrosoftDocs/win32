---
title: IAdminIndexServer SetLongProperty method
description: Sets a content index registry value of type REG\_DWORD, as described in Registry Entries.
ms.assetid: 99912305-2523-43f5-87a3-6d9f1ac2a9e0
keywords:
- SetLongProperty method Indexing Service
- SetLongProperty method Indexing Service , IAdminIndexServer interface
- IAdminIndexServer interface Indexing Service , SetLongProperty method
topic_type:
- apiref
api_name:
- IAdminIndexServer.SetLongProperty
api_location:
- Ciodm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAdminIndexServer::SetLongProperty method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Sets a content index registry value of type **REG\_DWORD**, as described in [Registry Entries](registry-entries.md).

## Syntax


```C++
HRESULT SetLongProperty(
  [in] BSTR bstrPropName,
  [in] LONG lVal
);
```



## Parameters

<dl> <dt>

*bstrPropName* \[in\]
</dt> <dd>

The name of an existing registry value of type **REG\_DWORD**.

</dd> <dt>

*lVal* \[in\]
</dt> <dd>

The value to be stored.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method does not validate that a property name/value is a valid Indexing Service property. It is the caller's responsibility to verify that the property name and value are valid under the **HKLM\\System\\CurrentControlSet\\Control\\ContentIndex** entries. If *bstrPropName* exists, its value is set to *lVal*. Otherwise, the *bstrPropName* value name is created and set to *lVal*.

## Examples


```VB
' Set the current value of the flag that determines whether
'    to filter the system properties of directories.  
objAdminIS.SetLongProperty( "FilterDirectories", 1)
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ciodm.dll</dt> </dl> |



## See also

<dl> <dt>

[**IAdminIndexServer**](iadminindexserver.md)
</dt> </dl>

 

 





