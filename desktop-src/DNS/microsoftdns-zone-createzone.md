---
title: CreateZone method of the MicrosoftDNS_Zone class
description: The CreateZone method creates a DNS zone.
ms.assetid: 55756284-20ef-4d38-a8d9-357f53a6fa4d
keywords:
- CreateZone method DNS
- CreateZone method DNS , MicrosoftDNS_Zone class
- MicrosoftDNS_Zone class DNS , CreateZone method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Zone.CreateZone
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateZone method of the MicrosoftDNS\_Zone class

The **CreateZone** method creates a DNS zone.

## Syntax


```mof
void CreateZone(
  [in]           string            ZoneName,
  [in]           uint32            ZoneType,
  [in]           boolean           DsIntegrated,
  [in, optional] string            DataFileName,
  [in, optional] string            IpAddr[],
  [in, optional] string            AdminEmailName,
  [out, ref]     MicrosoftDns_Zone &RR
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

String representing the name of the zone.

</dd> <dt>

*ZoneType* \[in\]
</dt> <dd>

Type of zone. Valid values are the following:



| Value                                                                        | Meaning                                                                                                             |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>1</dt> </dl> | AD integrated.<br/>                                                                                           |
| <dl> <dt>2</dt> </dl> | Secondary zone.<br/>                                                                                          |
| <dl> <dt>3</dt> </dl> | Stub zone.<br/> **Windows Server 2003:** This zone type is introduced in Windows Server 2003.<br/>      |
| <dl> <dt>4</dt> </dl> | Zone forwarder.<br/> **Windows Server 2003:** This zone type is introduced in Windows Server 2003.<br/> |



 

</dd> <dt>

*DsIntegrated* \[in\]
</dt> <dd>

Indicates whether zone data is stored in the Active Directory or in files. If TRUE, the data is stored in the Active Directory; if FALSE, the data is stored in files.

</dd> <dt>

*DataFileName* \[in, optional\]
</dt> <dd>

Name of the data file associated with the zone.

</dd> <dt>

*IpAddr* \[in, optional\]
</dt> <dd>

IP address of the master DNS Server for the zone.

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

[**ChangeZoneType Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-changezonetype.md)
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

 

 





