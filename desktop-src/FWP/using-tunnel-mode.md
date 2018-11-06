---
title: Using Tunnel Mode
description: Following sample code demonstrates how to configure a point-to-point IPsec tunnel using the Windows Filtering Platform (WFP) API.
ms.assetid: 6bbe7e94-6a5f-4984-ac61-b187dcf25366
ms.topic: article
ms.date: 05/31/2018
---

# Using Tunnel Mode

The following sample code demonstrates how to configure a point-to-point IPsec tunnel using the Windows Filtering Platform (WFP) API.


```C++
#include <winsock2.h>
#include <ws2ipdef.h>
#include <mstcpip.h>
#include <fwpmu.h>
#include <stdio.h>

#pragma comment(lib, "Fwpuclnt.lib")
#pragma comment(lib, "ws2_32.lib")

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }
   
// 5fb216a8-e2e8-4024-b853-391a4168641e
const GUID PROVIDER_KEY =
{
   0x5fb216a8,
   0xe2e8,
   0x4024,
   { 0xb8, 0x53, 0x39, 0x1a, 0x41, 0x68, 0x64, 0x1e }
};

DWORD ConfigureIPsecTunnelMode(
         __in HANDLE engine,
         __in PCWSTR policyName,
         __in_opt const GUID* providerKey,
         __in const SOCKADDR* localAddr,
         __in const SOCKADDR* remoteAddr,
         __in const FWP_BYTE_BLOB* presharedKey
         )
{
   DWORD result = ERROR_SUCCESS;
   FWPM_FILTER_CONDITION0 filterConditions[2];
   IPSEC_TUNNEL_ENDPOINTS0 endpoints;
   IKEEXT_AUTHENTICATION_METHOD0 mmAuthMethods[1];
   IKEEXT_PROPOSAL0 mmProposals[1];
   IKEEXT_POLICY0 mmPolicy;
   FWPM_PROVIDER_CONTEXT0 mmProvCtxt;
   IPSEC_AUTH_AND_CIPHER_TRANSFORM0 qmTransform00;
   const IPSEC_SA_LIFETIME0 qmLifetime =
   {
      3600,       // lifetimeSeconds
      100000,     // lifetimeKilobytes
      0x7FFFFFFF  // lifetimePackets
   };
   IPSEC_SA_TRANSFORM0 qmTransforms0[1];
   IPSEC_PROPOSAL0 qmProposals[1];
   IPSEC_TUNNEL_POLICY0 qmPolicy;
   FWPM_PROVIDER_CONTEXT0 qmProvCtxt;

   // Fill in the version-independent fields in the filter conditions.
   memset(filterConditions, 0, sizeof(filterConditions));
   filterConditions[0].fieldKey = FWPM_CONDITION_IP_LOCAL_ADDRESS;
   filterConditions[0].matchType = FWP_MATCH_EQUAL;
   filterConditions[1].fieldKey = FWPM_CONDITION_IP_REMOTE_ADDRESS;
   filterConditions[1].matchType = FWP_MATCH_EQUAL;

   // Do the version-dependent processing of the tunnel endpoints.
   if (localAddr->sa_family == AF_INET)
   {
      endpoints.ipVersion = FWP_IP_VERSION_V4;
      endpoints.localV4Address = ntohl(*(ULONG*)INETADDR_ADDRESS(localAddr));
      endpoints.remoteV4Address = ntohl(*(ULONG*)INETADDR_ADDRESS(remoteAddr));

      // For a point-to-point tunnel, the filter conditions are the same as the
      // tunnel endpoints. If this were a site-to-site tunnel, these would be
      // the local and remote subnets instead.
      filterConditions[0].conditionValue.type = FWP_UINT32;
      filterConditions[0].conditionValue.uint32 = endpoints.localV4Address;
      filterConditions[1].conditionValue.type = FWP_UINT32;
      filterConditions[1].conditionValue.uint32 = endpoints.remoteV4Address;
   }
   else
   {
      endpoints.ipVersion = FWP_IP_VERSION_V6;
      memcpy(
         endpoints.localV6Address,
         INETADDR_ADDRESS(localAddr),
         sizeof(endpoints.localV6Address)
         );
      memcpy(
         endpoints.remoteV6Address,
         INETADDR_ADDRESS(remoteAddr),
         sizeof(endpoints.remoteV6Address)
         );

      filterConditions[0].conditionValue.type = FWP_BYTE_ARRAY16_TYPE;
      filterConditions[0].conditionValue.byteArray16 =
         (FWP_BYTE_ARRAY16*)(endpoints.localV6Address);
      filterConditions[1].conditionValue.type = FWP_BYTE_ARRAY16_TYPE;
      filterConditions[1].conditionValue.byteArray16 =
         (FWP_BYTE_ARRAY16*)(endpoints.remoteV6Address);
   }

   // Main mode authentication uses a pre-shared key.
   memset(mmAuthMethods, 0, sizeof(mmAuthMethods));
   mmAuthMethods[0].authenticationMethodType = IKEEXT_PRESHARED_KEY;
   mmAuthMethods[0].presharedKeyAuthentication.presharedKey = *presharedKey;

   // There is a single main mode proposal: AES-128/SHA-1 with 8 hour lifetime.
   memset(mmProposals, 0, sizeof(mmProposals));
   mmProposals[0].cipherAlgorithm.algoIdentifier = IKEEXT_CIPHER_AES_128;
   mmProposals[0].integrityAlgorithm.algoIdentifier = IKEEXT_INTEGRITY_SHA1;
   mmProposals[0].maxLifetimeSeconds = 8 * 60 * 60;
   mmProposals[0].dhGroup = IKEEXT_DH_GROUP_2;

   memset(&mmPolicy, 0, sizeof(mmPolicy));
   mmPolicy.numAuthenticationMethods = ARRAYSIZE(mmAuthMethods);
   mmPolicy.authenticationMethods = mmAuthMethods;
   mmPolicy.numIkeProposals = ARRAYSIZE(mmProposals);
   mmPolicy.ikeProposals = mmProposals;

   memset(&mmProvCtxt, 0, sizeof(mmProvCtxt));
   // For MUI compatibility, object names should be indirect strings. 
   // See SHLoadIndirectString for details.
   mmProvCtxt.displayData.name = (PWSTR)policyName;
   // Link all our objects to our provider. When multiple providers are
   // installed on a computer, this makes it easy to determine who added what.
   mmProvCtxt.providerKey = (GUID*)providerKey;
   mmProvCtxt.type = FWPM_IPSEC_IKE_MM_CONTEXT;
   mmProvCtxt.authIpMmPolicy = &mmPolicy;

   // For quick mode use ESP authentication and cipher.
   memset(&qmTransform00, 0, sizeof(qmTransform00));
   qmTransform00.authTransform.authTransformId =
      IPSEC_AUTH_TRANSFORM_ID_HMAC_SHA_1_96;
   qmTransform00.cipherTransform.cipherTransformId =
      IPSEC_CIPHER_TRANSFORM_ID_AES_128;

   memset(qmTransforms0, 0, sizeof(qmTransforms0));
   qmTransforms0[0].ipsecTransformType = IPSEC_TRANSFORM_ESP_AUTH_AND_CIPHER;
   qmTransforms0[0].espAuthAndCipherTransform = &qmTransform00;

   memset(qmProposals, 0, sizeof(qmProposals));
   qmProposals[0].lifetime = qmLifetime;
   qmProposals[0].numSaTransforms = ARRAYSIZE(qmTransforms0);
   qmProposals[0].saTransforms = qmTransforms0;

   memset(&qmPolicy, 0, sizeof(qmPolicy));
   qmPolicy.numIpsecProposals = ARRAYSIZE(qmProposals);
   qmPolicy.ipsecProposals = qmProposals;
   qmPolicy.tunnelEndpoints = endpoints;
   qmPolicy.saIdleTimeout.idleTimeoutSeconds = 300;
   qmPolicy.saIdleTimeout.idleTimeoutSecondsFailOver = 60;

   memset(&qmProvCtxt, 0, sizeof(qmProvCtxt));
   qmProvCtxt.displayData.name = (PWSTR)policyName;
   qmProvCtxt.providerKey = (GUID*)providerKey;
   qmProvCtxt.type = FWPM_IPSEC_IKE_QM_TUNNEL_CONTEXT;
   qmProvCtxt.ikeQmTunnelPolicy = &qmPolicy;

   result = FwpmIPsecTunnelAdd0(
               engine,
               FWPM_TUNNEL_FLAG_POINT_TO_POINT,
               &mmProvCtxt,
               &qmProvCtxt,
               ARRAYSIZE(filterConditions),
               filterConditions,
               NULL
               );
   EXIT_ON_ERROR(FwpmIPsecTunnelAdd0);

CLEANUP:
   return result;
}
```



 

 




