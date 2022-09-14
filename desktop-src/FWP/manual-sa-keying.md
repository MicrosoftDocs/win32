---
title: Manual SA Keying
description: Following sample code demonstrates how to create Security Associations (SA) using Windows Filtering Platform.
ms.assetid: a929456e-e824-44d3-97f7-be75716a1ecd
ms.topic: article
ms.date: 05/31/2018
---

# Manual SA Keying

The following sample code demonstrates how to create Security Associations (SA) using Windows Filtering Platform.


```C++
#include <windows.h>
#include <fwpmu.h>
#include <stdio.h>
#include <conio.h>

#pragma comment(lib, "fwpuclnt.lib")
#pragma comment(lib, "ws2_32.lib")

// 5fb216a8-e2e8-4024-b853-391a4168641e
const GUID PROVIDER_KEY =
{
   0x5fb216a8,
   0xe2e8,
   0x4024,
   { 0xb8, 0x53, 0x39, 0x1a, 0x41, 0x68, 0x64, 0x1e }
};

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

unsigned long inet_addrW(__in PCWSTR cp)
{
   size_t converted;
   char mbstr[sizeof("255.255.255.255")];
   errno_t cerr;

   cerr = wcstombs_s(&converted, mbstr, sizeof(mbstr), cp, wcslen(cp));

   return (cerr == 0) ? inet_addr(mbstr) : INADDR_NONE;

}

// Helper function to delete an SA context and the associated transport
// filters.
void DeleteSaContextAndFilters(
        __in HANDLE engine,
        __in UINT64 inFilterId,
        __in UINT64 outFilterId,
        __in UINT64 saId
        )
{
   DWORD result;

   // Allow the LUIDs to be zero, so we can use this function to cleanup
   // partial results.
   if (saId != 0)
   {
      result = IPsecSaContextDeleteById0(engine, saId);
      if (result != ERROR_SUCCESS)
      {
         // There's not much we can do if delete fails, so continue trying to
         // clean up the remaining objects.
         printf("IPsecSaContextDeleteById0 = 0x%08X\n", result);
      }
   }
   if (outFilterId != 0)
   {
      result = FwpmFilterDeleteById0(engine, outFilterId);
      if (result != ERROR_SUCCESS)
      {
         printf("FwpmFilterDeleteById0 = 0x%08X\n", result);
      }
   }
   if (inFilterId != 0)
   {
      result = FwpmFilterDeleteById0(engine, inFilterId);
      if (result != ERROR_SUCCESS)
      {
         printf("FwpmFilterDeleteById0 = 0x%08X\n", result);
      }
   }
}


// Illustrates the first part of SA establishment using AH. The caller supplies
// the local and remote IP addresses and the inbound authentication key. The
// function returns the inbound SPI.
DWORD AddInboundSa(
         __in HANDLE engine,
         __in PCWSTR filterName,
         __in_opt const GUID* providerKey,
         __in UINT32 localAddr,
         __in UINT32 remoteAddr,
         __in const FWP_BYTE_BLOB* authKey,
         __out UINT64* inFilterId,
         __out UINT64* outFilterId,
         __out UINT64* saId,
         __out IPSEC_SA_SPI* spi
         )
{
   DWORD result = ERROR_SUCCESS;
   UINT64 tmpInFilterId = 0, tmpOutFilterId = 0, tmpSaId = 0;
   FWPM_FILTER_CONDITION0 conds[2];
   FWPM_FILTER0 filter;
   IPSEC_TRAFFIC0 outTraffic;
   IPSEC_GETSPI0 getSpi;
   IPSEC_SA_AUTH_INFORMATION0 info;
   IPSEC_SA0 sa;
   IPSEC_SA_BUNDLE0 bundle;

   //////////
   // Create IPsec filters matching the local and remote IP address at both the
   // inbound and outbound transport layers. This has to be done first since we
   // need the filter LUIDs to create the SA context and get the inbound SPI.
   //////////

   conds[0].fieldKey = FWPM_CONDITION_IP_LOCAL_ADDRESS;
   conds[0].matchType = FWP_MATCH_EQUAL;
   conds[0].conditionValue.type = FWP_UINT32;
   conds[0].conditionValue.uint32 = localAddr;

   conds[1].fieldKey = FWPM_CONDITION_IP_REMOTE_ADDRESS;
   conds[1].matchType = FWP_MATCH_EQUAL;
   conds[1].conditionValue.type = FWP_UINT32;
   conds[1].conditionValue.uint32 = remoteAddr;

   // Fill in the common fields shared by both filters.
   memset(&filter, 0, sizeof(filter));
   // For MUI compatibility, object names should be indirect strings. See
   // SHLoadIndirectString for details.
   filter.displayData.name = (PWSTR)filterName;
   // Link all objects to our provider. When multiple providers are installed
   // on a computer, this makes it easy to determine who added what.
   filter.providerKey = (GUID*)providerKey;
   filter.numFilterConditions = 2;
   filter.filterCondition = conds;
   filter.action.type = FWP_ACTION_CALLOUT_TERMINATING;

   // Add the inbound filter.
   filter.layerKey = FWPM_LAYER_INBOUND_TRANSPORT_V4;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_INBOUND_TRANSPORT_V4;
   result = FwpmFilterAdd0(
               engine,
               &filter,
               NULL,
               &tmpInFilterId
               );
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Add the outbound filter.
   filter.layerKey = FWPM_LAYER_OUTBOUND_TRANSPORT_V4;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_OUTBOUND_TRANSPORT_V4;
   result = FwpmFilterAdd0(
               engine,
               &filter,
               NULL,
               &tmpOutFilterId
               );
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Create the SA context using the outbound traffic descriptor.
   memset(&outTraffic, 0, sizeof(outTraffic));
   outTraffic.ipVersion = FWP_IP_VERSION_V4;
   outTraffic.localV4Address = localAddr;
   outTraffic.remoteV4Address = remoteAddr;
   outTraffic.trafficType = IPSEC_TRAFFIC_TYPE_TRANSPORT;
   outTraffic.ipsecFilterId = tmpOutFilterId;
   result = IPsecSaContextCreate0(
               engine,
               &outTraffic,
               NULL,
               &tmpSaId
               );
   EXIT_ON_ERROR(IPsecSaContextCreate0);

   // Get the inbound SPI using the inbound traffic descriptor.
   memset(&getSpi, 0, sizeof(getSpi));
   getSpi.inboundIpsecTraffic.ipVersion = FWP_IP_VERSION_V4;
   getSpi.inboundIpsecTraffic.localV4Address = localAddr;
   getSpi.inboundIpsecTraffic.remoteV4Address = remoteAddr;
   getSpi.inboundIpsecTraffic.trafficType = IPSEC_TRAFFIC_TYPE_TRANSPORT;
   getSpi.inboundIpsecTraffic.ipsecFilterId = tmpInFilterId;
   getSpi.ipVersion = FWP_IP_VERSION_V4;
   result = IPsecSaContextGetSpi0(
               engine,
               tmpSaId,
               &getSpi,
               spi
               );
   EXIT_ON_ERROR(result);

   /////////
   // Add the inbound SA using the authentication key supplied by the caller.
   /////////

   memset(&info, 0, sizeof(info));
   info.authTransform.authTransformId = IPSEC_AUTH_TRANSFORM_ID_HMAC_SHA_1_96;
   info.authKey = *authKey;

   memset(&sa, 0, sizeof(sa));
   sa.spi = *spi;
   sa.saTransformType = IPSEC_TRANSFORM_AH;
   sa.ahInformation = &info;

   memset(&bundle, 0, sizeof(bundle));
   bundle.numSAs = 1;
   bundle.saList = &sa;
   bundle.ipVersion = FWP_IP_VERSION_V4;

   result = IPsecSaContextAddInbound0(engine, tmpSaId, &bundle);
   EXIT_ON_ERROR(IPsecSaContextAddInbound0);

   // Return the various LUIDs to the caller, so he can clean up.
   *inFilterId = tmpInFilterId;
   *outFilterId = tmpOutFilterId;
   *saId = tmpSaId;

CLEANUP:
   if (result != ERROR_SUCCESS)
   {
      DeleteSaContextAndFilters(
         engine,
         tmpInFilterId,
         tmpOutFilterId,
         tmpSaId
         );
   }
   return result;
}


// After successfully calling AddInboundSa, the caller will use some
// out-of-band mechanism to exchange inbound SPIs and authentication keys with
// the remote peer (who presumably has also called AddInboundSa). The remote
// peer's inbound SPI and key become the outbound SPI and key on the local
// machine.
DWORD AddOutboundSa(
         __in HANDLE engine,
         __in UINT64 saId,
         __in IPSEC_SA_SPI spi,
         __in const FWP_BYTE_BLOB* authKey
         )
{
   DWORD result = ERROR_SUCCESS;
   IPSEC_SA_AUTH_INFORMATION0 info;
   IPSEC_SA0 sa;
   IPSEC_SA_BUNDLE0 bundle;

   memset(&info, 0, sizeof(info));
   info.authTransform.authTransformId = IPSEC_AUTH_TRANSFORM_ID_HMAC_SHA_1_96;
   info.authKey = *authKey;

   memset(&sa, 0, sizeof(sa));
   sa.spi = spi;
   sa.saTransformType = IPSEC_TRANSFORM_AH;
   sa.ahInformation = &info;

   memset(&bundle, 0, sizeof(bundle));
   bundle.numSAs = 1;
   bundle.saList = &sa;
   bundle.ipVersion = FWP_IP_VERSION_V4;

   result = IPsecSaContextAddOutbound0(engine, saId, &bundle);
   EXIT_ON_ERROR(IPsecSaContextAddOutbound0);

CLEANUP:
   return result;
}
```



 

 




