---
Description: Remotable version of the IMFContentProtectionManagerBeginEnableContent method.
ms.assetid: d06f752f-3f9a-4c7c-9c49-c886a675fe3a
title: RemoteBeginEnableContent
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteBeginEnableContent

Remotable version of the [**IMFContentProtectionManager::BeginEnableContent**](/windows/win32/mfidl/nf-mfidl-imfcontentprotectionmanager-beginenablecontent?branch=master) method.

``` syntax
[call_as(BeginEnableContent)]
HRESULT RemoteBeginEnableContent(
    REFCLSID clsidType,
    BYTE *pbData,
    DWORD cbData,
    IMFRemoteAsyncCallback *pCallback
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**BeginEnableContent**](/windows/win32/mfidl/nf-mfidl-imfcontentprotectionmanager-beginenablecontent?branch=master) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mfuuid.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**IMFContentProtectionManager**](/windows/win32/mfidl/nn-mfidl-imfcontentprotectionmanager?branch=master)
</dt> </dl>

 

 




