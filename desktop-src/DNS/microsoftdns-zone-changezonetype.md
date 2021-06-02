---
title: ChangeZoneType method of the MicrosoftDNS_Zone class
description: The ChangeZoneType method changes the type of a zone.
ms.assetid: a0a9f495-fdbb-4258-a313-ee9551da762f
keywords:
- ChangeZoneType method DNS
- ChangeZoneType method DNS , MicrosoftDNS_Zone class
- MicrosoftDNS_Zone class DNS , ChangeZoneType method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Zone.ChangeZoneType
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ChangeZoneType method of the MicrosoftDNS\_Zone class

The **ChangeZoneType** method changes the type of a zone.

## Syntax


```mof
void ChangeZoneType(
  [in]           uint32            ZoneType,
  [in, optional] string            DataFileName,
  [in, optional] string            IpAddr[],
  [in, optional] string            AdminEmailName,
  [out, ref]     MicrosoftDns_Zone &RR
);
```



## Parameters

<dl> <dt>

*ZoneType* \[in\]
</dt> <dd>

Type of zone. Valid values are the following:



| Value                                                                        | Meaning                    |
|------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl> | Primary zone.<br/>   |
| <dl> <dt>1</dt> </dl> | Secondary zone.<br/> |
| <dl> <dt>2</dt> </dl> | Stub zone.<br/>      |
| <dl> <dt>3</dt> </dl> | Zone forwarder.<br/> |



 

</dd> <dt>

*DataFileName* \[in, optional\]
</dt> <dd>

Name of the data file associated with the zone.

</dd> <dt>

*IpAddr* \[in, optional\]
</dt> <dd>

IP address of the mater DNS Server for the zone.

</dd> <dt>

*AdminEmailName* \[in, optional\]
</dt> <dd>

Email address of the administrator responsible for the zone.

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

RR of type **MicrosoftDns\_Zone**.

</dd> </dl>

## Return value

This method does not return a value.

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

 

 





