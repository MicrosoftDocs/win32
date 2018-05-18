---
title: Add method of the PS\_DnsServerSigningKey class
description: Adds a KSK or ZSK to the input zone.
audience: developer
ms.assetid: '4c72a317-31aa-4833-9328-532c082141c6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DnsServerSigningKey class", "PS_DnsServerSigningKey class, Add method"]
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKey.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Add method of the PS\_DnsServerSigningKey class

Adds a KSK or ZSK to the input zone.

## Syntax


```mof
uint32 Add(
  [in]  string              ZoneName,
  [in]  string              Type,
  [in]  string              CryptoAlgorithm,
  [in]  string              ComputerName,
  [in]  uint32              KeyLength,
  [in]  datetime            InitialRolloverOffset,
  [in]  datetime            DnsKeySignatureValidityPeriod,
  [in]  datetime            DSSignatureValidityPeriod,
  [in]  datetime            ZoneSignatureValidityPeriod,
  [in]  datetime            RolloverPeriod,
  [in]  string              ActiveKey,
  [in]  string              StandbyKey,
  [in]  string              NextKey,
  [in]  string              KeyStorageProvider,
  [in]  boolean             StoreKeysInAD,
  [in]  boolean             PassThru,
  [out] DnsServerSigningKey cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies name of the zone on which DnsSec operations are performed.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Specifies if the key is a **KeySigningKey** or a **ZoneSigningKey.**

</dd> <dt>

*CryptoAlgorithm* \[in\]
</dt> <dd>

Specifies the cryptographic algorithm used for key generation.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies an optional DNS server name.

</dd> <dt>

*KeyLength* \[in\]
</dt> <dd>

Specifies the length in bits of keys.

</dd> <dt>

*InitialRolloverOffset* \[in\]
</dt> <dd>

Specifies amount of time to delay the first scheduled key rollover. This allows for key rollovers to be staggered.

</dd> <dt>

*DnsKeySignatureValidityPeriod* \[in\]
</dt> <dd>

Amount of time that signatures covering DNSKEY record sets should be valid.

</dd> <dt>

*DSSignatureValidityPeriod* \[in\]
</dt> <dd>

Specifies amount of time that signatures covering DS record sets should be valid.

</dd> <dt>

*ZoneSignatureValidityPeriod* \[in\]
</dt> <dd>

Specifies amount of time that signatures covering all other record sets should be valid.

</dd> <dt>

*RolloverPeriod* \[in\]
</dt> <dd>

Specifies amount of time between scheduled key rollovers.

</dd> <dt>

*ActiveKey* \[in\]
</dt> <dd>

Specifies signing key pointer string for the **KeySigningKey**'s active key.

</dd> <dt>

*StandbyKey* \[in\]
</dt> <dd>

Specifies signing key pointer string for the **KeySigningKey**'s standby key.

</dd> <dt>

*NextKey* \[in\]
</dt> <dd>

Specifies signing key pointer string for the **KeySigningKey**'s next key. This key will be used during the next key rollover event.

</dd> <dt>

*KeyStorageProvider* \[in\]
</dt> <dd>

Specifies the Key Storage Provider used to generate keys.

</dd> <dt>

*StoreKeysInAD* \[in\]
</dt> <dd>

If specified, stores the keys in Active Directory. Applicable only for AD integrated zones and the vendor of *KeyStorageProvider* is Microsoft. Not applicable otherwise.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives and embedded instance of the [**DnsServerSigningKey**](dnsserversigningkey.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerSigningKey**](ps-dnsserversigningkey.md)
</dt> </dl>

 

 





