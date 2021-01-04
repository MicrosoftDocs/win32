---
title: IMsRdpClient4 interface
description: Provides the methods and properties needed to configure and use the client control. Derives from the IMsRdpClient3 interface.
ms.assetid: c3382a86-f044-4924-b69b-5907f2506eb6
ms.tgt_platform: multiple
keywords:
- IMsRdpClient4 interface Remote Desktop Services
- IMsRdpClient4 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClient4
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient4 interface

Provides the methods and properties needed to configure and use the client control. Derives from the [**IMsRdpClient3**](imsrdpclient3.md) interface.

## Members

The **IMsRdpClient4** interface inherits from [**IMsRdpClient3**](imsrdpclient3.md). **IMsRdpClient4** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsRdpClient4** interface has these properties.



| Property                                                                | Access type          | Description                                                                                             |
|:------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------|
| [**AdvancedSettings5**](imsrdpclient4-advancedsettings5.md)<br/> | Read-only<br/> | An [**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md) interface pointer.<br/> |



 

## Remarks

The **IMsRdpClient4** interface has been extended by the following interfaces, with each new interface inheriting all the methods and properties of the previous interfaces:

-   [**IMsRdpClient5**](imsrdpclient5.md)
-   [**IMsRdpClient6**](imsrdpclient6.md)
-   [**IMsRdpClient7**](imsrdpclient7.md)
-   [**IMsRdpClient8**](imsrdpclient8.md)
-   [**IMsRdpClient9**](imsrdpclient9.md)
-   [**IMsRdpClient10**](imsrdpclient10.md)

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CLSID<br/>                    | CLSID\_MsRdpClient10 is defined as C0EFA91A-EEB7-41C7-97FA-F0ED645EFB24<br/> CLSID\_MsRdpClient10NotSafeForScripting is defined as A0C63C30-F08D-4AB4-907C-34905D770C7D<br/> CLSID\_MsRdpClient4 is defined as 4EDCB26C-D24C-4E72-AF07-B576699AC0DE<br/> CLSID\_MsRdpClient4a is defined as 54CE37E0-9834-41AE-9896-4DAB69DC022B<br/> CLSID\_MsRdpClient4NotSafeForScripting is defined as 6AE29350-321B-42BE-BBE5-12FB5270C0DE<br/> CLSID\_MsRdpClient5 is defined as 4EB89FF4-7F78-4A0F-8B8D-2BF02E94E4B2<br/> CLSID\_MsRdpClient5NotSafeForScripting is defined as 4EB2F086-C818-447E-B32C-C51CE2B30D31<br/> CLSID\_MsRdpClient6 is defined as 7390F3D8-0439-4C05-91E3-CF5CB290C3D0<br/> CLSID\_MsRdpClient6NotSafeForScripting is defined as D2EA46A7-C2BF-426B-AF24-E19C44456399<br/> CLSID\_MsRdpClient7 is defined as A9D7038D-B5ED-472E-9C47-94BEA90A5910<br/> CLSID\_MsRdpClient7NotSafeForScripting is defined as 54D38BF7-B1EF-4479-9674-1BD6EA465258<br/> CLSID\_MsRdpClient8 is defined as 5F681803-2900-4C43-A1CC-CF405404A676<br/> CLSID\_MsRdpClient8NotSafeForScripting is defined as A3BC03A0-041D-42E3-AD22-882B7865C9C5<br/> CLSID\_MsRdpClient9 is defined as 301B94BA-5D25-4A12-BFFE-3B6E7A616585<br/> CLSID\_MsRdpClient9NotSafeForScripting is defined as 8B918B82-7985-4C24-89DF-C33AD2BBFBCD<br/> |
| IID<br/>                      | IID\_IMsRdpClient4 is defined as 095E0738-D97D-488b-B9F6-DD0E8D66C0DE<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



## See also

<dl> <dt>

[**IMsRdpClient3**](imsrdpclient3.md)
</dt> <dt>

[**IMsRdpClient2**](imsrdpclient2.md)
</dt> <dt>

[**IMsRdpClient**](imsrdpclient-interface.md)
</dt> <dt>

[**IMsTscAx**](imstscax-interface.md)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

 





