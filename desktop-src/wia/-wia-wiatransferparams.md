---
description: The WiaTransferParams is transmitted to an application during a data transfer by the Windows Image Acquisition (WIA) run-time system to the IWiaTransferCallback::TransferCallback method.
ms.assetid: 4f1bbacf-e9fd-4129-ab05-3edaeecfaf43
title: WiaTransferParams structure (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WiaTransferParams
api_type: 
- HeaderDef
api_location: 
- Wia.h
---

# WiaTransferParams structure

The **WiaTransferParams** is transmitted to an application during a data transfer by the Windows Image Acquisition (WIA) run-time system to the [**IWiaTransferCallback::TransferCallback**](-wia-iwiatransfercallback-transfercallback.md) method.

## Syntax


```C++
typedef struct _WiaTransferParams {
  LONG    lMessage;
  LONG    lPercentComplete;
  ULONG64 ulTransferredBytes;
  HRESULT hrErrorStatus;
} WiaTransferParams;
```



## Members

<dl> <dt>

**lMessage**
</dt> <dd>

Type: **LONG**

</dd> <dd>

Indicates the status of the data transfer.

<dt>

<span id="WIA_TRANSFER_MSG_STATUS"></span><span id="wia_transfer_msg_status"></span>

<span id="WIA_TRANSFER_MSG_STATUS"></span><span id="wia_transfer_msg_status"></span>**WIA\_TRANSFER\_MSG\_STATUS**


</dt> <dd></dd> <dt>

<span id="WIA_TRANSFER_MSG_END_OF_STREAM"></span><span id="wia_transfer_msg_end_of_stream"></span>

<span id="WIA_TRANSFER_MSG_END_OF_STREAM"></span><span id="wia_transfer_msg_end_of_stream"></span>**WIA\_TRANSFER\_MSG\_END\_OF\_STREAM**


</dt> <dd></dd> <dt>

<span id="WIA_TRANSFER_MSG_END_OF_TRANSFER"></span><span id="wia_transfer_msg_end_of_transfer"></span>

<span id="WIA_TRANSFER_MSG_END_OF_TRANSFER"></span><span id="wia_transfer_msg_end_of_transfer"></span>**WIA\_TRANSFER\_MSG\_END\_OF\_TRANSFER**


</dt> <dd></dd> <dt>

<span id="WIA_TRANSFER_MSG_DEVICE_STATUS"></span><span id="wia_transfer_msg_device_status"></span>

<span id="WIA_TRANSFER_MSG_DEVICE_STATUS"></span><span id="wia_transfer_msg_device_status"></span>**WIA\_TRANSFER\_MSG\_DEVICE\_STATUS**


</dt> <dd></dd> <dt>

<span id="WIA_TRANSFER_MSG_NEW_PAGE"></span><span id="wia_transfer_msg_new_page"></span>

<span id="WIA_TRANSFER_MSG_NEW_PAGE"></span><span id="wia_transfer_msg_new_page"></span>**WIA\_TRANSFER\_MSG\_NEW\_PAGE**


</dt> <dd></dd> </dl> </dd> <dt>

**lPercentComplete**
</dt> <dd>

Type: **LONG**

</dd> <dd>

Indicates the progress of the data transfer as a percentage.

</dd> <dt>

**ulTransferredBytes**
</dt> <dd>

Type: **ULONG64**

</dd> <dd>

Indicates the amount of data transferred.

</dd> <dt>

**hrErrorStatus**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

The status, or error state, of the device set by the driver; for example, "warming up".

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl> |



 

 




