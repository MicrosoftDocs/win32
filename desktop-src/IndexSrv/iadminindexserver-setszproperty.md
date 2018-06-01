---
Description: Sets a content index registry value of type REG\_SZ, as described in Registry Entries.
ms.assetid: 22fc2023-68ea-4439-bbcf-85fcf3eca830
title: IAdminIndexServer::SetSZProperty method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAdminIndexServer::SetSZProperty method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Sets a content index registry value of type **REG\_SZ**, as described in [Registry Entries](registry-entries.md).

## Syntax


```C++
HRESULT SetSZProperty(
  [in] BSTR bstrPropName,
  [in] BSTR bstrVal
);
```



## Parameters

<dl> <dt>

*bstrPropName* \[in\]
</dt> <dd>

The name of an existing registry value of type **REG\_SZ**.

</dd> <dt>

*bstrVal* \[in\]
</dt> <dd>

The value to be stored.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method does not validate that a property name/value is a valid Indexing Service property. It is the caller's responsibility to verify that the property name and value are valid under the **HKLM\\System\\CurrentControlSet\\Control\\ContentIndex** entries. If *bstrPropName* exists, its value is set to *lVal*. Otherwise, the *bstrPropName* value name is created and set to *lVal*.

## Examples


```VB
 Set the default Catalog directory 
objAdminIS.SetSZProperty("ISAPIDefaultCatalogDirectory","system") 
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ciodm.dll</dt> </dl> |



## See also

<dl> <dt>

[**IAdminIndexServer**](iadminindexserver.md)
</dt> </dl>

 

 




