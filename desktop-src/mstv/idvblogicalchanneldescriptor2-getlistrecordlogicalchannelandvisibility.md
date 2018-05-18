---
title: IDvbLogicalChannelDescriptor2 GetListRecordLogicalChannelAndVisibility method
description: Gets the visible\_service\_flag and logical\_channel\_number fields from a Digital Video Broadcast (DVB) logical channel descriptor.
ms.assetid: '899B82FB-5667-42F1-8E28-485ADBFBF65F'
keywords: ["GetListRecordLogicalChannelAndVisibility method Microsoft TV Technologies", "GetListRecordLogicalChannelAndVisibility method Microsoft TV Technologies , IDvbLogicalChannelDescriptor2 interface", "IDvbLogicalChannelDescriptor2 interface Microsoft TV Technologies , GetListRecordLogicalChannelAndVisibility method"]
topic_type:
- apiref
api_name:
- IDvbLogicalChannelDescriptor2.GetListRecordLogicalChannelAndVisibility
api_location:
- Dvbsiparser.idl
api_type:
- COM
---

# IDvbLogicalChannelDescriptor2::GetListRecordLogicalChannelAndVisibility method

Gets the visible\_service\_flag and logical\_channel\_number fields from a Digital Video Broadcast (DVB) logical channel descriptor. The visible\_service\_flag indicates whether a service record in the DVB logical channel descriptor is visible through the receiver service list and can be selected. The logical\_channel\_number field contains a broadcaster-defined channel number that is used to order services.

## Syntax


```C++
HRESULT GetListRecordLogicalChannelAndVisibility(
  [in]  BYTE bListIndex,
  [in]  BYTE bRecordIndex,
  [out] WORD *pwVal
);
```



## Parameters

<dl> <dt>

*bListIndex* \[in\]
</dt> <dd>

Specifies the channel list record number, indexed from zero. Call the [**GetCountOfLists**](idvblogicalchannel2descriptor-getcountoflists.md) method to get the number of channel list records in the logical channel descriptor.

</dd> <dt>

*bRecordIndex* \[in\]
</dt> <dd>

Specifies the service record number, indexed from zero. Call the [**GetListCountOfRecords**](idvblogicalchannel2descriptor-getlistcountofrecords.md) method to get the number of service records in the logical channel descriptor.

</dd> <dt>

*pwVal* \[out\]
</dt> <dd>

Receives the visible\_service\_flag (defined by bit 15) and logical\_channel\_number (defined by bits 0 - 9) field values.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The combinations of visible\_service\_flag and local\_channel\_number field values have the following meanings.



| visible\_service\_flag | logical\_channel\_number | Meaning                                                                                                                                                                                                |
|------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                      | 0                        | Service not suitable for selection by the user. For example, the value zero may be used for data services intended only for selection from interactive applications or for firmware download services. |
| 1                      | 0                        | Reserved for future use.                                                                                                                                                                               |
| 0                      | 1-1024                   | Reserved for future use.                                                                                                                                                                               |
| 1                      | 1-999                    | Service is displayed in service lists and Event Schedule Guide (ESG). Service is accessible via P+/- keys or from numeric keys (same value as decimal value of logical\_channel\_number).              |
| 1                      | &gt; 999                 | Reserved.                                                                                                                                                                                              |



 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                  |
| IDL<br/>                      | <dl> <dt>Dvbsiparser.idl</dt> </dl> |



## See also

<dl> <dt>

[**IDvbLogicalChannelDescriptor2**](idvblogicalchanneldescriptor2.md)
</dt> <dt>

[**GetCountOfLists**](idvblogicalchannel2descriptor-getcountoflists.md)
</dt> <dt>

[**GetListCountOfRecords**](idvblogicalchannel2descriptor-getlistcountofrecords.md)
</dt> </dl>

 

 





