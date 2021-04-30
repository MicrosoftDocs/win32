---
title: UpdateFromDS method of the MicrosoftDNS_Zone class
description: The UpdateFromDS method forces an update of the zone from the Directory Service (DS).
ms.assetid: 471f0754-1221-4d1d-8ffd-36c1ab54b7e5
keywords:
- UpdateFromDS method DNS
- UpdateFromDS method DNS , MicrosoftDNS_Zone class
- MicrosoftDNS_Zone class DNS , UpdateFromDS method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Zone.UpdateFromDS
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# UpdateFromDS method of the MicrosoftDNS\_Zone class

The **UpdateFromDS** method forces an update of the zone from the Directory Service (DS).

## Syntax


```mof
void UpdateFromDS();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

In order to successfully execute this method, the ZoneType must be zero, and the zone must be stored on the DS.

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

[**AgeAllRecords Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-ageallrecords.md)
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

[**WriteBackZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-writebackzone.md)
</dt> </dl>

 

 





