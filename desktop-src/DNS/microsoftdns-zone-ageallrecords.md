---
title: AgeAllRecords method of the MicrosoftDNS_Zone class
description: The AgeAllRecords method enables aging for some or all non-NS and non-SOA records in a zone.
ms.assetid: 0e0df1ab-6c7c-4bc4-b292-8f89095970eb
keywords:
- AgeAllRecords method DNS
- AgeAllRecords method DNS , MicrosoftDNS_Zone class
- MicrosoftDNS_Zone class DNS , AgeAllRecords method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Zone.AgeAllRecords
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AgeAllRecords method of the MicrosoftDNS\_Zone class

The **AgeAllRecords** method enables aging for some or all non-NS and non-SOA records in a zone.

## Syntax


```mof
uint32 AgeAllRecords(
  [in, optional] string  NodeName,
  [in, optional] boolean ApplyToSubtree
);
```



## Parameters

<dl> <dt>

*NodeName* \[in, optional\]
</dt> <dd>

Name of the node to age.

</dd> <dt>

*ApplyToSubtree* \[in, optional\]
</dt> <dd>

Specifies whether aging should apply to all records in the subtree. Set to TRUE to apply aging to all records in the subtree, beginning with NodeName.

</dd> </dl>

## Return value

ERROR\_SUCCESS indicates the aging was successfully completed. Any other value is an error code.

## Remarks

If *NodeName* is not specified, all records will be subject to aging and scavenging.

If *NodeName* is specified and *ApplyToSubtree* is not specified or set to zero, records at the specified node will be subjected to aging and scavenging.

If *NodeName* is specified and *ApplyToSubtree* is set to 1, all records of the subtree starting at *NodeName* will be subjected to aging and scavenging. The time stamp is set to the current time for all non-NS and non-SOA RRs with the owner name(s) identified by the input parameters.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_Zone**](microsoftdns-zone.md)
</dt> <dt>

[**ChangeZoneType Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-changezonetype.md)
</dt> <dt>

[**CreateZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-createzone.md)
</dt> <dt>

[**ForceRefresh Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-forcerefresh.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-getdistinguishedname.md)
</dt> <dt>

[**PauseZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-pausezone.md)
</dt> <dt>

[**ReloadZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-reloadzone.md)
</dt> <dt>

[**ResetSecondaries Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-resetsecondaries.md)
</dt> <dt>

[**ResumeZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-resumezone.md)
</dt> <dt>

[**UpdateFromDS Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-updatefromds.md)
</dt> <dt>

[**WriteBackZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-writebackzone.md)
</dt> </dl>

 

 





