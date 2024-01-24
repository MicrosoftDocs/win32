---
title: SoHAttributeValue union (NapProtocol.h)
description: Defines the contents of the type member in a SoHAttribute structure.
ms.assetid: 53b30455-33a5-4cf5-8d4e-f0fa8e4e1a12
keywords:
- SoHAttributeValue union NAP
topic_type:
- apiref
api_name:
- SoHAttributeValue
api_location:
- NapProtocol.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SoHAttributeValue union

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **SoHAttributeValue** union defines the contents of the **type** member in a [**SoHAttribute**](/windows/win32/api/naptypes/ns-naptypes-sohattribute) structure. The structure of the **SoHAttributeValue** union is determined by the [**SoHAttributeType**](sohattributetype-enum.md) specified in the **type** member of the [**SoHAttribute**](/windows/win32/api/naptypes/ns-naptypes-sohattribute) structure.

## Syntax


```C++
typedef union tagSoHAttributeValue {
  SystemHealthEntityId     idVal;
  struct tagIpv4Addresses {
    UINT16      count;
    Ipv4Address *addresses;
  } v4AddressesVal;
  struct tagIpv6Addresses {
    UINT16      count;
    Ipv6Address *addresses;
  } v6AddressesVal;
  ResultCodes              codesVal;
  FILETIME                 dateTimeVal;
  struct tagVendorSpecific {
    UINT32 vendorId;
    UINT16 size;
    BYTE   *vendorSpecificData;
  } vendorSpecificVal;
  UINT8                    uint8Val;
  struct tagOctetString {
    UINT16 size;
    BYTE   *data;
  } octetStringVal;
} SoHAttributeValue;
```



## Members

<dl> <dt>

**idVal**
</dt> <dd>

**case(sohAttributeTypeSystemHealthId)**

