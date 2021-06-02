---
description: Issues a command to a Windows Image Acquisition (WIA) 2.0 hardware device.
ms.assetid: a077448f-2029-4fd3-8bce-c0291afd0b79
title: IWiaItem2::DeviceCommand method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.DeviceCommand
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::DeviceCommand method

Issues a command to a Windows Image Acquisition (WIA) 2.0 hardware device.

## Syntax


```C++
HRESULT DeviceCommand(
  [in]            LONG      lFlags,
  [in]      const GUID      *pCmdGUID,
  [in, out]       IWiaItem2 **ppIWiaItem2
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> <dt>

*pCmdGUID* \[in\]
</dt> <dd>

Type: **const GUID\***

Specifies the command to send to the WIA 2.0 device. See [**WIA Device Commands**](-wia-wia-device-commands.md).

</dd> <dt>

*ppIWiaItem2* \[in, out\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\*\***

Receives the address of a pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) item created by the command, if any.

</dd> </dl>

## Return value

Type: **HRESULT**

In addition to the standard COM error codes, the method may return the following value.



| Return code                                                                                       | Description                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_CMDNOTSUPPORTED**</dt> </dl> | The command is not implemented for the [**IWiaItem2**](-wia-iwiaitem2.md) interface on which the method is called. The numeric value for this error is not yet defined. <br/> |



 

## Remarks

The behavior of this method is different depending on the category of the node on which the method is called.

When the application sends the [**WIA\_CMD\_TAKE\_PICTURE**](-wia-wia-device-commands.md) command to the device using the **IWiaItem2::DeviceCommand** method, the WIA 2.0 run-time system creates an [**IWiaItem2**](-wia-iwiaitem2.md) object to represent the image. The **IWiaItem2::DeviceCommand** method stores the address of the interface in the *ppIWiaItem2* parameter.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppIWiaItem2* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
