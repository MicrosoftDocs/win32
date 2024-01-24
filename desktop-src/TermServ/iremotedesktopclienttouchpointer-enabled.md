---
title: IRemoteDesktopClientTouchPointer Enabled property
description: Whether the touch pointer feature is enabled on the RDP app container client control.
ms.assetid: f1e2f2f2-1b96-4c5a-b0dd-fd57627c5ec3
ms.tgt_platform: multiple
keywords:
- Enabled property Remote Desktop Services
- Enabled property Remote Desktop Services , IRemoteDesktopClientTouchPointer interface
- IRemoteDesktopClientTouchPointer interface Remote Desktop Services , Enabled property
topic_type:
- apiref
api_name:
- IRemoteDesktopClientTouchPointer.Enabled
- IRemoteDesktopClientTouchPointer.get_Enabled
- IRemoteDesktopClientTouchPointer.put_Enabled
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRemoteDesktopClientTouchPointer::Enabled property

Whether the touch pointer feature is enabled on the RDP app container client control.

This property is read/write.

## Syntax


```C++
HRESULT put_Enabled(
  [in]          VARIANT_BOOL Enabled
);

HRESULT get_Enabled(
  [out, retval] VARIANT_BOOL *Enabled
);
```



## Property value

**true** if the touch pointer feature is enabled; otherwise, **false**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>              |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>              |
| IID<br/>                      | IID\_IRemoteDesktopClientTouchPointer is defined as 260EC22D-8CBC-44B5-9E88-2A37F6C93AE9<br/> |



## See also

<dl> <dt>

[**IRemoteDesktopClientTouchPointer**](/windows/win32/api/rdpappcontainerclient/nn-rdpappcontainerclient-iremotedesktopclienttouchpointer)
</dt> </dl>

 