A unique [SystemHealthEntityId](nap-datatypes.md) that contains the ID of the System Health Agent (SHA) or System Health Validator (SHV) that constructed this [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet.

</dd> <dt>

**v4AddressesVal**
</dt> <dd>

**case(sohAttributeTypeIpv4FixupServers)**

The IPv4 addresses of the fix-up servers in use by the NAP system.

<dl> <dt>

**count**
</dt> <dd>

The number of IPv4 addresses in the **addresses** member in the range 1 to [**maxIpv4CountPerSoHAttribute**](nap-type-constants.md).

</dd> <dt>

**addresses**
</dt> <dd>

An array of [**Ipv4Address**](/windows/win32/api/naptypes/ns-naptypes-ipv4address) structures that contain the IPv4 addresses.

</dd> </dl> </dd> <dt>

**v6AddressesVal**
</dt> <dd>

**case(sohAttributeTypeIpv6FixupServers)**

The IPv6 addresses of the fix-up servers in use by the NAP system.

<dl> <dt>

**count**
</dt> <dd>

The number of IPv4 addresses in the **addresses** member in the range 1 to [**maxIpv6CountPerSoHAttribute**](nap-type-constants.md).

</dd> <dt>

**addresses**
</dt> <dd>

An array of [**Ipv6Address**](/windows/win32/api/naptypes/ns-naptypes-ipv6address) structures that contain the IPv4 addresses.

</dd> </dl> </dd> <dt>

**codesVal**
</dt> <dd>

**case(sohAttributeTypeComplianceResultCodes, sohAttributeTypeErrorCodes)**

A [**ResultCodes**](/windows/win32/api/naptypes/ns-naptypes-resultcodes) structure that contains either the application defined compliance result codes of the client or [**NAP error constants**](nap-error-constants.md). An [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet must contain this TLV or the **sohAttributeTypeFailureCategory** TLV.

</dd> <dt>

**dateTimeVal**
</dt> <dd>

**case(sohAttributeTypeTimeOfLastUpdate, sohAttributeTypeSoHGenerationTime)**

A [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure that contains the time of the last [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) update or the **SoH** generation time.

</dd> <dt>

**vendorSpecificVal**
</dt> <dd>

**case(sohAttributeTypeVendorSpecific)**

Application-specific data that is defined by the vendor.

<dl> <dt>

**vendorId**
</dt> <dd>

A 4-byte identifier that defines the SHA/SHV pair ID. The first 3 bytes are the IETF-assigned SMI code of the vendor, and the last byte identifies the component itself. When implementing a SHA or SHV, do not use the ID values assigned to internal Microsoft system health components on [**NAP vendor constants**](nap-vendor-constants.md).

</dd> <dt>

**size**
</dt> <dd>

The size, in bytes, of the vendor data in the range 0 to ([**maxSoHAttributeSize**](nap-type-constants.md) - 4).

</dd> <dt>

**vendorSpecificData**
</dt> <dd>

A pointer to the vendor specific data in network byte order.

</dd> </dl> </dd> <dt>

**uint8Val**
</dt> <dd>

**case(sohAttributeTypeHealthClass, sohAttributeTypeFailureCategory,sohAttributeTypeExtendedIsolationState)**

The health class, failure category, or extended isolation state of a NAP component as either a [**HealthClassValue**](healthclassvalue-enum.md) or [**FailureCategory**](/windows/win32/api/naptypes/ne-naptypes-failurecategory) value, or a [**IsolationInfoEx**](/windows/win32/api/naptypes/ns-naptypes-isolationinfoex) structure.

</dd> <dt>

**octetStringVal**
</dt> <dd>

**default**

The following attributes' values are octet strings:

-   sohAttributeTypeSoftwareVersion
-   sohAttributeTypeClientId
-   sohAttributeTypeProductName
-   sohAttributeTypeHealthClassStatus

For forward compatibility, all unrecognized attributes are returned as octet strings. **data** must be in network byte order.

<dl> <dt>

**size**
</dt> <dd>

The size, in bytes, of **data** in the range 0 to [**maxSoHAttributeSize**](nap-type-constants.md).

</dd> <dt>

**data**
</dt> <dd>

A pointer to the octet string value.

</dd> </dl> </dd> </dl>

## Actual data layout

Due to the nature of the SDK publishing environment, unions are not clearly represented in syntax blocks. Here is the actual syntax from the NapProtocol.h header file.


```C++
#include <windows.h>

typedef [switch_type(SoHAttributeType)] 
   union tagSoHAttributeValue
   {
      [case(sohAttributeTypeSystemHealthId)]
         SystemHealthEntityId idVal;
   
      [case(sohAttributeTypeIpv4FixupServers)]
         struct tagIpv4Addresses
         {
            [range(1, maxIpv4CountPerSoHAttribute)] 
               UINT16 count;
            [size_is(count)] Ipv4Address* addresses;
         } v4AddressesVal;

      [case(sohAttributeTypeIpv6FixupServers)]
         struct tagIpv6Addresses
         {
            [range(1, maxIpv6CountPerSoHAttribute)]
               UINT16 count;
            [size_is(count)] Ipv6Address* addresses;
         } v6AddressesVal;

      [case(sohAttributeTypeComplianceResultCodes, 
            sohAttributeTypeErrorCodes)]
         ResultCodes codesVal;

      [case(sohAttributeTypeTimeOfLastUpdate, 
            sohAttributeTypeSoHGenerationTime)]
         FILETIME dateTimeVal;

      [case(sohAttributeTypeVendorSpecific)]
         struct tagVendorSpecific
         {
            UINT32 vendorId;
            [range(0, maxSoHAttributeSize - 4)] 
               UINT16 size;
            [size_is(size)] BYTE* vendorSpecificData;
         } vendorSpecificVal;

      [case(sohAttributeTypeHealthClass, 
            sohAttributeTypeFailureCategory,
            sohAttributeTypeExtendedIsolationState)]
         UINT8 uint8Val;

      [default]
         struct tagOctetString
         {
            [range(0, maxSoHAttributeSize)] UINT16 size;
            [size_is(size)] BYTE* data;
         } octetStringVal;

   } SoHAttributeValue;
};
```



## Remarks

These attribute types are consumed by the NAP system:

-   sohAttributeTypeSystemHealthId
-   sohAttributeTypeIpv4FixupServers
-   sohAttributeTypeIpv6FixupServers
-   sohAttributeTypeComplianceResultCodes
-   sohAttributeTypeFailureCategory

The rest of the [**SoHAttributeTypes**](sohattributetype-enum.md) are meant purely as prescriptive guidance for usage by SHAs and SHVs.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>NapProtocol.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapProtocol.idl</dt> </dl> |



## See also

<dl> <dt>

[NAP Reference](nap-reference.md)
</dt> <dt>

[NAP Structures](nap-structures.md)
</dt> </dl>

 

