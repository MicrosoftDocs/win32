---
Description: Remotable version of the IMFContentProtectionManagerEndEnableContent method.
ms.assetid: aa7a2b3a-5982-4fd8-b5de-7439fc374dfa
title: RemoteEndEnableContent
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemoteEndEnableContent

Remotable version of the [**IMFContentProtectionManager::EndEnableContent**](/windows/win32/mfidl/nf-mfidl-imfcontentprotectionmanager-endenablecontent?branch=master) method.

``` syntax
[call_as(EndEnableContent)]
HRESULT RemoteEndEnableContent(
    IUnknown *pResult
);
```

## Remarks

Applications cannot call this method directly, and objects do not implement this method. The method does not appear in the vtable for the interface. If [**EndEnableContent**](/windows/win32/mfidl/nf-mfidl-imfcontentprotectionmanager-endenablecontent?branch=master) is called across process boundaries, the Media Foundation proxy/stub DLL translates the call into a call to the remote method and then translates it back.

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

 

 




