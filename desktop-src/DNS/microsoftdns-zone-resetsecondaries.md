---
title: ResetSecondaries method of the MicrosoftDNS_Zone class
description: The ResetSecondaries method resets the IP addresses for secondary DNS Servers in the zone.
ms.assetid: b9a47714-f180-40cf-831a-f59e804a4ca2
keywords:
- ResetSecondaries method DNS
- ResetSecondaries method DNS , MicrosoftDNS_Zone class
- MicrosoftDNS_Zone class DNS , ResetSecondaries method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Zone.ResetSecondaries
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ResetSecondaries method of the MicrosoftDNS\_Zone class

The **ResetSecondaries** method resets the IP addresses for secondary DNS Servers in the zone.

## Syntax


```mof
void ResetSecondaries(
  [in]       string            SecondaryServers[],
  [in]       uint32            SecureSecondaries,
  [in]       string            NotifyServers[],
  [in]       uint32            Notify,
  [out, ref] MicrosoftDns_Zone &RR
);
```



## Parameters

<dl> <dt>

*SecondaryServers* \[in\]
</dt> <dd>

Array of IP addresses for secondary DNS Servers.

</dd> <dt>

*SecureSecondaries* \[in\]
</dt> <dd>

Specifies the security to be applied and must be one of the following:

-   ZONE\_SECSECURE\_NO\_SECURITY
-   ZONE\_SECSECURE\_NS\_ONLY
-   ZONE\_SECSECURE\_LIST\_ONLY
-   ZONE\_SECSECURE\_NO\_XFR

</dd> <dt>

*NotifyServers* \[in\]
</dt> <dd>

IP address of DNS Servers to be notified when the zone changes.

</dd> <dt>

*Notify* \[in\]
</dt> <dd>

Notification setting and must be one of the following:

-   ZONE\_NOTIFY\_OFF
-   ZONE\_NOTIFY\_ALL\_SECONDARIES
-   ZONE\_NOTIFY\_LIST\_ONLY

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

RR of type [**MicrosoftDNS\_Zone**](microsoftdns-zone.md).

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

[**ResumeZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-resumezone.md)
</dt> <dt>

[**UpdateFromDS Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-updatefromds.md)
</dt> <dt>

[**WriteBackZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-writebackzone.md)
</dt> </dl>

 

 





