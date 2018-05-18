---
Description: 'The FaxOutboundRoutingRule configuration object is used by a fax client application to set and retrieve information about an individual fax outbound routing rule.'
ms.assetid: 'e027093a-314c-4292-b591-29c2bc58c031'
title: FaxOutboundRoutingRule object
---

# FaxOutboundRoutingRule object

The **FaxOutboundRoutingRule** configuration object is used by a fax client application to set and retrieve information about an individual fax outbound routing rule.

## Members

The **FaxOutboundRoutingRule** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxOutboundRoutingRule** object has these methods.



| Method                                                     | Description                                                                                                                                                   |
|:-----------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Refresh**](-mfax-faxoutboundroutingrule-refresh-vb.md) | The [**Refresh**](-mfax-faxoutboundroutingrule-refresh-vb.md) method refreshes **FaxOutboundRoutingRule** object information from the fax server.<br/> |
| [**Save**](-mfax-faxoutboundroutingrule-save-vb.md)       | The [**Save**](-mfax-faxoutboundroutingrule-save-vb.md) method saves the **FaxOutboundRoutingRule** object data.<br/>                                  |



 

### Properties

The **FaxOutboundRoutingRule** object has these properties.



| Property                                                                      | Access type           | Description                                                                                                                                                                                                              |
|:------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AreaCode**](-mfax-faxoutboundroutingrule-areacode-vb.md)<br/>       | Read-only<br/>  | The [**AreaCode**](-mfax-faxoutboundroutingrule-areacode-vb.md) property specifies the area code to which the outbound routing rule applies.<br/>                                                                 |
| [**CountryCode**](-mfax-faxoutboundroutingrule-countrycode-vb.md)<br/> | Read-only<br/>  | The [**CountryCode**](-mfax-faxoutboundroutingrule-countrycode-vb.md) property specifies the country/region code to which the outbound routing rule applies.<br/>                                                 |
| [**DeviceId**](-mfax-faxoutboundroutingrule-deviceid-vb.md)<br/>       | Read/write<br/> | The [**DeviceId**](-mfax-faxoutboundroutingrule-deviceid-vb.md) property specifies the device ID if the outbound routing rule points to a single fax device.<br/>                                                 |
| [**GroupName**](-mfax-faxoutboundroutingrule-groupname-vb.md)<br/>     | Read/write<br/> | The [**GroupName**](-mfax-faxoutboundroutingrule-groupname-vb.md) property specifies the group name if the outbound routing rule points to a group of fax devices.<br/>                                           |
| [**Status**](-mfax-faxoutboundroutingrule-status-vb.md)<br/>           | Read-only<br/>  | The [**Status**](-mfax-faxoutboundroutingrule-status-vb.md) property indicates the current status of the outbound routing rule; for example, whether the rule is valid and whether it can apply to fax jobs.<br/> |
| [**UseDevice**](-mfax-faxoutboundroutingrule-usedevice-vb.md)<br/>     | Read/write<br/> | The [**UseDevice**](-mfax-faxoutboundroutingrule-usedevice-vb.md) property is a Boolean value that indicates whether the outbound routing rule points to a single fax device.<br/>                                |



 

## Remarks

A **FaxOutboundRoutingRule** object is accessed through a [**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md) object.

![faxoutboundroutingrules and faxoutboundroutingrule objects](images/faxoutboundroutingrule.png)

> [!Note]  
> Changes made to the **FaxOutboundRoutingRule** object will not be saved until you call the [**Save**](-mfax-faxoutboundroutingrule-save-vb.md) method.

 

To create a **FaxOutboundRoutingRule** object in Microsoft Visual Basic, call the [**Item**](-mfax-faxoutboundroutingrules-item.md) property of the **FaxOutboundRoutingRule** object.

To create a **FaxOutboundRoutingRule** object in C++, call the [**Item**](-mfax-faxoutboundroutingrules-item.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxOutboundRoutingRule<br/>                                                |



 

 




