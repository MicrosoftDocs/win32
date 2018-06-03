---
title: StorPortEtwEvent8 routine
description: The StorPortEtwEvent8 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log eight general purpose ETW parameters. The ETW parameters are expressed as eight name-value pairs.
ms.assetid: FC0E8267-5AA6-47D6-9F98-B6B19CA3F260
keywords:
- StorPortEtwEvent8 routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortEtwEvent8
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortEtwEvent8 routine

The **StorPortEtwEvent8** publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log eight general purpose ETW parameters. The ETW parameters are expressed as eight name-value pairs.

## Syntax


```C++
ULONG StorPortEtwEvent8(
  _In_     PVOID                     HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS             Address,
  _In_     ULONG                     EventId,
  _In_     PWSTR                     EventDescription,
  _In_     ULONGLONG                 EventKeywords,
  _In_     STORPORT_ETW_LEVEL        EventLevel,
  _In_     STORPORT_ETW_EVENT_OPCODE EventOpcode,
  _In_opt_ PSCSI_REQUEST_BLOCK       Srb,
  _In_opt_ PWSTR                     Parameter1Name,
  _In_     ULONGLONG                 Parameter1Value,
  _In_opt_ PWSTR                     Parameter2Name,
  _In_     ULONGLONG                 Parameter2Value,
  _In_opt_ PWSTR                     Parameter3Name,
  _In_     ULONGLONG                 Parameter3Value,
  _In_opt_ PWSTR                     Parameter4Name,
  _In_     ULONGLONG                 Parameter4Value,
  _In_opt_ PWSTR                     Parameter5Name,
  _In_     ULONGLONG                 Parameter5Value,
  _In_opt_ PWSTR                     Parameter6Name,
  _In_     ULONGLONG                 Parameter6Value,
  _In_opt_ PWSTR                     Parameter7Name,
  _In_     ULONGLONG                 Parameter7Value,
  _In_opt_ PWSTR                     Parameter8Name,
  _In_     ULONGLONG                 Parameter8Value
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Address* \[in, optional\]
</dt> <dd>

The storage unit device address. This parameter is NULL for adapter devices.

</dd> <dt>

*EventId* \[in\]
</dt> <dd>

A miniport defined identifier for the ETW event.

</dd> <dt>

*EventDescription* \[in\]
</dt> <dd>

The description text for the event. This text string must be &lt;= STORPORT\_ETW\_MAX\_DESCRIPTION\_LENGTH.

</dd> <dt>

*EventKeywords* \[in\]
</dt> <dd>

Keyword flags for event categorization. Set to 0 if no keyword is desired. The keywords are a bitwise OR combination of the following.



| Value                                                                                                                                                                                                                                       | Meaning                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <span id="STORPORT_ETW_EVENT_KEYWORD_IO"></span><span id="storport_etw_event_keyword_io"></span><dl> <dt>**STORPORT\_ETW\_EVENT\_KEYWORD\_IO**</dt> </dl>                            | The event is related to device IO operations.<br/> |
| <span id="STORPORT_ETW_EVENT_KEYWORD_PERFORMANCE"></span><span id="storport_etw_event_keyword_performance"></span><dl> <dt>**STORPORT\_ETW\_EVENT\_KEYWORD\_PERFORMANCE**</dt> </dl> | The event is performance related.<br/>             |
| <span id="STORPORT_ETW_EVENT_KEYWORD_POWER"></span><span id="storport_etw_event_keyword_power"></span><dl> <dt>**STORPORT\_ETW\_EVENT\_KEYWORD\_POWER**</dt> </dl>                   | The event is related to device power.<br/>         |
| <span id="STORPORT_ETW_EVENT_KEYWORD_ENUMERATION"></span><span id="storport_etw_event_keyword_enumeration"></span><dl> <dt>**STORPORT\_ETW\_EVENT\_KEYWORD\_ENUMERATION**</dt> </dl> | The event is related to device enumeration.<br/>   |



 

</dd> <dt>

*EventLevel* \[in\]
</dt> <dd>

The event level. This value can indicate the importance or severity of the event. This is one of the following values.



| Value                                                                                                                                                                                                                                                        | Meaning                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="StorportEtwLevelLogAlways"></span><span id="storportetwlevellogalways"></span><span id="STORPORTETWLEVELLOGALWAYS"></span><dl> <dt>**StorportEtwLevelLogAlways**</dt> </dl>                 | Log the event unconditionally. The event is logged regardless of any filters set.<br/> |
| <span id="StorportEtwLevelCritical"></span><span id="storportetwlevelcritical"></span><span id="STORPORTETWLEVELCRITICAL"></span><dl> <dt>**StorportEtwLevelCritical**</dt> </dl>                     | Critical level event.<br/>                                                             |
| <span id="StorportEtwLevelError"></span><span id="storportetwlevelerror"></span><span id="STORPORTETWLEVELERROR"></span><dl> <dt>**StorportEtwLevelError**</dt> </dl>                                 | Error level event.<br/>                                                                |
| <span id="StorportEtwLevelWarning"></span><span id="storportetwlevelwarning"></span><span id="STORPORTETWLEVELWARNING"></span><dl> <dt>**StorportEtwLevelWarning**</dt> </dl>                         | Warning level event.<br/>                                                              |
| <span id="StorportEtwLevelInformational"></span><span id="storportetwlevelinformational"></span><span id="STORPORTETWLEVELINFORMATIONAL"></span><dl> <dt>**StorportEtwLevelInformational**</dt> </dl> | Informational event.<br/>                                                              |
| <span id="StorportEtwLevelVerbose"></span><span id="storportetwlevelverbose"></span><span id="STORPORTETWLEVELVERBOSE"></span><dl> <dt>**StorportEtwLevelVerbose**</dt> </dl>                         | Verbose event information provided.<br/>                                               |



 

</dd> <dt>

*EventOpcode* \[in\]
</dt> <dd>

The operational nature of the event. This is one of the following values.



| Value                                                                                                                                                                                                                                                                | Meaning                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="StorportEtwEventOpcodeInfo"></span><span id="storportetweventopcodeinfo"></span><span id="STORPORTETWEVENTOPCODEINFO"></span><dl> <dt>**StorportEtwEventOpcodeInfo**</dt> </dl>                     | General informational event.<br/>                                                         |
| <span id="StorportEtwEventOpcodeStart"></span><span id="storportetweventopcodestart"></span><span id="STORPORTETWEVENTOPCODESTART"></span><dl> <dt>**StorportEtwEventOpcodeStart**</dt> </dl>                 | Device or unit was starting.<br/>                                                         |
| <span id="StorportEtwEventOpcodeStop"></span><span id="storportetweventopcodestop"></span><span id="STORPORTETWEVENTOPCODESTOP"></span><dl> <dt>**StorportEtwEventOpcodeStop**</dt> </dl>                     | Device or unit was stopping. The event corresponds to the last unpaired start event.<br/> |
| <span id="StorportEtwEventOpcodeDC_Start"></span><span id="storportetweventopcodedc_start"></span><span id="STORPORTETWEVENTOPCODEDC_START"></span><dl> <dt>**StorportEtwEventOpcodeDC\_Start**</dt> </dl>    | A data collection starting event. These are rundown event types.<br/>                     |
| <span id="StorportEtwEventOpcodeDC_Stop"></span><span id="storportetweventopcodedc_stop"></span><span id="STORPORTETWEVENTOPCODEDC_STOP"></span><dl> <dt>**StorportEtwEventOpcodeDC\_Stop**</dt> </dl>        | A data collection stopping event. These are rundown event types.<br/>                     |
| <span id="StorportEtwEventOpcodeExtension"></span><span id="storportetweventopcodeextension"></span><span id="STORPORTETWEVENTOPCODEEXTENSION"></span><dl> <dt>**StorportEtwEventOpcodeExtension**</dt> </dl> | An extension event.<br/>                                                                  |
| <span id="StorportEtwEventOpcodeReply"></span><span id="storportetweventopcodereply"></span><span id="STORPORTETWEVENTOPCODEREPLY"></span><dl> <dt>**StorportEtwEventOpcodeReply**</dt> </dl>                 | A reply event.<br/>                                                                       |
| <span id="StorportEtwEventOpcodeResume"></span><span id="storportetweventopcoderesume"></span><span id="STORPORTETWEVENTOPCODERESUME"></span><dl> <dt>**StorportEtwEventOpcodeResume**</dt> </dl>             | Device or unit was resuming after suspend.<br/>                                           |
| <span id="StorportEtwEventOpcodeSuspend"></span><span id="storportetweventopcodesuspend"></span><span id="STORPORTETWEVENTOPCODESUSPEND"></span><dl> <dt>**StorportEtwEventOpcodeSuspend**</dt> </dl>         | Device or unit is suspended pending completion of another operation.<br/>                 |
| <span id="StorportEtwEventOpcodeReceive"></span><span id="storportetweventopcodereceive"></span><span id="STORPORTETWEVENTOPCODERECEIVE"></span><dl> <dt>**StorportEtwEventOpcodeReceive**</dt> </dl>         | Transfer of activity is received from another component.<br/>                             |



 

</dd> <dt>

*Srb* \[in, optional\]
</dt> <dd>

A pointer to the SRB associated with the logged event. If this parameter contains a valid SRB, this SRB pointer and the associated SRB pointer are logged.

</dd> <dt>

*Parameter1Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter1Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter1Value* \[in\]
</dt> <dd>

The value for parameter 1.

</dd> <dt>

*Parameter2Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter2Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter2Value* \[in\]
</dt> <dd>

The value for parameter 2.

</dd> <dt>

*Parameter3Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter3Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter3Value* \[in\]
</dt> <dd>

The value for parameter 3.

</dd> <dt>

*Parameter4Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter4Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter4Value* \[in\]
</dt> <dd>

The value for parameter 4.

</dd> <dt>

*Parameter5Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter5Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter5Value* \[in\]
</dt> <dd>

The value for parameter 5.

</dd> <dt>

*Parameter6Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter6Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter6Value* \[in\]
</dt> <dd>

The value for parameter 6.

</dd> <dt>

*Parameter7Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter7Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter7Value* \[in\]
</dt> <dd>

The value for parameter 7.

</dd> <dt>

*Parameter8Name* \[in, optional\]
</dt> <dd>

A description of the of the meaning of *Parameter8Value*. This parameter name string must be &lt;= STORPORT\_ETW\_MAX\_PARAM\_NAME\_LENGTH.

</dd> <dt>

*Parameter8Value* \[in\]
</dt> <dd>

The value for parameter 8.

</dd> </dl>

## Return value

**StorPortEtwEvent8** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The event published successfully storage ETW channel.<br/>                                                                                                                                                                                                                              |
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | Tracing is not enabled for storage events.<br/>                                                                                                                                                                                                                                         |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The *HwDeviceExtension* parameter is NULL.<br/> -or-<br/> *EventDescription* is NULL.<br/> -or-<br/> *EventDescription* is greater than the maximum name length.<br/> -or-<br/> An ETW parameter name is greater than the maximum name length.<br/> |



 

## Remarks

If any parameter is not named, ParameterXName = NULL, the routine will set the corresponding parameter value to 0.

Events generated from StorPort miniport drivers are published to the "Microsoft-Windows-Storage-Storport/Diagnose" ETW channel.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.1.<br/>                                                                                      |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**StorPortEtwEvent2**](storportetwevent2.md)
</dt> <dt>

[**StorPortEtwEvent4**](storportetwevent4.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortEtwEvent8%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






